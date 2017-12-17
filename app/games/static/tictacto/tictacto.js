$(document).ready(function() {

	var playerSign = "X";
	var computer = "Y";
	var symbol = "X";
	var fieldClicked = "";
	var gameWon = "";
	var difficulty = "Easy";
	
	var game = {
		f0: "",
		f1: "",
		f2: "",
		f3: "",
		f4: "",
		f5: "",
		f6: "",
		f7: "",
		f8: ""
	};
	
	var winCombos = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6]];
		
	/* Listener for all the cells of the board */
	$(".cell").click(function() {
		buttonId = "#"+ this.id;
		fieldClicked = buttonId.replace("#b", "f");
		if (game[fieldClicked] == "") {
			$(buttonId).html(symbol);
			game[fieldClicked] = symbol;
			
			/* Check for winning combo */
			gameWon =  checkWin ();
			if (gameWon != "") {
				/* Game ended with a winner */
				showWinner (gameWon);
			}
			else {
				/* Change the symbol */
				if (symbol == "X") {
					symbol = "O";
				} else {
					symbol = "X";
				}
				/* Check for comuter as a player */
				if (computer == "Y") {
					computerTurn ();
				}
			}
		}
	})

	/* Check for the number of players */
	$(document).on("change", "input[name=gametype]", function () {
		var type = $('[name="gametype"]:checked').val ();
		console.log ("Type: " + type);
		if (type == "computer") {
			computer = "Y";
		}
		else {
			computer = "N"
		};
	});

	/* Check for the difficulty */
	$(document).on("change", "input[name=level]", function () {
		var level = $('[name="level"]:checked').val ();
		console.log ("Level: " + level);
		difficulty = level;
	});

	/* Check to play with "X" or "O" */
	$(document).on("change", "input[name=player]", function () {
		var player = $('[name="player"]:checked').val ();
		console.log ("Player: " + player);
		playerSign = player;

		/* Check if the computer have to make a move */
		if (computer == "Y" && playerSign != symbol) {
			computerTurn ();
		}
	});

	/* Listener for the new game button */
	$("#reset").click(function () {
		reset();
	})

	function reset() {
		/* Reset all the values to inital values */
		console.log("In reset");
		var field = "";
		var buttonRes = "";
		var buttonResId = "";
		console.log(game);
		for (var key in game) {
			console.log(key, game[key]);
			game[key] = "";
			buttonRes = key.replace("f", "#b");
			$(buttonRes).html("&nbsp");
			buttonResId = document.getElementById(key.replace("f", "b"));
			buttonResId.style.color = "black";
		};
		fieldClicked = "";
		gameWon = "";
		symbol = "X";

		/* Check if the computer have to make a move */
		if (computer == "Y" && playerSign == "O") {
			computerTurn ();
		}
	}

	function pickKey (avKeys) {
		var choice = "";
		var writeField = ""
		choice = avKeys[avKeys.length * Math.random() << 0];
		writeField = choice.replace ("f", "#b");
		$(writeField).html(symbol);
		game[choice] = symbol;
	}

	function computerTurn () {
		/* Function to determine the move of the computer */
		var keys = [];
		var move = "";
		var field = "";
		var keysChoose = [];
		var result = "";

		for (var key in game) {
			if (game[key] == "") {
				keys.push(key);
			}
		}
		if (difficulty == "Easy") {
			/* Difficulty Easy, just pick a random empty cell */
			pickKey (keys);
		}
		else {
			/* Difficulty Hard, make the best possible move */
			/* First turn, choose one of the corners */
			if (keys.length == 9) {
				keysChoose = ["f0", "f2", "f6", "f8"];
				pickKey (keysChoose);
			}
			else {
				if (keys.length == 8) {
					/* Second turn. Look to block */
					if (game["f4"] != "") {
						/* mid position taken. Choose a corner */
						keysChoose = ["f0", "f2", "f6", "f8"];
						pickKey (keysChoose);
					}
					else {
						if (game["f0"] != "") {
							keysChoose = ["f8"];
						}
						else {
							if (game["f2"] != "") {
								keysChoose = ["f6"];
							}
							else {
								if (game["f6"] != "") {
									keysChoose = ["f2"];
								}
								else {
									if (game["f8"] != "") {
										keysChoose = ["f0"];
									}
									else {
										/* No corner and not the middle selected. Choose middle */
										keysChoose = "[f4]";
									}
								}
							}
						}
						pickKey (keysChoose);
					}
				}
				else {
					/* Not the first or second turn. Look for a blocker or a winner. */
					/* First look for a winner */
					for (var i = 0; i < keys.length; i++) {
						game[keys[i]] = symbol;
						result = checkWin();
						if (result != "") {
							/* Winning combo. */
							keysChoose = keys[i];
							break;
						}
						else {
							game[keys[i]] = "";
						}
					}
					if (keysChoose != "") {
						pickKey (keysChoose);
					}
					else {
						/* Check for a blocker */
						for (var i = 0; i < keys.length; i++) {
							/* Temporary change the symbol */
							if (symbol == "X") {
								symbol = "O";
							}
							else {
								symbol = "X";
							}
							game[keys[i]] = symbol;
							result = checkWin();
							if (result != "") {
								/* Winning combo for opponent. Choose this to block */
								keysChoose = [keys[i]];
								break;
							}
							else {
								game[keys[i]] = "";
							}
						}
						/* Change back the symbol */
						if (symbol == "X") {
							symbol = "O";
						}
						else {
							symbol = "X";
						}
						game[keys[i]] = "";
						if (keysChoose != "") {
							pickKey (keysChoose);
						}
						else {
							/* no blocker, and no winner. Random pick another */
							pickKey (keys);
						}
					}
				}
			}
		}
		/* Check for winning combo */
		gameWon =  checkWin ();
		if (gameWon != "") {
			/* Game ended with a winner */
			console.log("Winner " + gameWon);
			showWinner (gameWon);
		}
		else {
			/* Change the symbol */
			if (symbol == "X") {
				symbol = "O";
			} else {
				symbol = "X";
			}
		}
	}

	function checkWin () {
		var combo = "";
		var checkField = "";
		var winner = false;
		
		for (var i=0; i < winCombos.length; i++) {
			combo = winCombos[i];
			winner = true;
			for (var k=0; k <combo.length; k++) {
				checkField = "f" + combo[k];
				console.log("checkField " + game[checkField] + " symbol " + symbol);
				if (game[checkField] != symbol) {
					/* Combo is not a winning combo */
					winner = false;
					break;
				}
			}
			if (winner == true) {
				break;
			}
		}
		if (winner == true) {
			return combo;
		}
		else {
			return "";
		}
	}

	function showWinner (winner) {
		/* Color the winning combo */
		var celWin = "";

		for (var i=0; i<winner.length; i++) {
			celWin = document.getElementById("b"+winner[i]);
			celWin.style.color = "blue";
		}
	}
})