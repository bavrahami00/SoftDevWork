var fibonacci=function(n) {
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }
  return fibonacci(n-1)+fibonacci(n-2);
}
var gcd=function(a,b) {
  var x;
  var ans = 0;
  for (x = 0; x <= a; x++) {
    if (a%x == 0 && b%x == 0) {
      ans = x;
    }
  }
  return ans;
}
var randomStudent=function() {
  var arr = [3];
  arr[0] = "Alice";
  arr[1] = "Bob";
  arr[2] = "Carol";
  return arr[Math.floor(Math.random()*3)];
}
