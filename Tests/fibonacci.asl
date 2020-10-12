// Dalio, Brian A.
// dalioba
// 2019-10-18

{
  // Compute this fibonacci number.
  int n;
  read( n );

  // Some temporaries.
  int previous = 0;       // Fibonacci(0) = 0
  int current  = 1;       // Fibonacci(1) = 1
  int next;

  // Loop n-1 times to compute Fibonacci(n).
  // (We already know Fibonacci(1) as a base case.)
  for i = 2 to n do
    // next is now Fibbonaci(i)
    next     = previous + current;

    // Remember the last two Fibonacci numbers for
    // the next iteration.
    previous = current;
    current  = next;
  end for;

  // At this point, current is Fibonacci(n).
  write( current );
}
