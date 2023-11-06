$(document).ready(function() {
  $('#btn_translate').on('click', function() {
    translateHello();
  });

  $('#language_code').on('keydown', function(event) {
    if (event.key === 'Enter') {
      translateHello();
    }
  });
  function translateHello() {
    let languageCode = $('#language_code').val();
    let apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  }
});
