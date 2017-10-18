
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NAME NUMBER STRING LINE_COMMENT POINT EQ NEQ GT LT GTE LTE ASSIGN SUM SUBST PROD DIV LPARENT RPARENT COL SEMCOL COMA INPUT PRINT IF ELSE WHILE CLASS AND OR NOT RETURN DEFsuite    : stmt\n                | stmt suite\n    stmt : exprStmt\n            | declar\n            | call SEMCOL\n            | selectionStmt\n            | iterationStmt\n            | returnStmt SEMCOL\n            | inputStmt SEMCOL\n            | outputStmt SEMCOL\n            | commentLine\n    declar   : varDeclar SEMCOL\n                | funcDeclar\n                | objDeclar\n    varDeclar    : NAME ASSIGN STRING\n                    | NAME ASSIGN exprStmt\n    funcDeclar   : DEF NAME LPARENT RPARENT COL suite\n                    | DEF NAME LPARENT params RPARENT COL suite\n    params   : paramsList\n    paramsList   : NAME COMA paramsList\n                    | NAME\n    objDeclar    : CLASS NAME COL suite\n    call : NAME\n            | NAME POINT call\n            | NAME LPARENT RPARENT\n            | NAME LPARENT params RPARENT\n            | call POINT call\n    exprStmt : simpleExpr\n    selectionStmt    : IF simpleExpr COL suite\n                        | IF simpleExpr COL suite ELSE COL suite\n    iterationStmt    : WHILE simpleExpr COL suite\n    returnStmt   : RETURN\n                    | RETURN simpleExpr\n    simpleExpr   : simpleExpr OR andExpr\n                    | andExpr\n    andExpr  : andExpr AND unaryRelExpr\n                | unaryRelExpr\n    unaryRelExpr : NOT unaryRelExpr\n                    | relExpr\n    relExpr  : sumExpr relop sumExpr\n                | sumExpr\n    relop    : LTE\n                | LT\n                | GTE\n                | GT\n                | EQ\n                | NEQ\n    sumExpr  : sumExpr sumop term\n                | term\n    sumop    : SUM\n                | SUBST\n    term : term mulop opElement\n            | opElement\n    opElement    : call\n                    | NUMBER\n    mulop    : PROD\n                | DIV\n    inputStmt : INPUT LPARENT RPARENT\n    outputStmt : PRINT LPARENT STRING RPARENT\n    commentLine  : LINE_COMMENT\n    '
    
