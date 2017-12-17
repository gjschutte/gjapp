var totalTime = 23;
var pauzeTime = 5;
var seconds = 60;
var minutes = totalTime;
var status = "Active";
var timer = "";
var active = false;
var audioFile = "http://www.freesfx.co.uk/rx2/mp3s/5/17725_1462204255.mp3";
var audio = new Audio(audioFile);

function pad(num) {
	/* Pad: format a number to two digits, preceding 0 when needed */
    var s = "0" + num;
    return s.substr(s.length-2);
}

function switchStatus(origin) {
	/* Switch statusses: Active, Pauze, Relax */
	if (origin == "Button") {
		/* Button pressed, just stop or activate the time */
		if (active == false) {
			timer = setInterval(displayCounter, 1000);
			active = true;
			if (status == "Active") {
				console.log("Bij button");
				$("#statusText").html("Active period");
			}
			else {
				$("#statusText").html("Time to relax!");
			}
		}
		else {
			clearInterval(timer);
			active = false;
		}
	}
	else {
		/* Time elapsed, switch Active and Relax */
		if (status == "Pauze") {
			/* From Pauze to Active */
			console.log("Switch status");
			status = "Active";
			minutes = totalTime;
			seconds = 60;
			console.log("bij andere");
			$("#statusText").html("Active period.");
			audio.play();
		}
		else {
			/* From Active to pauze */
			status = "Pauze";
			minutes = pauzeTime;
			seconds = 00;
			$("#statusText").html("Time to relax!");
			audio.play();
		}
	}
}

function displayCounter () {
	if (seconds == 60) {
		minutes -= 1;
	}
	seconds -= 1;
	if (seconds < 0) {
		seconds = 59;
		minutes -= 1;
		if (minutes < 0) {
			switchStatus ("Time");
		}
	}
	$("#counter").html(pad(minutes) + ":" + pad(seconds));
}

function resetTime () {
	status = "Active";
	console.log("Switch status 2");
	minutes = totalTime;
	seconds = 00;

}

function tPlusClick () {
	if (active == false) {
		totalTime += 1;
		$("#totalTime").html(pad(totalTime) + ":00");
		resetTime();
	}
}

function tMinClick() {
	if (active == false) {
		if (totalTime > 1) {
			totalTime -= 1;
			$("#totalTime").html(pad(totalTime) + ":00");
			resetTime();
		}
	}
}

function rPlusClick () {
	if (active == false) {
		pauzeTime += 1;
		$("#pauze").html(pauzeTime + ":00");
		resetTime();
	}
}

function rMinClick() {
	if (active == false) {
		if (pauzeTime > 1) {
			pauzeTime -= 1;
			$("#pauze").html(pauzeTime + ":00");
			resetTime();
		}
	}
}

$(document).ready(function() {

	$("#totalTime").html(totalTime + ":00");
	$("#counter").html(totalTime + ":00");
	$("#pauze").html(pauzeTime + ":00");

	$("#counter").click(function(){
		switchStatus("Button");
	});
})