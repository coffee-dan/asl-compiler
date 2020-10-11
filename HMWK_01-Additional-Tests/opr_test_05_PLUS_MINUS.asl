// Dalio, Brian A.
// dalioba
// 2019-09-25

// Test of PLUS / MINUS precedence / associativity.
// PLUS and MINUS have the same settings so these should parse
// just as if it were the same operator all the way through.

// Strict left-to-right test.
a = 1 + 2 - 3 + 4;
a = 1 - 2 + 3 - 4;

// Left-to-right, but with override due to ( ).
b = 5 + ( 6 - 7 ) + 8;
b = 5 - ( 6 + 7 ) - 8