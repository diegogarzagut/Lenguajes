# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('AND', 'BEGIN', 'BOOL', 'COLON', 'COMA', 'CTE_FL', 'CTE_INT', 'DIVIDE', 'DWHILE', 'ELSE', 'END', 'EQUAL', 'ET', 'FL', 'FOR', 'FUNCTION', 'GT', 'ID', 'IF', 'INT', 'LCOR', 'LPAREN', 'LT', 'MAIN', 'MINUS', 'OR', 'PIPE', 'PLUS', 'PRINT', 'RCOR', 'READ', 'RPAREN', 'SEMICOLON', 'THEN', 'TIMES', 'UNTIL', 'WHILE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_MAIN>main)|(?P<t_READ>read)|(?P<t_LCOR>\\{)|(?P<t_RCOR>\\})|(?P<t_PRINT>print)|(?P<t_BEGIN>begin)|(?P<t_END>end)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_PIPE>\\|)|(?P<t_COLON>\\:)|(?P<t_SEMICOLON>\\;)|(?P<t_EQUAL>\\=)|(?P<t_GT>\\>)|(?P<t_LT>\\<)|(?P<t_ET>\\&)|(?P<t_ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_CTE_FL>\\d+\\.\\d+)|(?P<t_CTE_INT>\\d+)|(?P<t_newline>\\n+)|(?P<t_ignore_COMMENT>\\#.*)|(?P<t_PLUS>\\+)|(?P<t_TIMES>\\*)|(?P<t_COMA>\\,)|(?P<t_MINUS>-)|(?P<t_DIVIDE>/)', [None, ('t_MAIN', 'MAIN'), ('t_READ', 'READ'), ('t_LCOR', 'LCOR'), ('t_RCOR', 'RCOR'), ('t_PRINT', 'PRINT'), ('t_BEGIN', 'BEGIN'), ('t_END', 'END'), ('t_LPAREN', 'LPAREN'), ('t_RPAREN', 'RPAREN'), ('t_PIPE', 'PIPE'), ('t_COLON', 'COLON'), ('t_SEMICOLON', 'SEMICOLON'), ('t_EQUAL', 'EQUAL'), ('t_GT', 'GT'), ('t_LT', 'LT'), ('t_ET', 'ET'), ('t_ID', 'ID'), ('t_CTE_FL', 'CTE_FL'), ('t_CTE_INT', 'CTE_INT'), ('t_newline', 'newline'), (None, None), (None, 'PLUS'), (None, 'TIMES'), (None, 'COMA'), (None, 'MINUS'), (None, 'DIVIDE')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
