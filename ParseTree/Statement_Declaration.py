# Ramirez, Daniel G.
# dgr2815
# 2019-10-19
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Declaration() :
  def __init__( self, lineNum, declType, declID, initExpr ) :
    self.m_NodeType = 'Statement_Declaration'

    self.m_LineNum   = lineNum
    self.m_Type      = declType
    self.m_ID        = declID
    self.m_InitExpr  = initExpr

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (DECLARATION)', fp )

    self.m_Type.dump( indent+1, fp = fp )
    self.m_ID.dump( indent+1, fp = fp )
    self.m_InitExpr.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#
