/*
 * Javascript Client Detection
 * Gert-Jan Schutte, 8-11-2015
 */
 
function screenSize (window) {
	{
		var unknown = '-';
		
		// screen
		var screenSize = '';
		if (screen.width) {
			width = (screen.width) ? screen.width : '';
			height = (screen.height) ? screen.height : '';
			screenSize += '' + width + " x " + height;
		
		return screenSize;
	}
