# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Expression_Identifier() :
  def __init__( self, lineNum, identifier ) :
    self.m_NodeType = 'Identifier'

    self.m_LineNum  = lineNum
    self.m_ID       = identifier

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'IDENTIFIER {self.m_ID!r}', fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    entry = symbolTable.findName( self.m_ID )
    if entry == None :
      raise SemanticError( f'[{self.m_LineNum}] Undeclared identifier "{self.m_ID}".' )
    
    parts = [ 'LVALUE', entry.qualifiedName ]
    isConst = False
    value = None

    # ( 'EXPR', [ 'LVALUE', 'Scope_1:a' ], 'int', False, None )
    return ( 'EXPR', parts, entry.myType, isConst, value )

#---------#---------#---------#---------#---------#--------#
