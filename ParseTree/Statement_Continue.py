# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_Continue() :
  def __init__( self, lineNum ) :
    self.m_NodeType = 'Statement_Continue'

    self.m_LineNum   = lineNum

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (CONTINUE)', fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    inLoop = kwargs.get( 'inLoop', False )
    if inLoop :
      return ( 'CONTINUE', )
    else :
      raise SemanticError( f'[{self.m_LineNum}] CONTINUE not within loop construct.' )

#---------#---------#---------#---------#---------#--------#
