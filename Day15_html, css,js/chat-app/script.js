const chatBox =
document.getElementById("chatBox");

const input =
document.getElementById("userInput");

const sendBtn =
document.getElementById("sendBtn");

let chats =
JSON.parse(localStorage.getItem("chatHistory"))
|| [];

loadChats();

sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keypress",(e)=>{

    if(e.key==="Enter"){

        sendMessage();

    }

});

function sendMessage(){

    let message = input.value.trim();

    if(message===""){

        return;

    }

    addMessage(message,"user");

    input.value="";

    setTimeout(()=>{

        let reply =
        generateReply(message);

        addMessage(reply,"bot");

    },1000);
}

function addMessage(text,type){

    let msg = {

        text:text,
        type:type
    };

    chats.push(msg);

    localStorage.setItem(
        "chatHistory",
        JSON.stringify(chats)
    );

    let div =
    document.createElement("div");

    div.classList.add("message");

    div.classList.add(type);

    div.textContent=text;

    chatBox.appendChild(div);

    chatBox.scrollTop =
    chatBox.scrollHeight;
}

function loadChats(){

    chats.forEach(msg=>{

        let div =
        document.createElement("div");

        div.classList.add("message");

        div.classList.add(msg.type);

        div.textContent =
        msg.text;

        chatBox.appendChild(div);

    });

}

function generateReply(message){

    message =
    message.toLowerCase();

    if(message.includes("hello")){

        return "Hello Aashish 👋";
    }

    if(message.includes("name")){

        return "I am your AI Assistant.";
    }

    if(message.includes("college")){

        return "You study at MIT ADT University.";
    }

    if(message.includes("java")){

        return "Java is an Object Oriented Programming Language.";
    }

    return "Sorry, I don't understand that yet.";
}