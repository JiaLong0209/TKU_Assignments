
function loop(func, n = 10){
	console.log('------------------')
	for(let i = 1; i <=n; i++){
		console.log(`${func(i)}`)
	}
}

function c(n){
	return 3**n - 2**n
}

function d(n){
	return Math.floor(Math.sqrt(n))
}

function e(n){
	return !(n^1) ? 1 : !(n^2) ? 5 : e(n-1) + e(n-2)
}

function f(n){
	return 2**n - 1
}

function g(n){
	return n==1 ? 1 : !(n%2) ? g(n-1)+n/2 : g(n-1)*~~(n/2)
}

function h(n){
	return Array.from({length:n}, (_,i) => Array.from({length:i+1}, (_, j) => j+1).reduce((a,c) => a*c)).filter(x => x <= n).length
}

//
// loop(x=>3**x)
// loop(x=>2**x)
// loop(x=>Math.sqrt(x))

loop(c)
loop(d)
loop(e)
loop(f)
loop(g)
loop(h)
