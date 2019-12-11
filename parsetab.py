
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLOSE COMMA EQUALS INTEGER IP JOIN LPAREN NEWLINE OPEN RECEIVE RPAREN SEMI SEND STRING WORD\n    function : OPEN LPAREN RPAREN\n    \n    function : CLOSE LPAREN RPAREN\n    \n    function : JOIN LPAREN IP RPAREN\n    \n    data : STRING\n         | WORD\n         | INTEGER\n    '
    
_lr_action_items = {'OPEN':([0,],[2,]),'CLOSE':([0,],[3,]),'JOIN':([0,],[4,]),'$end':([1,8,9,11,],[0,-1,-2,-3,]),'LPAREN':([2,3,4,],[5,6,7,]),'RPAREN':([5,6,10,],[8,9,11,]),'IP':([7,],[10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> function","S'",1,None,None,None),
  ('function -> OPEN LPAREN RPAREN','function',3,'p_function_open','ConvoParser.py',9),
  ('function -> CLOSE LPAREN RPAREN','function',3,'p_function_close','ConvoParser.py',16),
  ('function -> JOIN LPAREN IP RPAREN','function',4,'p_function_join','ConvoParser.py',22),
  ('data -> STRING','data',1,'p_data','ConvoParser.py',28),
  ('data -> WORD','data',1,'p_data','ConvoParser.py',29),
  ('data -> INTEGER','data',1,'p_data','ConvoParser.py',30),
]
