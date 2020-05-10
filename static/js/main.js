$(document).ready(function () {
  $("#search-btn").click(function () {
    $(".center-items").addClass("center-items-hidden");
    $(".center-list").addClass("center-items-centered");
    $(".search-form").addClass("show-form");
    $(".close-search").addClass("active");
    $(".right-list").addClass("hide-icons");
  });

  $(".close-search").click(function () {
    $(".center-items").removeClass("center-items-hidden");
    $(".center-list").removeClass("center-items-centered");
    $(".search-form").removeClass("show-form");
    $(".close-search").removeClass("active");
    $(".right-list").removeClass("hide-icons");
  });
});
