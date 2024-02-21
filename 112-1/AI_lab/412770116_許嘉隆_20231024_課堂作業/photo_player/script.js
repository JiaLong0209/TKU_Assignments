let buttons = document.querySelectorAll('button')
let files = Array.from({length:5}, (v,i)=>`${i}.png`)
let index = 0;

changeImage = n => {
    index += n;
    document.querySelector('img').src = `./images/${files[index%=files.length]}`;
}

buttons.forEach((v,i) => v.onclick = () => changeImage(!i?files.length-1:1))