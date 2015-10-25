import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), sys.stdout.encoding, 'replace')


def remove_comments(script):
    cm = False
    r = ''
    for char in script:
        if char == '#':
            cm = True
        elif char == '\n':
            cm = False
        else:
            r.append(char)

    return r


def lex(script):
    script = remove_comments(script)

    return [x for x in script]