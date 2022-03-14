"""
Holds functions related to text colors.
"""

# Inspiration from:
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal


class Colors:
    """
    Used for set colors on consol text.
    """
    white = '\033[0m'
    red = '\033[31m'
    blue = '\033[96m'
    yellow = '\033[0;33m'
    pink = '\033[38;5;206m'
    green = '\033[0;32m'


def print_text_color_red(text):
    """
    Print the consol text red.
    """
    print(Colors.red + text + Colors.white)


def print_text_color_blue(text):
    """
    Print the consol text blue.
    """
    print(Colors.blue + text + Colors.white)


def print_text_color_yellow(text):
    """
    Print the consol text yellow.
    """
    print(Colors.yellow + text + Colors.white)


def print_text_color_green(text):
    """
    Print the consol text yellow.
    """
    print(Colors.green + text + Colors.white)
