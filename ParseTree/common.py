# Daniel, Ranirez G.
# dgr2815
# 2019-09-26
#---------#---------#---------#---------#---------#--------#
INDENT_STR = '  '

#---------#---------#---------#---------#---------#--------#
def dumpHeaderLine( indent, lineNum, contents, fp ) :
  print( f'({lineNum:4d}) '+(INDENT_STR*indent)+contents, file = fp )

#---------#---------#---------#---------#---------#--------#
