# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_Read() :
  def __init__( self, lineNum, idList ) :
    self.m_NodeType = 'Statement_Read'

    self.m_LineNum   = lineNum
    self.m_IDList    = idList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (READ)', fp )

    dumpHeaderLine( indent+1, self.m_LineNum,
      f'ID LIST [{len(self.m_IDList)}]', fp )

    for i in self.m_IDList :
      i.dump( indent+2, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    lvalASTs = []
    for identifer in self.m_IDList :
      if symbolTable.findName( identifer.m_ID ) == None :
        raise SemanticError( f'{self.m_NodeType} error {identifer.m_ID} does not exist in the symbol table, at line: {self.m_LineNum}' )
      else :
        lvalASTs.append( identifer.semantic( symbolTable, **kwargs ) )

      if kwargs.get( 'bannedVars') != None :
        # check if unqualified var name matches current loop variable
        if identifer.m_ID in kwargs['bannedVars'] :
          if symbolTable.nameExistsInCurrentScope( identifer.m_ID ) == False :
            raise SemanticError( f'[{self.m_LineNum}] FOR index variable in READ argument list.' )

    return ( 'READ', lvalASTs )

#---------#---------#---------#---------#---------#--------#
