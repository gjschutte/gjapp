// Initialize audio variales:
var greenAudio  = new Audio('https://s3.amazonaws.com/freecodecamp/simonSound1.mp3');
var redAudio    = new Audio('https://s3.amazonaws.com/freecodecamp/simonSound2.mp3');
var yellowAudio = new Audio('https://s3.amazonaws.com/freecodecamp/simonSound3.mp3');
var blueAudio   = new Audio('https://s3.amazonaws.com/freecodecamp/simonSound4.mp3');
/* other variables */
var player = [];
var computer = [];
var strickt = false;
var turn = 0;
var choice = 0;
var round = 1;
var winLimit = 3;
var switchOff = false;


/* Functions with actions when a color is clicked */
function green () {
	clearColors();
	$('#green').addClass("clickedGreen");
	greenAudio.play();
}

function red () {
	clearColors();
	$('#red').addClass("clickedRed");
	redAudio.play();
}

function yellow () {
	clearColors();
	$('#yellow').addClass("clickedYellow");
	yellowAudio.play();
}

function blue () {
	clearColors();
	$('#blue').addClass("clickedBlue");
	blueAudio.play();
}

function compTurn () {
	/* Computer turn. Add a sound to the computerqueue */
	var selectColor = 0;

	selectColor = Math.floor(Math.random() * 4);
	console.log("Color: " + selectColor);
	computer.push(selectColor);
	playComputer();
}

function playComputer() {
	/* Play all the computer sounds */
	console.log("In Play");
	var count = 0;
	var playSounds = setInterval (function() {
		console.log ("To play " + computer[count]);
		clearColors();
		switch (computer[count]) {
			case 0:
				green();
				break;
			case 1:
				red();
				break;
			case 2:
				yellow();
				break;
			case 3:
				blue();
				break;
		}
		console.log ("Count: " + count);
		console.log("Computer: " + computer.length );
		if (count == computer.length) {
			/* end of the array reached, stop playing the sounds */
			clearInterval(playSounds);
			setTimeout (function() {
				clearColors();
			}, 1000);
		}
		else {
			/* more sounds to play */
			count += 1;
		}
	}, 1000);
}

function clearColors () {
	/* Clear the special colors of the buttons */
	$('#green').removeClass("clickedGreen");
	$('#red').removeClass("clickedRed");
	$('#yellow').removeClass("clickedYellow");
	$('#blue').removeClass("clickedBlue");
	$('#green').removeClass("greenLoser");
	$('#red').removeClass("redLoser");
	$('#yellow').removeClass("yellowLoser");
	$('#blue').removeClass("blueLoser");
	$('#green').removeClass("greenWinner");
	$('#red').removeClass("redWinner");
	$('#yellow').removeClass("yellowwinner");
	$('#blue').removeClass("blueWinner");
}

function resetRound() {
	/* set initial values at the beginning of a round */
	clearColors();
	turn = 0;
}

function resetGame() {
	/* set initial values to start a new game */
	resetRound();
	round = 1;
	computer = [];
	writeRound(round);
	compTurn();
}

function playUser() {
	/* Evaluate the situation, when the user pushes a color */

	player.push(choice);

	if (choice == computer[turn]) {
		console.log("Good choice");

		/* Check if next round has to start */
		if ((turn + 1) == computer.length) {
			/* Check if player is a winner */
			if (round == winLimit) {
				$('#green').addClass("greenWinner");
				$('#red').addClass("redWinner");
				$('#yellow').addClass("yellowWinner");
				$('#blue').addClass("blueWinner");
				setTimeout (function () {
					resetGame();
				},2000);
			}
			else {
				/* Start next round */
				setTimeout (function() {
					console.log("Next round");
					resetRound();
					round += 1;
					writeRound (round);
					compTurn();
				}, 1000);
			}
		}
		else {
			turn += 1;
		}
	}
	else {
		console.log("wrong choice");
		switch (choice) {
			case 0:
				$('#green').addClass("greenLoser");
				break;
			case 1: 
				$('#red').addClass("redLoser");
				break;
			case 2:
				$('#yellow').addClass("yellowLoser");
				break;
			case 3:
				$('#blue').addClass("blueLoser");
				break;
		}
		if (strickt == false) {
			/* Play the computersounds again after 1 second */
			setTimeout (function() {
				clearColors ();
				playComputer ();
			}, 1000);
		}
		else {
			/* Game over */
			round = "XX";
			writeRound (round);
			setTimeout (function() {
				resetGame();
			}, 1000);
		}
	}
}

function writeRound (roundNumber) {
	$("#gameCounter").html(roundNumber);
}

$(document).ready(function() {

	/* Listeners for clicking the colors */
	$('#green').click(function() {
		green();
		choice = 0;
		playUser ();
	});

	$('#red').click(function() {
		red();
		choice = 1;
		playUser ();
	});

	$('#yellow').click(function() {
		yellow();
		choice = 2;
		playUser ();
	});

	$('#blue').click(function() {
		blue();
		choice = 3;
		playUser ();
	});

	/* Listener for the Play button */
	$('#startGame').click(function() {
		resetGame ();
	});

	/* Listeners for the switches */
	$('#switchRight').change(function(){
		console.log ("Strickt changed");
		if (strickt == false) {
			strickt = true; 
		}
		else {
			strickt = false;
		}
	});

	$('#switchLeft').change(function(){
		/* On - Off */
		console.log ("Switch: " + switchOff);
		if (switchOff == false) {
			/* Turning game off */
			switchOff = true;
			round = "--";
			writeRound(round);
			$('#green').addClass("greenLoser");
			$('#red').addClass("redLoser");
			$('#yellow').addClass("yellowLoser");
			$('#blue').addClass("blueLoser");
			document.getElementById('green').style.pointerEvents = 'none';
			document.getElementById('red').style.pointerEvents = 'none';
			document.getElementById('yellow').style.pointerEvents = 'none';
			document.getElementById('blue').style.pointerEvents = 'none';
		}
		else {
			/* Turn game on */
			switchOff = false;
			document.getElementById('green').style.pointerEvents = 'auto';
			document.getElementById('red').style.pointerEvents = 'auto';
			document.getElementById('yellow').style.pointerEvents = 'auto';
			document.getElementById('blue').style.pointerEvents = 'auto';
			resetGame();
		}
	});

})