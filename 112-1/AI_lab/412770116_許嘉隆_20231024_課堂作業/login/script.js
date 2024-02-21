let login_btn = document.querySelector('#login_btn')
let user_name = document.querySelector('#user_name')
let user_password = document.querySelector('#user_password')
let data = [{'username':'jialong', 'password':'12341234'}]

function login(e){
  if(!e.key || e.key == "Enter"){
    let name = user_name.value;
    let password = user_password.value;
    if(!(name && password)){
      alert("Name and password required")
    }else if(data.findIndex(i=>i.username == name && i.password == password) != -1){
      alert("Login successfully!")
      window.location.href = '../todo_list/index.html'
    }else{
      alert("Wrong username or password.")
    }
  }
}

login_btn.addEventListener('click', login)
document.addEventListener('keyup', login) 

