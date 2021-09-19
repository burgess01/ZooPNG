
from sly import Lexer, Parser
from PIL import Image

class ZooLexer(Lexer):
    tokens = {IMAGES, ANIMAL, IF, THEN, ELSE, DISPLAY, EQEQ}
    ignore = ' \t'
    literals = {':'}
    #DISPLAY = r"DISPLAY"
    IMAGES = r'images'
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
    ANIMAL = r'[a-zA-Z_][a-zA-Z0-9_]*' #if this is usable 

    @_(r"\".*?\"")
    def STRING(self, t):
        t.value = t.value.strip("\"")

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
    
class ZooParser(Parser):
    tokens = ZooLexer.tokens
    #print(tokens)
    def __init__(self):
        pass
    
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

    @_('IMAGES ":" ANIMAL')
    def img_value(self, p):
        #print(p[2])
        # displays an image of the animal
        if(p[2] == "cat"):
            print("4 Legs")
            cat = 4
            im = Image.open(r"../img/cat.jpeg")
            im.show()
            
        elif p[2] == ("horse"):
            print("4 legs")
            im = Image.open(r"../img/horse.jpeg")
            im.show()
            
        elif p[2] == ("dog"):
            print("4 legs")
            im = Image.open(r"../img/dog.jpeg")
            im.show()

        elif p[2] == ("lion"):
            print("4 legs")
            
        elif p[2] == ("bee"):
            print("6 legs")

        elif p[2] == ("rooster"):
            print("2 legs")

        elif p[2] == ("bear"):
            print("4 legs")
            

       
if __name__ == '__main__':
    # Class to:
    #display images of animals
    #display the number of legs they have
    #display traits the animal has
    cat = 4
    dog = 4
    horse = 4
    lion = 4
    bear = 4

    lexer = ZooLexer()
    parser = ZooParser()
    #parser.parse(lexer.tokenize("images : cat"))
    parser.parse(lexer.tokenize("if dog == 4 then display \"true\" else display \"false\""))

    '''
    while True:
        try:
            text = input('Animals> ')
        except EOFError:
            break
        if text: 
            lex = lexer.tokenize(text)
            #for token in lex:
                #   print(token)
            parser.parse(lex)
    '''

            