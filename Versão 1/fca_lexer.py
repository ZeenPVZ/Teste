import ply.lex as lex

class ArithLexer:
    tokens = ("num", "varid", "escrever", "entrada", "string", "concat")
    
    literals = ['+', '-', '*', '(', ')', '=', ';']
    t_ignore = " \t"
    
    def __init__(self):
        self.lexer = None
    
    def t_num(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t
    
    def t_escrever(self, t):
        r"[a-z_][a-zA-Z_0-9]*(\?|!)?"
        return t
    
    def t_entrada(self, t):
        r"[a-z_][a-zA-Z_0-9]*(\?|!)?"
        return t
    
    def t_string(self, t):
        r'"([^\\"]|\\.)*"'
        t.value = t.value[1:-1] #Remove as aspas
        return t
    
    def t_concat(self, t):
        r"<>"
        return t
    
    def t_varid(self, t):
        r"[a-z_][a-zA-Z_0-9]*(\?|!)?"
        return t
    
    def t_comment (self, t):
        r"\-\-.*"
        pass #Ignora os comentários de uma linha
    
    def t_multiline_comment(self, t):
        r"\{\-(.|\n)*?\-\}"
        t.lexer.lineno += t.value.count('\n')
        pass #Ignora os comentários com várias linhas
    
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def input(self, string):
        self.lexer.input(string)
    
    def token(self):
        return self.lexer.token()
    
    def t_error(self, t):
        print(f"Token inesperado: [{t.value[:10]}]")
        t.lexer.skip(1)