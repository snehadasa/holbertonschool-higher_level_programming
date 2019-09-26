$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (const ti of data.results) {
    $('UL#list_movies').append($('<li></li>').text(ti.title));
  }
});
