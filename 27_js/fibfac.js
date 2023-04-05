// Team Casa Blanca :: Ameer Alnasser, Sam Cowan
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------

// as a duo...
// pair programming style,
// implement a fact and fib fxn
function fact(n){
  if(n < 2){
    return 1;
  }
  return (n*fact(n-1));
}
function fib(n){
  if(n === 0){
    return 0;
  }
  else if (n < 3) {
    return 1;
  }
  return fib(n-1)+fib(n-2);
}

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
