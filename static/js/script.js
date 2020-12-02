// navbar initialization
$(document).ready(function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);

    // var elems = document.querySelectorAll('select');
    // var instances = M.FormSelect.init(elems, options);

    $('#add-ingredient-btn').click(function(e){
        e.preventDefault();
        // Add ingredient logic
        console.info("Inside the button click event");
    });
});
