/* The following line defines global variables defined elsewhere. */
/*globals require*/


if(require === undefined){
  require = function(reqs, torun){
    'use strict';
    return torun(window.jQuery);
  };
}

require([
  'jquery',
  'jquery.cookie'
], function($, cookie) {
  'use strict';

  var cookieName = 'hide-dsgvo-banner';
  var expires = 31 * 12 * 10;
  var hide = function() {
    $.cookie(cookieName, 'true', {expires: expires});
  };
  var isHidden = function() {
    return Boolean($.cookie(cookieName) !== 'true');
  };

  $(function () {
    $('.dsgvo-close-banner').click(function (event) {
      hide();
      $('.dsgvo-banner').fadeOut();
      event.preventDefault();
    });
  });
});
