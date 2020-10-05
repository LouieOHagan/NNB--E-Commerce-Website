// Mouse Enter/Leave Event Listeners for Ad One
document.querySelector('.ad-one').addEventListener("mouseover", imageHover.bind(this, "one"));
document.querySelector('.ad-one').addEventListener("mouseleave", imageLeave.bind(this, "one"));
// Mouse Enter/Leave Event Listeners for Ad Two
document.querySelector('.ad-two').addEventListener("mouseover", imageHover.bind(this, "two"));
document.querySelector('.ad-two').addEventListener("mouseleave", imageLeave.bind(this, "two"));

// Adds ad-image-hover class to respective card image when mouse is hovered over card.
function imageHover(adNumber) {
    let image = document.querySelector(`.ad-${adNumber}-image`);
    image.classList.add("ad-image-hover");
}

// Removes ad-image-hover class to respective card image when mouse leaves/is no longer hovering over card.
function imageLeave(adNumber) {
    let image = document.querySelector(`.ad-${adNumber}-image`);
    image.classList.remove("ad-image-hover");
}
