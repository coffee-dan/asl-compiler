# Ramirez, Daniel G.
# dgr2815
# 2019-10-10
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Type() :
  def __init__( self, lineNum, kind ) :
    self.m_NodeType = 'Type'

    self.m_LineNum  = lineNum
    self.m_Kind     = kind

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'TYPE ({self.m_Kind!r})', fp )

#---------#---------#---------#---------#---------#--------#
