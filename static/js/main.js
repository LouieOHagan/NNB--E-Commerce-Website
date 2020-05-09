$(document).ready(function () {
  $("#search-btn").click(function () {
    $(".center-items").addClass("center-items-hidden");
    $(".search-form").addClass("show-form");
    $(".close-search").addClass("active");
    $(".right-list").hide();
  });

  $(".close-search").click(function () {
    $(".center-items").removeClass("center-items-hidden");
    $(".search-form").removeClass("show-form");
    $(".close-search").removeClass("active");
    $(".right-list").show();
  });
});
