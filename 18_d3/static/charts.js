var start = document.getElementById("rend");
var move = document.getElementById("tran");
var chart = document.getElementsByClassName("chart")

var curr = 0;

var graph = d3.select(".chart");
var render = function(e) {
	var data = states[curr];
	var arr = [];
	var dict = scores[data];
	for (var k in dict) {
		arr.push(dict[k]);
	}
	var x = d3.scaleLinear().domain([0,d3.max(arr)]).range([0,1000]);
	var end = graph.selectAll("div").data(arr).join("div");
	end.text(d => d);
	end.style("width", d => `${x(d)}px`);
	end.style("background","blue");
	end.style("text-align","right");
	curr = curr + 1;
}

var rend = function(e) {
	chart[0].innerHTML = "";
	curr = 0;
	render(e);
}

var tran = function(e) {
	if (curr != 0) {
		chart[0].innerHTML = "";
		render(e);
	}
}

start.addEventListener("click",rend);
move.addEventListener("click",tran);