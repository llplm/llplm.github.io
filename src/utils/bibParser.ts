// Simple BibTeX parser for publications
export interface Publication {
  id: string;
  type: string;
  title: string;
  author: string;
  year: string;
  journal?: string;
  booktitle?: string;
  volume?: string;
  pages?: string;
  doi?: string;
  url?: string;
  arxiv?: string;
  selected?: boolean;
  abstract?: string;
  citations?: number;
}

// Clean LaTeX special characters
function cleanLatex(text: string): string {
  return text
    // Handle dotless i and j first (used for accents in LaTeX)
    .replace(/\\i(?=\s|\\|{|}|$)/g, 'i')
    .replace(/\\j(?=\s|\\|{|}|$)/g, 'j')
    // Acute accents (´) - handle both {\'X} and \'X patterns
    .replace(/\{\\'([aeiouAEIOUcnsy])\}/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú',
        'A': 'Á', 'E': 'É', 'I': 'Í', 'O': 'Ó', 'U': 'Ú',
        'c': 'ć', 'n': 'ń', 's': 'ś', 'y': 'ý'
      };
      return map[char] || char;
    })
    .replace(/\\'([aeiouAEIOUcnsy])/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú',
        'A': 'Á', 'E': 'É', 'I': 'Í', 'O': 'Ó', 'U': 'Ú',
        'c': 'ć', 'n': 'ń', 's': 'ś', 'y': 'ý'
      };
      return map[char] || char;
    })
    // Grave accents (`)
    .replace(/\{\\`([aeiouAEIOU])\}/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'à', 'e': 'è', 'i': 'ì', 'o': 'ò', 'u': 'ù',
        'A': 'À', 'E': 'È', 'I': 'Ì', 'O': 'Ò', 'U': 'Ù'
      };
      return map[char] || char;
    })
    .replace(/\\`([aeiouAEIOU])/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'à', 'e': 'è', 'i': 'ì', 'o': 'ò', 'u': 'ù',
        'A': 'À', 'E': 'È', 'I': 'Ì', 'O': 'Ò', 'U': 'Ù'
      };
      return map[char] || char;
    })
    // Tilde (~)
    .replace(/\{\\~([aonAON])\}/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'ã', 'o': 'õ', 'n': 'ñ',
        'A': 'Ã', 'O': 'Õ', 'N': 'Ñ'
      };
      return map[char] || char;
    })
    .replace(/\\~([aonAON])/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'ã', 'o': 'õ', 'n': 'ñ',
        'A': 'Ã', 'O': 'Õ', 'N': 'Ñ'
      };
      return map[char] || char;
    })
    // Umlaut/diaeresis (¨)
    .replace(/\{\\\"([aeiouyAEIOUY])\}/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü', 'y': 'ÿ',
        'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü', 'Y': 'Ÿ'
      };
      return map[char] || char;
    })
    .replace(/\\\"([aeiouyAEIOUY])/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü', 'y': 'ÿ',
        'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü', 'Y': 'Ÿ'
      };
      return map[char] || char;
    })
    // Circumflex (^)
    .replace(/\{\\^([aeiouAEIOU])\}/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'â', 'e': 'ê', 'i': 'î', 'o': 'ô', 'u': 'û',
        'A': 'Â', 'E': 'Ê', 'I': 'Î', 'O': 'Ô', 'U': 'Û'
      };
      return map[char] || char;
    })
    .replace(/\\^([aeiouAEIOU])/g, (_, char) => {
      const map: Record<string, string> = {
        'a': 'â', 'e': 'ê', 'i': 'î', 'o': 'ô', 'u': 'û',
        'A': 'Â', 'E': 'Ê', 'I': 'Î', 'O': 'Ô', 'U': 'Û'
      };
      return map[char] || char;
    })
    // Caron/hacek (ˇ)
    .replace(/\{\\v\{?([scrzCSRZ])\}?\}/g, (_, char) => {
      const map: Record<string, string> = {
        's': 'š', 'c': 'č', 'r': 'ř', 'z': 'ž',
        'S': 'Š', 'C': 'Č', 'R': 'Ř', 'Z': 'Ž'
      };
      return map[char] || char;
    })
    .replace(/\\v\{?([scrzCSRZ])\}?/g, (_, char) => {
      const map: Record<string, string> = {
        's': 'š', 'c': 'č', 'r': 'ř', 'z': 'ž',
        'S': 'Š', 'C': 'Č', 'R': 'Ř', 'Z': 'Ž'
      };
      return map[char] || char;
    })
    // Cedilla (¸)
    .replace(/\{\\c\{?([cC])\}?\}/g, (_, char) => char === 'c' ? 'ç' : 'Ç')
    .replace(/\\c\{?([cC])\}?/g, (_, char) => char === 'c' ? 'ç' : 'Ç')
    // Special characters
    .replace(/\\o\b/g, 'ø')
    .replace(/\\O\b/g, 'Ø')
    .replace(/\\aa\b/g, 'å')
    .replace(/\\AA\b/g, 'Å')
    .replace(/\\ae\b/g, 'æ')
    .replace(/\\AE\b/g, 'Æ')
    .replace(/\\ss\b/g, 'ß')
    // Remove extra braces (but preserve content)
    .replace(/\{([^{}]+)\}/g, '$1')
    // En dash and em dash (do this after brace removal)
    .replace(/---/g, '—')
    .replace(/--/g, '–')
    // Clean up whitespace
    .trim();
}

