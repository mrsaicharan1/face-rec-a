

var course_value="";
var selected_course="";
var link = "";




$(document).ready(function() {

  $("#employer-form").hide();
  $("#employee").addClass('life');
  $("#view").hide();
  $("#MARK").addClass('life');
  $("#view1").show(500);
  $("#VIEW").addClass('life');
  $('.alert').alert('close');
  $('#alert_modal').modal('show')
  


  
 

  $('#settings_job_vac').modal('show');

  $("#employer").click(function() {
    $("#employee-form").hide();
    $("#employee").removeClass('life');
    $("#employer-form").show(500);
    $("#employer").addClass('life');
  });
  $("#employee").click(function() {
    $("#employer-form").hide();
    $("#employer").removeClass('life');
    $("#employee-form").show(500);
    $("#employee").addClass('life');
  });


  $("#VIEW").click(function() {
    $("#view1").hide();
    
    $("#view1").show(500);
    $("#VIEW").addClass('life');
  });



  $("#MARK").click(function() {
    $("#view").hide();
    $("#CHANGE").removeClass('life');
    $("#mark").show(500);
    $("#MARK").addClass('life');
  });
  $("#CHANGE").click(function() {
    $("#mark").hide();
    $("#MARK").removeClass('life');
    $("#view").show(500);
    $("#CHANGE").addClass('life');
  });

  $("#filter-list").hide();
  $("#sort").addClass('life');

  $("#filter").click(function() {
    $("#sort-list").hide();
    $("#sort").removeClass('life');
    $("#filter-list").show(500);
    $("#filter").addClass('life');
  });
  
  $("#sort").click(function() {
    $("#filter-list").hide();
    $("#filter").removeClass('life');
    $("#sort-list").show(500);
    $("#sort").addClass('life');
  });

  $("#m1-employer-form").hide();
  $("#m1-employee").addClass('life');

  $("#m1-employer").click(function() {
    $("#m1-employee-form").hide();
    $("#m1-employee").removeClass('life');
    $("#m1-employer-form").show(500);
    $("#m1-employer").addClass('life');
  });
  $("#m1-employee").click(function() {
    $("#m1-employer-form").hide();
    $("#m1-employer").removeClass('life');
    $("#m1-employee-form").show(500);
    $("#m1-employee").addClass('life');
  });

  $("#signin-box").hide();


  $("#login-for-employee").click(function() {
    $('#signup-box').fadeOut();
    $("#signin-box").fadeIn(700);
  });

  $("#login-for-employer").click(function() {
    $('#signin-box').fadeIn(700);
    $("#signup-box").fadeOut();
  });

  $("#signup-for-employee").click(function() {
    $('#signin-box').fadeOut();
    $("#signup-box").fadeIn(700);
  });

  $("#signup-for-employer").click(function() {
    $('#signin-box').fadeOut();
    $("#signup-box").fadeIn(700);
  });

  $('#percent').keypress(function(e) {
    if(e.which == 13) {
      //alert("hello");
      var per = $('#percent').val();
      //alert(per);
      var p = "p" + per;
      //alert(p);
      $('#match_skill').addClass(p);
      $('.inp-skill-percent').hide();
    }
  });
  
  $('#course_list li').click(function(){

    $("#course_list li").removeClass('life');
    $(this).addClass('life');
     
       course_value = $(this).text();
      console.log(course_value);
  });

  $('#ok-btn').click(function(){

    $('#settings_job_vac').modal('hide');


         

       selected_course = course_value;
       document.getElementById("selected").innerHTML=selected_course;

       $.getJSON("/getlink", {"selected_course": selected_course},function(data,status,xhr)

       {
         console.log("tt")
         console.log(data.link);
         link=data.link;
         
        //  link = "https://docs.google.com/spreadsheets/d/1xlgbxidPaQ20MmZ9rElBlGG2whKbBQa9G8-J5DzCvIo/edit?usp=sharing";
         document.getElementById("google_sheet").setAttribute("href",link);

       }

      
      
      
      );
    
      console.log( selected_course +"222");
  });

});