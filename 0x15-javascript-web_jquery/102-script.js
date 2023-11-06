$(document).ready(function() {
  $('#btn_translate').on('click', function() {
    let languageCode = $('#language_code').val();
    let apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=
		  ${languageCode}`;
    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  });
});
