
class colors:
    white = '\033[0m'
    red = '\033[31m'

def text_color_red(text):
    print(colors.red + text + colors.white)
