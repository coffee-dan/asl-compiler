// Dalio, Brian A.
// dalioba
// 2019-11-11

{
  int a; int b;

  // Test of DIVIDE associativity.

  // Strict left-to-right test.
  a = 1 % 2 % 3 % 4;

  // Left-to-right, but with override due to ( ).
  b = 5 % ( 6 % 7 ) % 8
}
