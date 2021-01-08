// Mouse Enter/Leave Event Listeners for Ad One
document.querySelector('.ad-one').addEventListener("mouseover", imageHover.bind(this, "one", "enter"));
document.querySelector('.ad-one').addEventListener("mouseleave", imageHover.bind(this, "one", "leave"));
// Mouse Enter/Leave Event Listeners for Ad Two
document.querySelector('.ad-two').addEventListener("mouseover", imageHover.bind(this, "two", "enter"));
document.querySelector('.ad-two').addEventListener("mouseleave", imageHover.bind(this, "two", "leave"));

// Adds OR removes ad-image-hover class to respective card image depending on user actions.
function imageHover(adNumber, action) {
    let image = document.querySelector(`.ad-${adNumber}-image`);
    if (action === "enter") {
        image.classList.add("ad-image-hover");
    } else if (action === "leave") {
        image.classList.remove("ad-image-hover");
    }
}
