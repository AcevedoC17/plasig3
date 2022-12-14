
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'defdefsARROW BECOMES COLON COMMA COMMENT DEF ELSE EQ GE GT ID IF INT LBRACE LE LPAREN LT MINUS NE NUM PCT PLUS RBRACE RPAREN SEMI SLASH STAR VAR WHITESPACEdefdefs : defdef defdefs\n              | defdefdefdef : DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACEparmsopt : parms\n                | emptyparms : vardef COMMA parms\n            | vardefvardef : ID COLON typetype : INT\n            | LPAREN typesopt RPAREN ARROW typetypesopt : types\n                | emptytypes : type COMMA types\n            | typevardefsopt : VAR vardef SEMI vardefsopt\n                  | emptydefdefsopt : defdefs\n                  | emptyexpras : expra SEMI expras\n              | expraexpra : ID BECOMES expr\n            | exprexpr : IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE\n            | term\n            | expr PLUS term\n            | expr MINUS termterm : factor\n            | term STAR factor\n            | term SLASH factor\n            | term  PCT factorfactor : ID\n              | NUM\n              | LPAREN expr RPAREN\n              | factor LPAREN argsopt RPARENtest : expr NE expr\n            | expr LT expr\n            | expr LE expr\n            | expr GE expr\n            | expr GT expr\n            | expr EQ exprargsopt : args\n              | emptyargs : expr COMMA args\n            | exprempty :'
    
