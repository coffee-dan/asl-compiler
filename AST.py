# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from Exceptions     import *

#---------#---------#---------#---------#---------#--------#
INDENT_STR = '  '

def dumpLine( indent, contents, fp ) :
  print( (INDENT_STR*indent)+contents, file = fp )

#---------#---------#---------#---------#---------#--------#
class AST() :
  @staticmethod
  def dump( ast, indent = 0, fp = sys.stdout ) :
    if ast is None :
      dumpLine( indent, '<None>', fp = fp )

    elif ast[0] == 'BREAK' :
      dumpLine( indent, 'BREAK', fp )

    elif ast[0] == 'CONTINUE' :
      dumpLine( indent, 'CONTINUE', fp )

    elif ast[0] == 'EXPR' :
      _, parts, resultType, const, value = ast

      if parts[0] == 'LITERAL' :
        valStr = f'{value:.16e}' if resultType.isReal() else f'{value!r}'
        dumpLine( indent, f'LITERAL {resultType!r}, {valStr}', fp )

      elif parts[0] == 'LVALUE' :
        dumpLine( indent, f'LVALUE {parts[1]!r} {resultType!r}', fp )

      elif parts[0] == 'BINARY_OP' :
        dumpLine( indent, f'BINARY_OP {parts[1]!r} {resultType!r}', fp )
        AST.dump( parts[2], indent+1, fp )
        AST.dump( parts[3], indent+1, fp )

      elif parts[0] == 'UNARY_OP' :
        dumpLine( indent, f'UNARY_OP {parts[1]!r} {resultType!r}', fp )
        AST.dump( parts[2], indent+1, fp )

      else :
        raise InternalError( f'Unknown AST EXPR kind {parts[0]!r}.' )

    elif ast[0] == 'FOR' :
      _, indexAST, startAST, stopAST, stepAST, bodyAST = ast
      dumpLine( indent, 'FOR', fp )
      AST.dump( indexAST, indent+1, fp )
      AST.dump( startAST, indent+1, fp )
      AST.dump( stopAST, indent+1, fp )
      AST.dump( stepAST, indent+1, fp )
      AST.dump( bodyAST, indent+1, fp )

    elif ast[0] == 'IF' :
      _, testListAST, elseAST = ast
      dumpLine( indent, f'IF <{len(testListAST)}>', fp )
      for test, scope in testListAST :
        AST.dump( test, indent+2, fp )
        AST.dump( scope, indent+2, fp )
      AST.dump( elseAST, indent+1, fp )

    elif ast[0] == 'LOOP' :
      dumpLine( indent, 'LOOP', fp )
      AST.dump( ast[1], indent+1, fp )

    elif ast[0] == 'NOOP' :
      dumpLine( indent, 'NOOP', fp )

    elif ast[0] == 'READ' :
      lvals = ast[1]
      dumpLine( indent, f'READ <{len(lvals)}>', fp )
      for lv in lvals :
        AST.dump( lv, indent+1, fp )

    elif ast[0] == 'SCOPE' :
      _, name, stmts = ast
      dumpLine( indent, f'SCOPE {name!r} <{len(stmts)}>', fp )
      for s in stmts :
        AST.dump( s, indent+1, fp )

    elif ast[0] == 'VARIABLE_INIT' :
      _, name, expr = ast
      dumpLine( indent, f'VARIABLE_INIT {name}', fp )
      AST.dump( expr, indent+1, fp )

    elif ast[0] == 'WHILE' :
      _, test, stmt = ast
      dumpLine( indent, 'WHILE', fp )
      AST.dump( test, indent+1, fp )
      AST.dump( stmt, indent+1, fp )

    elif ast[0] == 'WRITE' :
      exprs = ast[1]
      dumpLine( indent, f'WRITE <{len(exprs)}>', fp )
      for e in exprs :
        AST.dump( e, indent+1, fp )

    else :
      raise InternalError( f'Unknown AST node type {ast[0]!r}.' )

#---------#---------#---------#---------#---------#--------#
