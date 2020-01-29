var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = this.innerHTML;
  //console.log(h.innerHTML);
};

var removeItem = function(e) {
  this.remove();
}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  //console.log(lis[i]);
  //console.log("Length: " + lis.length);
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!";});
  lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!";});
  item.addEventListener('click', removeItem);
  list.append(item);
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
  console.log(n);
  if (n < 2) {
    return 1;
  }
  else {
    return fib(n-1) + fib(n-2);
  }
}

var addFib = function(e) {
  console.log(e);
  var list = document.getElementById("fiblist");
  //console.log(list);
  var item = document.createElement("li");
  if (list.childNodes.length < 3) {
    item.innerHTML = fib(list.childNodes.length-1);
  }
  else {
    item.innerHTML = addFib2();
  }
  list.append(item);
}

var addFib2 = function(e) {
  var list = document.getElementById("fiblist");
  var len = list.childNodes.length;
  //console.log(list.childNodes[len-2]);
  return Number(list.childNodes[len-2].innerHTML)+Number(list.childNodes[len-1].innerHTML);
}

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);
