function toggleMenu() {
    var menuLink = document.getElementById("menu-link");
    var cartContainer = document.getElementById("container");
    
    if (menuLink.style.display === "none") {
        menuLink.style.display = "block";
        cartContainer.style.transform = `translateX(${menuLink.clientHeight}px)`;
    } else {
        menuLink.style.display = "none";
        cartContainer.style.transform = "translateX(0)";
    }
}
