
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NAME NUMBER STRING LINE_COMMENT POINT EQ NEQ GT LT GTE LTE ASSIGN SUM SUBST PROD DIV LPARENT RPARENT COL SEMCOL COMA INPUT PRINT IF ELSE WHILE CLASS AND OR NOT RETURN DEFline : suite\n    suite    : stmt\n                | stmt suite\n    stmt : exprStmt\n            | declar\n            | call SEMCOL\n            | selectionStmt\n            | iterationStmt\n            | returnStmt SEMCOL\n            | inputStmt SEMCOL\n            | outputStmt SEMCOL\n            | commentLine\n    declar   : varDeclar SEMCOL\n                | funcDeclar\n                | objDeclar\n    varDeclar    : NAME ASSIGN STRING\n                    | NAME ASSIGN exprStmt\n                    | NAME ASSIGN inputStmt\n    funcDeclar   : DEF NAME LPARENT RPARENT COL suite\n                    | DEF NAME LPARENT params RPARENT COL suite\n    params   : paramsList\n    paramsList   : NAME COMA paramsList\n                    | NAME\n    objDeclar    : CLASS NAME COL suite\n    call : NAME\n            | NAME POINT call\n            | NAME LPARENT RPARENT\n            | NAME LPARENT params RPARENT\n            | call POINT call\n    exprStmt : simpleExpr\n    selectionStmt    : IF simpleExpr COL suite\n                        | IF simpleExpr COL suite ELSE COL suite\n    iterationStmt    : WHILE simpleExpr COL suite\n    returnStmt   : RETURN\n                    | RETURN simpleExpr\n    simpleExpr   : simpleExpr OR andExpr\n                    | andExpr\n    andExpr  : andExpr AND unaryRelExpr\n                | unaryRelExpr\n    unaryRelExpr : NOT unaryRelExpr\n                    | relExpr\n    relExpr  : sumExpr relop sumExpr\n                | sumExpr\n    relop    : LTE\n                | LT\n                | GTE\n                | GT\n                | EQ\n                | NEQ\n    sumExpr  : sumExpr sumop term\n                | term\n    sumop    : SUM\n                | SUBST\n    term : term mulop opElement\n            | opElement\n    opElement    : call\n                    | NUMBER\n    mulop    : PROD\n                | DIV\n    inputStmt : INPUT LPARENT RPARENT\n    outputStmt   : PRINT LPARENT STRING RPARENT\n                    | PRINT LPARENT NAME RPARENT\n    commentLine  : LINE_COMMENT\n    '
    
