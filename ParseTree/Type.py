# Dalio, Brian A.
# dalioba
# 2019-11-11
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
  def isCoerceableTo( self, other ) :
    if self.isNumeric() and other.isNumeric() :
      return True

    else :
      return False

  def isInteger( self ) :
    return self.m_Kind == 'int'

  def isNumeric( self ) :
    return self.isInteger() or self.isReal()

  def isReal( self ) :
    return self.m_Kind == 'real'

  def isSame( self, other ) :
    return self.m_Kind == other.m_Kind

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'TYPE ({self.m_Kind!r})', fp )

#---------#---------#---------#---------#---------#--------#
