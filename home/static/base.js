document.querySelector(".menu-button").addEventListener("click", () => {
    const navbar = document.querySelector(".nav-bar")
    if(navbar.classList.contains("open-menu")) {
        navbar.classList.remove("open-menu")
    } else {
        navbar.classList.add("open-menu")
    }
})
