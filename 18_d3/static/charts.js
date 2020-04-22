var start = document.getElementById("rend");
var move = document.getElementById("tran");
var chart = document.getElementsByTagName("svg");

var curr = 0;


var width = 1000;


var render = function(e) {
	var data = states[curr];
	var arr = [];
	var dict = scores[data];
	for (var k in dict) {
		arr.push(dict[k]);
	}
	var x = d3.scaleLinear().domain([0,d3.max(arr)]).range([0,width]); // Creates a conversion between the numbers given in the data and the width I want the graph to have
	var y = d3.scaleBand().domain(d3.range(arr.length)).range([0,20 * arr.length]); // Allows each element of the bar chart to have the same height (20)
	var graph = d3.select("svg").attr("width", width).attr("height", y.range()[1]).attr("font-family", "sans-serif").attr("font-size", "10").attr("text-anchor", "end"); // Changes some stylistic aspects of the svg area (height, width, font, and font size)
	var end = graph.selectAll("g").data(arr).join("g").attr("transform", (d,i) =>  `translate(0,${y(i)})`);
	end.append("rect").attr("fill","blue").attr("width",x).attr("height",y.bandwidth()-1); // Sets up each bar of the bar chart (gives it its color, height, and width)
	end.append("text").attr("fill","white").attr("x", d => x(d) - 3).attr("y", y.bandwidth() / 2).attr("dy", "0.35em").text(d => d); // Places each piece of text in the right location
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
