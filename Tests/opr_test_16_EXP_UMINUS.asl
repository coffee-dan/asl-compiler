// Dalio, Brian A.
// dalioba
// 2019-10-06

{
  // Test of EXPONENTIATION / UMINUS precedence / associativity.
  // UMINUS has a higher precedence than EXPONENTIATION so the
  // right-to-left test will NOT be strict.  The UMINUS
  // operations will happen BEFORE the EXPONENTIATION operations.

  // Right-to-left test -- should show UMINUS before EXPONENTIATION.
  a = - 2 ^ 3;
  a = - - 2 ^ 3;
}
