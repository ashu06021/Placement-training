let fruits = [
    "🍎","🥭","🍒",
    "🥭","🍒","🍎",
    "🥭","🍒","🥭",
    "🍎"
];

for(let i=0;i<fruits.length;i++){

    console.log(fruits[i]);

    if(fruits[i] === "🍒"){

        document.getElementById("cherry").textContent += " 🍒";

    }
    else if(fruits[i] === "🥭"){

        document.getElementById("mango").textContent += " 🥭";

    }
    else{

        document.getElementById("apple").textContent += " 🍎";

    }
}