_lr_action_items = {'DEF':([0,2,30,32,34,48,52,61,],[3,3,-45,3,-16,-45,-3,-15,]),'$end':([1,2,4,52,],[0,-2,-1,-3,]),'ID':([2,3,4,6,14,30,32,33,34,35,36,37,40,48,49,52,53,54,55,56,57,58,59,60,61,77,78,79,80,81,82,84,85,96,],[-2,5,-1,7,7,-45,-45,7,-16,39,-17,-18,51,-45,51,-3,39,51,51,51,51,51,51,51,-15,51,51,51,51,51,51,51,39,39,]),'IF':([2,4,30,32,34,35,36,37,40,48,49,52,53,56,60,61,77,78,79,80,81,82,84,85,96,],[-2,-1,-45,-45,-16,44,-17,-18,44,-45,44,-3,44,44,44,-15,44,44,44,44,44,44,44,44,44,]),'NUM':([2,4,30,32,34,35,36,37,40,48,49,52,53,54,55,56,57,58,59,60,61,77,78,79,80,81,82,84,85,96,],[-2,-1,-45,-45,-16,47,-17,-18,47,-45,47,-3,47,47,47,47,47,47,47,47,-15,47,47,47,47,47,47,47,47,47,]),'LPAREN':([2,4,5,12,17,18,26,28,30,32,34,35,36,37,39,40,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,63,69,70,71,77,78,79,80,81,82,83,84,85,96,],[-2,-1,6,17,17,17,17,17,-45,-45,-16,40,-17,-18,-31,40,56,60,-32,-45,40,-31,-3,40,40,40,40,40,40,40,40,-15,-33,60,60,60,40,40,40,40,40,40,-34,40,40,40,]),'RPAREN':([6,8,9,10,11,15,16,17,19,20,21,22,23,29,31,45,46,47,50,51,60,63,65,66,67,69,70,71,72,73,74,75,83,86,87,88,89,90,91,92,98,],[-45,13,-4,-5,-7,-8,-9,-45,-6,25,-14,-11,-12,-13,-10,-24,-27,-32,63,-31,-45,-33,-25,-26,76,-28,-29,-30,83,-41,-42,-44,-34,-35,-36,-37,-38,-39,-40,-43,-23,]),'COLON':([7,13,],[12,18,]),'COMMA':([11,15,16,21,31,45,46,47,51,63,65,66,69,70,71,75,83,98,],[14,-8,-9,26,-10,-24,-27,-32,-31,-33,-25,-26,-28,-29,-30,84,-34,-23,]),'INT':([12,17,18,26,28,],[16,16,16,16,16,]),'SEMI':([15,16,31,38,39,42,43,45,46,47,51,62,63,65,66,69,70,71,83,98,],[-8,-9,-10,48,-31,53,-22,-24,-27,-32,-31,-21,-33,-25,-26,-28,-29,-30,-34,-23,]),'BECOMES':([16,24,31,39,],[-9,27,-10,49,]),'ARROW':([25,],[28,]),'LBRACE':([27,76,95,],[30,85,96,]),'VAR':([30,48,],[33,33,]),'STAR':([39,45,46,47,51,63,65,66,69,70,71,83,],[-31,57,-27,-32,-31,-33,57,57,-28,-29,-30,-34,]),'SLASH':([39,45,46,47,51,63,65,66,69,70,71,83,],[-31,58,-27,-32,-31,-33,58,58,-28,-29,-30,-34,]),'PCT':([39,45,46,47,51,63,65,66,69,70,71,83,],[-31,59,-27,-32,-31,-33,59,59,-28,-29,-30,-34,]),'PLUS':([39,43,45,46,47,50,51,62,63,65,66,68,69,70,71,75,83,86,87,88,89,90,91,98,],[-31,54,-24,-27,-32,54,-31,54,-33,-25,-26,54,-28,-29,-30,54,-34,54,54,54,54,54,54,-23,]),'MINUS':([39,43,45,46,47,50,51,62,63,65,66,68,69,70,71,75,83,86,87,88,89,90,91,98,],[-31,55,-24,-27,-32,55,-31,55,-33,-25,-26,55,-28,-29,-30,55,-34,55,55,55,55,55,55,-23,]),'RBRACE':([39,41,42,43,45,46,47,51,62,63,64,65,66,69,70,71,83,93,97,98,],[-31,52,-20,-22,-24,-27,-32,-31,-21,-33,-19,-25,-26,-28,-29,-30,-34,94,98,-23,]),'NE':([45,46,47,51,63,65,66,68,69,70,71,83,98,],[-24,-27,-32,-31,-33,-25,-26,77,-28,-29,-30,-34,-23,]),'LT':([45,46,47,51,63,65,66,68,69,70,71,83,98,],[-24,-27,-32,-31,-33,-25,-26,78,-28,-29,-30,-34,-23,]),'LE':([45,46,47,51,63,65,66,68,69,70,71,83,98,],[-24,-27,-32,-31,-33,-25,-26,79,-28,-29,-30,-34,-23,]),'GE':([45,46,47,51,63,65,66,68,69,70,71,83,98,],[-24,-27,-32,-31,-33,-25,-26,80,-28,-29,-30,-34,-23,]),'GT':([45,46,47,51,63,65,66,68,69,70,71,83,98,],[-24,-27,-32,-31,-33,-25,-26,81,-28,-29,-30,-34,-23,]),'EQ':([45,46,47,51,63,65,66,68,69,70,71,83,98,],[-24,-27,-32,-31,-33,-25,-26,82,-28,-29,-30,-34,-23,]),'ELSE':([94,],[95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'defdefs':([0,2,32,],[1,4,36,]),'defdef':([0,2,32,],[2,2,2,]),'parmsopt':([6,],[8,]),'parms':([6,14,],[9,19,]),'empty':([6,17,30,32,48,60,],[10,23,34,37,34,74,]),'vardef':([6,14,33,],[11,11,38,]),'type':([12,17,18,26,28,],[15,21,24,21,31,]),'typesopt':([17,],[20,]),'types':([17,26,],[22,29,]),'vardefsopt':([30,48,],[32,61,]),'defdefsopt':([32,],[35,]),'expras':([35,53,85,96,],[41,64,93,97,]),'expra':([35,53,85,96,],[42,42,42,42,]),'expr':([35,40,49,53,56,60,77,78,79,80,81,82,84,85,96,],[43,50,62,43,68,75,86,87,88,89,90,91,75,43,43,]),'term':([35,40,49,53,54,55,56,60,77,78,79,80,81,82,84,85,96,],[45,45,45,45,65,66,45,45,45,45,45,45,45,45,45,45,45,]),'factor':([35,40,49,53,54,55,56,57,58,59,60,77,78,79,80,81,82,84,85,96,],[46,46,46,46,46,46,46,69,70,71,46,46,46,46,46,46,46,46,46,46,]),'test':([56,],[67,]),'argsopt':([60,],[72,]),'args':([60,84,],[73,92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> defdefs","S'",1,None,None,None),
  ('defdefs -> defdef defdefs','defdefs',2,'p_defdefs','fusion.py',169),
  ('defdefs -> defdef','defdefs',1,'p_defdefs','fusion.py',170),
  ('defdef -> DEF ID LPAREN parmsopt RPAREN COLON type BECOMES LBRACE vardefsopt defdefsopt expras RBRACE','defdef',13,'p_defdef','fusion.py',178),
  ('parmsopt -> parms','parmsopt',1,'p_parmsopt','fusion.py',186),
  ('parmsopt -> empty','parmsopt',1,'p_parmsopt','fusion.py',187),
  ('parms -> vardef COMMA parms','parms',3,'p_parms','fusion.py',192),
  ('parms -> vardef','parms',1,'p_parms','fusion.py',193),
  ('vardef -> ID COLON type','vardef',3,'p_vardef','fusion.py',201),
  ('type -> INT','type',1,'p_type','fusion.py',206),
  ('type -> LPAREN typesopt RPAREN ARROW type','type',5,'p_type','fusion.py',207),
  ('typesopt -> types','typesopt',1,'p_typesopt','fusion.py',215),
  ('typesopt -> empty','typesopt',1,'p_typesopt','fusion.py',216),
  ('types -> type COMMA types','types',3,'p_types','fusion.py',221),
  ('types -> type','types',1,'p_types','fusion.py',222),
  ('vardefsopt -> VAR vardef SEMI vardefsopt','vardefsopt',4,'p_vardefsopt','fusion.py',230),
  ('vardefsopt -> empty','vardefsopt',1,'p_vardefsopt','fusion.py',231),
  ('defdefsopt -> defdefs','defdefsopt',1,'p_defdefsopt','fusion.py',239),
  ('defdefsopt -> empty','defdefsopt',1,'p_defdefsopt','fusion.py',240),
  ('expras -> expra SEMI expras','expras',3,'p_expras','fusion.py',245),
  ('expras -> expra','expras',1,'p_expras','fusion.py',246),
  ('expra -> ID BECOMES expr','expra',3,'p_expra','fusion.py',254),
  ('expra -> expr','expra',1,'p_expra','fusion.py',255),
  ('expr -> IF LPAREN test RPAREN LBRACE expras RBRACE ELSE LBRACE expras RBRACE','expr',11,'p_expr','fusion.py',266),
  ('expr -> term','expr',1,'p_expr','fusion.py',267),
  ('expr -> expr PLUS term','expr',3,'p_expr','fusion.py',268),
  ('expr -> expr MINUS term','expr',3,'p_expr','fusion.py',269),
  ('term -> factor','term',1,'p_term','fusion.py',285),
  ('term -> term STAR factor','term',3,'p_term','fusion.py',286),
  ('term -> term SLASH factor','term',3,'p_term','fusion.py',287),
  ('term -> term PCT factor','term',3,'p_term','fusion.py',288),
  ('factor -> ID','factor',1,'p_factor','fusion.py',305),
  ('factor -> NUM','factor',1,'p_factor','fusion.py',306),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor','fusion.py',307),
  ('factor -> factor LPAREN argsopt RPAREN','factor',4,'p_factor','fusion.py',308),
  ('test -> expr NE expr','test',3,'p_test','fusion.py',318),
  ('test -> expr LT expr','test',3,'p_test','fusion.py',319),
  ('test -> expr LE expr','test',3,'p_test','fusion.py',320),
  ('test -> expr GE expr','test',3,'p_test','fusion.py',321),
  ('test -> expr GT expr','test',3,'p_test','fusion.py',322),
  ('test -> expr EQ expr','test',3,'p_test','fusion.py',323),
  ('argsopt -> args','argsopt',1,'p_argsopt','fusion.py',339),
  ('argsopt -> empty','argsopt',1,'p_argsopt','fusion.py',340),
  ('args -> expr COMMA args','args',3,'p_args','fusion.py',345),
  ('args -> expr','args',1,'p_args','fusion.py',346),
  ('empty -> <empty>','empty',0,'p_empty','fusion.py',361),
]
