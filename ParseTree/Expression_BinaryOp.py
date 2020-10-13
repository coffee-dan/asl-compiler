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

logical_operators = [ r'&&', r'\|\|', r'==', r'<>', r'<', r'<=', r'>', r'>=' ]

#---------#---------#---------#---------#---------#--------#
def _binaryResultType( op, lType, rType, lineNum ) :
  if lType.m_Kind == 'string' or rType.m_Kind == 'string' :
    raise SemanticError( f'[{lineNum}] Inappropriate types \'{lType.m_Kind}\', \'{rType.m_Kind}\' for binary operator "{op}".' )

  if op in logical_operators and ( lType.isReal() or rType.isReal() ) :
    raise SemanticError( 'error, real does not support logical operators' )

  if lType.isSame( rType ) :
    return lType
  else :
    # strongly typed language
    if op == '=' :
      raise SemanticError( 'error, this is a strongly typed language' )
    else :
      return REAL_TYPE


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
    if kwargs.get( 'bannedVars') != None :
      if self.m_Op == '=' :
        # check if unqualified var name matches current loop variable
        if self.m_Left.m_ID in kwargs['bannedVars'] :
          if symbolTable.nameExistsInCurrentScope( self.m_Left.m_ID ) == False :
            raise SemanticError( f'[{self.m_LineNum}] FOR index variable on LHS of assignment.' )

    leftAST = self.m_Left.semantic( symbolTable, **kwargs )
    rightAST = self.m_Right.semantic( symbolTable, **kwargs )
    _type = _binaryResultType( self.m_Op, leftAST[2], rightAST[2], self.m_LineNum )
    isConst = False
    value = None

    return ( 'EXPR', [ 'BINARY_OP', self.m_Op, leftAST, rightAST ], _type, isConst, value )

#---------#---------#---------#---------#---------#--------#
