let red = document.getElementById("red");
let yellow = document.getElementById("yellow");
let green = document.getElementById("green");

function trafficSignal(){

    red.style.background = "red";
    yellow.style.background = "gray";
    green.style.background = "gray";

    setTimeout(() => {

        red.style.background = "gray";
        yellow.style.background = "yellow";
        green.style.background = "gray";

    }, 3000);

    setTimeout(() => {

        red.style.background = "gray";
        yellow.style.background = "gray";
        green.style.background = "green";

    }, 5000);
}

trafficSignal();

setInterval(trafficSignal, 8000);