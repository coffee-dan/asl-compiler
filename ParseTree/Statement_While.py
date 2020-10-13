# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_While() :
  def __init__( self, lineNum, testExpr, stmtList ) :
    self.m_NodeType = 'Statement_While'

    self.m_LineNum   = lineNum
    self.m_TestExpr  = testExpr
    self.m_StmtList  = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (WHILE)', fp )

    self.m_TestExpr.dump( indent+1, fp = fp )
    self.m_StmtList.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    test = self.m_TestExpr.semantic( symbolTable, **kwargs )
    if test[2].m_Kind != 'int' :
      raise SemanticError( f'[{self.m_LineNum}] WHILE test expression must be of integer type, not \'{test[2].m_Kind}\'.' )

    new_kwargs = kwargs.copy()
    new_kwargs[ 'inLoop' ] = True

    body = self.m_StmtList.semantic( symbolTable, **new_kwargs )

    return ( 'WHILE', test, body )

#---------#---------#---------#---------#---------#--------#
