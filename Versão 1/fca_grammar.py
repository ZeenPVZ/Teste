import ply.yacc as pyacc
from fca_lexer import ArithLexer

class ArithGrammar:
    precedence = (
        ('left', '+', '-'), #Level=1 assoc=left
        ('left', '*'), #Level=2 assoc=left
    )
    
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None
    
    def build(self, **kwargs):
        self.lexer = ArithLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)
    
    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)
    
    def p_z(self, p):
        """Z : LstV ';'"""
        p[0] = p[1]
    
    def p_lstv_head(self, p):
        """LstV : V"""
        p[0] = {'op': 'seq', 'args': [p[1]]}
    
    def p_lstv_tail(self, p):
        """LstV : LstV ';' V"""
        lstArgs = p[1]['args']
        lstArgs.append(p[3])
        p[0] = {'op': 'seq', 'args': lstArgs}
    
    def p_atrib(self, p):
        """V : varid '=' E"""
        p[0] = {'op': 'atr', 'args': [p[1], p[3]]}
    
    def p_esc(self, p):
        """V : escrever E"""
        p[0] = {'op': 'esc', 'args': [p[2]]}
    
    def p_expr_op(self, p):
        """E : E '+' E
               | E '-' E
               | E '*' E"""
        p[0] = {'op': p[2], 'args': [p[1], p[3]]}
    
    def p_expr_pare(self, p):
        """E : '(' E ')'"""
        p[0] = p[2]
    
    def p_expr_num(self, p):
        """E : num"""
        p[0] = p[1]
    
    def p_expr_var(self, p):
        """E : varid"""
        p[0] = {'var': p[1]}
    
    def p_expr_string(self, p):
        """E : string"""
        p[0] = {'op': 'string', 'args': [p[1]]}
    
    def p_expr_concat(self, p):
        """E : E concat E"""
        p[0] = {'op': 'concat', 'args': [p[1], p[3]]}
    
    def p_expr_entrada(self, p):
        """E : entrada '(' ')'"""
        p[0] = {'op': 'entrada', 'args': []}
    
    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print(f"Syntax error: unexpected end of file")
        exit(1)