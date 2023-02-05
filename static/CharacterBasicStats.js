var max_stats = 20
const form = document.getElementById('p-form')
const number = document.getElementById('number')
const info = document.getElementById('info-text')
number.innerText = max_stats

const_INT = document.getElementById('id_stat_INT')
const_REF = document.getElementById('id_stat_REF')
const_TECH = document.getElementById('id_stat_TECH')
const_COOL = document.getElementById('id_stat_COOL')
const_ATTR = document.getElementById('id_stat_ATTR')
const_LUCK = document.getElementById('id_stat_LUCK')
const_BODY = document.getElementById('id_stat_BODY')
const_EMP = document.getElementById('id_stat_EMP')


const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

function add_all() {
  return Number(const_INT.value) + Number(const_REF.value) + Number(const_TECH.value) + Number(const_COOL.value) +
    Number(const_ATTR.value) + Number(const_LUCK.value) + Number(const_BODY.value) + Number(const_EMP.value);
}

const url=""
const_INT.addEventListener('change', ()=>{
    console.log(add_all() )
    max_stats = 20 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats > 0){
        info.innerText = "You used too much points"
    }
    number.innerText = max_stats
    console.log(max_stats)
})
console.log(form)