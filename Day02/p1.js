let content = document.querySelector('h1');
console.log(content);

let btn = document.querySelector('button');
console.log(btn);

btn.addEventListener('click', () => {
    if (content.textContent === "i am learning JS") {
        content.textContent = "I want to Learn React";
    } else {
        content.textContent = "i am learning JS";
    }
});

// function myText() {
//     content.textContent = "I want to Learn React";
// }

function add(a, b) {
    console.log(a + b);
}

add(6, 7);
add(3, 6);

const add1=(x,y)=>{
    console.log(x+y)
}
add1(6, 2);
add1(4, 7);

//if else 
    let age = 15;
if(age>=18){
    console.log("You can vote");
}
else{
    console.log("You cannot vote");
}