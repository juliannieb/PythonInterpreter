
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NAME NUMBER STRING LINE_COMMENT POINT EQ NEQ GT LT GTE LTE ASSIGN SUM SUBST PROD DIV LPARENT RPARENT COL SEMCOL COMA INPUT PRINT IF ELSE WHILE CLASS AND OR NOT RETURN DEFsuite    : stmt\n                | stmt suite\n    stmt : exprStmt\n            | declar\n            | call SEMCOL\n            | selectionStmt\n            | iterationStmt\n            | returnStmt SEMCOL\n            | inputStmt SEMCOL\n            | outputStmt SEMCOL\n            | commentLine\n    declar   : varDeclar SEMCOL\n                | funcDeclar\n                | objDeclar\n    varDeclar    : NAME ASSIGN STRING\n                    | NAME ASSIGN NUMBER\n                    | NAME ASSIGN NAME\n                    | NAME ASSIGN objConstruct\n    funcDeclar   : DEF NAME LPARENT RPARENT COL suite\n                    | DEF NAME LPARENT params RPARENT COL suite\n    params   : paramsList\n    paramsList   : NAME COMA paramsList\n                    | NAME\n    objDeclar    : CLASS NAME COL suite\n    objConstruct : NAME LPARENT RPARENT\n                    | NAME LPARENT params RPARENT\n    call : NAME\n            | NAME POINT call\n            | NAME LPARENT RPARENT\n            | NAME LPARENT params RPARENT\n            | call POINT call\n    exprStmt : simpleExpr\n    selectionStmt    : IF simpleExpr COL suite\n                        | IF simpleExpr COL suite ELSE COL suite\n    iterationStmt    : WHILE simpleExpr COL suite\n    returnStmt   : RETURN\n                    | RETURN simpleExpr\n    simpleExpr   : simpleExpr OR andExpr\n                    | andExpr\n    andExpr  : andExpr AND unaryRelExpr\n                | unaryRelExpr\n    unaryRelExpr : NOT unaryRelExpr\n                    | relExpr\n    relExpr  : sumExpr relop sumExpr\n                | sumExpr\n    relop    : LTE\n                | LT\n                | GTE\n                | GT\n                | EQ\n                | NEQ\n    sumExpr  : sumExpr sumop term\n                | term\n    sumop    : SUM\n                | SUBST\n    term : term mulop opElement\n            | opElement\n    opElement    : call\n                    | NUMBER\n    mulop    : PROD\n                | DIV\n    inputStmt : INPUT LPARENT RPARENT\n    outputStmt : PRINT LPARENT STRING RPARENT\n    commentLine  : LINE_COMMENT\n    '
    
