let $ = (s) => document.querySelector(s);
let $a = (s) => document.querySelectorAll(s);
let p = $(`#demo1`);

let btns = $a("button");

let d = new Date();


let func1 = () => {
    p.innerHTML = `
    星期${d.getDay()} <br>
    ${d.getMonth() + 1}/${d.getDate()}/${d.getFullYear()}<br>
    時間${d.getHours()}:${d.getMinutes()}:${d.getSeconds()} <br>
    自1970年1月1日以來的毫秒總數:${d.getTime()}
    `
}

let func2 = (t) => {
    p.innerHTML += `<br>Hello world`
}