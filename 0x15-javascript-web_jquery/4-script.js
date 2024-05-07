#!/usr/bin/node
//A script that toggles the class of the <header> element on click on the tag.

$('#toggle_header').click(() => {
	$('HEADER').toggleClass('red green');
});
