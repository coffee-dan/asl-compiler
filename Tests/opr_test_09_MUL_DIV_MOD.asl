// Dalio, Brian A.
// dalioba
// 2019-10-06

{
  // Test of MULTIPLY / DIVIDE / MODULUS precedence / associativity.
  // MULTIPLY, DIVIDE, and MODULUS have the same settings so these
  // should parse just as if it were the same operator all the way
  // through.

  // Strict left-to-right test.
  a = 1 * 2 / 3 % 4;
  a = 1 * 2 % 3 / 4;
  a = 1 / 2 % 3 * 4;
  a = 1 / 2 * 3 % 4;
  a = 1 % 2 * 3 / 4;
  a = 1 % 2 / 3 * 4;

  // Left-to-right, but with override due to ( ).
  b = 1 * ( 2 / 3 ) % 4;
  b = 1 * ( 2 % 3 ) / 4;
  b = 1 / ( 2 % 3 ) * 4;
  b = 1 / ( 2 * 3 ) % 4;
  b = 1 % ( 2 * 3 ) / 4;
  b = 1 % ( 2 / 3 ) * 4;
}
