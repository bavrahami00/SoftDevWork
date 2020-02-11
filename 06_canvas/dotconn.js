// retrieve node in DOM via ID
var c = document.getElementById("playground");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// current drawing mode
var currentMode = document.getElementById("mode");

var lastX;
var lastY;

var draw = function(e) {
  ctx.fillStyle = "#8B008B";
  ctx.beginPath();
  ctx.moveTo(e.offsetX,e.offsetY);
  ctx.lineTo(lastX,lastY);
  ctx.stroke();
  ctx.closePath();
  ctx.beginPath(); // allows the drawing to start
  ctx.arc(e.offsetX, e.offsetY, 20, 0, 2 * Math.PI, true);
  ctx.closePath();
  ctx.fill();
  lastX = e.offsetX;
  lastY = e.offsetY;
}

c.addEventListener("click",draw);



var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height);
    lastX = undefined;
    lastY = undefined;
}

// event listener for clearing canvas
var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clear);
