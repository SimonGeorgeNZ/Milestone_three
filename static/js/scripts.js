

$(document).ready(function () {
    $(".collapsible").collapsible();
    $("select").material_select();
    $(".button-collapse").sideNav();
    document
        .getElementById("matfix")
        .addEventListener("click", function (e) {
        e.stopPropagation();
        });
    });
    
$(".datepicker").pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: "Today",
    clear: "Clear",
    close: "Ok",
    closeOnSelect: false, // Close upon selecting a date,
});

$(document).ready(function() {
        start_date = Date.parse('{{first.start_date}}');
        end_date = Date.parse('{{first.end_date}}');
        $('#start_date').pickadate('picker').set('select', start_date, { format: 'dd/mm/yyyy' }).trigger('change');
        $('#end_date').pickadate('picker').set('select', end_date, { format: 'dd/mm/yyyy' }).trigger('change');
    });





