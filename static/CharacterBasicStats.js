var max_stats = 60
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
const_MA = document.getElementById('id_stat_MA')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

function add_all() {
  return Number(const_INT.value) + Number(const_REF.value) + Number(const_TECH.value) + Number(const_COOL.value) +
    Number(const_ATTR.value) + Number(const_LUCK.value) + Number(const_BODY.value) + Number(const_EMP.value);
}

const url=""
const_INT.addEventListener('change', ()=>{
    if (Number(const_INT.value) <=2){
        const_INT.value = 2
    }
    if (Number(const_INT.value) >=10){
        const_INT.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "Intelligence is measure of your problem solving ability, noticing things, remembering information etc."
    }

    number.innerText = max_stats
    console.log(max_stats)
})

const_REF.addEventListener('change', ()=>{
    if (Number(const_REF.value) <=2){
        const_REF.value = 2
    }
    if (Number(const_REF.value) >=10){
        const_REF.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "Reflex covers your basic dexterity, but also your coordination, and how well you handle weapons and vehicles"
    }

    number.innerText = max_stats
    console.log(max_stats)
})

const_TECH.addEventListener('change', ()=>{
    if (Number(const_TECH.value) <=2){
        const_TECH.value = 2
    }
    if (Number(const_TECH.value) >=10){
        const_TECH.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "This is an index of how well you relate to hardware and other technically oriented things."
    }

    number.innerText = max_stats
    console.log(max_stats)
})

const_COOL.addEventListener('change', ()=>{
    if (Number(const_COOL.value) <=2){
        const_COOL.value = 2
    }
    if (Number(const_COOL.value) >=10){
        const_COOL.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "Cool measures how well the character stands up to stress, fear, pressure, physical pain."
    }

    number.innerText = max_stats
    console.log(max_stats)
})

const_ATTR.addEventListener('change', ()=>{
    if (Number(const_ATTR.value) <=2){
        const_ATTR.value = 2
    }
    if (Number(const_ATTR.value) >=10){
        const_ATTR.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "This is how good-looking you are."
    }

    number.innerText = max_stats
    console.log(max_stats)
})

const_LUCK.addEventListener('change', ()=>{
    if (Number(const_LUCK.value) <=2){
        const_LUCK.value = 2
    }
    if (Number(const_LUCK.value) >=10){
        const_LUCK.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = " Your luck represents how many points you may use each game to influence the outcome of a critical event."
    }

    number.innerText = max_stats
    console.log(max_stats)
})


const_MA.addEventListener('change', ()=>{
    if (Number(const_MA.value) <=2){
        const_MA.value = 2
    }
    if (Number(const_MA.value) >=10){
        const_MA.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "The higher your Movement Allowance, the more distance you can cover in a turn."
    }

    number.innerText = max_stats
    console.log(max_stats)
})

const_EMP.addEventListener('change', ()=>{
    if (Number(const_EMP.value) <=2){
        const_EMP.value = 2
    }
    if (Number(const_EMP.value) >=10){
        const_EMP.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "This Stat represents how well you relate to other living things.\n Also measure of how close you are to cyberpsychosis"
    }

    number.innerText = max_stats
    console.log(max_stats)
})

const_BODY.addEventListener('change', ()=>{
    if (Number(const_BODY.value) <=2){
        const_BODY.value = 2
    }
    if (Number(const_BODY.value) >=10){
        const_BODY.value = 10
    }
    console.log(add_all() )
    max_stats = 60 - add_all()
    if (max_stats < 0) {
        info.innerText = "You used too much points"
    }
    if (max_stats >= 0){
        info.innerText = "Body Type determines how much damage you can take in wounds,\n how much you can lift or carry, how well you recover from shock,\n and how much additional damage you cause with physical attacks"
    }

    number.innerText = max_stats
    console.log(max_stats)
})

console.log(form)