# Ramirez, Daniel G.
# dgr2815
# 2019-11-01
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Type() :
  def __init__( self, lineNum, kind ) :
    self.m_NodeType = 'Type'

    self.m_LineNum   = lineNum
    self.m_Kind      = kind

  def __repr__( self ) :
    return f'{self.m_Kind!r}'

  #---------------------------------------
  def isReal( self ) :
    return self.m_Kind == 'real'

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'TYPE ({self.m_Kind!r})', fp )

#---------#---------#---------#---------#---------#--------#
