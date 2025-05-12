import random

class ArithEval:
    symbols = {}
    
    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "concat": lambda args: str(args[0]) + str(args[1]),
        "/": lambda args: args[0] // args[1], #Divisão inteira
        "~": lambda args: -args[1], #Simétrico de um número
        "seq": lambda args: args[-1],
        "atr": lambda args: ArithEval._attrib(args),
        "esc": lambda args: print(args[0]),
        "string": lambda args: ArithEval._process_string(args[0]),
        "entrada": lambda args: ArithEval._entrada(),
    }
    
    @staticmethod
    def _attrib(args):
        value = args[1]
        ArithEval.symbols[args[0]] = 0
        return value
    
    @staticmethod
    def evaluate(ast):
        if type(ast) is int or type(ast) is str: #constant value, eg in (int, str)
            return ast
        if type(ast) is dict: #{'op': ..., 'args': ...}
            return ast
        if type(ast) is str:
            return ast
        raise Exception(f"Unknown AST type")
    
    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast:
            op = ast["op"]
            args = [ArithEval.evaluate(a) for a in ast['args']]
            if op in ArithEval.operators:
                func = ArithEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")
        
        if 'var' in ast:
            varid = ast["var"]
            if varid in ArithEval.symbols:
                return ArithEval.symbols[varid]
            raise Exception(f"Error: local variable '{varid}' referenced before assignment")
        
        raise Exception('Undefined AST')
    
    @staticmethod
    def _process_string(string):
        import re
        pattern = re.complice(r"#\{([a-zA-Z_][a-zA-Z_0-9]*)\}")
        result = string
        
        matches = pattern.findall(string)
        for var in matches:
            if var in ArithEval.symbols:
                result = result.replace(f"#{{{var}}}", str(ArithEval.symbols[var]))
            else:
                raise Exception(f"Variable {var} not defined")
        return result
    
    @staticmethod
    def _entrada():
        return input("Enter a value: ")