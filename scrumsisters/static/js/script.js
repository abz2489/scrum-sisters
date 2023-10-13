$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    $('.timepicker').timepicker();
    $('#span-year').html(new Date().getFullYear());
  });