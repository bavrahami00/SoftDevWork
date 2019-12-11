var fibonacci = function(n) {
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }
  else {
    return fibonacci(n-1)+fibonacci(n-2);
  }
}

var gcd = function(a,b) {
  var ans = 0;
  for (x = 1; x <= a; x++) {
    if (a%x == 0) {
      if (b/x == 0) {
        ans = x;
      }
    }
  }
  return ans;
}
