# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Statement_List() :
  def __init__( self, lineNum, stmtList ) :
    self.m_NodeType = 'Statement_List'

    self.m_LineNum  = lineNum
    self.m_StmtList = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'STATEMENT LIST [{len(self.m_StmtList)}]', fp )

    for s in self.m_StmtList :
      s.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    name = symbolTable.openScope( self.m_LineNum )
    sListASTs = [ s.semantic( symbolTable, **kwargs ) for s in self.m_StmtList ]
    symbolTable.closeScope()
    return ( 'SCOPE', name, sListASTs )

#---------#---------#---------#---------#---------#--------#
