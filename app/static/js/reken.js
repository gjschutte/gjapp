function random (maxValue) {
	var num = Math.floor((Math.random() * maxValue) + 1);
	return num;
}

var calculation = {
	number1: 0,
	number2: 0,
	sumType: 1,
	outcome: function() {
		var hlp = 0;
		switch (this.sumType) {
			case 1:
				hlp = this.number1 + this.number2;
				break;
			case 2:
				hlp = this.number1 - this.number2;
				break;
			case 3:
				hlp = this.number1 * this.number2;
				break;
			case 4:
				hlp = Math.round (this.number1 / this.number2);
				break;
		}
		return hlp
	}
}

var score = {
	total: 0,
	correct: 0,
	percent: function() {
		var h_percent = 0;
		if (this.total != 0) {
			h_percent = Math.round ((this.correct / this.total) * 100);
		}
		return h_percent;
	}
}

function showScore () {
	document.getElementById('ex1').innerHTML = "Total exercises: " +
	score.total;
	document.getElementById('ex2').innerHTML = "Correct: " +
	score.percent() + " %";
}

function init () {
	score.total = 0;
	score.correct = 0;
	showScore();
}

function switchNumber () {
	if (calculation.number1 < calculation.number2) {
		hulp = calculation.number1;
		calculation.number1 = calculation.number2;
		calculation.number2 = hulp;
	}
}

function showSum (sumType) {
	var calcText = '';
	if (document.quizform.level[0].checked)
		maxValue = 10;
	else {
		if (document.quizform.level[1].checked)
			maxValue = 30;
		else {
			maxValue = 60;
		}
	}

	calculation.sumType = sumType;
	calculation.number1 = random (maxValue);
	calculation.number2 = random (maxValue);
	switch (sumType) {
		case 1:
			calcText = 	calculation.number1 + ' + ' + 
			calculation.number2 + ' = ';
			break;
		case 2: 
			switchNumber();
			calcText = 	calculation.number1 + ' - ' + 
			calculation.number2 + ' = ';
			break;
		case 3:
			calcText = 	calculation.number1 + ' x ' + 
			calculation.number2 + ' = ';
			break;
		case 4:
			switchNumber();
			calcText = 	calculation.number1 + ' : ' + 
			calculation.number2 + ' = ';
			break;
	}
	document.getElementById('task').innerHTML = calcText;
	document.getElementById('outcome').value = "";
}

function checkResult () {
	var outc = document.getElementById('outcome');
	score.total += 1;
	
	if (outc.value == calculation.outcome()) {
		document.getElementById('reslt').innerHTML = "Correct";
		document.getElementById('answer').innerHTML = ""; 
		score.correct += 1;
	}
	else {
		document.getElementById('reslt').innerHTML = "Fail!";
		document.getElementById('answer').innerHTML = 
		calculation.number1 + ' + ' + calculation.number2 + ' = ' +
		calculation.outcome();
	}
	showScore ();
	showSum (calculation.sumType);
}
