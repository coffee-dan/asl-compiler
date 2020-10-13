# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *
from .Type         import Type

#---------#---------#---------#---------#---------#--------#
INT_TYPE  = Type( 0, 'int' )
REAL_TYPE = Type( 0, 'real' )

#---------#---------#---------#---------#---------#--------#
def _unaryResultType( op, rType ) :
  if rType.m_Kind == INT_TYPE.m_Kind or rType.m_Kind == REAL_TYPE.m_Kind :
    return rType
  else :
    return None

#---------#---------#---------#---------#---------#--------#
class Expression_UnaryOp() :
  def __init__( self, lineNum, op, right ) :
    self.m_NodeType = 'UnaryOp'

    self.m_LineNum  = lineNum
    self.m_Op       = op
    self.m_Right    = right

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'UNARY_OP {self.m_Op!r}', fp )

    self.m_Right.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :    
    # if m_Right is Unary Operation
    parts = []
    _type = ''
    isConst = False
    value = None

    if self.m_Right.m_NodeType == 'UnaryOp' :
      recurseAST = self.m_Right.semantic( symbolTable, **kwargs )

      parts = [ 'UNARY_OP', self.m_Op, recurseAST ]
      _type = _unaryResultType( self.m_Op, recurseAST[2] )

    # if m_Right is an Identifier
    elif self.m_Right.m_NodeType == 'Identifier' :

      entry = symbolTable.findName( self.m_Right.m_ID )

      if entry == None :
        raise SemanticError( f'{self.m_NodeType} error, identifier does not exist in the symbol table, at line: {self.m_LineNum}' )
      else :
        _type = _unaryResultType( self.m_Op, entry.myType )

        if _type == None :
          raise SemanticError( f'{self.m_NodeType} error, operator operand combination not supported, at line: {self.m_LineNum}' )
        
        parts = [ 'UNARY_OP', self.m_Op, self.m_Right.semantic( symbolTable, **kwargs ) ]
        isConst = False
        value = None


    # if m_Right is a Literal
    elif self.m_Right.m_NodeType == 'Literal' :

      _type = _unaryResultType( self.m_Op, self.m_Right.m_Type )

      if _type == None :
        raise SemanticError( f'[{self.m_LineNum}] Inappropriate type \'{self.m_Right.m_Type.m_Kind}\' for unary operator "{self.m_Op}".' )
      
      parts = [ 'UNARY_OP', self.m_Op, self.m_Right.semantic( symbolTable, **kwargs ) ]
      isConst = False
      value = None

    return ( 'EXPR', parts, _type, isConst, value )

#---------#---------#---------#---------#---------#--------#
