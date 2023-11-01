$.get('https://swapi-api.alx-tools.com/api/film/?format=json', function (data) {
  data.results.forEach(function (element) {
    $('UL#list_movies').append($('<li></li>').text(element.title));
  });
});
