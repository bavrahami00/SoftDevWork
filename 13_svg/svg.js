var pic = document.getElementById("vimage");
var btn = document.getElementById("clear");


var addCircle = function(e) {
	if (e.originalTarget.id == "vimage") {
		var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
		c.setAttribute( "cx", e.offsetX);
		c.setAttribute( "cy", e.offsetY);
		c.setAttribute( "r", "25");
		c.setAttribute( "fill", "red");
		//c.setAttribute( "stroke", "black" );
		pic.appendChild(c);
		c.addEventListener("click", changeColor);
		//c.addEventListener("click", e => {c.remove();});
	}
}

var changeColor = function(e) {
	e.originalTarget.remove();
	console.log(e.originalTarget);
	var d = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	d.setAttribute( "cx", e.originalTarget.cx.animVal.value);
	d.setAttribute( "cy", e.originalTarget.cy.animVal.value);
	d.setAttribute( "r", "25");
	d.setAttribute( "fill", "teal");
	pic.appendChild(d);
	d.addEventListener("click", e => {d.remove()})
}

//pic.appendChild( c );
pic.addEventListener("click",addCircle)
btn.addEventListener("click", e => {pic.innerHTML = "";})