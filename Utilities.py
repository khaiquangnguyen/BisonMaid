import math

from PIL import ImageFont


# the empty bank is not a simple ' '. it's actually a unicode character
# U+2004	&#8196	Three-Per-Em Space	[ ]
def right_padding(s: str, desired_width: int = 106, padding_char=' ') -> str:
    s_width = calculate_width_of_string(s)
    padded_whitespace = math.floor((desired_width - s_width) // 4) * padding_char
    return f'{s}{padded_whitespace}'


def convert_char_to_monospace(char: str, first_converted_char='A', first_comparison_char='A') -> str:
    return chr(ord(char) - ord(first_comparison_char) + ord(first_converted_char))


def convert_string_to_monospace(t: str) -> str:
    out_s = ''
    for c in t:
        if c.isdigit():
            out_s += chr(ord(c) - ord('0') + ord('𝟶'))
        elif c.isalpha():
            out_s += chr(ord(c.upper()) - ord('A') + ord('𝙰'))
        else:
            out_s += c
    return out_s


# def convert_string_to_monospace(s: str, first_converted_char='𝙰', first_comparison_char='A') -> str:
#     return ''.join([convert_char_to_monospace(c.upper(), first_converted_char, first_comparison_char) for c in s])


def calculate_width_of_string(s: str) -> int:
    font = ImageFont.truetype('whitney.ttf', 16)
    return font.getsize(s)[0]
