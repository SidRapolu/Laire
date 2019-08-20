$("body").addClass("disable-scroll");
$('.mainst').hide()
var fadeTime = 4000;



$('#prelod').fadeOut(fadeTime, function() {
  $(this).remove();

});




//$(function(){  // $(document).ready shorthand



//$('.mainst').hide().fadeIn(fadeTime);

//});

setTimeout(function() {
  $('.mainst').hide().fadeIn('fast');
    $("body").removeClass("disable-scroll")
}, 3000);
