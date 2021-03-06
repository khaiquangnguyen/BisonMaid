from enum import Enum

font_sizes = {'\x00': (6, 12), '\x01': (6, 12), '\x02': (6, 12), '\x03': (6, 12), '\x04': (6, 12), '\x05': (6, 12),
              '\x06': (6, 12), '\x07': (6, 12), '\x08': (6, 12), '\t': (6, 12), '\n': (6, 12), '\x0b': (6, 12),
              '\x0c': (6, 12), '\r': (6, 12), '\x0e': (6, 12), '\x0f': (6, 12), '\x10': (6, 12), '\x11': (6, 12),
              '\x12': (6, 12), '\x13': (6, 12), '\x14': (6, 12), '\x15': (6, 12), '\x16': (6, 12), '\x17': (6, 12),
              '\x18': (6, 12), '\x19': (6, 12), '\x1a': (6, 12), '\x1b': (6, 12), '\x1c': (6, 12), '\x1d': (6, 12),
              '\x1e': (6, 12), '\x1f': (6, 12), ' ': (3, 12), '!': (3, 12), '"': (5, 12), '#': (8, 12), '$': (6, 13),
              '%': (11, 12), '&': (9, 12), "'": (3, 12), '(': (5, 13), ')': (5, 13), '*': (5, 12), '+': (7, 12),
              ',': (3, 14), '-': (4, 12), '.': (3, 12), '/': (7, 13), '0': (7, 12), '1': (4, 12), '2': (6, 12),
              '3': (6, 12), '4': (7, 12), '5': (6, 12), '6': (7, 12), '7': (6, 12), '8': (7, 12), '9': (7, 12),
              ':': (3, 12), ';': (3, 14), '<': (7, 12), '=': (7, 12), '>': (7, 12), '?': (6, 12), '@': (10, 14),
              'A': (8, 12), 'B': (7, 12), 'C': (8, 12), 'D': (8, 12), 'E': (6, 12), 'F': (6, 12), 'G': (8, 12),
              'H': (8, 12), 'I': (3, 12), 'J': (4, 12), 'K': (8, 12), 'L': (6, 12), 'M': (11, 12), 'N': (8, 12),
              'O': (9, 12), 'P': (6, 12), 'Q': (9, 14), 'R': (7, 12), 'S': (6, 12), 'T': (7, 12), 'U': (8, 12),
              'V': (8, 12), 'W': (12, 12), 'X': (8, 12), 'Y': (8, 12), 'Z': (7, 12), '[': (5, 13), '\\': (7, 14),
              ']': (5, 13), '^': (5, 12), '_': (6, 13), '`': (5, 12), 'a': (6, 12), 'b': (6, 12), 'c': (6, 12),
              'd': (6, 12), 'e': (6, 12), 'f': (4, 12), 'g': (6, 14), 'h': (6, 12), 'i': (3, 12), 'j': (4, 14),
              'k': (6, 12), 'l': (3, 12), 'm': (10, 12), 'n': (6, 12), 'o': (6, 12), 'p': (6, 14), 'q': (6, 14),
              'r': (4, 12), 's': (5, 12), 't': (4, 12), 'u': (6, 12), 'v': (6, 12), 'w': (9, 12), 'x': (6, 12),
              'y': (6, 14), 'z': (5, 12), '{': (6, 13), '|': (3, 14), '}': (6, 13), '~': (5, 12), '\x7f': (6, 12),
              '\x80': (6, 12), '\x81': (6, 12), '\x82': (6, 12), '\x83': (6, 12), '\x84': (6, 12), '\x85': (6, 12),
              '\x86': (6, 12), '\x87': (6, 12), '\x88': (6, 12), '\x89': (6, 12), '\x8a': (6, 12), '\x8b': (6, 12),
              '\x8c': (6, 12), '\x8d': (6, 12), '\x8e': (6, 12), '\x8f': (6, 12), '\x90': (6, 12), '\x91': (6, 12),
              '\x92': (6, 12), '\x93': (6, 12), '\x94': (6, 12), '\x95': (6, 12), '\x96': (6, 12), '\x97': (6, 12),
              '\x98': (6, 12), '\x99': (6, 12), '\x9a': (6, 12), '\x9b': (6, 12), '\x9c': (6, 12), '\x9d': (6, 12),
              '\x9e': (6, 12), '\x9f': (6, 12), '\xa0': (1, 12), '¡': (3, 12), '¢': (6, 12), '£': (7, 12), '¤': (7, 12),
              '¥': (7, 12), '¦': (6, 14), '§': (7, 12), '¨': (5, 12), '©': (10, 12), 'ª': (5, 12), '«': (6, 12),
              '¬': (7, 12), '\xad': (6, 12), '®': (7, 12), '¯': (5, 12), '°': (5, 12), '±': (7, 12), '²': (6, 14),
              '³': (6, 14), '´': (5, 12), 'µ': (7, 12), '¶': (6, 12), '·': (3, 12), '¸': (5, 14), '¹': (6, 14),
              'º': (5, 12), '»': (6, 12), '¼': (6, 14), '½': (6, 14), '¾': (6, 14), '¿': (6, 12), 'À': (8, 12),
              'Á': (8, 12), 'Â': (8, 12), 'Ã': (8, 12), 'Ä': (8, 12), 'Å': (8, 12), 'Æ': (10, 12), 'Ç': (8, 14)}

relationship_statuses = {
    'Hang': 'looking to be captured',
    'Khai': 'captured',
    'Phuong': 'just got captured',
    'Khoi': 'escaped',
    'Trung': 'winner'
}

ZERO_WIDTH_CHAR = '\u200b'


class FeatureTypes(Enum):
    REQUESTED = 'requested'
    DEVELOPING = 'developing',
    COMPLETED = 'completed',
