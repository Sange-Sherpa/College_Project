function $(value) {
    return document.getElementById(value);
}

// // change div color when active i.e black to white
const active_page = window.location.pathname;
const links = document.querySelectorAll('.nav-link a')

links.forEach(link => {
    if(link.href.includes(`${active_page}`)) {
        link.classList.add('active');
    }
});

// ------------------------------------------------------
// ------------------------------------------------------
// ------------------------------------------------------
// CODE BELOW is for the logout Modal

// LOGOUT MODAL Selector
const logout_modal = $('logout_modal')

// Selector to open logout modal
const logout_modal_open = $('logout_modal_open');

// Selector to open logout modal
const logout_modal_close = $('logout_modal_close');

// logout_modal_open.addEventListener('click', alert("This is an alert !"));
// logout_modal_close.addEventListener('click', alert("This is an alert !"));