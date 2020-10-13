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
def _unaryResultType( op, rType ) :
  # TODO: Using op and rType, return the proper type of the result
  #       of using op on an operand of the given type.

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
    # TODO: Do the semantic analysis required for a unary op
    #       expression.  (You will benefit from writing and using
    #       the _unaryResultType() function above.)
    #       Fix the return statement to return the correct AST
    #       form for a unary op expression.

    return ( 'EXPR', )

#---------#---------#---------#---------#---------#--------#
