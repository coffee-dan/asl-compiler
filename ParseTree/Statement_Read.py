# Dalio, Brian A.
# dalioba
# 2019-10-18
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_Read() :
  def __init__( self, lineNum, idList ) :
    self.m_NodeType = 'Statement_Read'

    self.m_LineNum   = lineNum
    self.m_IDList    = idList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (READ)', fp )

    dumpHeaderLine( indent+1, self.m_LineNum,
      f'ID LIST [{len(self.m_IDList)}]', fp )

    for i in self.m_IDList :
      i.dump( indent+2, fp = fp )

#---------#---------#---------#---------#---------#--------#
