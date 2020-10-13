# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *
from Exceptions    import *

#---------#---------#---------#---------#---------#--------#
class Statement_For() :
  def __init__( self, lineNum, loopVar, startExpr, stopExpr, stepExpr, stmtList ) :
    self.m_NodeType = 'Statement_For'

    self.m_LineNum   = lineNum
    self.m_LoopVar   = loopVar
    self.m_StartExpr = startExpr
    self.m_StopExpr  = stopExpr
    self.m_StepExpr  = stepExpr
    self.m_StmtList  = stmtList

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      'STATEMENT (FOR)', fp )

    self.m_LoopVar.dump( indent+1, fp = fp )
    self.m_StartExpr.dump( indent+1, fp = fp )
    self.m_StopExpr.dump( indent+1, fp = fp )
    self.m_StepExpr.dump( indent+1, fp = fp )
    self.m_StmtList.dump( indent+1, fp = fp )

  #---------------------------------------
  def semantic( self, symbolTable, **kwargs ) :
    start = self.m_StartExpr.semantic( symbolTable, **kwargs )
    if start[2].m_Kind != 'int' :
      raise SemanticError( f'[{self.m_LineNum}] FOR start expression type must be integer, not \'{start[2].m_Kind}\'.' )

    stop = self.m_StopExpr.semantic( symbolTable, **kwargs )
    if stop [2].m_Kind != 'int' :
      raise SemanticError( f'[{self.m_LineNum}] FOR stop expression type must be integer, not \'{stop[2].m_Kind}\'.' )
    
    step = self.m_StepExpr.semantic( symbolTable, **kwargs )
    if step[2].m_Kind != 'int' :
      raise SemanticError( f'[{self.m_LineNum}] FOR step expression type must be integer, not \'{step[2].m_Kind}\'.' )

    index = self.m_LoopVar.semantic( symbolTable, **kwargs )

    # kwargs is a dict
    # python always passes kwargs as reference
    new_kwargs = kwargs.copy()

    # pass var name down the tree
    # check var list exists
    if kwargs.get( 'bannedVars') != None :
      if self.m_LoopVar.m_ID not in kwargs['bannedVars'] :
        kwargs['bannedVars'].append( self.m_LoopVar.m_ID )
    else:
      # create list of vars and append current var
      bannedVars = [self.m_LoopVar.m_ID]
      new_kwargs['bannedVars'] = bannedVars
      
    new_kwargs[ 'inLoop' ] = True

    body = self.m_StmtList.semantic( symbolTable, **new_kwargs )

    return ( 'FOR', index, start, stop, step, body )

#---------#---------#---------#---------#---------#--------#
