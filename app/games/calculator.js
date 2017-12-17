$(document).ready(function() {

	var input = '';
	var currInput = "0";
	var totalSum = "";
	var firstValue = "";
	var secValue = "";
	var calculation = "";
	var operator = "";
	var equalSign = false;

	function calcResult (first, second, operate) {
		var result = 0;
		switch (operate) {
			case "+":
				result = parseFloat(first) + parseFloat(second);
				break;
			case "-":
				result = parseFloat(first) - parseFloat(second);
				break;
			case "*":
				result = parseFloat(first) * parseFloat(second);
				break;
			case "/":
				if (second == "0") {
					return "Error"
				}
				else {
					result = parseFloat(first) / parseFloat(second);
					break;
				}
		}

		/* Round the result */
		/* var endResult = Math.round(result/100)*100; */
		result = +result.toFixed(2);
		console.log("Endresult: " + result);
		return result.toString();
	}

	function printCalculation () {
		if (operator == "") {
			$("#totalInput").html(currInput);
		}
		else {
			if (secValue == "") {
				/* No calculation, so no equal sign */
			$("#totalInput").html(totalSum + operator + currInput);
			}
			else {
				$("#totalInput").html(secValue + operator + currInput + "=" + totalSum);
			}
		}
	}

	function init () {
		totalSum = "";
		secValue = "";
		operator = "";
		currInput = "0";
		equalSign = false;
	}

	$('button').click(function() {
		input = $(this).attr("value");

		switch (input) {
			case "0":
			case "1":
			case "2":
			case "3":
			case "4":
			case "5":
			case "6":
			case "7":
			case "8":
			case "9":
				if (equalSign == true) {
					/* just calculated, start a new calculation */
					init ();
					currInput = input;
				}
				else {
					/* Replace when 0, add the number when not 0 */
					if (currInput == "0") {
						currInput = input;
					}
					else {
						currInput += input;
					}
				}
				$("#input").html(currInput);
				printCalculation ();
				break;

			case "dot":
				if (equalSign == true) {
					/* just calculated, start a new calculation */
					init ();
					currInput = "0."
				}
				else {
					/* Check if already a dot exists */
					if (currInput.indexOf(".") == -1) {
						currInput += ".";
					}
				}
				$("#input").html(currInput);
				printCalculation ();
				break;

			case "+" :
			case "-" :
			case "*" :
			case "/" :
				/* If first value, then no calculation */
				console.log("CurrInput " + currInput + " secValue " + secValue);
				if (equalSign == true) {
					/* Just performed calculation, start new one */
					equalSign = false;
					currInput = "0";
					operator = input;
					totalSum = "";
					$("#input").html(operator);
					printCalculation();
				}
				else {
					if (secValue == "") {
						secValue = currInput;
						currInput = "0";
						operator = input;
						$("#input").html(operator);
						printCalculation();
					}
					else {
						/* plus press, while already 2 numbers available as input */
						totalSum = calcResult(secValue, currInput, operator);
						$("#input").html(totalSum);
						printCalculation();
						currInput = "0";
						secValue = totalSum;
						operator = input;
					}
				}
				console.log("CurrInput " + currInput + " secValue " + secValue);
				break;

			case "equal" :
				console.log("CurrInput " + currInput + " secValue " + secValue);
				if (secValue != "" & operator != "") {
					equalSign = true;
					totalSum = calcResult(secValue, currInput, operator);
					$("#input").html(totalSum);
					printCalculation();
					secValue = totalSum;
				}
				break;

			case "AC" :
			case "CE" :
				init();
				$("#input").html(currInput);
				printCalculation();
				break;
		};

		console.log(input);
    	/*
    	$('#input').html(currInput);
    	$('#totalInput').html(input);
    	*/
	})


})