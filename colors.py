class Colors:
    white = '\033[0m'
    red = '\033[31m'
    blue = '\033[96m'
    yellow = '\033[33m'
    purple = '\033[35m'


def text_color_red(text):
    print(Colors.red + text + Colors.white)


def text_color_blue(text):
    print(Colors.blue + text + Colors.white)


def text_color_purple(text):
    print(Colors.purple + text + Colors.white)