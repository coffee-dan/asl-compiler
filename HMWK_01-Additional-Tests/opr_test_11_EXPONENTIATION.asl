// Dalio, Brian A.
// dalioba
// 2019-09-25

// Test of EXPONENTIATION associativity.

// Strict right-to-left test.
a = 1 ^ 2 ^ 3 ^ 4;

// Right-to-left, but with override due to ( ).
b = 5 ^ ( 6 ^ 7 ) ^ 8