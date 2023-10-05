
class BoxGenerator{
    constructor(size = 20, color = '#fff', randomColor = false, deltaTime = 10, parents = content){
        this.size = size;
        this.area = size**2;
        this.color = color;
        this.parents = parents;
        this.deltaTime = deltaTime;
        this.boxList = [];
        this.createTimeoutList = [];
        this.randomColor = randomColor;
        console.log(this)
    }

    getRandomColor(){
        return this.hsl(Math.random() * 360, Math.random()*70 + 30, Math.random()*70 + 30)
    }

    hsl(h, s, l){
        return `hsl(${h},${s}%,${l}%)`
    }

    create(color = this.color ,randomColor = this.randomColor){
        let box = document.createElement('div');
        box.classList.add('box');
        if(randomColor){    
            box.style.backgroundColor = this.getRandomColor();
        }else{  
            box.style.backgroundColor = color;
        }
        box.style.width = this.size + 'px';
        box.style.height = this.size + 'px';
        this.parents.append(box);
        this.boxList.push(box);

        return this;
    }

    fillScreen(randomColor = false ,delta = this.deltaTime){
        let screenArea = innerHeight * innerWidth;
        this.count = ~~ (screenArea / this.area);
        let randomHue = Math.random()*360;
        this.createInterval = setInterval(()=>{
            if(this.count){
                if(randomColor){
                    this.create(this.getRandomColor(), false);
                }else{
                    this.create(this.hsl((randomHue + this.count)%360,60,60), false);
                }
                this.count -= 1;
            }
        }, delta)
        return this;
    }

    changeDeltaTime(delta){
        this.deltaTime = delta;
        return this;
    }

    changeColor(randomColor = false){
        this.boxList.forEach((box)=>{
            let color = this.getRandomColor();
            if(randomColor){
                box.style.backgroundColor = color;
            }else{
                box.style.backgroundColor = this.color;
            }
        })
        return this;
    }

    clear(){
        this.parents.innerHTML = "";
        this.boxList = [];
        clearInterval(this.createInterval)
        return this;
    }

    regenerate(randomColor = false){
        this.clear().fillScreen(randomColor);
        return this;
    }
    
}

function toTwoDigits(num){
    return `0${num}`.slice(-2)
}

function toggleTime(){
    isShowTime = !isShowTime;
    showTime()
}

function showTime(){
    let time = document.querySelector('.time');
    let currentDate = new Date();
    let y = currentDate.getFullYear();
    let m = currentDate.getMonth()+1;
    let d = currentDate.getDate();
    m = toTwoDigits(m);
    d = toTwoDigits(d);
    
    time.textContent = isShowTime ? `${y}-${m}-${d} ${String(currentDate).slice(16,24)}` : '' ;
}

let isShowTime = false
let boxSize = (innerWidth / 25);
let content = document.querySelector('.content');
let changeColorBtn = document.querySelector('#changeColorBtn');
let randomColorBtn = document.querySelector('#randomColorBtn');
let showTimeBtn = document.querySelector('#showTimeBtn');
let regenerateBtn = document.querySelector('#regenerateBtn');

function init(){
    a = new BoxGenerator(boxSize, '#fff', true, 20).fillScreen(); 
    showTime();
    setInterval(showTime, 1000);
    changeColorBtn.addEventListener('click', ()=>{
        a.changeColor(true);
    });

    showTimeBtn.addEventListener('click', toggleTime);
    regenerateBtn.addEventListener('click', ()=>{
        a.regenerate();
    });
    document.addEventListener('keypress', ()=>{
        a.regenerate();
    })
    randomColorBtn.addEventListener('click', ()=>{
        a.regenerate(true)
    });
}



window.onload = init;
