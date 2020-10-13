# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

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

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    # TODO: Do the semantic analysis of each item passed to the
    #       READ.
    #       Fix the return statement to return the correct AST
    #       form for a READ statement.

    return ( 'READ', )

#---------#---------#---------#---------#---------#--------#
