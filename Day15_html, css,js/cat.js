let btn = document.getElementById("btn");
let catImage = document.getElementById("catImage");

btn.addEventListener("click", () => {

    fetch("https://api.thecatapi.com/v1/images/search")

    .then(response => response.json())

    .then(data => {

        catImage.src = data[0].url;

    })

    .catch(error => {

        console.log(error);

    });

});