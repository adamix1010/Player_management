const form = document.getElementById('p-form');
const number = document.getElementById('number');
const info = document.getElementById('info-text');

const stats = {
  INT: document.getElementById('id_stat_INT'),
  REF: document.getElementById('id_stat_REF'),
  TECH: document.getElementById('id_stat_TECH'),
  COOL: document.getElementById('id_stat_COOL'),
  ATTR: document.getElementById('id_stat_ATTR'),
  LUCK: document.getElementById('id_stat_LUCK'),
  BODY: document.getElementById('id_stat_BODY'),
  EMP: document.getElementById('id_stat_EMP'),
  MA: document.getElementById('id_stat_MA')
};

const csrf = document.getElementsByName('csrfmiddlewaretoken');
console.log(csrf);

let max_stats = 60;
number.innerText = max_stats;

function add_all() {
  let sum = 0;
  for (const key in stats) {
    if (Object.hasOwnProperty.call(stats, key)) {
      const statInput = stats[key];
      sum += Number(statInput.value);
    }
  }
  return sum;
}

function handleStatInputChange(inputElement) {
  if (Number(inputElement.value) <= 2) {
    inputElement.value = 2;
  }
  if (Number(inputElement.value) >= 10) {
    inputElement.value = 10;
  }
  max_stats = 60 - add_all();
  if (max_stats < 0) {
    info.innerText = 'You used too much points';
  } else {
    const statInfo = `This is an index of how hard will be rolls for ${inputElement.id.split('_')[2]} oriented things.`;
    info.innerText = statInfo;
  }
  number.innerText = max_stats;

}

for (const key in stats) {
  if (Object.hasOwnProperty.call(stats, key)) {
    const statInput = stats[key];
    statInput.addEventListener('change', () => {
      handleStatInputChange(statInput);
      console.log(max_stats);
    });
  }
}
