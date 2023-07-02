let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navlist');

menu.onclick = () => {
    menu.classList.toggle('bx-x')
    navlist.classList.toggle('open')
}


let btn = document.querySelector('#success-btn');
let success = document.querySelector('.success');

btn.onclick = () => {
    success.classList.toggle('close')
}

