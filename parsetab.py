
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION COLON COMMA DIVIDE FORGET ID JOKE LC LEARN LP MODULO MULTIPLY NUMBER PERIOD PLUS POWER RANDOM RC RESPONSE ROLLDICE ROOT RP SEMICOLON STRING SUBTRACT SUM UNKNOWNstatement : create_bot\n                    | statement create_botresponse_rule : STRING COLON RESPONSE LP STRING RP SEMICOLONlearn_rule : STRING COLON LEARN LP ID RP SEMICOLONforget_rule : STRING COLON FORGET LP ID RP SEMICOLONaction_rule : STRING COLON ACTION PERIOD SUM LP ID COMMA ID RP SEMICOLON\n                    | STRING COLON ACTION PERIOD SUBTRACT LP ID COMMA ID RP SEMICOLON\n                    | STRING COLON ACTION PERIOD MULTIPLY LP ID COMMA ID RP SEMICOLON\n                    | STRING COLON ACTION PERIOD POWER LP ID COMMA ID RP SEMICOLON\n                    | STRING COLON ACTION PERIOD JOKE LP RP SEMICOLON\n                    | STRING COLON ACTION PERIOD ROLLDICE LP RP SEMICOLON\n                    | STRING COLON ACTION PERIOD ROOT LP ID RP SEMICOLON\n                    | STRING COLON ACTION PERIOD DIVIDE LP ID COMMA ID RP SEMICOLON\n                    | STRING COLON ACTION PERIOD MODULO LP ID COMMA ID RP SEMICOLON\n                    | STRING COLON ACTION PERIOD RANDOM LP RP SEMICOLONrules : response_rule\n                | learn_rule\n                | action_rule\n                | rules response_rule\n                | rules action_rule\n                | rules learn_rulecreate_bot : ID LC rules RC'
    
_lr_action_items = {'ID':([0,1,2,4,11,22,38,39,40,41,44,45,46,60,61,62,63,67,68,],[3,3,-1,-2,-22,25,50,51,52,53,56,57,58,70,71,72,73,75,76,]),'$end':([1,2,4,11,],[0,-1,-2,-22,]),'LC':([3,],[5,]),'STRING':([5,6,7,8,9,12,13,14,21,48,49,64,65,69,74,83,84,85,86,87,88,],[10,15,-16,-17,-18,-19,-20,-21,24,-3,-4,-10,-11,-15,-12,-6,-7,-8,-9,-13,-14,]),'RC':([6,7,8,9,12,13,14,48,49,64,65,69,74,83,84,85,86,87,88,],[11,-16,-17,-18,-19,-20,-21,-3,-4,-10,-11,-15,-12,-6,-7,-8,-9,-13,-14,]),'COLON':([10,15,],[16,17,]),'RESPONSE':([16,17,],[18,18,]),'LEARN':([16,17,],[19,19,]),'ACTION':([16,17,],[20,20,]),'LP':([18,19,26,27,28,29,30,31,32,33,34,35,],[21,22,38,39,40,41,42,43,44,45,46,47,]),'PERIOD':([20,],[23,]),'SUM':([23,],[26,]),'SUBTRACT':([23,],[27,]),'MULTIPLY':([23,],[28,]),'POWER':([23,],[29,]),'JOKE':([23,],[30,]),'ROLLDICE':([23,],[31,]),'ROOT':([23,],[32,]),'DIVIDE':([23,],[33,]),'MODULO':([23,],[34,]),'RANDOM':([23,],[35,]),'RP':([24,25,42,43,47,56,70,71,72,73,75,76,],[36,37,54,55,59,66,77,78,79,80,81,82,]),'SEMICOLON':([36,37,54,55,59,66,77,78,79,80,81,82,],[48,49,64,65,69,74,83,84,85,86,87,88,]),'COMMA':([50,51,52,53,57,58,],[60,61,62,63,67,68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'create_bot':([0,1,],[2,4,]),'rules':([5,],[6,]),'response_rule':([5,6,],[7,12,]),'learn_rule':([5,6,],[8,14,]),'action_rule':([5,6,],[9,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> create_bot','statement',1,'p_statement','JarvisYacc.py',33),
  ('statement -> statement create_bot','statement',2,'p_statement','JarvisYacc.py',34),
  ('response_rule -> STRING COLON RESPONSE LP STRING RP SEMICOLON','response_rule',7,'p_response_rule','JarvisYacc.py',51),
  ('learn_rule -> STRING COLON LEARN LP ID RP SEMICOLON','learn_rule',7,'p_learn_rule','JarvisYacc.py',60),
  ('forget_rule -> STRING COLON FORGET LP ID RP SEMICOLON','forget_rule',7,'p_forget_rule','JarvisYacc.py',66),
  ('action_rule -> STRING COLON ACTION PERIOD SUM LP ID COMMA ID RP SEMICOLON','action_rule',11,'p_action_rule','JarvisYacc.py',74),
  ('action_rule -> STRING COLON ACTION PERIOD SUBTRACT LP ID COMMA ID RP SEMICOLON','action_rule',11,'p_action_rule','JarvisYacc.py',75),
  ('action_rule -> STRING COLON ACTION PERIOD MULTIPLY LP ID COMMA ID RP SEMICOLON','action_rule',11,'p_action_rule','JarvisYacc.py',76),
  ('action_rule -> STRING COLON ACTION PERIOD POWER LP ID COMMA ID RP SEMICOLON','action_rule',11,'p_action_rule','JarvisYacc.py',77),
  ('action_rule -> STRING COLON ACTION PERIOD JOKE LP RP SEMICOLON','action_rule',8,'p_action_rule','JarvisYacc.py',78),
  ('action_rule -> STRING COLON ACTION PERIOD ROLLDICE LP RP SEMICOLON','action_rule',8,'p_action_rule','JarvisYacc.py',79),
  ('action_rule -> STRING COLON ACTION PERIOD ROOT LP ID RP SEMICOLON','action_rule',9,'p_action_rule','JarvisYacc.py',80),
  ('action_rule -> STRING COLON ACTION PERIOD DIVIDE LP ID COMMA ID RP SEMICOLON','action_rule',11,'p_action_rule','JarvisYacc.py',81),
  ('action_rule -> STRING COLON ACTION PERIOD MODULO LP ID COMMA ID RP SEMICOLON','action_rule',11,'p_action_rule','JarvisYacc.py',82),
  ('action_rule -> STRING COLON ACTION PERIOD RANDOM LP RP SEMICOLON','action_rule',8,'p_action_rule','JarvisYacc.py',83),
  ('rules -> response_rule','rules',1,'p_rules','JarvisYacc.py',112),
  ('rules -> learn_rule','rules',1,'p_rules','JarvisYacc.py',113),
  ('rules -> action_rule','rules',1,'p_rules','JarvisYacc.py',114),
  ('rules -> rules response_rule','rules',2,'p_rules','JarvisYacc.py',115),
  ('rules -> rules action_rule','rules',2,'p_rules','JarvisYacc.py',116),
  ('rules -> rules learn_rule','rules',2,'p_rules','JarvisYacc.py',117),
  ('create_bot -> ID LC rules RC','create_bot',4,'p_create_bot','JarvisYacc.py',133),
]