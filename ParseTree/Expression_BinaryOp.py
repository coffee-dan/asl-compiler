# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *
from .Type         import Type

#---------#---------#---------#---------#---------#--------#
INT_TYPE  = Type( 0, 'int' )
REAL_TYPE = Type( 0, 'real' )

#---------#---------#---------#---------#---------#--------#
def _binaryResultType( op, lType, rType ) :
  # TODO: Using op, lType, and rType, return the proper type
  #       of the result of using op on operands of the given
  #       types.

#---------#---------#---------#---------#---------#--------#
class Expression_BinaryOp() :
  def __init__( self, lineNum, op, left, right ) :
    self.m_NodeType = 'BinaryOp'

    self.m_LineNum  = lineNum
    self.m_Op       = op
    self.m_Left     = left
    self.m_Right    = right

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'BINARY_OP {self.m_Op!r}', fp )

    self.m_Left.dump( indent+1, fp = fp )
    self.m_Right.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    # TODO: Do the semantic analysis required for a binary op
    #       expression.  (You will benefit from writing and using
    #       the _binaryResultType() function above.)
    #       Fix the return statement to return the correct AST
    #       form for a binary op expression.

    return ( 'EXPR', )

#---------#---------#---------#---------#---------#--------#
