$(document).ready(function () {
        $(".collapsible").collapsible();
        $("select").material_select();
        $(".button-collapse").sideNav();
      });

$(".datepicker").pickadate({
selectMonths: true, 
selectYears: 15, 
today: "Today",
clear: "Clear",
closeOnSelect: true, 
});

function showToast(message, duration) {
            Materialize.toast(message, duration);
        }



