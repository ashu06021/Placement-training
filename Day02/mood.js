let photo = document.querySelector('img')
console.log(photo)

let b1 = document.querySelectorAll('button')[0]
console.log(b1)

b1.addEventListener('click', ()=>{
    photo.src = "images.jpg"
})

b2 = document.querySelectorAll('button')[1]
b2.addEventListener('click', ()=>{
    photo.src = "sad.jpg"
})

b3 = document.querySelectorAll('button')[2]
b3.addEventListener('click', ()=>{
    photo.src = "angry.jpg"
})