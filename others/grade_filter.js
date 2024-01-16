(() => {
	let table = document.querySelectorAll('table')
	let s = table[1]
	let trs = s.querySelectorAll('tr')
	let s_tr = Array.from(trs).slice(1)

	min_credit = 1
	min_grade = 1
	black_list = ['大學學習']

	s_tr.forEach(tr => {
		let name = tr.children[0].innerText
		let credit = ~~tr.children[1].innerText
		let grade = ~~tr.children[2].innerText
		if(black_list.indexOf(name) != -1 || credit < min_credit || grade < min_grade){
			tr.remove()
		}
	})
})();

