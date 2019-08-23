//http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=xml&lang=en
//http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en

$(document).ready(function() {
/*
	var quote;
	var author;
*/
	function getNewQuote() {
		$.ajax({
			url: 'http://api.forismatic.com/api/1.0/',
			jsonp: 'jsonp',
			dataType: 'jsonp',
			data: {
				method: 'getQuote',
				lang: 'en',
				format: 'jsonp',
			},
			success: function(response) {
				console.log(response);
				quote = response.quoteText;
				author = response.quoteAuthor;
				$('#quote').text('"' + quote +'"');
				if (author) {
					$('#author').text('- ' + author);
				} else {
					$('#author').text('- unknown');
				}
				}
		});
	}
	getNewQuote();

$('.get-quote').on('click', function(event) {

	getNewQuote();

});

});




/*
=====================================
ATTEMPT 2
=====================================
document.getElementById("quoteAJAX").addEventListener("click", function( event )

}, false);

$('#test')}.click(function(event))
 {}
 */



/* 
=====================================
ATTEMPT 1
=====================================
$('#quoteGETJSON').click(function() {
  $.getJSON("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?")
    .done(update)
    .fail(handleErr);
});

$('#quoteAJAX').click(function() {
  $.ajax({
      url: "https://api.forismatic.com/api/1.0/",
      jsonp: "jsonp",
      dataType: "jsonp",
      data: {
        method: "getQuote",
        lang: "en",
        format: "jsonp"
      }
    })
    .done(update)
    .fail(handleErr);
});

function update(response) {
  $('#log').prepend('<pre>' + $('#response').html() + '</pre>');
  $('#response').html(JSON.stringify(response));
}

function handleErr(jqxhr, textStatus, err) {
  console.log("Request Failed: " + textStatus + ", " + err);
}
*/