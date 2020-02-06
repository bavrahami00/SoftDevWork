// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// current drawing mode
var currentMode = document.getElementById("mode");

// get offsets: offLeft is the left offset (how far away the canvas is
// from the left side of the screen) and offTop is the top offset
var offLeft = c.offsetLeft;
var offTop = c.offsetTop;

// draw function to draw box or dot depending on mode
var draw = function(e) {
    if (currentMode.innerHTML == "Draw a Box") {
        ctx.fillStyle = "#FF00FF";
        ctx.fillRect(e.clientX-offLeft, e.clientY-offTop, 33, 33);
    }
    else {
        ctx.fillStyle = "#8B008B";
        ctx.beginPath(); // allows the drawing to start
        ctx.arc(e.clientX-offLeft, e.clientY-offTop, 20, 0, 2 * Math.PI, true);
        ctx.fill();
    }
}

// add event listener to canvas
c.addEventListener("click", draw);

// toggle drawing mode function
var toggleMode = function(e) {
    if (currentMode.innerHTML == "Draw a Box") {
        currentMode.innerHTML = "Draw a Dot";
        console.log("Changed drawing mode to: Draw a Dot.")
    }
    else {
        currentMode.innerHTML = "Draw a Box";
        console.log("Changed drawing mode to: Draw a Box.")
    }
}

// event listener to toggle drawing mode
var toggleButton = document.getElementById("toggle");
toggleButton.addEventListener("click", toggleMode);

// function to clear the canvas today
var clear = function(e) {
    ctx.clearRect(0, 0, c.width, c.height);
    console.log("You destroyed the Mona Lisa!");
}

// event listener for clearing canvas
var clearButton = document.getElementById("clear");
clearButton.addEventListener("click", clear);


