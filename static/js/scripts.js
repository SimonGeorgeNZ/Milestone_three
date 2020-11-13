// Elements on pages taken from Materialise 

$(document).ready(function () {
  $(".collapsible").collapsible();
  $("select").material_select();
  $(".button-collapse").sideNav();


$(".datepicker").pickadate({
  selectMonths: true, 
  selectYears: 15, 
  today: "Today",
  clear: "",
  close: "Ok",
  closeOnSelect: false, 
  max: new Date(),
  
});

});










