let table = document.querySelectorAll('table')
let s = table[1]
let trs = s.querySelector('tr')
let s_tr = Array.from(trs).slice(1)

min_credit = 1
min_grade = 1

s_tr.forEach(tr => {
	let credit = ~~tr.children[1].innerText
	let grade = ~~tr.children[2].innerText

	if(credit < min_credit || grade < min_grade){
		tr.remove()
	}
})








