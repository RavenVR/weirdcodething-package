def convert(code):
    fcode = code.replace('can you please output this?', "print")
    fcode = fcode.replace('wait so', "if")
    fcode = fcode.replace('is this real?', "True")
    fcode = fcode.replace('okay now this is cap', "False")
    fcode = fcode.replace('enterpls', '\n')
    fcode = fcode.replace('ineedatabrq', "\t")
    fcode = fcode.replace('rlly?', 'while')
    fcode = fcode.replace('fr', ':')
    fcode = fcode.replace('please stop', 'break')
    fcode = fcode.replace('after all this shit, output this for me rq', 'return')
    fcode = fcode.replace('i need this function', 'def')
    fcode = fcode.replace('bro', '(')
    fcode = fcode.replace('stop', ')')
    fcode = fcode.replace('equals to', '=')
    fcode = fcode.replace('is equal to', '==')
    fcode = fcode.replace('this is NOT it', '!=')
    fcode = fcode.replace('im', '[')
    fcode = fcode.replace('angry!', ']')
    fcode = fcode.replace('inport', 'import')
    fcode = fcode.replace('fullstop', '.')
    exec(fcode)
    return fcode

def normalcodetofunnicode(code):
    fcode = code.replace("print", ' can you please output this? ')
    fcode = fcode.replace("if", ' wait so ')
    fcode = fcode.replace("True", ' is this real? ')
    fcode = fcode.replace("False", ' okay now this is cap ')
    fcode = fcode.replace('\n', ' enterpls ')
    fcode = fcode.replace("\t", ' ineedatabrq ')
    fcode = fcode.replace('while', ' rlly? ')
    fcode = fcode.replace(':', ' fr ')
    fcode = fcode.replace('break', ' please stop ')
    fcode = fcode.replace('return', ' after all this shit, output this for me rq ')
    fcode = fcode.replace('def', ' i need this function ')
    fcode = fcode.replace('(', ' bro ')
    fcode = fcode.replace(')', ' stop ')
    fcode = fcode.replace('=', ' equals to ')
    fcode = fcode.replace('==', ' is equal to ')
    fcode = fcode.replace('!=', ' this is NOT it ')
    fcode = fcode.replace('[', ' im ')
    fcode = fcode.replace(']',' angry! ')
    fcode = fcode.replace('import', ' inport ')
    fcode = fcode.replace('.',' fullstop ')
    print(fcode)

def helpmsg():
    """dont need to run this through a print func, it auto prints. just add this to your code: weirdcodething.help()"""
    print("""Names and assignment:
    can you please output this? - print
    wait so - if
    is this real? - True
    okay now this is cap - False
    enterpls - newline
    ineedatabrq - tab
    rlly? - while
    fr - :
    please stop - break
    after all this shit, output this for me rq - return
    i need this function - def
    bro - (
    stop - )
    equals to - =
    is equals to - ==
    this is NOT it - !=
    im - [
    angry! - ]
    inport - import
    fullstop - .
Usage:
    input
        import weirdcodething

        code = 'can you output this? bro 'hello world' stop

        weirdcodething.convert(code)

    output
        >> hello world""")