// Dalio, Brian A.
// dalioba
// 2019-10-18

{
  // Compute factorial of this number.
  int n;
  read( n );

  // Resulting value.
  int fact = 1;

  // Loop up to n, doing a multiply at each step.
  for i = 1 to n do
    fact = fact * i;
  end for;

  // At this point, fact is n!.
  write( fact );
}
