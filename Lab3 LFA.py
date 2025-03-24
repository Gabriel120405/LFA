import re
import math

# Token types
TOKEN_TYPES = {
    'NUMBER': r'\d+\.\d+|\d+',  # Matches integers and floats
    'PLUS': r'\+',
    'MINUS': r'\-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'/',
    'LEFTPAREN': r'\(',
    'RIGHTPAREN': r'\)',
    'SIN': r'sin',
    'COS': r'cos',
}

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES.items())

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"
        

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
    
    def tokenize(self):
        for match in re.finditer(TOKEN_REGEX, self.text):
            token_type = match.lastgroup
            value = match.group()
            if token_type == 'NUMBER':
                value = float(value) if '.' in value else int(value)
            self.tokens.append(Token(token_type, value))
        return self.tokens

if __name__ == "__main__":
    expression = "56 - 2 + sin(50)/cos(50)"
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    print(f"The input is: {expression}" )
    print(tokens)