# Dalio, Brian A.
# dalioba
# 2019-10-31
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Expression_Literal() :
  def __init__( self, lineNum, valType, value ) :
    self.m_NodeType = 'Literal'

    self.m_LineNum  = lineNum
    self.m_Type     = valType
    self.m_Value    = value

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    if self.m_Type.isReal() :
      dumpHeaderLine( indent, self.m_LineNum,
        f'LITERAL {self.m_Type!r} {self.m_Value:.16e}', fp )

    else :
      dumpHeaderLine( indent, self.m_LineNum,
        f'LITERAL {self.m_Type!r} {self.m_Value!r}', fp )

#---------#---------#---------#---------#---------#--------#
