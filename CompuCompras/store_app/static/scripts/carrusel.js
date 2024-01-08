
var images = [
    { src: "./imagenes/uno.jpg", alt: "Image 1" },
    { src: "/imagenes/dos.jpg", alt: "Image 2" },
    { src: "/imagenes/tres.jpg", alt: "Image 3" }
];

var imageIndex = 0;
var carousel = document.getElementById("carousel");

setInterval(function() {
    carousel.src = images[imageIndex].src;
    carousel.alt = images[imageIndex].alt;
    imageIndex = (imageIndex + 1) % images.length;
}, 2000);