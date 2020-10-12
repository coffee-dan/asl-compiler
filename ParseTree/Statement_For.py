# Dalio, Brian A.
# dalioba
# 2019-09-28
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_For() :
  def __init__( self, lineNum, loopVar, startExpr, stopExpr, stepExpr, stmtList ) :
    self.m_NodeType = 'Statement_For'

    self.m_LineNum   = lineNum
    self.m_LoopVar   = loopVar
    self.m_StartExpr = startExpr
    self.m_StopExpr  = stopExpr
    self.m_StepExpr  = stepExpr
    self.m_StmtList  = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (FOR)', fp )

    self.m_LoopVar.dump( indent+1, fp = fp )
    self.m_StartExpr.dump( indent+1, fp = fp )
    self.m_StopExpr.dump( indent+1, fp = fp )
    self.m_StepExpr.dump( indent+1, fp = fp )
    self.m_StmtList.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#
