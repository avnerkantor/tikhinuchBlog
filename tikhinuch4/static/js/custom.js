
$(function(){
    $("#Pisa2").hide();
    $("#Analyze").hide();
     $('#Search').hide();
  $('#PisaLink').click(function(){
     $('#Pisa').show();
      $("#Pisa2").hide();
     $('#Analyze').hide();
     $('#Search').hide();
  });
    $('#Pisa2Link').click(function(){
     $('#Pisa').hide();
      $("#Pisa2").show();
     $('#Analyze').hide();
     $('#Search').hide();
  });
  $('#AnalyzeLink').click(function(){
     $('#Pisa').hide();
      $("#Pisa2").hide();
      $('#Search').hide();
     $('#Analyze').show();
  });
    $('#SearchLink').click(function(){
     $('#Pisa').hide();
        $("#Pisa2").hide();
      $('#Search').show();
     $('#Analyze').hide();
  });
});

//$(function () {
//    $('#aa').click(function () {
//        alert("df");
//        $('#myiframe').contents().find('#7448-3').click();
//    });
//});

