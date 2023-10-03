
class BoxGenerator{
    constructor(size, color, parents = content){
        this.size = size;
        this.area = size**2;
        this.color = color;
        this.parents = parents;
    }

    create(size = this.size, color = this.color){
        let box = document.createElement('div');
        box.classList.add('box');
        box.style.backgroundColor = color;
        box.style.width = this.size + 'px';
        box.style.height = this.size + 'px';
        this.parents.append(box);

        return this;
    }

    fillScreen(delta = 40){
        let screenArea = innerHeight * innerWidth;
        let count = ~~ (screenArea / this.area);
        for(let i = 0; i < count; i++){
            setTimeout(() => {
                this.create();
            }, i * delta)
            
            // }
        }
    }
    
}

function changeColor(){
    console.log(1);
}

function showTime(){
    let time = document.querySelector('.time');
    let currentDate = new Date();
    console.log(currentDate);
    let y = currentDate.getFullYear();
    let m = currentDate.getMonth()+1;
    let d = currentDate.getDate();
    m = m ? Number(m) >= 10 : `0${m}`;
    d = d ? Number(d) >= 10 : `0${d}`;
    console.log(y);
    console.log(m);
    console.log(d);

    time.textContent = `${y}-${m}-${d}`;
    
}

let boxSize = 50;
let content = document.querySelector('.content');
let changeColorBtn = document.querySelector('#changeColorBtn');
let showTimeBtn = document.querySelector('#showTimeBtn');

function init(){
    changeColorBtn.addEventListener('click', changeColor);
    showTimeBtn.addEventListener('click', showTime);
    a = new BoxGenerator(boxSize, '#f33');
    a.create();
    a.fillScreen();
}

window.onload = init;
