# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('BEGIN', 'CHAR', 'COLON', 'COMA', 'CTE_FL', 'CTE_INT', 'DIVIDE', 'DWHILE', 'ELSE', 'END', 'EQUAL', 'FL', 'FOR', 'FUNCTION', 'ID', 'IF', 'INT', 'LPAREN', 'MAIN', 'MINUS', 'NUMBER', 'PLUS', 'RPAREN', 'SEMICOLON', 'THEN', 'TIMES', 'UNTIL', 'WHILE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_MAIN>main)|(?P<t_BEGIN>begin)|(?P<t_END>end)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_COLON>\\:)|(?P<t_SEMICOLON>\\;)|(?P<t_EQUAL>\\=)|(?P<t_ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_CTE_INT>\\d+)|(?P<t_CTE_FL>\\d+\\.\\d+)|(?P<t_newline>\\n+)|(?P<t_ignore_COMMENT>\\#.*)|(?P<t_PLUS>\\+)|(?P<t_TIMES>\\*)|(?P<t_COMA>\\,)|(?P<t_MINUS>-)|(?P<t_DIVIDE>/)', [None, ('t_MAIN', 'MAIN'), ('t_BEGIN', 'BEGIN'), ('t_END', 'END'), ('t_LPAREN', 'LPAREN'), ('t_RPAREN', 'RPAREN'), ('t_COLON', 'COLON'), ('t_SEMICOLON', 'SEMICOLON'), ('t_EQUAL', 'EQUAL'), ('t_ID', 'ID'), ('t_CTE_INT', 'CTE_INT'), ('t_CTE_FL', 'CTE_FL'), ('t_newline', 'newline'), (None, None), (None, 'PLUS'), (None, 'TIMES'), (None, 'COMA'), (None, 'MINUS'), (None, 'DIVIDE')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
