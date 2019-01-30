function toggleDropDownMenu() {
    document.getElementById("dropdown").classList.toggle("dropdown--show");
}

window.onclick = function(event) {
    if (!event.target.matches('.toggle')) {
        var dropdowns = document.getElementsByClassName("dropdown");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('dropdown--show')) {
                openDropdown.classList.remove('dropdown--show');
            }
        }
    }
};