_lr_action_items = {'NAME':([0,3,4,5,6,7,8,12,13,15,16,17,18,19,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,51,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,79,80,84,85,86,87,88,89,90,91,92,93,98,101,103,104,105,106,107,],[17,17,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,47,47,47,-63,-37,53,54,-39,47,-41,-43,-51,-55,-57,-3,-6,47,-9,-10,-11,47,-13,47,72,47,-56,-25,83,47,-40,47,47,-44,-45,-46,-47,-48,-49,-52,-53,47,-58,-59,-29,-36,-26,-27,17,17,-38,72,17,-42,-50,-54,72,-28,-31,-33,-24,17,17,-19,17,-32,-20,]),'IF':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[18,18,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,18,18,-38,18,-42,-50,-54,-28,-31,-33,-24,18,18,-19,18,-32,-20,]),'WHILE':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[19,19,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,19,19,-38,19,-42,-50,-54,-28,-31,-33,-24,19,19,-19,19,-32,-20,]),'RETURN':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[20,20,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,20,20,-38,20,-42,-50,-54,-28,-31,-33,-24,20,20,-19,20,-32,-20,]),'INPUT':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,44,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[21,21,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,21,-56,-25,-40,-29,-36,-26,-27,21,21,-38,21,-42,-50,-54,-28,-31,-33,-24,21,21,-19,21,-32,-20,]),'PRINT':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[22,22,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,22,22,-38,22,-42,-50,-54,-28,-31,-33,-24,22,22,-19,22,-32,-20,]),'LINE_COMMENT':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[23,23,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,23,23,-38,23,-42,-50,-54,-28,-31,-33,-24,23,23,-19,23,-32,-20,]),'DEF':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[25,25,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,25,25,-38,25,-42,-50,-54,-28,-31,-33,-24,25,25,-19,25,-32,-20,]),'CLASS':([0,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[26,26,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,26,26,-38,26,-42,-50,-54,-28,-31,-33,-24,26,26,-19,26,-32,-20,]),'NOT':([0,3,4,5,6,7,8,12,13,15,16,17,18,19,20,23,24,27,28,29,30,31,32,33,34,35,37,38,39,40,41,44,46,47,52,55,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[28,28,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,28,28,28,-63,-37,-39,28,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,28,-13,28,-56,-25,28,-40,-29,-36,-26,-27,28,28,-38,28,-42,-50,-54,-28,-31,-33,-24,28,28,-19,28,-32,-20,]),'NUMBER':([0,3,4,5,6,7,8,12,13,15,16,17,18,19,20,23,24,27,28,29,30,31,32,33,34,35,37,38,39,40,41,44,46,47,52,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,79,80,84,86,87,88,89,91,92,93,98,101,103,104,105,106,107,],[33,33,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,33,33,33,-63,-37,-39,33,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,33,-13,33,-56,-25,33,-40,33,33,-44,-45,-46,-47,-48,-49,-52,-53,33,-58,-59,-29,-36,-26,-27,33,33,-38,33,-42,-50,-54,-28,-31,-33,-24,33,33,-19,33,-32,-20,]),'$end':([1,2,3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,84,87,88,89,91,92,93,98,104,106,107,],[0,-1,-2,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,-38,-42,-50,-54,-28,-31,-33,-24,-19,-32,-20,]),'ELSE':([3,4,5,6,7,8,12,13,15,16,17,23,24,27,29,30,31,32,33,34,35,37,38,39,41,46,47,55,69,70,71,73,84,87,88,89,91,92,93,98,104,106,107,],[-2,-4,-5,-56,-7,-8,-12,-30,-14,-15,-25,-63,-37,-39,-41,-43,-51,-55,-57,-3,-6,-9,-10,-11,-13,-56,-25,-40,-29,-36,-26,-27,-38,-42,-50,-54,-28,100,-33,-24,-19,-32,-20,]),'SEMCOL':([6,9,10,11,13,14,17,20,24,27,29,30,31,32,33,46,47,49,55,69,70,71,73,76,77,78,81,84,87,88,89,91,94,95,],[35,37,38,39,-30,41,-25,-34,-37,-39,-41,-43,-51,-55,-57,-56,-25,-35,-40,-29,-36,-26,-27,-16,-17,-18,-60,-38,-42,-50,-54,-28,-61,-62,]),'POINT':([6,17,46,47,69,71,73,91,],[36,42,36,42,36,36,-27,-28,]),'PROD':([6,17,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,67,-55,-57,-56,-25,-29,-26,-27,67,-54,-28,]),'DIV':([6,17,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,68,-55,-57,-56,-25,-29,-26,-27,68,-54,-28,]),'LTE':([6,17,30,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,58,-51,-55,-57,-56,-25,-29,-26,-27,-50,-54,-28,]),'LT':([6,17,30,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,59,-51,-55,-57,-56,-25,-29,-26,-27,-50,-54,-28,]),'GTE':([6,17,30,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,60,-51,-55,-57,-56,-25,-29,-26,-27,-50,-54,-28,]),'GT':([6,17,30,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,61,-51,-55,-57,-56,-25,-29,-26,-27,-50,-54,-28,]),'EQ':([6,17,30,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,62,-51,-55,-57,-56,-25,-29,-26,-27,-50,-54,-28,]),'NEQ':([6,17,30,31,32,33,46,47,69,71,73,88,89,91,],[-56,-25,63,-51,-55,-57,-56,-25,-29,-26,-27,-50,-54,-28,]),'SUM':([6,17,30,31,32,33,46,47,69,71,73,87,88,89,91,],[-56,-25,64,-51,-55,-57,-56,-25,-29,-26,-27,64,-50,-54,-28,]),'SUBST':([6,17,30,31,32,33,46,47,69,71,73,87,88,89,91,],[-56,-25,65,-51,-55,-57,-56,-25,-29,-26,-27,65,-50,-54,-28,]),'AND':([6,17,24,27,29,30,31,32,33,46,47,55,69,70,71,73,84,87,88,89,91,],[-56,-25,52,-39,-41,-43,-51,-55,-57,-56,-25,-40,-29,52,-26,-27,-38,-42,-50,-54,-28,]),'OR':([6,13,17,24,27,29,30,31,32,33,45,46,47,48,49,55,69,70,71,73,84,87,88,89,91,],[-56,40,-25,-37,-39,-41,-43,-51,-55,-57,40,-56,-25,40,40,-40,-29,-36,-26,-27,-38,-42,-50,-54,-28,]),'LPARENT':([17,21,22,47,53,],[43,50,51,43,85,]),'ASSIGN':([17,],[44,]),'COL':([24,27,29,30,31,32,33,45,46,47,48,54,55,69,70,71,73,84,87,88,89,91,96,100,102,],[-37,-39,-41,-43,-51,-55,-57,79,-56,-25,80,86,-40,-29,-36,-26,-27,-38,-42,-50,-54,-28,101,103,105,]),'RPARENT':([43,50,72,74,75,82,83,85,97,99,],[73,81,-23,91,-21,94,95,96,102,-22,]),'STRING':([44,51,],[76,82,]),'COMA':([72,],[90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,],[1,]),'suite':([0,3,79,80,86,101,103,105,],[2,34,92,93,98,104,106,107,]),'stmt':([0,3,79,80,86,101,103,105,],[3,3,3,3,3,3,3,3,]),'exprStmt':([0,3,44,79,80,86,101,103,105,],[4,4,77,4,4,4,4,4,4,]),'declar':([0,3,79,80,86,101,103,105,],[5,5,5,5,5,5,5,5,]),'call':([0,3,18,19,20,28,36,40,42,44,52,56,57,66,79,80,86,101,103,105,],[6,6,46,46,46,46,69,46,71,46,46,46,46,46,6,6,6,6,6,6,]),'selectionStmt':([0,3,79,80,86,101,103,105,],[7,7,7,7,7,7,7,7,]),'iterationStmt':([0,3,79,80,86,101,103,105,],[8,8,8,8,8,8,8,8,]),'returnStmt':([0,3,79,80,86,101,103,105,],[9,9,9,9,9,9,9,9,]),'inputStmt':([0,3,44,79,80,86,101,103,105,],[10,10,78,10,10,10,10,10,10,]),'outputStmt':([0,3,79,80,86,101,103,105,],[11,11,11,11,11,11,11,11,]),'commentLine':([0,3,79,80,86,101,103,105,],[12,12,12,12,12,12,12,12,]),'simpleExpr':([0,3,18,19,20,44,79,80,86,101,103,105,],[13,13,45,48,49,13,13,13,13,13,13,13,]),'varDeclar':([0,3,79,80,86,101,103,105,],[14,14,14,14,14,14,14,14,]),'funcDeclar':([0,3,79,80,86,101,103,105,],[15,15,15,15,15,15,15,15,]),'objDeclar':([0,3,79,80,86,101,103,105,],[16,16,16,16,16,16,16,16,]),'andExpr':([0,3,18,19,20,40,44,79,80,86,101,103,105,],[24,24,24,24,24,70,24,24,24,24,24,24,24,]),'unaryRelExpr':([0,3,18,19,20,28,40,44,52,79,80,86,101,103,105,],[27,27,27,27,27,55,27,27,84,27,27,27,27,27,27,]),'relExpr':([0,3,18,19,20,28,40,44,52,79,80,86,101,103,105,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'sumExpr':([0,3,18,19,20,28,40,44,52,56,79,80,86,101,103,105,],[30,30,30,30,30,30,30,30,30,87,30,30,30,30,30,30,]),'term':([0,3,18,19,20,28,40,44,52,56,57,79,80,86,101,103,105,],[31,31,31,31,31,31,31,31,31,31,88,31,31,31,31,31,31,]),'opElement':([0,3,18,19,20,28,40,44,52,56,57,66,79,80,86,101,103,105,],[32,32,32,32,32,32,32,32,32,32,32,89,32,32,32,32,32,32,]),'relop':([30,],[56,]),'sumop':([30,87,],[57,57,]),'mulop':([31,88,],[66,66,]),'params':([43,85,],[74,97,]),'paramsList':([43,85,90,],[75,75,99,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> suite','line',1,'p_line','pythonInterpreter.py',142),
  ('suite -> stmt','suite',1,'p_suite','pythonInterpreter.py',147),
  ('suite -> stmt suite','suite',2,'p_suite','pythonInterpreter.py',148),
  ('stmt -> exprStmt','stmt',1,'p_stmt','pythonInterpreter.py',156),
  ('stmt -> declar','stmt',1,'p_stmt','pythonInterpreter.py',157),
  ('stmt -> call SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',158),
  ('stmt -> selectionStmt','stmt',1,'p_stmt','pythonInterpreter.py',159),
  ('stmt -> iterationStmt','stmt',1,'p_stmt','pythonInterpreter.py',160),
  ('stmt -> returnStmt SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',161),
  ('stmt -> inputStmt SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',162),
  ('stmt -> outputStmt SEMCOL','stmt',2,'p_stmt','pythonInterpreter.py',163),
  ('stmt -> commentLine','stmt',1,'p_stmt','pythonInterpreter.py',164),
  ('declar -> varDeclar SEMCOL','declar',2,'p_declar','pythonInterpreter.py',169),
  ('declar -> funcDeclar','declar',1,'p_declar','pythonInterpreter.py',170),
  ('declar -> objDeclar','declar',1,'p_declar','pythonInterpreter.py',171),
  ('varDeclar -> NAME ASSIGN STRING','varDeclar',3,'p_var_declar','pythonInterpreter.py',176),
  ('varDeclar -> NAME ASSIGN exprStmt','varDeclar',3,'p_var_declar','pythonInterpreter.py',177),
  ('varDeclar -> NAME ASSIGN inputStmt','varDeclar',3,'p_var_declar','pythonInterpreter.py',178),
  ('funcDeclar -> DEF NAME LPARENT RPARENT COL suite','funcDeclar',6,'p_func_declar','pythonInterpreter.py',183),
  ('funcDeclar -> DEF NAME LPARENT params RPARENT COL suite','funcDeclar',7,'p_func_declar','pythonInterpreter.py',184),
  ('params -> paramsList','params',1,'p_params','pythonInterpreter.py',189),
  ('paramsList -> NAME COMA paramsList','paramsList',3,'p_params_list','pythonInterpreter.py',194),
  ('paramsList -> NAME','paramsList',1,'p_params_list','pythonInterpreter.py',195),
  ('objDeclar -> CLASS NAME COL suite','objDeclar',4,'p_obj_declaration','pythonInterpreter.py',200),
  ('call -> NAME','call',1,'p_call','pythonInterpreter.py',205),
  ('call -> NAME POINT call','call',3,'p_call','pythonInterpreter.py',206),
  ('call -> NAME LPARENT RPARENT','call',3,'p_call','pythonInterpreter.py',207),
  ('call -> NAME LPARENT params RPARENT','call',4,'p_call','pythonInterpreter.py',208),
  ('call -> call POINT call','call',3,'p_call','pythonInterpreter.py',209),
  ('exprStmt -> simpleExpr','exprStmt',1,'p_expr_stmt','pythonInterpreter.py',215),
  ('selectionStmt -> IF simpleExpr COL suite','selectionStmt',4,'p_selection_stmt','pythonInterpreter.py',220),
  ('selectionStmt -> IF simpleExpr COL suite ELSE COL suite','selectionStmt',7,'p_selection_stmt','pythonInterpreter.py',221),
  ('iterationStmt -> WHILE simpleExpr COL suite','iterationStmt',4,'p_iteration_stmt','pythonInterpreter.py',226),
  ('returnStmt -> RETURN','returnStmt',1,'p_return','pythonInterpreter.py',231),
  ('returnStmt -> RETURN simpleExpr','returnStmt',2,'p_return','pythonInterpreter.py',232),
  ('simpleExpr -> simpleExpr OR andExpr','simpleExpr',3,'p_simple_expr','pythonInterpreter.py',237),
  ('simpleExpr -> andExpr','simpleExpr',1,'p_simple_expr','pythonInterpreter.py',238),
  ('andExpr -> andExpr AND unaryRelExpr','andExpr',3,'p_and_expr','pythonInterpreter.py',246),
  ('andExpr -> unaryRelExpr','andExpr',1,'p_and_expr','pythonInterpreter.py',247),
  ('unaryRelExpr -> NOT unaryRelExpr','unaryRelExpr',2,'p_unary_rel_expr','pythonInterpreter.py',255),
  ('unaryRelExpr -> relExpr','unaryRelExpr',1,'p_unary_rel_expr','pythonInterpreter.py',256),
  ('relExpr -> sumExpr relop sumExpr','relExpr',3,'p_rel_expr','pythonInterpreter.py',264),
  ('relExpr -> sumExpr','relExpr',1,'p_rel_expr','pythonInterpreter.py',265),
  ('relop -> LTE','relop',1,'p_relop','pythonInterpreter.py',273),
  ('relop -> LT','relop',1,'p_relop','pythonInterpreter.py',274),
  ('relop -> GTE','relop',1,'p_relop','pythonInterpreter.py',275),
  ('relop -> GT','relop',1,'p_relop','pythonInterpreter.py',276),
  ('relop -> EQ','relop',1,'p_relop','pythonInterpreter.py',277),
  ('relop -> NEQ','relop',1,'p_relop','pythonInterpreter.py',278),
  ('sumExpr -> sumExpr sumop term','sumExpr',3,'p_sum_expr','pythonInterpreter.py',283),
  ('sumExpr -> term','sumExpr',1,'p_sum_expr','pythonInterpreter.py',284),
  ('sumop -> SUM','sumop',1,'p_sumop','pythonInterpreter.py',292),
  ('sumop -> SUBST','sumop',1,'p_sumop','pythonInterpreter.py',293),
  ('term -> term mulop opElement','term',3,'p_term','pythonInterpreter.py',298),
  ('term -> opElement','term',1,'p_term','pythonInterpreter.py',299),
  ('opElement -> call','opElement',1,'p_op_element','pythonInterpreter.py',307),
  ('opElement -> NUMBER','opElement',1,'p_op_element','pythonInterpreter.py',308),
  ('mulop -> PROD','mulop',1,'p_mulop','pythonInterpreter.py',313),
  ('mulop -> DIV','mulop',1,'p_mulop','pythonInterpreter.py',314),
  ('inputStmt -> INPUT LPARENT RPARENT','inputStmt',3,'p_input_stmt','pythonInterpreter.py',319),
  ('outputStmt -> PRINT LPARENT STRING RPARENT','outputStmt',4,'p_output_stmt','pythonInterpreter.py',324),
  ('outputStmt -> PRINT LPARENT NAME RPARENT','outputStmt',4,'p_output_stmt','pythonInterpreter.py',325),
  ('commentLine -> LINE_COMMENT','commentLine',1,'p_comment_line','pythonInterpreter.py',330),
]
