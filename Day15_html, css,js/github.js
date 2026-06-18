let btn = document.getElementById("searchBtn");
let profile = document.getElementById("profile");

btn.addEventListener("click", async () => {

    let username =
    document.getElementById("username").value;

    try{

        let response = await fetch(
            `https://api.github.com/users/${username}`
        );

        let data = await response.json();

        profile.innerHTML = `
            <div class="card">

                <img src="${data.avatar_url}">

                <h2>${data.name || "No Name"}</h2>

                <p><b>Username:</b> ${data.login}</p>

                <p><b>Followers:</b> ${data.followers}</p>

                <p><b>Following:</b> ${data.following}</p>

                <p><b>Repositories:</b> ${data.public_repos}</p>

                <p><b>Location:</b> ${data.location || "Not Available"}</p>

            </div>
        `;

    }
    catch(error){

        profile.innerHTML =
        "<h2>User Not Found</h2>";

    }

});