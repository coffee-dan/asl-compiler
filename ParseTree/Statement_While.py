# Ramirez, Daniel G.
# dgr2815
# 2019-10-19
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_While() :
  def __init__( self, lineNum, testExpr, stmtList ) :
    self.m_NodeType = 'Statement_While'

    self.m_LineNum   = lineNum
    self.m_TestExpr  = testExpr
    self.m_StmtList  = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (WHILE)', fp )

    self.m_TestExpr.dump( indent+1, fp = fp )
    self.m_StmtList.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#
