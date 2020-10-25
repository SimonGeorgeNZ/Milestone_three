$(document).ready(function () {
  $(".collapsible").collapsible();
  $("select").material_select();
  $(".button-collapse").sideNav();
  document.getElementById("matfix").addEventListener("click", function (e) {
    e.stopPropagation();
  });
});

$(".datepicker").pickadate({
  selectMonths: true, 
  selectYears: 15, 
  today: "Today",
  clear: "Clear",
  close: "Ok",
  closeOnSelect: false, 
});

$(document).ready(function () {
  start_date = Date.parse("{{first.start_date}}");
  end_date = Date.parse("{{first.end_date}}");
  $("#start_date")
    .pickadate("picker")
    .set("select", start_date, { format: "dd/mm/yyyy" })
    .trigger("change");
  $("#end_date")
    .pickadate("picker")
    .set("select", end_date, { format: "dd/mm/yyyy" })
    .trigger("change");
});



