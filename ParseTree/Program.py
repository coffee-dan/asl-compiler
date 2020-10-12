# Ramirez, Daniel G.
# dgr2815
# 2019-10-19
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Program() :
  def __init__( self, lineNum, stmtList ) :
    self.m_NodeType = 'Program'

    self.m_LineNum  = lineNum
    self.m_StmtList = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'PROGRAM', fp )

    self.m_StmtList.dump( indent+1, fp = fp )

#---------#---------#---------#---------#---------#--------#
