#!/usr/bin/node
// a ascript that fetches from a given url and sisplays the value of hello.

$(document).ready(function() {
	  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
		      $('DIV#hello').text(data.hello);
		    });
});
