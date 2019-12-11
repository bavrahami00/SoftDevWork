var fact = function(n) {
	if (n == 1){
    return 1;
  }
  else {
    return n * (fact(n - 1));
  }
};

var fibonacci = function(n) {
  var first = 0;
  var second = 1;
  while (n > 0){
    var temp = first;
    first = second;
    second = temp + second;
    n -= 1;
  }
  return first;
};

var gcd = function(a, b) {
  var dend, dsor, r;
  if (a > b){
    dend = a;
    dsor = b;
    r = a % b;
  }
  else{
    dend = b;
    dsor = a;
    r = b % a;
  }
  while (r > 0){
    dend = dsor;
    dsor = r;
    r = dend % dsor;
  }
  return dsor;
};

var randomStudent = function() {
  var list = ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'];
  return list[Math.floor(Math.random() * 1000 % list.length)];
};

var run_fib = function() {
  //console.log(fibonacci(12));
  var par = document.createElement("p"); //forms a <p> ... </p> tag in HTML
  var text = document.createTextNode(fibonacci(12)+""); //forms text in HTML
  par.appendChild(text); //puts text inside par
  //console.log(par);
  var body = document.getElementByTagName(body);
  body.appendChild(par); //puts the paragraph in the body
}

var fib = document.getElementById("bonacci"); // the fib button in the HTML page
//console.log(fib);
fib.addEventListener('click',run_fib); //runs the function run_fib once fib is clicked
