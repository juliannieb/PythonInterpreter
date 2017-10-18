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
    'not': 'NOT',
    'return': 'RETURN',
    'def': 'DEF'
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
    'GTE',
    'LTE',
    'ASSIGN',
    'SUM',
    'SUBST',
    'PROD',
    'DIV',
    'LPARENT',
    'RPARENT',
    'COL',
    'SEMCOL',
    'COMA'
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
t_GTE = r'>='
t_LTE = r'<='
t_ASSIGN = r'='
t_SUM = r'\+'
t_SUBST = r'-'
t_PROD = r'\*'
t_DIV = r'/'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COL = r':'
t_SEMCOL = r';'
t_COMA = r','

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

def p_suite(p):
    """suite    : stmt
                | stmt suite
    """
    pass

def p_stmt(p):
    """stmt : exprStmt
            | declar
            | call SEMCOL
            | selectionStmt
            | iterationStmt
            | returnStmt SEMCOL
            | inputStmt SEMCOL
            | outputStmt SEMCOL
            | commentLine
    """

def p_declar(p):
    """declar   : varDeclar SEMCOL
                | funcDeclar
                | objDeclar
    """
    pass

def p_var_declar(p):
    """varDeclar    : NAME ASSIGN STRING
                    | NAME ASSIGN NUMBER
                    | NAME ASSIGN NAME
                    | NAME ASSIGN objConstruct
    """
    pass

def p_func_declar(p):
    """funcDeclar   : DEF NAME LPARENT RPARENT COL suite
                    | DEF NAME LPARENT params RPARENT COL suite
    """
    pass

def p_params(p):
    """params   : paramsList
    """
    pass

def p_params_list(p):
    """paramsList   : NAME COMA paramsList
                    | NAME
    """
    pass

def p_obj_declaration(p):
    """objDeclar    : CLASS NAME COL suite
    """
    pass

def p_obj_construct(p):
    """objConstruct : NAME LPARENT RPARENT
                    | NAME LPARENT params RPARENT
    """
    pass

def p_call(p):
    """call : NAME
            | NAME POINT call
            | NAME LPARENT RPARENT
            | NAME LPARENT params RPARENT
            | call POINT call
    """
    pass

def p_expr_stmt(p):
    """exprStmt : simpleExpr
    """
    pass

def p_selection_stmt(p):
    """selectionStmt    : IF simpleExpr COL suite
                        | IF simpleExpr COL suite ELSE COL suite
    """
    pass

def p_iteration_stmt(p):
    """iterationStmt    : WHILE simpleExpr COL suite
    """
    pass

def p_return(p):
    """returnStmt   : RETURN
                    | RETURN simpleExpr
    """
    pass

def p_simple_expr(p):
    """simpleExpr   : simpleExpr OR andExpr
                    | andExpr
    """
    pass

def p_and_expr(p):
    """andExpr  : andExpr AND unaryRelExpr
                | unaryRelExpr
    """
    pass

def p_unary_rel_expr(p):
    """unaryRelExpr : NOT unaryRelExpr
                    | relExpr
    """
    pass

def p_rel_expr(p):
    """relExpr  : sumExpr relop sumExpr
                | sumExpr
    """
    pass

def p_relop(p):
    """relop    : LTE
                | LT
                | GTE
                | GT
                | EQ
                | NEQ
    """
    pass

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
    """opElement    : call
                    | NUMBER
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

def p_comment_line(p):
    """commentLine  : LINE_COMMENT
    """
    pass

"""
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
"""

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

while 1:
    try:
        s = raw_input('python -2.7 > ')
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