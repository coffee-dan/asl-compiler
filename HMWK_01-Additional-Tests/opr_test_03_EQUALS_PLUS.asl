// Dalio, Brian A.
// dalioba
// 2019-09-25

// Test of EQUALS / PLUS precedence / associativity.
// PLUS has a higher precedence than EQUALS so the left-to-right
// test will NOT be strict.  The PLUS operations will happen
// BEFORE the EQUALS operations.

// NOTE:  This test is purely for precedence / associativity.
// The following expressions are SEMANTICALLY incorrect as the
// LHS of an assignment must be a L-value.  This error is caught
// in a later phase of the compilation process.

// Left-to-right test -- should show PLUS before EQUALS.
// EQUALS is right-to-left, but since these tests do not have
// multiple adjacent EQUALS operations, that does not come into
// play.
a = b = c + d = e;
a = b + c = d + e;

// Left-to-right and right-to-left, but with override due to ( ).
// The ( ) should override the higher precedence of PLUS so the
// EQUALS happens first.
b = c + ( d = e ) + f
