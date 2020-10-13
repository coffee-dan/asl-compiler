# Dalio, Brian A.
# dalioba
# 2019-11-12
#---------#---------#---------#---------#---------#--------#
import sys

#---------#---------#---------#---------#---------#--------#
class _Unique() :
  c_nameIndex = 0

  def name( prefix = 'g' ) :
    _Unique.c_nameIndex += 1

    name = f'{prefix}{_Unique.c_nameIndex}'

    return name

#-----------------------------------------------------------
class _Entry() :
  def __init__( self, name, myType, lineNum = 0 ) :
    self.m_Name    = name
    self.m_MyType  = myType
    self.m_LineNum = lineNum
    self.m_Scope   = None

  @property
  def name( self ) : return self.m_Name

  @property
  def myType( self ) : return self.m_MyType

  @property
  def lineNum( self ) : return self.m_LineNum

  @property
  def scope( self ) : return self.m_Scope
  @scope.setter
  def scope( self, scope ) : self.m_Scope = scope

  @property
  def qualifiedName( self ) :
    if self.scope is None :
      raise ValueError( f'Entry {self.name!r}({self.lineNum}) has no scope.' )

    result = f'{self.scope.name}:{self.name}'

    return result

  def __repr__( self ) :
    if self.scope is None :
      scopeStr = ''

    else :
      scopeStr = self.scope.name

    return f'<Entry {scopeStr}({self.lineNum}) {self.name!r}:{self.myType!r}>'

#-----------------------------------------------------------
class _Scope() :
  def __init__( self, parentName, lineNum = 0, name = None ) :
    if name is None :
      name = _Unique.name( 'SCOPE_' )

    self.m_Name       = name
    self.m_ParentName = parentName
    self.m_LineNum    = lineNum
    self.m_Includes   = dict()

  @property
  def name( self ) : return self.m_Name

  @property
  def parentName( self ) : return self.m_ParentName

  @property
  def lineNum( self ) : return self.m_LineNum

  def __repr__( self ) :
    return f'<Scope ({self.lineNum}) {self.name!r}({self.parentName!r}) [{len(self.m_Includes)}]>'

  #---------------------------------------
  def addEntry( self, entry ) :
    entryAlready = self.getEntry( entry.name )
    if entryAlready is not None :
      print( f'Warning: replacing {entryAlready} in scope {self.name}({self.lineNum}) with {entry}.' )

    self.m_Includes[ entry.name ] = entry
    entry.scope = self

  def getEntry( self, name ) :
    return self.m_Includes.get( name, None )

  def getNamesAndTypes( self ) :
    return [ ( e.qualifiedName, e.myType ) for e in self.m_Includes ]

  #---------------------------------------
  def dump( self, fp = sys.stdout ) :
    print( f'Scope {self.name}({self.lineNum}) [{len(self.m_Includes)}] <{self.parentName}>', file = fp )

    for name in sorted( self.m_Includes.keys() ) :
      print( f'  {self.getEntry( name )}', file = fp )

#-----------------------------------------------------------
class SymbolTable() :
  c_AllScopes = {}

  def __init__( self ) :
    env = _Scope( 'NONE', name = 'ENVIRONMENT' )
    SymbolTable.c_AllScopes[ env.name ] = env

    self.m_Scopes = [ env ]

  @property
  def scope( self ) :
    return self.m_Scopes[0]

  #---------------------------------------
  def openScope( self, lineNum = 0 ) :
    scope = _Scope( self.scope.name, lineNum )
    self.m_Scopes.insert( 0, scope )

    SymbolTable.c_AllScopes[ scope.name ] = scope

    return scope.name

  def closeScope( self ) :
    self.m_Scopes = self.m_Scopes[1:]

  #---------------------------------------
  def addName( self, name, _type, lineNum = 0 ) :
    entry = _Entry( name, _type, lineNum )
    self.scope.addEntry( entry )
    return entry

  def findName( self, name ) :
    for scope in self.m_Scopes :
      entry = scope.getEntry( name )
      if entry is not None :
        return entry

    return None

  def nameExistsInCurrentScope( self, name ) :
    return self.scope.getEntry( name ) is not None

  #---------------------------------------
  @staticmethod
  def dump( fp = sys.stdout ) :
    for scope in SymbolTable.c_AllScopes.values() :
      scope.dump( fp = fp )

  #---------------------------------------
  @staticmethod
  def scopeByName( name ) :
    return SymbolTable.c_AllScopes.get( name, None )

#---------#---------#---------#---------#---------#--------#
def _main() :
  st = SymbolTable()

  st.openScope( 10 )
  e = st.addName( 'fred', 'int', 12 )
  f = st.findName( 'fred' )
  fn = 'NONE' if f is None else f.qualifiedName
  print( f'added fred: {e}\nfound: {fn}' )

  st.openScope( 20 )
  e = st.addName( 'barney', 'int', 23 )
  f = st.findName( 'barney' )
  fn = 'NONE' if f is None else f.qualifiedName
  print( f'added barney: {e}\nfound: {fn}' )

  f = st.findName( 'fred' )
  fn = 'NONE' if f is None else f.qualifiedName
  print( f'found fred again: {fn}' )

  st.closeScope()

  f = st.findName( 'barney' )
  fn = 'NONE' if f is None else f.qualifiedName
  print( f'should not find barney: {fn}' )

  st.openScope( 30 )
  e = st.addName( 'wilma', 'int', 34 )
  f = st.findName( 'wilma' )
  fn = 'NONE' if f is None else f.qualifiedName
  print( f'added wilma: {e}\nfound: {fn}' )

  e = st.addName( 'fred', 'int', 36 )
  f = st.findName( 'fred' )
  fn = 'NONE' if f is None else f.qualifiedName
  print( f'added another fred: {e}\nfound: {fn}' )

  f = st.findName( 'barney' )
  fn = 'NONE' if f is None else f.qualifiedName
  print( f'should not find barney: {fn}' )

  st.closeScope()

  st.closeScope()

  print( '\n=== Symbol table dump ===' )
  st.dump()

if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
