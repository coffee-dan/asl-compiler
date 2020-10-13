# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Write() :
  def __init__( self, lineNum, exprList ) :
    self.m_NodeType = 'Statement_Write'

    self.m_LineNum   = lineNum
    self.m_ExprList  = exprList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (WRITE)', fp )

    dumpHeaderLine( indent+1, self.m_LineNum,
      f'EXPR LIST [{len(self.m_ExprList)}]', fp )

    for e in self.m_ExprList :
      e.dump( indent+2, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    # TODO: Do the semantic analysis of each expression passed
    #       to the WRITE.
    #       Fix the return statement to return the correct AST
    #       form for a WRITE statement.

    return ( 'WRITE', )

#---------#---------#---------#---------#---------#--------#
