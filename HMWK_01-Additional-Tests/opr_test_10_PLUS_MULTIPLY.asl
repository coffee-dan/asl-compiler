// Dalio, Brian A.
// dalioba
// 2019-09-25

// Test of PLUS / MULTIPLY precedence / associativity.
// MULTIPLY has a higher precedence than PLUS so the left-to-right
// test will NOT be strict.  The MULTIPLY operations will happen
// BEFORE the PLUS operations.

// Left-to-right test -- should show MULTIPLY before PLUS.
a = 1 + 2 * 3 + 4;
a = 1 * 2 + 3 * 4;

// Left-to-right, but with override due to ( ).
// First case should be same shape as if ( ) were NOT there as
// MULTIPLY already has higher precedence than PLUS.
// In the second case the ( ) should override the higher
// precedence of MULTIPLY so the PLUS happens first.
b = 5 + ( 6 * 7 ) + 8;
b = 5 * ( 6 + 7 ) * 8