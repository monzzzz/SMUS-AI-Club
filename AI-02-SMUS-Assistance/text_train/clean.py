import re

def noise_removal(text):
    text = re.sub("(<.*?>)", "", text)
    text = re.sub("(\\W|\\d)", "", text)

    text = text.strip()
    return text

def remove_headers_footers(text, header_patterns=None, footer_patterns=None):
    if header_patterns is None:
        header_patterns = [r'^.*Header.*$']
    if footer_patterns is None:
        footer_patterns = [r'^.*Footer.*$']

    for pattern in header_patterns + footer_patterns:
        text = re.sub(pattern, '', text, flags=re.MULTILINE)

    return text.strip()

def remove_special_characters(text, special_chars=None):
    if special_chars is None:
        special_chars = r'[^A-Za-z0-9\s\.,;:\'\"\?\!\-]'

    text = re.sub(special_chars, '', text)
    return text.strip()

def remove_repeated_substrings(text, pattern=r'\.{2,}'):
    text = re.sub(pattern, '.', text)
    return text.strip()

def remove_extra_spaces(text):
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()