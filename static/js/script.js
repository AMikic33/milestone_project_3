// navbar initialization
$(document).ready(function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});

// add another ingrediant function
$('#create_button').click(function() {
  var html = $('.child_div:first').parent().html();
  $(html).insertBefore(this);
});

$(document).on("click", ".deleteButton", function() {
  $(this).closest('.child_div').remove();
});

