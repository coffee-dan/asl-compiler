# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

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

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    # TODO: Do the semantic analysis of the id, start expression,
    #       stop expression, step expression, and body of the FOR.
    #       Fix the return statement to return the correct AST
    #       form for a FOR statement.

    return ( 'FOR', )

#---------#---------#---------#---------#---------#--------#
