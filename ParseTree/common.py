# Ramirez, Daniel G.
# dgr2815
# 2019-11-16
#---------#---------#---------#---------#---------#--------#
INDENT_STR = '  '

#---------#---------#---------#---------#---------#--------#
def dumpHeaderLine( indent, lineNum, contents, fp ) :
  print( f'({lineNum:4d}) '+(INDENT_STR*indent)+contents, file = fp )

#---------#---------#---------#---------#---------#--------#
