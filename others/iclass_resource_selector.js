(() => {
	let box = document.querySelectorAll('input[type="checkbox"]');
	let is_select_all = false;
	let left = 1, right = 10;
	if (is_select_all) {
		box[0].click()
	} else {
		for (let index in box) {
			if (index >= left && index <= right) {
				box[index].click()
			}
		}
	}
})()

