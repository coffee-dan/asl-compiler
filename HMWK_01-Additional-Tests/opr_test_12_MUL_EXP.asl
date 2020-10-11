// Dalio, Brian A.
// dalioba
// 2019-09-25

// Test of MULTIPLY / EXPONENTIATION precedence / associativity.
// EXPONENTIATION has a higher precedence than MULTIPLY so the
// left-to-right test will NOT be strict.  The EXPONENTIATION
// operations will happen BEFORE the MULTIPLY operations.

// Left-to-right test -- should show EXPONENTIATION before
// MULTIPLY.
// EXPONENTIATION is right-to-left, but since these tests do not
// have multiple adjacent EXPONENTIATION operations, that does
// not come into play.
a = 1 * 2 ^ 3 * 4;
a = 1 ^ 2 * 3 ^ 4;

// Left-to-right and right-to-left, but with override due to ( ).
// First case should be same shape as if ( ) were NOT there as
// EXPONENTIATION already has higher precedence than MULTIPLY.
// In the second case the ( ) should override the higher
// precedence of EXPONENTIATION so the MULTIPLY happens first.
// Also in the second case, the right-to-left associativity of
// EXPONENTIATION should be seen.
b = 5 * ( 6 ^ 7 ) * 8;
b = 5 ^ ( 6 * 7 ) ^ 8