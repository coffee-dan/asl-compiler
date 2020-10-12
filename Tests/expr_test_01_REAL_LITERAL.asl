// Dalio, Brian A.
// dalioba
// 2019-10-18

{
  // Check precision.
  3.14159265358979323846264338327950288;

  // Has decimal point but no exponent.
  .1234;
  1234.;
  12.34;

  // Has decimal point and e exponent, no sign.
  .1234e123;
  1234.e123;
  12.34e123;

  // Has decimal point and E exponent, no sign.
  .1234E123;
  1234.E123;
  12.34E123;

  // Has decimal point and e exponent, + sign.
  .1234e+123;
  1234.e+123;
  12.34e+123;

  // Has decimal point and E exponent, + sign.
  .1234E+123;
  1234.E+123;
  12.34E+123;

  // Has decimal point and e exponent, - sign.
  .1234e-123;
  1234.e-123;
  12.34e-123;

  // Has decimal point and E exponent, - sign.
  .1234E-123;
  1234.E-123;
  12.34E-123;

  // No decimal point but e exponent, no sign.
  1234e123;

  // No decimal point but E exponent, no sign.
  1234E123;

  // No decimal point but e exponent, + sign.
  1234e+123;

  // No decimal point but E exponent, + sign.
  1234E+123;

  // No decimal point but e exponent, - sign.
  1234e-123;

  // No decimal point but E exponent, - sign.
  1234E-123;
}