export function parseBibFile(bibContent: string): Publication[] {
  const entries: Publication[] = [];

  // Match BibTeX entries
  const entryRegex = /@(\w+)\{([^,]+),\s*([\s\S]*?)\n\}/g;
  let match;

  while ((match = entryRegex.exec(bibContent)) !== null) {
    const [, type, id, content] = match;

    const entry: Publication = {
      id,
      type: type.toLowerCase(),
      title: '',
      author: '',
      year: '',
    };

    // Parse fields - need to handle nested braces
    const fieldPattern = /(\w+)\s*=\s*\{/g;
    let fieldMatch;

    while ((fieldMatch = fieldPattern.exec(content)) !== null) {
      const key = fieldMatch[1];
      let braceCount = 1;
      let valueStart = fieldMatch.index + fieldMatch[0].length;
      let i = valueStart;

      // Find matching closing brace
      while (i < content.length && braceCount > 0) {
        if (content[i] === '{') braceCount++;
        else if (content[i] === '}') braceCount--;
        i++;
      }

      const value = content.substring(valueStart, i - 1);
      const cleanValue = cleanLatex(value.trim());

      switch (key.toLowerCase()) {
        case 'title':
          entry.title = cleanValue;
          break;
        case 'author':
          entry.author = cleanValue;
          break;
        case 'year':
          entry.year = cleanValue;
          break;
        case 'journal':
          entry.journal = cleanValue;
          break;
        case 'booktitle':
          entry.booktitle = cleanValue;
          break;
        case 'volume':
          entry.volume = cleanValue;
          break;
        case 'pages':
          entry.pages = cleanValue;
          break;
        case 'doi':
          entry.doi = cleanValue;
          break;
        case 'url':
          entry.url = cleanValue;
          break;
        case 'arxiv':
          entry.arxiv = cleanValue;
          break;
        case 'abstract':
          entry.abstract = cleanValue;
          break;
        case 'selected':
          entry.selected = cleanValue === 'true';
          break;
        case 'citations':
          entry.citations = parseInt(cleanValue) || 0;
          break;
      }
    }

    entries.push(entry);
  }

  // Sort by year (descending)
  return entries.sort((a, b) => parseInt(b.year) - parseInt(a.year));
}

export function formatAuthors(authors: string, maxAuthors: number = 3): string {
  // Split by 'and' to get individual authors
  const authorList = authors.split(' and ').map(a => a.trim());

  // Convert from "Last, First" to "First Last" format
  const formattedAuthors = authorList.map(author => {
    // Check if author has comma (BibTeX format: Last, First)
    if (author.includes(',')) {
      const parts = author.split(',').map(p => p.trim());
      // Reverse to "First Last"
      return parts.reverse().join(' ');
    }
    // If no comma, return as-is
    return author;
  });

  if (formattedAuthors.length <= maxAuthors) {
    return formattedAuthors.join(', ');
  }

  const displayed = formattedAuthors.slice(0, maxAuthors);
  const remaining = formattedAuthors.length - maxAuthors;
  return `${displayed.join(', ')}, et al. (${remaining} more)`;
}
