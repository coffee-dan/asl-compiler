# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_If() :
  def __init__( self, lineNum, testList, elseStmtList ) :
    self.m_NodeType = 'Statement_If'

    self.m_LineNum      = lineNum
    self.m_TestList     = testList
    self.m_ElseStmtList = elseStmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (IF)', fp )

    dumpHeaderLine( indent+1, 0, f'TEST LIST [{len(self.m_TestList)}]', fp )
    for ( test, stmtList ) in self.m_TestList :
      test.dump( indent+2, fp = fp )
      stmtList.dump( indent+2, fp = fp )

    self.m_ElseStmtList.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    testList = []
    for ( test, stmtList ) in self.m_TestList :
      exprAST = test.semantic( symbolTable, **kwargs )
      if not exprAST[2].m_Kind == 'int' :
        raise SemanticError( f'[{self.m_LineNum}] IF test expression must be of integer type, not \'{exprAST[2].m_Kind}\'.' )
      sListAST = stmtList.semantic( symbolTable, **kwargs )
      testList.append( ( exprAST, sListAST ) )

    elseStmtList = self.m_ElseStmtList.semantic( symbolTable, **kwargs )

    #( 'IF', <testList>, <else> )
    return ( 'IF', testList, elseStmtList )

#---------#---------#---------#---------#---------#--------#
