// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

var logo = new Image();
logo.src = "logo_dvd.jpg";

var r = 20;
var grow = true;
var id = 0;

var draw = function(e) {
  //console.log(c);
  ctx.clearRect(0,0,c.width,c.height);
  ctx.beginPath();
  //draws a circle, centered at (c.width/2,c.height/2) and has radius r. Starts at angle 0, ends at 2pi, goes counterclockwise
  ctx.arc(c.width/2, c.height/2, r, 0, 2 * Math.PI, true);
  //Fills in the interior of the circle
  ctx.fill();
  if (grow) {
    r++;
    if (r == Math.min(c.height,c.width)/2) {
      grow = false;
    }
  }
  else {
    r--;
    if (r == 0) {
      grow = true;
    }
  }
  //calls draw (again) when the canvas is "repainted"
  id = window.requestAnimationFrame(draw);
  //console.log(id);
}

var xpos = Math.floor(c.width * Math.random());
var ypos = Math.floor(c.height * Math.random());
var right = true;
var down = true;

var bounce = new function(e) {
  ctx.drawImage(xpos,ypos);
  if (right) {
    xpos++;
    if (xpos == c.width) {
      right = false;
    }
  }
  else {
    xpos--;
    if (xpos == 0) {
      right = true;
    }
  }
  if (down) {
    ypos++;
    if (ypos == c.height) {
      down = false;
    }
  }
  else {
    ypos--;
    if (ypos == 0) {
      down = true;
    }
  }
}

var go = document.getElementById("anim");
var begin = function(e) {
  window.requestAnimationFrame(draw);
  go.removeEventListener("click",begin);
}

go.addEventListener("click",begin);

var stop = document.getElementById("stop");
var end = function(e) {
  window.cancelAnimationFrame(id);
  go.addEventListener("click",begin);
}

stop.addEventListener("click",end);
