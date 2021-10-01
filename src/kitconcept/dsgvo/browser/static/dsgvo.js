"use strict";
var dsgvo = (function () {

// Lightweight getCookie https://gomakethings.com/working-with-cookies-in-vanilla-js/
var getCookie = function (name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2)
    return parts
      .pop()
      .split(";")
      .shift();
};

  var $ = jQuery;
  // We rely on Plone for setting the cookie, so no heavy JS deps on JQuery cookie
  var setCookie = function () {
    $.get("@@close-dsgvo-info");
  };
  
  var init = function () {
    $(".dsgvo-close-banner").click(function (event) {
      setCookie();
      $(".dsgvo-banner").fadeOut();
      event.preventDefault();
    });
  }

  return {
    setCookie: setCookie,
    getCookie: getCookie,
    init:      init
    }
})();
	
$(document).ready(function () {
  dsgvo.init();
  if (!dsgvo.getCookie("hide-dsgvo-banner")) {
    $(".dsgvo-banner").show();
  }
});
