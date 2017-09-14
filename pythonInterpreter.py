# Julian Niebieskikwiat Godoy - A01207868

import sys

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME',
    'NUMBER',
    'STRING',
    'LINE_COMMENT',
    'INPUT',
    'PRINT',
    'IF',
    'ELSE',
    'WHILE',
    'POINT',
    'EQ',
    'NEQ',
    'GT',
    'LT',
    'GET',
    'LET',
)

literals = ['=', '+', '-', '*', '/', '(', ')', ':']

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

line = r'.*'

t_STRING = r'("' + line + '"|\'' + line + '\')'

t_LINE_COMMENT = r'\#' + line

def t_POINT(t):
    r'\.'
    return t

def t_EQ(t):
    r'=='
    return t

def t_NEQ(t):
    r'!='
    return t

def t_GT(t):
    r'>'
    return t

def t_GET(t):
    r'>='
    return t

def t_LT(t):
    r'<'
    return t

def t_LET(t):
    r'<='
    return t

def t_INPUT(t):
    #r'input\(' + t_STRING + '\)'
    r'input'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]


def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_string(p):
    "expression : STRING"
    p[0] = p[1]

def p_expression_line_comment(p):
    "expression : LINE_COMMENT"

def p_expression_point(p):
    "expression : POINT"
    # TODO: handle point in objects

def p_expression_eq(p):
    "expression : EQ"
    # TODO: handle equals

def p_expression_neq(p):
    "expression : NEQ"
    # TODO: handle not equals

def p_expression_gt(p):
    "expression : GT"
    # TODO: handle greater than

def p_expression_get(p):
    "expression : GET"
    # TODO: handle greater or equals than

def p_expression_lt(p):
    "expression : LT"
    # TODO: handle less than

def p_expression_let(p):
    "expression : LET"
    # TODO: handle less or equals than

def p_expression_input(p):
    "expression : INPUT"
    # TODO: handle input

def p_expression_print(p):
    "expression : PRINT"
    # TODO: handle print

def p_expression_if(p):
    "expression : IF"
    # TODO: handle if

def p_expression_else(p):
    "expression : ELSE"
    # TODO: handle else

def p_expression_while(p):
    "expression : WHILE"
    # TODO: handle while

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while 1:
    """
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
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