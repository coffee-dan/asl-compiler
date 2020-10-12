# Ramirez, Daniel G.
# dgr2815
# 2019-10-19
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_If() :
  def __init__( self, lineNum, testExpr, thenStmtList, elifList, elseStmtList ) :
    self.m_NodeType = 'Statement_If'

    self.m_LineNum      = lineNum
    self.m_TestExpr     = testExpr
    self.m_ThenStmtList = thenStmtList
    self.m_ElifList     = elifList
    self.m_ElseStmtList = elseStmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (IF)', fp )

    self.m_TestExpr.dump( indent+1, fp = fp )
    self.m_ThenStmtList.dump( indent+1, fp = fp )

    dumpHeaderLine( indent+1, 0, f'ELIF LIST [{len(self.m_ElifList)}]', fp )
    for ( test, stmtList ) in self.m_ElifList :
      test.dump( indent+2, fp = fp )
      stmtList.dump( indent+2, fp = fp )

    self.m_ElseStmtList.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#
