# http://cs.indstate.edu/~jkinne/cs420-s2019/code/?view=./sly-calc.py
# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------

from sly import Lexer, Parser
class MPLLexer(Lexer):
    tokens = {IF, THEN, ELSE, DISPLAY, STRING, NUMBER, EQEQ}
    ignore = ' \t'
    literals = {':'}
    #DISPLAY = r"DISPLAY"
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    DISPLAY = r'display'
    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Tokens
    @_(r"\".*?\"")
    def STRING(self, t):
        t.value = t.value.strip("\"")
        return t
    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class MPLParser(Parser):
    tokens = MPLLexer.tokens
    #print(tokens)
    def __init__(self):
        pass
    @_('DISPLAY STRING')
    def statement(self, p):
        return p[1]
 
    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)
    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        #print("Debug", p.condition, p.statement0, p.statement1)
        #return ('if_stmt', p.condition, ('branch', p.statement0, p.statement1))
        if (p.condition):
            print(p.statement0) 
        else: 
            print(p.statement1)
    @_('expr EQEQ expr')
    def condition(self, p):
        if (p.expr0 == p.expr1): 
            return 1
        else: 
            return 0
   

if __name__ == '__main__':
    lexer = MPLLexer()
    parser = MPLParser()
    parser.parse(lexer.tokenize("if 15 == 15 then display \"true\" else display \"false\""))
    
      

    