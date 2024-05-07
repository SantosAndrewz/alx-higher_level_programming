#!/usr/bin/node
// a script that fetches and lists titles for all movies from a given url.

$(document).ready(function() {
	  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
		  data.results.forEach(function(movie) {
			            $('<li>').text(movie.title).appendTo('DIV#list_movies');
			          });
		    });
});
