// denominations
function change(n, d){
	coins = {}
	for(let i of d.sort((a,b) => b - a)){
		while(n >= i){
			coins[i] = coins[i] ? coins[i] + 1 : 1
			n -= i
		}
	}
	console.log(coins)
	return Object.keys(coins).reduce((a, c) => a + c)
}

n = 16469
d = [1, 5, 10, 50, 100, 500, 1000]

change(n, d)
