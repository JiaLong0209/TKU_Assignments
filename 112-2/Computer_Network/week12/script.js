let $ = (s) => document.querySelector(s);
let $a = (s) => document.querySelectorAll(s);

function openMenu(evt, menuName) {
    var i, x, tablinks;
    x = $a(".menu")
    tablinks = $a(".tablink");
    x.forEach((i) => {i.style.display = "none"})
    tablinks.forEach( i => i.className = i.className.replace(" w3-dark-grey", "") )
    $(`#${menuName}`).style.display = "block";
    console.log($(`#${menuName}`));
    evt.currentTarget.firstElementChild.className += " w3-dark-grey";
}

$("#myLink").click();
