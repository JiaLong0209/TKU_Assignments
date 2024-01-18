
let table = document.querySelectorAll('table')
let s = table[1]
let trs = s.querySelectorAll('tr')
let s_tr = Array.from(trs).slice(1)
let scores = [].map.call(s_tr, x => ~~x.children[2].innerText)
let mean_score = scores.reduce((a,c) => a+c) / scores.length

console.log(scores)
console.log(mean_score)



