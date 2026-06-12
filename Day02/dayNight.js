let website = document.querySelector("body");
console.log(website);

let btn = document.querySelector("button");
console.log(btn);

btn.addEventListener("click", function() {
    website.classList.toggle("night");
    if(btn.textContent === "🌙")     {
        btn.textContent = "☀️";
    } else {
        btn.textContent = "🌙";
    }
});