# Julian Niebieskikwiat Godoy - A01207868

import sys

if sys.version_info[0] >= 3:
    raw_input = input

reserved_words = {
    'input': 'INPUT',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'class': 'CLASS',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

tokens = (
    'NAME',
    'NUMBER',
    'STRING',
    'LINE_COMMENT',
    'POINT',
    'EQ',
    'NEQ',
    'GT',
    'LT',
    'GET',
    'LET',
    'ASSIGN',
    'SUM',
    'SUBST',
    'PROD',
    'DIV',
    'LPARENT',
    'RPARENT',
    'COL',
    'SEMCOL'
) + tuple(reserved_words.values())

# Tokens

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_words.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

line = r'.*'

t_STRING = r'("' + line + '"|\'' + line + '\')'

t_LINE_COMMENT = r'\#' + line

t_INPUT = r'input'
t_PRINT = r'print'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_POINT = r'\.'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_GET = r'>='
t_LET = r'<='
t_ASSIGN = r'='
t_SUM = r'\+'
t_SUBST = r'-'
t_PROD = r'\*'
t_DIV = r'/'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COL = r':'
t_SEMCOL = r';'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t"

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

"""
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)
"""

# dictionary of names
names = {}

def p_sum_expr(p):
    """sumExpr  : sumExpr sumop term
                | term
    """
    pass

def p_sumop(p):
    """sumop    : SUM
                | SUBST
    """
    pass

def p_term(p):
    """term : term mulop opElement
            | opElement
    """
    pass

def p_op_element(p):
    """opElement    : name
                    | number
    """
    pass

def p_mulop(p):
    """mulop    : PROD
                | DIV
    """
    pass

def p_input_stmt(p):
    """inputStmt : INPUT LPARENT RPARENT
    """
    pass

def p_output_stmt(p):
    """outputStmt : PRINT LPARENT STRING RPARENT
    """
    pass

def p_number(p):
    "number : NUMBER"
    p[0] = p[1]

def p_string(p):
    "string : STRING"
    p[0] = p[1]

def p_name(p):
    "name : NAME"
    # try:
        # p[0] = names[p[1]]
    # except LookupError:
        # print("Undefined name '%s'" % p[1])
        # p[0] = 0
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
    """
    try:
        s = raw_input('python 5.0 > ')
    except EOFError:
        break
    if not s:
        continue
    print(s)
    lexer.input(s)
    for token in lexer:
        print(token)
    print()
    """