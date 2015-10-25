def removeHashComments(script):
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