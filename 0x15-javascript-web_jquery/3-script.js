#!/usr/bin/node
// a script that adds class red to the <header> element DIV on click.


$('DIV#red_header').click(() => {
	$('HEADER').addClass('red');
});
