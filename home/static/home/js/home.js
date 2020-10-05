// Mouse Enter/Leave Event Listeners for Ad One
document.querySelector('.ad-one').addEventListener("mouseover", imageHover.bind(this, "adOne"));
document.querySelector('.ad-one').addEventListener("mouseleave", imageLeave.bind(this, "adOne"));
// Mouse Enter/Leave Event Listeners for Ad Two
document.querySelector('.ad-two').addEventListener("mouseover", imageHover.bind(this, "adTwo"));
document.querySelector('.ad-two').addEventListener("mouseleave", imageLeave.bind(this, "adTwo"));

let adImage = document.querySelector('.ad-one-image');
let adImageTwo = document.querySelector('.ad-two-image');

// Adds ad-image-hover class when mouse is hovered over card
function imageHover(adNumber) {
    if(adNumber === "adOne") {
        adImage.classList.add("ad-image-hover");
    } else {
        adImageTwo.classList.add("ad-image-hover");
    }
};

// Removes ad-image-hover class when mouse leaves/is no longer hovering over card
function imageLeave(adNumber) {
    if(adNumber === "adOne") {
        adImage.classList.remove("ad-image-hover");
    } else {
        adImageTwo.classList.remove("ad-image-hover");
    }
};
