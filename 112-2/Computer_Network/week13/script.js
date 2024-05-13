let $ = (s) => document.querySelector(s);
let $a = (s) => document.querySelectorAll(s);
let btns = $a("button");
let func = [ () => $('#demo').style.display="none", () => $('#demo').style.display="block", () => $('#demo').style.fontSize="40px", () => $('#demo').style.fontSize="20px", ]

for(let i in btns){
    btns[i].addEventListener("click", () => func[i])
}