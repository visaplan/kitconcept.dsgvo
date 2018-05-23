'use strict';
(function() {
  var $ = jQuery;
  var cookieName = 'hide-dsgvo-banner';
  var expires = 31 * 12 * 10;
  var setCookie = function() {
    $.get('@@close-dsgvo-info');
  };
  
  $(function () {
    $('.dsgvo-close-banner').click(function (event) {
      setCookie();
      $('.dsgvo-banner').fadeOut();
      event.preventDefault();
    });
  });
})();
