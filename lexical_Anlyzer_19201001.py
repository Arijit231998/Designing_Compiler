import re

def is_Arithmetic_operator(ch):
    return ch in '+-*/'
def is_logical_operator(ch):
    return ch in '>=><==<=!='
def is_punctuation_operator(ch):
    return ch in ',;:'

def is_valid_keyword(word):
    keywords = {'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
                'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int',
                'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
                'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'}
    return word in keywords

def remove_comments(code):
    lines = code.splitlines()
    result = []# stores the non commented lines
    comment = False

    for line in lines:
        if '/*' in line:
            comment = True 
        if not comment:
            line = line.split('//')[0]  # Remove single-line comments
            result.append(line)
        if '*/' in line:
            comment = False

    return '\n'.join(result)
   

def is_valid_identifier(identifier):
    pattern=r"[a-zA-Z]+[0-9]*|[a-zA-Z]+"
    return bool(re.match(pattern, identifier))

def remove_spaces(code):
    lines = code.splitlines()
    result=[]
    for line in lines:
        words=line.split()
        clean_line =' '.join(filter(None,words))#selecting elements from words
        result.append(clean_line)
    return '\n'.join(result)

def is_a_constant(s):
    constant_regex = r"\b\d+\b"
    return bool(re.match(constant_regex, s))

def tokenize(code):
    code_without_comments = remove_comments(code)
    code_without_spaces = remove_spaces(code_without_comments)
    tokens =re.findall(r"[a-zA-Z_]\w*|[+*/-]|[><=!]=?|[,;:{}:]", code_without_spaces)
    return tokens

def generate_lexical_analysis(code):
    tokens = tokenize(code)
    token_types = {
        'Keyword': set(),
        'Identifier': set(),
        'Arithmetic Operator': set(),
        'Constant': set(),
        'Punctuation': set(),
        'Parenthesis': set()
    }

    for token in tokens:
        if is_valid_keyword(token):
            token_types['Keyword'].add(token)
        elif is_valid_identifier(token):
            token_types['Identifier'].add(token)
        elif is_Arithmetic_operator(token):
            token_types['Arithmetic Operator'].add(token)
        elif is_a_constant(token):
            token_types['Constant'].add(token)
        elif is_punctuation_operator(token):
            token_types['Punctuation'].add(token)
        elif token in '{}':
            token_types['Parenthesis'].add(token)

    return token_types

def generate_output(token_types):
    for token_type, tokens in token_types.items():
        print(f"{token_type} ({len(tokens)}): {', '.join(tokens)}")

if __name__ == "__main__":
    code = input("Enter the code: ")
    token_types = generate_lexical_analysis(code)
    generate_output(token_types)


