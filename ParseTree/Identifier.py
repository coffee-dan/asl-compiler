# Dalio, Brian A.
# dalioba
# 2019-02-27
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Identifier() :
  def __init__( self, lineNum, identifier ) :
    self.m_NodeType = 'Identifier'

    self.m_LineNum  = lineNum
    self.m_ID       = identifier

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'IDENTIFIER {self.m_ID!r}', fp )

#---------#---------#---------#---------#---------#--------#
