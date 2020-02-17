import json
import math

from PIL import ImageFont
from Constants import FeatureTypes
from Constants import ZERO_WIDTH_CHAR
# the empty bank is not a simple ' '. it's actually a unicode character
# U+2004	&#8196	Three-Per-Em Space	[ ]
def right_padding(s: str, desired_width: int = 106, padding_char=' ') -> str:
    s_width = calculate_width_of_string(s)
    padded_whitespace = math.floor((desired_width - s_width) // 4) * padding_char
    return f'{s}{padded_whitespace}'


def to_monospace(t: str) -> str:
    out_s = ''
    for c in t:
        if c.isdigit():
            out_s += chr(ord(c) - ord('0') + ord('𝟶'))
        elif c.isalpha():
            if c.isupper():
                out_s += chr(ord(c) - ord('A') + ord('𝙰'))
            else:
                out_s += chr(ord(c) - ord('a') + ord('𝚊'))
        else:
            out_s += c
    return out_s


# def convert_string_to_monospace(s: str, first_converted_char='𝙰', first_comparison_char='A') -> str:
#     return ''.join([convert_char_to_monospace(c.upper(), first_converted_char, first_comparison_char) for c in s])


def calculate_width_of_string(s: str) -> int:
    font = ImageFont.truetype('whitney.ttf', 16)
    return font.getsize(s)[0]


def move_feature_log(origin_key: str, destination_key: str, index: int):
    with open('SimpleDB/features.json', 'r') as f:
        all_features = json.load(f)
        origin_features = all_features.get(origin_key, [])
        destination_features = all_features.get(destination_key, [])
        if index < len(origin_features):
            feature = origin_features.pop(index)
            destination_features.append(feature)
            all_features[origin_key] = origin_features
            all_features[destination_key] = destination_features
            with open('SimpleDB/features.json', 'w') as f:
                json.dump(all_features, f)
        response = to_monospace(f'- - {origin_key.upper()} - - \n') + '\n'.join(
            [f"{right_padding(f'**{index + 1}**', 12)} - {value['feature']}" for (index, value) in
             enumerate(destination_features)])
        return response


def get_feature_type(feature_key: FeatureTypes):
    with open('SimpleDB/features.json', 'r') as f:
        all_features = json.load(f)
        features = all_features.get(feature_key, [])
        response = '\n'.join([f"{right_padding(f'**{to_monospace(str(index))}**', 20)} - {value['feature']}" for (index, value) in
                              enumerate(features)])
        return response


def to_markdown(string):
    return f'```{string}```'