let add_btn = document.querySelector('#add_btn')
let add_input = document.querySelector('#add_input')
let list = document.querySelector('#list');
let data = []

function render(){
  list.innerHTML = ''
  for(let i in data){
    list.innerHTML += `
    <div class="item" data-id="${data[i].id}">
      <li>${~~i+1}. ${data[i].content}</li>
      <button type="submit" class="delete" >X</button>
    </div>
  `;   
  }
}

function addItem(e){
  if(add_input.value && (e.key == "Enter" || !e.key)){
    data.push({id:new Date().getTime(), content: add_input.value});
    render();
    add_input.value = ''
  }
}

function removeItem(e){
  let id = e.target.closest("div").dataset.id;
  if(e.target.getAttribute("class") == "delete"){
    data.splice(data.findIndex(i => id == i.id),1);
  }
  render();
}

add_btn.addEventListener('click', addItem)
document.addEventListener('keyup', addItem)
list.addEventListener('click', removeItem)