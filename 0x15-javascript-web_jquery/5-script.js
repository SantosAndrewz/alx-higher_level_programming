#!/usr/bin/node
// a script that adds a <li> element to a list on click on the tag.

$('DIV#add_item').click(() => {
	$('UL.my_list').append('<li>Item</li>');
});
