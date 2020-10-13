# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_Declaration() :
  def __init__( self, lineNum, declType, declID, initExpr ) :
    self.m_NodeType = 'Statement_Declaration'

    self.m_LineNum   = lineNum
    self.m_Type      = declType
    self.m_ID        = declID
    self.m_InitExpr  = initExpr

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (DECLARATION)', fp )

    self.m_Type.dump( indent+1, fp = fp )
    self.m_ID.dump( indent+1, fp = fp )
    self.m_InitExpr.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    name = self.m_ID.m_ID
    if not symbolTable.nameExistsInCurrentScope( name ) :

      initExprAST = self.m_InitExpr.semantic( symbolTable, **kwargs )

      if self.m_Type.isSame( initExprAST[2] ) :
        entry = symbolTable.addName( name, self.m_Type, self.m_LineNum )
      else :
        initType = initExprAST[2].m_Kind
        declType = self.m_Type.m_Kind
        raise SemanticError( f'[{self.m_LineNum}] Initialization expression type \'{initType}\' not the same as declaration type \'{declType}\'.' )
    else :
      raise SemanticError( f'[{self.m_LineNum}] Name "{name}" redeclared.' )
    
    return ( 'VARIABLE_INIT', entry.qualifiedName, initExprAST )

#---------#---------#---------#---------#---------#--------#
