// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

var r = 20;
var grow = true;

var draw = function(e) {
  //console.log(c);
  ctx.clearRect(0,0,c.height,c.width);
  ctx.beginPath();
  ctx.arc(c.height/2, c.width/2, r, 0, 2 * Math.PI, true);
  ctx.fill();
  if (grow) {
    r += 1;
    if (r == c.height/2) {
      grow = false;
    }
  }
  else {
    r -= 1;
    if (r == 0) {
      grow = true;
    }
  }
  window.requestAnimationFrame(draw);
}

window.requestAnimationFrame(draw);
