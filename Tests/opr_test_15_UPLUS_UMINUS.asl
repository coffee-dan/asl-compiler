// Dalio, Brian A.
// dalioba
// 2019-11-11

{
  int a;

  // Test of UPLUS / UMINUS precedence / associativity.
  // UPLUS and UMINUS have the same settings so these should parse
  // just as if it were the same operator all the way through.

  // Strict right-to-left test.
  a = + - + 1;
  a = - + - 1;
}
