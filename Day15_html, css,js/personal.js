let loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click", () => {

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if(username === "admin" && password === "1234"){

        document.getElementById("loginPage").style.display = "none";

        document.getElementById("detailsForm").style.display = "block";

    }
    else{

        document.getElementById("message").textContent =
        "Invalid Username or Password";

    }

});

let submitBtn = document.getElementById("submitBtn");

submitBtn.addEventListener("click", () => {

    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;

    document.getElementById("output").innerHTML = `
        <h3>Entered Details</h3>
        <p>Name : ${name}</p>
        <p>Age : ${age}</p>
        <p>Email : ${email}</p>
        <p>Phone : ${phone}</p>
    `;
});