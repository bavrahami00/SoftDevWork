var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.innerHTML;
};

var removeItem = function(e) {
  e.remove();
}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  console.log(lis[i]);
  console.log("Length: " + lis.length);
  lis[i].addEventListener('mouseover', changeHeading(lis[i]));
  lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World";});
  lis[i].addEventListener('click', removeItem(lis[i]));
}
