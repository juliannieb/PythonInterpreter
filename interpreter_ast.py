class SymbolTable:
    
    def __init__(self):
        self.symbol_table = dict()
    
    def __str__(self):
        return "{0}".format(self.symbol_table)

    def add_object(self, key, new_obj):
        self.symbol_table[key] = new_obj
        print(self.symbol_table)
    
    def get_object(self, key):
        try:
            return self.symbol_table[key]
        except LookupError:
            print("Undefined name '%s'" % key)
            return 0


symbol_table = SymbolTable()

class Node(object):

    def execute(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Suite(Node):
    """suite    : stmt
                | stmt suite
    """
    def __init__(self, stmt, suite=None):
        self.stmt = stmt
        self.suite = suite
    
    def execute(self):
        self.stmt.execute()
        if self.suite:
            self.suite.execute()

class Stmt(Node):
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
    def __init__(self, stmt):
        self.stmt = stmt
    
    def execute(self):
        self.stmt.execute()

class Declar(Node):
    """declar   : varDeclar SEMCOL
                | funcDeclar
                | objDeclar
    """
    def __init__(self, declar):
        self.declar = declar
    
    def execute(self):
        return self.declar.execute()

class VarDeclar(Node):
    """varDeclar    : NAME ASSIGN STRING
                    | NAME ASSIGN exprStmt
                    | NAME ASSIGN inputStmt
    """
    def __init__(self, name, assign, val):
        self.name = name
        self.assign = assign
        self.val = val

    def execute(self):
        if str(self.val)[0] == "'" or str(self.val)[0] == '"':
            symbol_table.add_object(str(self.name), self.val)
            return self.val
        else:
            value = self.val.execute()
            symbol_table.add_object(str(self.name), value)
            return value

class FuncDeclar(Node):
    """funcDeclar   : DEF NAME LPARENT RPARENT COL suite
                    | DEF NAME LPARENT params RPARENT COL suite
    """
    pass

class Params(Node):
    """params   : paramsList
    """
    pass

class Params_list(Node):
    """paramsList   : NAME COMA paramsList
                    | NAME
    """
    pass

class ObjDeclaration(Node):
    """objDeclar    : CLASS NAME COL suite
    """
    pass

class Call(Node):
    """call : NAME
            | NAME POINT call
            | NAME LPARENT RPARENT
            | NAME LPARENT params RPARENT
            | call POINT call
    """
    def __init__(self, name=None):
        self.name = name

    def execute(self):
        if self.name:
            return symbol_table.get_object(str(self.name))

class ExprStmt(Node):
    """exprStmt : simpleExpr
    """
    def __init__(self, simpleExpr):
        self.simpleExpr = simpleExpr
    
    def execute(self):
        return self.simpleExpr.execute()

class SelectionStmt(Node):
    """selectionStmt    : IF simpleExpr COL suite
                        | IF simpleExpr COL suite ELSE COL suite
    """
    def __init__(self, simpleExpr, suite1, suite2=None):
        self.simpleExpr = simpleExpr
        self.suite1 = suite1
        self.suite2 = suite2
    
    def execute(self):
        if self.simpleExpr.execute():
            self.suite1.execute()
        elif self.suite2:
            self.suite2.execute()

class IterationStmt(Node):
    """iterationStmt    : WHILE simpleExpr COL suite
    """
    pass

class Return(Node):
    """returnStmt   : RETURN
                    | RETURN simpleExpr
    """
    pass

class SimpleExpr(Node):
    """simpleExpr   : simpleExpr OR andExpr
                    | andExpr
    """
    def __init__(self, simpleExpr=None, orToken=None, andExpr=None):
        self.simpleExpr = simpleExpr
        self.orToken = orToken
        self.andExpr = andExpr
    
    def execute(self):
        if self.orToken:
            return self.simpleExpr.execute() or self.andExpr.execute()
        else:
            return self.andExpr.execute()

class AndExpr(Node):
    """andExpr  : andExpr AND unaryRelExpr
                | unaryRelExpr
    """
    def __init__(self, andExpr=None, andToken=None, unaryRelExpr=None):
        self.andExpr = andExpr
        self.andToken = andToken
        self.unaryRelExpr = unaryRelExpr
    
    def execute(self):
        if self.andToken:
            return self.andExpr.execute() and self.unaryRelExpr.execute()
        else:
            return self.unaryRelExpr.execute()

class UnaryRelExpr(Node):
    """unaryRelExpr : NOT unaryRelExpr
                    | relExpr
    """
    def __init__(self, notToken=None, unaryRelExpr=None, relExpr=None):
        self.notToken = notToken
        self.unaryRelExpr = unaryRelExpr
        self.relExpr = relExpr

    def execute(self):
        if self.notToken:
            return not self.unaryRelExpr.execute()
        else:
            return self.relExpr.execute()

class RelExpr(Node):
    """relExpr  : sumExpr relop sumExpr
                | sumExpr
    """
    def __init__(self, sumExpr1=None, relop=None, sumExpr2=None):
        self.sumExpr1 = sumExpr1
        self.relop = relop
        self.sumExpr2 = sumExpr2
    
    def execute(self):
        if self.relop:
            if self.relop.execute() == '<=': return self.sumExpr1.execute() <= self.sumExpr2.execute()
            elif self.relop.execute() == '<': return self.sumExpr1.execute() < self.sumExpr2.execute()
            elif self.relop.execute() == '>=': return self.sumExpr1.execute() >= self.sumExpr2.execute()
            elif self.relop.execute() == '>': return self.sumExpr1.execute() > self.sumExpr2.execute()
            elif self.relop.execute() == '==': return self.sumExpr1.execute() == self.sumExpr2.execute()
            elif self.relop.execute() == '!=': return self.sumExpr1.execute() != self.sumExpr2.execute()
        else:
            return self.sumExpr1.execute()

class Relop(Node):
    """relop    : LTE
                | LT
                | GTE
                | GT
                | EQ
                | NEQ
    """
    def __init__(self, token):
        self.token = token
    
    def execute(self):
        return self.token

class SumExpr(Node):
    """sumExpr  : sumExpr sumop term
                | term
    """
    def __init__(self, sumExpr=None, sumop=None, term=None):
        self.sumExpr = sumExpr
        self.sumop = sumop
        self.term = term
    
    def execute(self):
        if self.sumop:
            if self.sumop.execute() == '+': return self.sumExpr.execute() + self.term.execute()
            elif self.sumop.execute() == '-': return self.sumExpr.execute() - self.term.execute()
        else:
            return self.term.execute()

class Sumop(Node):
    """sumop    : SUM
                | SUBST
    """
    def __init__(self, token):
        self.token = token
    
    def execute(self):
        return self.token

class Term(Node):
    """term : term mulop opElement
            | opElement
    """
    def __init__(self, term=None, mulop=None, opElement=None):
        self.term = term
        self.mulop = mulop
        self.opElement = opElement

    def execute(self):
        if self.mulop:
            if self.mulop.execute() == '*': return self.term.execute() * self.opElement.execute()
            elif self.mulop.execute() == '/': return self.term.execute() / self.opElement.execute()
        else:
            return self.opElement.execute()

class OpElement(Node):
    """opElement    : call
                    | NUMBER
    """
    def __init__(self, opElement):
        self.opElement = opElement
    
    def execute(self):
        if str(self.opElement).isdigit():
            return self.opElement
        else:
            return self.opElement.execute()

class Mulop(Node):
    """mulop    : PROD
                | DIV
    """
    def __init__(self, token):
        self.token = token
    
    def execute(self):
        return self.token

class InputStmt(Node):
    """inputStmt : INPUT LPARENT RPARENT
    """
    def __init__(self):
        self.type = 'INPUT'
    
    def execute(self):
        return input()

class OutputStmt(Node):
    """outputStmt   : PRINT LPARENT STRING RPARENT
                    | PRINT LPARENT NAME RPARENT
    """
    def __init__(self, printElement):
        self.printElement = printElement
    
    def execute(self):
        if (self.printElement[0] == '"' or self.printElement[0] == "'"):
            print(self.printElement)
        else:
            print(symbol_table.get_object(str(self.printElement)))

class CommentLine(Node):
    """commentLine  : LINE_COMMENT
    """
    pass