# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_List() :
  def __init__( self, lineNum, stmtList ) :
    self.m_NodeType = 'Statement_List'

    self.m_LineNum  = lineNum
    self.m_StmtList = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'STATEMENT LIST [{len(self.m_StmtList)}]', fp )

    for s in self.m_StmtList :
      s.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    # TODO: Open a scope, do the semantic analysis of each item
    #       in the statement list, then close the scope.
    #       Fix the return statement to return the correct AST
    #       form for a statement list.

    return ( 'SCOPE', )

#---------#---------#---------#---------#---------#--------#
