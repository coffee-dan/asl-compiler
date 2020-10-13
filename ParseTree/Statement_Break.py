# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_Break() :
  def __init__( self, lineNum ) :
    self.m_NodeType = 'Statement_Break'

    self.m_LineNum   = lineNum

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (BREAK)', fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    # TODO: Do the semantic analysis required for a BREAK
    #       statement.
    #       Fix the return statement to return the correct AST
    #       form for a BREAK statement.  (Hey, is it _already_
    #       correct?  Are you _sure_?)

    return ( 'BREAK', )

#---------#---------#---------#---------#---------#--------#
