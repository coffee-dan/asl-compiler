# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_If() :
  def __init__( self, lineNum, testList, elseStmtList ) :
    self.m_NodeType = 'Statement_If'

    self.m_LineNum      = lineNum
    self.m_TestList     = testList
    self.m_ElseStmtList = elseStmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (IF)', fp )

    dumpHeaderLine( indent+1, 0, f'TEST LIST [{len(self.m_TestList)}]', fp )
    for ( test, stmtList ) in self.m_TestList :
      test.dump( indent+2, fp = fp )
      stmtList.dump( indent+2, fp = fp )

    self.m_ElseStmtList.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    # TODO: Do the semantic analysis of each test expression and
    #       statement list that's part of the IF / THEN / ELIF /
    #       THEN chain.  Do the semantic analysis of the ELSE
    #       statement list.
    #       Fix the return statement to return the correct AST
    #       form for an IF statement.

    return ( 'IF', )

#---------#---------#---------#---------#---------#--------#
