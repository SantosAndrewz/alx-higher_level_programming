#!/usr/bin/node
// A script that updates text-color of <header> element to red on click of DIV

$('DIV#red.header').click(() => {
	$('HEADER').css('color', '#FF0000')
})
