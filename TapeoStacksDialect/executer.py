import lexer
import stack as st


def execute(script):
    script = lexer.lex(script)
    data = [st.Stack()]

    i = 0
    cont = True
    while cont == True and i < len(script):
        com = script[i]

        if com == '':
            pass