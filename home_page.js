function zoomIn() {
	document.getElementById("zoom").style.transform = "scale(1.2)";
	document.getElementById("zoom").style.transition = "transform 0.5s";
}

function zoomOut() {
	document.getElementById("zoom").style.transform = "scale(1)";
	document.getElementById("zoom").style.transition = "transform 0.5s";
}