_lr_action_items = {'NAME':([0,2,3,4,5,6,7,11,12,14,15,16,17,18,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,81,82,83,84,85,86,87,88,89,90,94,97,99,100,101,102,103,],[16,16,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,46,46,46,-60,-35,52,53,-37,46,-39,-41,-49,-53,-55,-2,-5,46,-8,-9,-10,46,-12,46,71,46,-54,-23,46,-38,46,46,-42,-43,-44,-45,-46,-47,-50,-51,46,-56,-57,-27,-34,-24,-25,16,16,-36,71,16,-40,-48,-52,71,-26,-29,-31,-22,16,16,-17,16,-30,-18,]),'IF':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[17,17,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,17,17,-36,17,-40,-48,-52,-26,-29,-31,-22,17,17,-17,17,-30,-18,]),'WHILE':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[18,18,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,18,18,-36,18,-40,-48,-52,-26,-29,-31,-22,18,18,-17,18,-30,-18,]),'RETURN':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[19,19,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,19,19,-36,19,-40,-48,-52,-26,-29,-31,-22,19,19,-17,19,-30,-18,]),'INPUT':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[20,20,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,20,20,-36,20,-40,-48,-52,-26,-29,-31,-22,20,20,-17,20,-30,-18,]),'PRINT':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[21,21,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,21,21,-36,21,-40,-48,-52,-26,-29,-31,-22,21,21,-17,21,-30,-18,]),'LINE_COMMENT':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[22,22,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,22,22,-36,22,-40,-48,-52,-26,-29,-31,-22,22,22,-17,22,-30,-18,]),'DEF':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[24,24,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,24,24,-36,24,-40,-48,-52,-26,-29,-31,-22,24,24,-17,24,-30,-18,]),'CLASS':([0,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[25,25,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,25,25,-36,25,-40,-48,-52,-26,-29,-31,-22,25,25,-17,25,-30,-18,]),'NOT':([0,2,3,4,5,6,7,11,12,14,15,16,17,18,19,22,23,26,27,28,29,30,31,32,33,34,36,37,38,39,40,43,45,46,51,54,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[27,27,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,27,27,27,-60,-35,-37,27,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,27,-12,27,-54,-23,27,-38,-27,-34,-24,-25,27,27,-36,27,-40,-48,-52,-26,-29,-31,-22,27,27,-17,27,-30,-18,]),'NUMBER':([0,2,3,4,5,6,7,11,12,14,15,16,17,18,19,22,23,26,27,28,29,30,31,32,33,34,36,37,38,39,40,43,45,46,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,78,81,83,84,85,86,88,89,90,94,97,99,100,101,102,103,],[32,32,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,32,32,32,-60,-35,-37,32,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,32,-12,32,-54,-23,32,-38,32,32,-42,-43,-44,-45,-46,-47,-50,-51,32,-56,-57,-27,-34,-24,-25,32,32,-36,32,-40,-48,-52,-26,-29,-31,-22,32,32,-17,32,-30,-18,]),'$end':([1,2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,81,84,85,86,88,89,90,94,100,102,103,],[0,-1,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,-36,-40,-48,-52,-26,-29,-31,-22,-17,-30,-18,]),'ELSE':([2,3,4,5,6,7,11,12,14,15,16,22,23,26,28,29,30,31,32,33,34,36,37,38,40,45,46,54,68,69,70,72,81,84,85,86,88,89,90,94,100,102,103,],[-1,-3,-4,-54,-6,-7,-11,-28,-13,-14,-23,-60,-35,-37,-39,-41,-49,-53,-55,-2,-5,-8,-9,-10,-12,-54,-23,-38,-27,-34,-24,-25,-36,-40,-48,-52,-26,96,-31,-22,-17,-30,-18,]),'SEMCOL':([5,8,9,10,12,13,16,19,23,26,28,29,30,31,32,45,46,48,54,68,69,70,72,75,76,79,81,84,85,86,88,91,],[34,36,37,38,-28,40,-23,-32,-35,-37,-39,-41,-49,-53,-55,-54,-23,-33,-38,-27,-34,-24,-25,-15,-16,-58,-36,-40,-48,-52,-26,-59,]),'POINT':([5,16,45,46,68,70,72,88,],[35,41,35,41,35,35,-25,-26,]),'PROD':([5,16,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,66,-53,-55,-54,-23,-27,-24,-25,66,-52,-26,]),'DIV':([5,16,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,67,-53,-55,-54,-23,-27,-24,-25,67,-52,-26,]),'LTE':([5,16,29,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,57,-49,-53,-55,-54,-23,-27,-24,-25,-48,-52,-26,]),'LT':([5,16,29,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,58,-49,-53,-55,-54,-23,-27,-24,-25,-48,-52,-26,]),'GTE':([5,16,29,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,59,-49,-53,-55,-54,-23,-27,-24,-25,-48,-52,-26,]),'GT':([5,16,29,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,60,-49,-53,-55,-54,-23,-27,-24,-25,-48,-52,-26,]),'EQ':([5,16,29,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,61,-49,-53,-55,-54,-23,-27,-24,-25,-48,-52,-26,]),'NEQ':([5,16,29,30,31,32,45,46,68,70,72,85,86,88,],[-54,-23,62,-49,-53,-55,-54,-23,-27,-24,-25,-48,-52,-26,]),'SUM':([5,16,29,30,31,32,45,46,68,70,72,84,85,86,88,],[-54,-23,63,-49,-53,-55,-54,-23,-27,-24,-25,63,-48,-52,-26,]),'SUBST':([5,16,29,30,31,32,45,46,68,70,72,84,85,86,88,],[-54,-23,64,-49,-53,-55,-54,-23,-27,-24,-25,64,-48,-52,-26,]),'AND':([5,16,23,26,28,29,30,31,32,45,46,54,68,69,70,72,81,84,85,86,88,],[-54,-23,51,-37,-39,-41,-49,-53,-55,-54,-23,-38,-27,51,-24,-25,-36,-40,-48,-52,-26,]),'OR':([5,12,16,23,26,28,29,30,31,32,44,45,46,47,48,54,68,69,70,72,81,84,85,86,88,],[-54,39,-23,-35,-37,-39,-41,-49,-53,-55,39,-54,-23,39,39,-38,-27,-34,-24,-25,-36,-40,-48,-52,-26,]),'LPARENT':([16,20,21,46,52,],[42,49,50,42,82,]),'ASSIGN':([16,],[43,]),'COL':([23,26,28,29,30,31,32,44,45,46,47,53,54,68,69,70,72,81,84,85,86,88,92,96,98,],[-35,-37,-39,-41,-49,-53,-55,77,-54,-23,78,83,-38,-27,-34,-24,-25,-36,-40,-48,-52,-26,97,99,101,]),'RPARENT':([42,49,71,73,74,80,82,93,95,],[72,79,-21,88,-19,91,92,98,-20,]),'STRING':([43,50,],[75,80,]),'COMA':([71,],[87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'suite':([0,2,77,78,83,97,99,101,],[1,33,89,90,94,100,102,103,]),'stmt':([0,2,77,78,83,97,99,101,],[2,2,2,2,2,2,2,2,]),'exprStmt':([0,2,43,77,78,83,97,99,101,],[3,3,76,3,3,3,3,3,3,]),'declar':([0,2,77,78,83,97,99,101,],[4,4,4,4,4,4,4,4,]),'call':([0,2,17,18,19,27,35,39,41,43,51,55,56,65,77,78,83,97,99,101,],[5,5,45,45,45,45,68,45,70,45,45,45,45,45,5,5,5,5,5,5,]),'selectionStmt':([0,2,77,78,83,97,99,101,],[6,6,6,6,6,6,6,6,]),'iterationStmt':([0,2,77,78,83,97,99,101,],[7,7,7,7,7,7,7,7,]),'returnStmt':([0,2,77,78,83,97,99,101,],[8,8,8,8,8,8,8,8,]),'inputStmt':([0,2,77,78,83,97,99,101,],[9,9,9,9,9,9,9,9,]),'outputStmt':([0,2,77,78,83,97,99,101,],[10,10,10,10,10,10,10,10,]),'commentLine':([0,2,77,78,83,97,99,101,],[11,11,11,11,11,11,11,11,]),'simpleExpr':([0,2,17,18,19,43,77,78,83,97,99,101,],[12,12,44,47,48,12,12,12,12,12,12,12,]),'varDeclar':([0,2,77,78,83,97,99,101,],[13,13,13,13,13,13,13,13,]),'funcDeclar':([0,2,77,78,83,97,99,101,],[14,14,14,14,14,14,14,14,]),'objDeclar':([0,2,77,78,83,97,99,101,],[15,15,15,15,15,15,15,15,]),'andExpr':([0,2,17,18,19,39,43,77,78,83,97,99,101,],[23,23,23,23,23,69,23,23,23,23,23,23,23,]),'unaryRelExpr':([0,2,17,18,19,27,39,43,51,77,78,83,97,99,101,],[26,26,26,26,26,54,26,26,81,26,26,26,26,26,26,]),'relExpr':([0,2,17,18,19,27,39,43,51,77,78,83,97,99,101,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'sumExpr':([0,2,17,18,19,27,39,43,51,55,77,78,83,97,99,101,],[29,29,29,29,29,29,29,29,29,84,29,29,29,29,29,29,]),'term':([0,2,17,18,19,27,39,43,51,55,56,77,78,83,97,99,101,],[30,30,30,30,30,30,30,30,30,30,85,30,30,30,30,30,30,]),'opElement':([0,2,17,18,19,27,39,43,51,55,56,65,77,78,83,97,99,101,],[31,31,31,31,31,31,31,31,31,31,31,86,31,31,31,31,31,31,]),'relop':([29,],[55,]),'sumop':([29,84,],[56,56,]),'mulop':([30,85,],[65,65,]),'params':([42,82,],[73,93,]),'paramsList':([42,82,87,],[74,74,95,]),}

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
  ('varDeclar -> NAME ASSIGN exprStmt','varDeclar',3,'p_var_declar','pythonInterpreter.py',141),
  ('funcDeclar -> DEF NAME LPARENT RPARENT COL suite','funcDeclar',6,'p_func_declar','pythonInterpreter.py',146),
  ('funcDeclar -> DEF NAME LPARENT params RPARENT COL suite','funcDeclar',7,'p_func_declar','pythonInterpreter.py',147),
  ('params -> paramsList','params',1,'p_params','pythonInterpreter.py',152),
  ('paramsList -> NAME COMA paramsList','paramsList',3,'p_params_list','pythonInterpreter.py',157),
  ('paramsList -> NAME','paramsList',1,'p_params_list','pythonInterpreter.py',158),
  ('objDeclar -> CLASS NAME COL suite','objDeclar',4,'p_obj_declaration','pythonInterpreter.py',163),
  ('call -> NAME','call',1,'p_call','pythonInterpreter.py',168),
  ('call -> NAME POINT call','call',3,'p_call','pythonInterpreter.py',169),
  ('call -> NAME LPARENT RPARENT','call',3,'p_call','pythonInterpreter.py',170),
  ('call -> NAME LPARENT params RPARENT','call',4,'p_call','pythonInterpreter.py',171),
  ('call -> call POINT call','call',3,'p_call','pythonInterpreter.py',172),
  ('exprStmt -> simpleExpr','exprStmt',1,'p_expr_stmt','pythonInterpreter.py',177),
  ('selectionStmt -> IF simpleExpr COL suite','selectionStmt',4,'p_selection_stmt','pythonInterpreter.py',182),
  ('selectionStmt -> IF simpleExpr COL suite ELSE COL suite','selectionStmt',7,'p_selection_stmt','pythonInterpreter.py',183),
  ('iterationStmt -> WHILE simpleExpr COL suite','iterationStmt',4,'p_iteration_stmt','pythonInterpreter.py',188),
  ('returnStmt -> RETURN','returnStmt',1,'p_return','pythonInterpreter.py',193),
  ('returnStmt -> RETURN simpleExpr','returnStmt',2,'p_return','pythonInterpreter.py',194),
  ('simpleExpr -> simpleExpr OR andExpr','simpleExpr',3,'p_simple_expr','pythonInterpreter.py',199),
  ('simpleExpr -> andExpr','simpleExpr',1,'p_simple_expr','pythonInterpreter.py',200),
  ('andExpr -> andExpr AND unaryRelExpr','andExpr',3,'p_and_expr','pythonInterpreter.py',205),
  ('andExpr -> unaryRelExpr','andExpr',1,'p_and_expr','pythonInterpreter.py',206),
  ('unaryRelExpr -> NOT unaryRelExpr','unaryRelExpr',2,'p_unary_rel_expr','pythonInterpreter.py',211),
  ('unaryRelExpr -> relExpr','unaryRelExpr',1,'p_unary_rel_expr','pythonInterpreter.py',212),
  ('relExpr -> sumExpr relop sumExpr','relExpr',3,'p_rel_expr','pythonInterpreter.py',217),
  ('relExpr -> sumExpr','relExpr',1,'p_rel_expr','pythonInterpreter.py',218),
  ('relop -> LTE','relop',1,'p_relop','pythonInterpreter.py',223),
  ('relop -> LT','relop',1,'p_relop','pythonInterpreter.py',224),
  ('relop -> GTE','relop',1,'p_relop','pythonInterpreter.py',225),
  ('relop -> GT','relop',1,'p_relop','pythonInterpreter.py',226),
  ('relop -> EQ','relop',1,'p_relop','pythonInterpreter.py',227),
  ('relop -> NEQ','relop',1,'p_relop','pythonInterpreter.py',228),
  ('sumExpr -> sumExpr sumop term','sumExpr',3,'p_sum_expr','pythonInterpreter.py',233),
  ('sumExpr -> term','sumExpr',1,'p_sum_expr','pythonInterpreter.py',234),
  ('sumop -> SUM','sumop',1,'p_sumop','pythonInterpreter.py',239),
  ('sumop -> SUBST','sumop',1,'p_sumop','pythonInterpreter.py',240),
  ('term -> term mulop opElement','term',3,'p_term','pythonInterpreter.py',245),
  ('term -> opElement','term',1,'p_term','pythonInterpreter.py',246),
  ('opElement -> call','opElement',1,'p_op_element','pythonInterpreter.py',251),
  ('opElement -> NUMBER','opElement',1,'p_op_element','pythonInterpreter.py',252),
  ('mulop -> PROD','mulop',1,'p_mulop','pythonInterpreter.py',257),
  ('mulop -> DIV','mulop',1,'p_mulop','pythonInterpreter.py',258),
  ('inputStmt -> INPUT LPARENT RPARENT','inputStmt',3,'p_input_stmt','pythonInterpreter.py',263),
  ('outputStmt -> PRINT LPARENT STRING RPARENT','outputStmt',4,'p_output_stmt','pythonInterpreter.py',268),
  ('commentLine -> LINE_COMMENT','commentLine',1,'p_comment_line','pythonInterpreter.py',273),
]
