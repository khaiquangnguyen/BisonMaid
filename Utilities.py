import Constants


def right_padding(s: str, desired_width: int = 70, padding_char = ' ') -> str:
    s_width = sum([Constants.font_sizes[x][0] for x in s])
    if padding_char not in Constants.font_sizes:
        padding_char = ' '
    return s + (desired_width - s_width) // Constants.font_sizes[padding_char][0] * padding_char
