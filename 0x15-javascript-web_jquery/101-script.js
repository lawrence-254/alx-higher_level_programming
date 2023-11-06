$(document).ready(function() {
  $('#add_item').on('click', function() {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
  $('#remove_item').on('click', function() {
    $('ul.my_list li:last').remove();
  });
  $('#clear_list').on('click', function() {
    $('ul.my_list').empty();
  });
});
