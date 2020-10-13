# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
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
    inLoop = kwargs.get( 'inLoop', False )
    if inLoop :
      return ( 'BREAK', )
    else :
      raise SemanticError( f'[{self.m_LineNum}] BREAK not within loop construct.' )

#---------#---------#---------#---------#---------#--------#
