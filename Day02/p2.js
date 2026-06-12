let theCircle = document.getElementById('box');
console.log(theCircle);

theCircle.style.backgroundColor = "red";

function mycolors(){
    if(theCircle.style.backgroundColor == "red"){
        theCircle.style.backgroundColor = "blue";
    }
    else if(theCircle.style.backgroundColor == "blue"){
        theCircle.style.backgroundColor = "black";
    }
    else {
    theCircle.style.backgroundColor = "red"; 
    }
}