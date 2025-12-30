#!/usr/bin/env python3
"""
Update publications from ORCID API to BibTeX format.
Usage: python scripts/update_publications.py
"""

import requests
import json
import re
from typing import Dict, List, Optional

ORCID_ID = '0000-0002-3284-2152'
OUTPUT_FILE = 'public/data/papers.bib'


def clean_for_bibtex(text: str) -> str:
    """Clean text for BibTeX format."""
    if not text:
        return ""
    # Replace special characters
    replacements = {
        'á': r"{\'\i}",
        'é': r"{\'e}",
        'í': r"{\'\i}",
        'ó': r"{\'o}",
        'ú': r"{\'u}",
        'à': r"{\`a}",
        'è': r"{\`e}",
        'ì': r"{\`i}",
        'ò': r"{\`o}",
        'ù': r"{\`u}",
        'ä': r'{\"a}',
        'ë': r'{\"e}',
        'ï': r'{\"i}',
        'ö': r'{\"o}',
        'ü': r'{\"u}',
        'ñ': r'{\~n}',
        'ã': r'{\~a}',
        'õ': r'{\~o}',
        'ç': r'{\c{c}}',
        'š': r'{\v{s}}',
        'č': r'{\v{c}}',
        'ž': r'{\v{z}}',
        'Á': r"{\'A}",
        'É': r"{\'E}",
        'Í': r"{\'I}",
        'Ó': r"{\'O}",
        'Ú': r"{\'U}",
        'Ñ': r'{\~N}',
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text


def generate_bibtex_key(author: str, year: str, title: str) -> str:
    """Generate BibTeX citation key."""
    # Get first author's last name
    if ',' in author:
        last_name = author.split(',')[0].strip()
    else:
        parts = author.split()
        last_name = parts[-1] if parts else 'unknown'

    # Get first word of title
    title_words = re.findall(r'\w+', title.lower())
    first_word = title_words[0] if title_words else 'untitled'

    # Clean last name
    last_name = re.sub(r'[^a-z]', '', last_name.lower())

    return f"{last_name}{year}{first_word}"


def fetch_orcid_works() -> List[Dict]:
    """Fetch works from ORCID API."""
    print(f"Fetching publications for ORCID: {ORCID_ID}")

    # Get list of works
    url = f'https://pub.orcid.org/v3.0/{ORCID_ID}/works'
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    works = []
    if 'group' in data:
        for group in data['group']:
            if 'work-summary' in group and len(group['work-summary']) > 0:
                work_summary = group['work-summary'][0]
                put_code = work_summary['put-code']

                # Fetch detailed work info
                work_url = f'https://pub.orcid.org/v3.0/{ORCID_ID}/work/{put_code}'
                work_response = requests.get(work_url, headers=headers)
                work_response.raise_for_status()
                works.append(work_response.json())

    print(f"Found {len(works)} publications")
    return works


def convert_to_bibtex(work: Dict) -> Optional[str]:
    """Convert ORCID work to BibTeX entry."""
    try:
        # Extract basic info
        title = work.get('title', {}).get('title', {}).get('value', '')
        if not title:
            return None

        # Year
        pub_date = work.get('publication-date')
        year = pub_date.get('year', {}).get('value', '') if pub_date else ''

        # Type
        work_type = work.get('type', 'JOURNAL_ARTICLE')
        bibtex_type = 'article' if 'ARTICLE' in work_type else 'inproceedings'

        # Authors
        contributors = work.get('contributors', {}).get('contributor', [])
        authors = []
        for contrib in contributors:
            credit_name = contrib.get('credit-name', {})
            if credit_name:
                name = credit_name.get('value', '')
                if name:
                    authors.append(name)

        author_str = ' and '.join(authors) if authors else 'Unknown'

        # Journal/venue
        journal_title = work.get('journal-title', {})
        journal = journal_title.get('value', '') if journal_title else ''

        # External IDs (DOI, arxiv, etc.)
        external_ids = work.get('external-ids', {}).get('external-id', [])
        doi = ''
        arxiv = ''
        for ext_id in external_ids:
            id_type = ext_id.get('external-id-type', '')
            id_value = ext_id.get('external-id-value', '')
            if id_type == 'doi':
                doi = id_value
            elif id_type == 'arxiv':
                arxiv = id_value

        # URL
        url = work.get('url', {}).get('value', '')
        if not url and doi:
            url = f'https://doi.org/{doi}'

        # Generate citation key
        first_author = authors[0] if authors else 'unknown'
        citation_key = generate_bibtex_key(first_author, year, title)

        # Build BibTeX entry
        bibtex = f"@{bibtex_type}{{{citation_key},\n"
        bibtex += f"  title={{{clean_for_bibtex(title)}}},\n"
        bibtex += f"  author={{{clean_for_bibtex(author_str)}}},\n"
        bibtex += f"  year={{{year}}},\n"

        if journal:
            bibtex += f"  journal={{{clean_for_bibtex(journal)}}},\n"

        if doi:
            bibtex += f"  doi={{{doi}}},\n"

        if url:
            bibtex += f"  url={{{url}}},\n"

        if arxiv:
            bibtex += f"  arxiv={{{arxiv}}},\n"

        bibtex += "}\n"

        return bibtex

    except Exception as e:
        print(f"Error converting work: {e}")
        return None


def main():
    """Main function."""
    try:
        # Fetch works from ORCID
        works = fetch_orcid_works()

        # Convert to BibTeX
        bibtex_entries = []
        for work in works:
            entry = convert_to_bibtex(work)
            if entry:
                bibtex_entries.append(entry)

        # Write to file
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(bibtex_entries))

        print(f"\n✓ Successfully wrote {len(bibtex_entries)} entries to {OUTPUT_FILE}")
        print("\nNote: You may need to manually add:")
        print("  - selected={{true}} for featured papers")
        print("  - abstracts")
        print("  - citation counts")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching from ORCID: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
