$("body").addClass("disable-scroll");

var fadeTime = 7500;
$(function(){  // $(document).ready shorthand

  $('.mainst').hide().fadeIn(fadeTime);

});


setTimeout(function() {
  $('#prelod').fadeOut(fadeTime, function() {
    $(this).remove();
    $("body").removeClass("disable-scroll")
  });



}, 2000);
