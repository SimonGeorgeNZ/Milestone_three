$(document).ready(function () {
        $(".collapsible").collapsible();
        $("select").material_select();
      });

$(".datepicker").pickadate({
selectMonths: true, 
selectYears: 15, 
today: "Today",
clear: "Clear",
close: "Ok",
closeOnSelect: false, 
});



function showToast(message, duration) {
            Materialize.toast(message, duration);
         }

