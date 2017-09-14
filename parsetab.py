
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*/rightUMINUSNAME NUMBER STRING LINE_COMMENT INPUT PRINT IF ELSE WHILE POINT EQ NEQ GT LT GET LETstatement : NAME "=" expressionstatement : expressionexpression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expressionexpression : \'-\' expression %prec UMINUSexpression : \'(\' expression \')\'expression : NUMBERexpression : STRINGexpression : LINE_COMMENTexpression : POINTexpression : EQexpression : NEQexpression : GTexpression : GETexpression : LTexpression : LETexpression : INPUTexpression : PRINTexpression : IFexpression : ELSEexpression : WHILEexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,21,22,23,24,25,],[2,27,27,27,27,27,27,27,]),'-':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[4,-24,23,4,4,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,4,4,4,4,4,-7,-24,23,23,-3,-4,-5,-6,-8,]),'(':([0,4,5,21,22,23,24,25,],[5,5,5,5,5,5,5,5,]),'NUMBER':([0,4,5,21,22,23,24,25,],[6,6,6,6,6,6,6,6,]),'STRING':([0,4,5,21,22,23,24,25,],[7,7,7,7,7,7,7,7,]),'LINE_COMMENT':([0,4,5,21,22,23,24,25,],[8,8,8,8,8,8,8,8,]),'POINT':([0,4,5,21,22,23,24,25,],[9,9,9,9,9,9,9,9,]),'EQ':([0,4,5,21,22,23,24,25,],[10,10,10,10,10,10,10,10,]),'NEQ':([0,4,5,21,22,23,24,25,],[11,11,11,11,11,11,11,11,]),'GT':([0,4,5,21,22,23,24,25,],[12,12,12,12,12,12,12,12,]),'GET':([0,4,5,21,22,23,24,25,],[13,13,13,13,13,13,13,13,]),'LT':([0,4,5,21,22,23,24,25,],[14,14,14,14,14,14,14,14,]),'LET':([0,4,5,21,22,23,24,25,],[15,15,15,15,15,15,15,15,]),'INPUT':([0,4,5,21,22,23,24,25,],[16,16,16,16,16,16,16,16,]),'PRINT':([0,4,5,21,22,23,24,25,],[17,17,17,17,17,17,17,17,]),'IF':([0,4,5,21,22,23,24,25,],[18,18,18,18,18,18,18,18,]),'ELSE':([0,4,5,21,22,23,24,25,],[19,19,19,19,19,19,19,19,]),'WHILE':([0,4,5,21,22,23,24,25,],[20,20,20,20,20,20,20,20,]),'$end':([1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27,29,30,31,32,33,34,],[0,-24,-2,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-7,-24,-1,-3,-4,-5,-6,-8,]),'=':([2,],[21,]),'+':([2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27,28,29,30,31,32,33,34,],[-24,22,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-7,-24,22,22,-3,-4,-5,-6,-8,]),'*':([2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27,28,29,30,31,32,33,34,],[-24,24,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-7,-24,24,24,24,24,-5,-6,-8,]),'/':([2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27,28,29,30,31,32,33,34,],[-24,25,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-7,-24,25,25,25,25,-5,-6,-8,]),')':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,26,27,28,30,31,32,33,34,],[-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-7,-24,34,-3,-4,-5,-6,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,21,22,23,24,25,],[3,26,28,29,30,31,32,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME = expression','statement',3,'p_statement_assign','pythonInterpreter.py',122),
  ('statement -> expression','statement',1,'p_statement_expr','pythonInterpreter.py',127),
  ('expression -> expression + expression','expression',3,'p_expression_binop','pythonInterpreter.py',132),
  ('expression -> expression - expression','expression',3,'p_expression_binop','pythonInterpreter.py',133),
  ('expression -> expression * expression','expression',3,'p_expression_binop','pythonInterpreter.py',134),
  ('expression -> expression / expression','expression',3,'p_expression_binop','pythonInterpreter.py',135),
  ('expression -> - expression','expression',2,'p_expression_uminus','pythonInterpreter.py',147),
  ('expression -> ( expression )','expression',3,'p_expression_group','pythonInterpreter.py',152),
  ('expression -> NUMBER','expression',1,'p_expression_number','pythonInterpreter.py',156),
  ('expression -> STRING','expression',1,'p_expression_string','pythonInterpreter.py',160),
  ('expression -> LINE_COMMENT','expression',1,'p_expression_line_comment','pythonInterpreter.py',164),
  ('expression -> POINT','expression',1,'p_expression_point','pythonInterpreter.py',167),
  ('expression -> EQ','expression',1,'p_expression_eq','pythonInterpreter.py',171),
  ('expression -> NEQ','expression',1,'p_expression_neq','pythonInterpreter.py',175),
  ('expression -> GT','expression',1,'p_expression_gt','pythonInterpreter.py',179),
  ('expression -> GET','expression',1,'p_expression_get','pythonInterpreter.py',183),
  ('expression -> LT','expression',1,'p_expression_lt','pythonInterpreter.py',187),
  ('expression -> LET','expression',1,'p_expression_let','pythonInterpreter.py',191),
  ('expression -> INPUT','expression',1,'p_expression_input','pythonInterpreter.py',195),
  ('expression -> PRINT','expression',1,'p_expression_print','pythonInterpreter.py',199),
  ('expression -> IF','expression',1,'p_expression_if','pythonInterpreter.py',203),
  ('expression -> ELSE','expression',1,'p_expression_else','pythonInterpreter.py',207),
  ('expression -> WHILE','expression',1,'p_expression_while','pythonInterpreter.py',211),
  ('expression -> NAME','expression',1,'p_expression_name','pythonInterpreter.py',215),
]