_lr_action_items = {'NAME':([0,2,3,4,5,6,7,11,12,14,15,16,17,18,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,79,80,83,84,85,86,87,88,89,90,91,92,93,97,102,105,106,107,108,109,],[16,16,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,46,46,46,-64,-39,-59,52,53,-41,46,-43,-45,-53,-57,-2,-5,46,-8,-9,-10,46,-12,46,71,75,-58,-27,46,-42,46,46,-46,-47,-48,-49,-50,-51,-54,-55,46,-60,-61,-31,-38,-28,-29,16,16,-40,71,16,-44,-52,-56,71,-30,71,-33,-35,-24,16,16,-19,16,-34,-20,]),'IF':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[17,17,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,17,17,-40,17,-44,-52,-56,-30,-33,-35,-24,17,17,-19,17,-34,-20,]),'WHILE':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[18,18,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,18,18,-40,18,-44,-52,-56,-30,-33,-35,-24,18,18,-19,18,-34,-20,]),'RETURN':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[19,19,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,19,19,-40,19,-44,-52,-56,-30,-33,-35,-24,19,19,-19,19,-34,-20,]),'INPUT':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[20,20,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,20,20,-40,20,-44,-52,-56,-30,-33,-35,-24,20,20,-19,20,-34,-20,]),'PRINT':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[21,21,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,21,21,-40,21,-44,-52,-56,-30,-33,-35,-24,21,21,-19,21,-34,-20,]),'LINE_COMMENT':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[22,22,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,22,22,-40,22,-44,-52,-56,-30,-33,-35,-24,22,22,-19,22,-34,-20,]),'DEF':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[25,25,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,25,25,-40,25,-44,-52,-56,-30,-33,-35,-24,25,25,-19,25,-34,-20,]),'CLASS':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[26,26,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,26,26,-40,26,-44,-52,-56,-30,-33,-35,-24,26,26,-19,26,-34,-20,]),'NOT':([0,2,3,4,5,6,7,11,12,14,15,16,17,18,19,22,23,24,27,28,29,30,31,32,33,34,36,37,38,39,40,45,46,51,54,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[28,28,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,28,28,28,-64,-39,-59,-41,28,-43,-45,-53,-57,-2,-5,-8,-9,-10,28,-12,-58,-27,28,-42,-31,-38,-28,-29,28,28,-40,28,-44,-52,-56,-30,-33,-35,-24,28,28,-19,28,-34,-20,]),'NUMBER':([0,2,3,4,5,6,7,11,12,14,15,16,17,18,19,22,23,24,27,28,29,30,31,32,33,34,36,37,38,39,40,43,45,46,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,79,80,83,85,86,87,88,90,92,93,97,102,105,106,107,108,109,],[24,24,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,24,24,24,-64,-39,-59,-41,24,-43,-45,-53,-57,-2,-5,-8,-9,-10,24,-12,77,-58,-27,24,-42,24,24,-46,-47,-48,-49,-50,-51,-54,-55,24,-60,-61,-31,-38,-28,-29,24,24,-40,24,-44,-52,-56,-30,-33,-35,-24,24,24,-19,24,-34,-20,]),'$end':([1,2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,83,86,87,88,90,92,93,97,106,108,109,],[0,-1,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,-40,-44,-52,-56,-30,-33,-35,-24,-19,-34,-20,]),'ELSE':([2,3,4,5,6,7,11,12,14,15,16,22,23,24,27,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,83,86,87,88,90,92,93,97,106,108,109,],[-1,-3,-4,-58,-6,-7,-11,-32,-13,-14,-27,-64,-39,-59,-41,-43,-45,-53,-57,-2,-5,-8,-9,-10,-12,-58,-27,-42,-31,-38,-28,-29,-40,-44,-52,-56,-30,101,-35,-24,-19,-34,-20,]),'SEMCOL':([5,8,9,10,13,16,19,23,24,27,29,30,31,32,45,46,48,54,68,69,70,72,75,76,77,78,81,83,86,87,88,90,94,99,104,],[34,36,37,38,40,-27,-36,-39,-59,-41,-43,-45,-53,-57,-58,-27,-37,-42,-31,-38,-28,-29,-17,-15,-16,-18,-62,-40,-44,-52,-56,-30,-63,-25,-26,]),'POINT':([5,16,45,46,68,70,72,90,],[35,41,35,41,35,35,-29,-30,]),'PROD':([5,16,24,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,66,-57,-58,-27,-31,-28,-29,66,-56,-30,]),'DIV':([5,16,24,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,67,-57,-58,-27,-31,-28,-29,67,-56,-30,]),'LTE':([5,16,24,30,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,57,-53,-57,-58,-27,-31,-28,-29,-52,-56,-30,]),'LT':([5,16,24,30,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,58,-53,-57,-58,-27,-31,-28,-29,-52,-56,-30,]),'GTE':([5,16,24,30,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,59,-53,-57,-58,-27,-31,-28,-29,-52,-56,-30,]),'GT':([5,16,24,30,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,60,-53,-57,-58,-27,-31,-28,-29,-52,-56,-30,]),'EQ':([5,16,24,30,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,61,-53,-57,-58,-27,-31,-28,-29,-52,-56,-30,]),'NEQ':([5,16,24,30,31,32,45,46,68,70,72,87,88,90,],[-58,-27,-59,62,-53,-57,-58,-27,-31,-28,-29,-52,-56,-30,]),'SUM':([5,16,24,30,31,32,45,46,68,70,72,86,87,88,90,],[-58,-27,-59,63,-53,-57,-58,-27,-31,-28,-29,63,-52,-56,-30,]),'SUBST':([5,16,24,30,31,32,45,46,68,70,72,86,87,88,90,],[-58,-27,-59,64,-53,-57,-58,-27,-31,-28,-29,64,-52,-56,-30,]),'AND':([5,16,23,24,27,29,30,31,32,45,46,54,68,69,70,72,83,86,87,88,90,],[-58,-27,51,-59,-41,-43,-45,-53,-57,-58,-27,-42,-31,51,-28,-29,-40,-44,-52,-56,-30,]),'OR':([5,12,16,23,24,27,29,30,31,32,44,45,46,47,48,54,68,69,70,72,83,86,87,88,90,],[-58,39,-27,-39,-59,-41,-43,-45,-53,-57,39,-58,-27,39,39,-42,-31,-38,-28,-29,-40,-44,-52,-56,-30,]),'LPARENT':([16,20,21,46,52,75,],[42,49,50,42,84,91,]),'ASSIGN':([16,],[43,]),'COL':([23,24,27,29,30,31,32,44,45,46,47,53,54,68,69,70,72,83,86,87,88,90,95,101,103,],[-39,-59,-41,-43,-45,-53,-57,79,-58,-27,80,85,-42,-31,-38,-28,-29,-40,-44,-52,-56,-30,102,105,107,]),'RPARENT':([42,49,71,73,74,82,84,91,96,98,100,],[72,81,-23,90,-21,94,95,99,103,-22,104,]),'STRING':([43,50,],[76,82,]),'COMA':([71,],[89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'suite':([0,2,79,80,85,102,105,107,],[1,33,92,93,97,106,108,109,]),'stmt':([0,2,79,80,85,102,105,107,],[2,2,2,2,2,2,2,2,]),'exprStmt':([0,2,79,80,85,102,105,107,],[3,3,3,3,3,3,3,3,]),'declar':([0,2,79,80,85,102,105,107,],[4,4,4,4,4,4,4,4,]),'call':([0,2,17,18,19,28,35,39,41,51,55,56,65,79,80,85,102,105,107,],[5,5,45,45,45,45,68,45,70,45,45,45,45,5,5,5,5,5,5,]),'selectionStmt':([0,2,79,80,85,102,105,107,],[6,6,6,6,6,6,6,6,]),'iterationStmt':([0,2,79,80,85,102,105,107,],[7,7,7,7,7,7,7,7,]),'returnStmt':([0,2,79,80,85,102,105,107,],[8,8,8,8,8,8,8,8,]),'inputStmt':([0,2,79,80,85,102,105,107,],[9,9,9,9,9,9,9,9,]),'outputStmt':([0,2,79,80,85,102,105,107,],[10,10,10,10,10,10,10,10,]),'commentLine':([0,2,79,80,85,102,105,107,],[11,11,11,11,11,11,11,11,]),'simpleExpr':([0,2,17,18,19,79,80,85,102,105,107,],[12,12,44,47,48,12,12,12,12,12,12,]),'varDeclar':([0,2,79,80,85,102,105,107,],[13,13,13,13,13,13,13,13,]),'funcDeclar':([0,2,79,80,85,102,105,107,],[14,14,14,14,14,14,14,14,]),'objDeclar':([0,2,79,80,85,102,105,107,],[15,15,15,15,15,15,15,15,]),'andExpr':([0,2,17,18,19,39,79,80,85,102,105,107,],[23,23,23,23,23,69,23,23,23,23,23,23,]),'unaryRelExpr':([0,2,17,18,19,28,39,51,79,80,85,102,105,107,],[27,27,27,27,27,54,27,83,27,27,27,27,27,27,]),'relExpr':([0,2,17,18,19,28,39,51,79,80,85,102,105,107,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'sumExpr':([0,2,17,18,19,28,39,51,55,79,80,85,102,105,107,],[30,30,30,30,30,30,30,30,86,30,30,30,30,30,30,]),'term':([0,2,17,18,19,28,39,51,55,56,79,80,85,102,105,107,],[31,31,31,31,31,31,31,31,31,87,31,31,31,31,31,31,]),'opElement':([0,2,17,18,19,28,39,51,55,56,65,79,80,85,102,105,107,],[32,32,32,32,32,32,32,32,32,32,88,32,32,32,32,32,32,]),'relop':([30,],[55,]),'sumop':([30,86,],[56,56,]),'mulop':([31,87,],[65,65,]),'params':([42,84,91,],[73,96,100,]),'paramsList':([42,84,89,91,],[74,74,98,74,]),'objConstruct':([43,],[78,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> suite","S'",1,None,None,None),
  ('suite -> stmt','suite',1,'p_suite','pythonInterpreter.py',115),
  ('suite -> stmt suite','suite',2,'p_suite','pythonInterpreter.py',116),
  ('stmt -> exprStmt','stmt',1,'p_stmt','pythonInterpreter.py',121),
  ('stmt -> declar','stmt',1,'p_stmt','pythonInterpreter.py',122),
  ('stmt -> call SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',123),
  ('stmt -> selectionStmt','stmt',1,'p_stmt','pythonInterpreter.py',124),
  ('stmt -> iterationStmt','stmt',1,'p_stmt','pythonInterpreter.py',125),
  ('stmt -> returnStmt SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',126),
  ('stmt -> inputStmt SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',127),
  ('stmt -> outputStmt SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',128),
  ('stmt -> commentLine','stmt',1,'p_stmt','pythonInterpreter.py',129),
  ('declar -> varDeclar SEMCOL','declar',2,'p_declar','pythonInterpreter.py',133),
  ('declar -> funcDeclar','declar',1,'p_declar','pythonInterpreter.py',134),
  ('declar -> objDeclar','declar',1,'p_declar','pythonInterpreter.py',135),
  ('varDeclar -> NAME ASSIGN STRING','varDeclar',3,'p_var_declar','pythonInterpreter.py',140),
  ('varDeclar -> NAME ASSIGN NUMBER','varDeclar',3,'p_var_declar','pythonInterpreter.py',141),
  ('varDeclar -> NAME ASSIGN NAME','varDeclar',3,'p_var_declar','pythonInterpreter.py',142),
  ('varDeclar -> NAME ASSIGN objConstruct','varDeclar',3,'p_var_declar','pythonInterpreter.py',143),
  ('funcDeclar -> DEF NAME LPARENT RPARENT COL suite','funcDeclar',6,'p_func_declar','pythonInterpreter.py',148),
  ('funcDeclar -> DEF NAME LPARENT params RPARENT COL suite','funcDeclar',7,'p_func_declar','pythonInterpreter.py',149),
  ('params -> paramsList','params',1,'p_params','pythonInterpreter.py',154),
  ('paramsList -> NAME COMA paramsList','paramsList',3,'p_params_list','pythonInterpreter.py',159),
  ('paramsList -> NAME','paramsList',1,'p_params_list','pythonInterpreter.py',160),
  ('objDeclar -> CLASS NAME COL suite','objDeclar',4,'p_obj_declaration','pythonInterpreter.py',165),
  ('objConstruct -> NAME LPARENT RPARENT','objConstruct',3,'p_obj_construct','pythonInterpreter.py',170),
  ('objConstruct -> NAME LPARENT params RPARENT','objConstruct',4,'p_obj_construct','pythonInterpreter.py',171),
  ('call -> NAME','call',1,'p_call','pythonInterpreter.py',176),
  ('call -> NAME POINT call','call',3,'p_call','pythonInterpreter.py',177),
  ('call -> NAME LPARENT RPARENT','call',3,'p_call','pythonInterpreter.py',178),
  ('call -> NAME LPARENT params RPARENT','call',4,'p_call','pythonInterpreter.py',179),
  ('call -> call POINT call','call',3,'p_call','pythonInterpreter.py',180),
  ('exprStmt -> simpleExpr','exprStmt',1,'p_expr_stmt','pythonInterpreter.py',205),
  ('selectionStmt -> IF simpleExpr COL suite','selectionStmt',4,'p_selection_stmt','pythonInterpreter.py',210),
  ('selectionStmt -> IF simpleExpr COL suite ELSE COL suite','selectionStmt',7,'p_selection_stmt','pythonInterpreter.py',211),
  ('iterationStmt -> WHILE simpleExpr COL suite','iterationStmt',4,'p_iteration_stmt','pythonInterpreter.py',216),
  ('returnStmt -> RETURN','returnStmt',1,'p_return','pythonInterpreter.py',221),
  ('returnStmt -> RETURN simpleExpr','returnStmt',2,'p_return','pythonInterpreter.py',222),
  ('simpleExpr -> simpleExpr OR andExpr','simpleExpr',3,'p_simple_expr','pythonInterpreter.py',227),
  ('simpleExpr -> andExpr','simpleExpr',1,'p_simple_expr','pythonInterpreter.py',228),
  ('andExpr -> andExpr AND unaryRelExpr','andExpr',3,'p_and_expr','pythonInterpreter.py',233),
  ('andExpr -> unaryRelExpr','andExpr',1,'p_and_expr','pythonInterpreter.py',234),
  ('unaryRelExpr -> NOT unaryRelExpr','unaryRelExpr',2,'p_unary_rel_expr','pythonInterpreter.py',239),
  ('unaryRelExpr -> relExpr','unaryRelExpr',1,'p_unary_rel_expr','pythonInterpreter.py',240),
  ('relExpr -> sumExpr relop sumExpr','relExpr',3,'p_rel_expr','pythonInterpreter.py',245),
  ('relExpr -> sumExpr','relExpr',1,'p_rel_expr','pythonInterpreter.py',246),
  ('relop -> LTE','relop',1,'p_relop','pythonInterpreter.py',251),
  ('relop -> LT','relop',1,'p_relop','pythonInterpreter.py',252),
  ('relop -> GTE','relop',1,'p_relop','pythonInterpreter.py',253),
  ('relop -> GT','relop',1,'p_relop','pythonInterpreter.py',254),
  ('relop -> EQ','relop',1,'p_relop','pythonInterpreter.py',255),
  ('relop -> NEQ','relop',1,'p_relop','pythonInterpreter.py',256),
  ('sumExpr -> sumExpr sumop term','sumExpr',3,'p_sum_expr','pythonInterpreter.py',261),
  ('sumExpr -> term','sumExpr',1,'p_sum_expr','pythonInterpreter.py',262),
  ('sumop -> SUM','sumop',1,'p_sumop','pythonInterpreter.py',267),
  ('sumop -> SUBST','sumop',1,'p_sumop','pythonInterpreter.py',268),
  ('term -> term mulop opElement','term',3,'p_term','pythonInterpreter.py',273),
  ('term -> opElement','term',1,'p_term','pythonInterpreter.py',274),
  ('opElement -> call','opElement',1,'p_op_element','pythonInterpreter.py',279),
  ('opElement -> NUMBER','opElement',1,'p_op_element','pythonInterpreter.py',280),
  ('mulop -> PROD','mulop',1,'p_mulop','pythonInterpreter.py',285),
  ('mulop -> DIV','mulop',1,'p_mulop','pythonInterpreter.py',286),
  ('inputStmt -> INPUT LPARENT RPARENT','inputStmt',3,'p_input_stmt','pythonInterpreter.py',291),
  ('outputStmt -> PRINT LPARENT STRING RPARENT','outputStmt',4,'p_output_stmt','pythonInterpreter.py',296),
  ('commentLine -> LINE_COMMENT','commentLine',1,'p_comment_line','pythonInterpreter.py',301),
]
