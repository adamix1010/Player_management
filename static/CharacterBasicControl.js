const imgBox = document.getElementById('img-box')
const form = document.getElementById('p-form')

const image = document.getElementById('id_picture')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

const url=""
image.addEventListener('change', ()=>{
    const img_data = image.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(url)
    imgBox.innerHTML = `<img src="${url}" width="50%">`
})



console.log(form)