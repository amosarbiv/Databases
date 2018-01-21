var menu = document.querySelector('.nav__list');
var burger = document.querySelector('.burger');
var doc = $(document);
var l = $('.scrolly');
var panel = $('.panel');
var vh = $(window).height();
var firstTimeToggle = true;

var openMenu = function() {
  burger.classList.toggle('burger--active');
  menu.classList.toggle('nav__list--active');
};

// reveal content of first panel by default
panel.eq(0).find('.panel__content').addClass('panel__content--active');

var scrollFx = function() {
  var ds = doc.scrollTop();
  var of = vh / 4;
  
  // if the panel is in the viewport, reveal the content, if not, hide it.
  for (var i = 0; i < panel.length; i++) {
    if (panel.eq(i).offset().top < ds+of) {
     panel
       .eq(i)
       .find('.panel__content')
       .addClass('panel__content--active');
    } else {
      panel
        .eq(i)
        .find('.panel__content')
        .removeClass('panel__content--active')
    }
  }
};

var scrolly = function(e) {
  e.preventDefault();
  var target = this.hash;
  var $target = $(target);

  $('html, body').stop().animate({
      'scrollTop': $target.offset().top
  }, 300, 'swing', function () {
      window.location.hash = target;
  });
}

var init = function() {
  window.addEventListener('scroll', scrollFx, false);
  window.addEventListener('load', scrollFx, false);
  $('a[href^="#"]').on('click',scrolly);
  $.ajax({
    url: '/GetUserProfile',
    method: 'GET',
    }).success(function(response) {
      responseParse = JSON.parse(response);
      if(responseParse.PlaylistPrivacy == 1){
        $('#toggle-trigger').bootstrapToggle('on');
      }
      else{
        $('#toggle-trigger').bootstrapToggle('off');
      }
  });
  
  $(document).on("click", ".AddToPlaylist", function (e) {
    $.ajax({
      url: "/AddSongToPlaylist",
      data: JSON.stringify({'id': e.target.id}),
      dataType: "json",
      type: 'POST',
      contentType: "application/json"
    }).success(function() {
      var list = (e.target.id).split(" ");
      var tdId = "AddToPlaylist"+list[0];
      console.log(tdId);
      var node = document.getElementById(tdId);
      node.innerHTML = "<i class='fa fa-check fa-2x' style='color:#1a1a1a;' aria-hidden='true'></i>" 
      alert("The song has been added to your playlist");
      });
  });

}

jQuery(document).ready(function ($) {
    var slideCount1 = $('#slider1 ul li').length;
    var slideWidth1 = $('#slider1 ul li').width();
    var slideHeight1 = $('#slider1 ul li').height();
    var sliderUlWidth1 = slideCount1 * slideWidth1;
    
    $('#slider1').css({ width: slideWidth1, height: slideHeight1 });
    
    $('#slider1 ul').css({ width: sliderUlWidth1, marginLeft: - slideWidth1 });
    
      $('#slider1 ul li:last-child').prependTo('#slider1 ul');
  
      function moveLeft1() {
          $('#slider1 ul').animate({
              left: + slideWidth1
          }, 200, function () {
              $('#slider1 ul li:last-child').prependTo('#slider1 ul');
              $('#slider1 ul').css('left', '');
          });
      };
  
      function moveRight1() {
          $('#slider1 ul').animate({
              left: - slideWidth1
          }, 200, function () {
              $('#slider1 ul li:first-child').appendTo('#slider1 ul');
              $('#slider1 ul').css('left', '');
          });
      };
  
      $('a.control_prev1').click(function () {
          moveLeft1();
      });
  
      $('a.control_next1').click(function () {
          moveRight1();
      });

      var slideCount2 = $('#slider2 ul li').length;
      var slideWidth2 = $('#slider2 ul li').width();
      var slideHeight2 = $('#slider2 ul li').height();
      var sliderUlWidth2 = slideCount2 * slideWidth2;
      
      $('#slider2').css({ width: slideWidth2, height: slideHeight2 });
      
      $('#slider2 ul').css({ width: sliderUlWidth2, marginLeft: - slideWidth2 });
      
        $('#slider2 ul li:last-child').prependTo('#slider2 ul');
    
        function moveLeft2() {
            $('#slider2 ul').animate({
                left: + slideWidth2
            }, 200, function () {
                $('#slider2 ul li:last-child').prependTo('#slider2 ul');
                $('#slider2 ul').css('left', '');
            });
        };
    
        function moveRight2() {
            $('#slider2 ul').animate({
                left: - slideWidth2
            }, 200, function () {
                $('#slider2 ul li:first-child').appendTo('#slider2 ul');
                $('#slider2 ul').css('left', '');
            });
        };
    
        $('a.control_prev2').click(function () {
            moveLeft2();
        });
    
        $('a.control_next2').click(function () {
            moveRight2();
        });

        var slideCount3 = $('#slider3 ul li').length;
        var slideWidth3 = $('#slider3 ul li').width();
        var slideHeight3 = $('#slider3 ul li').height();
        var sliderUlWidth3 = slideCount3 * slideWidth3;
        
        $('#slider3').css({ width: slideWidth3, height: slideHeight3 });
        
        $('#slider3 ul').css({ width: sliderUlWidth3, marginLeft: - slideWidth3 });
        
          $('#slider3 ul li:last-child').prependTo('#slider3 ul');
      
          function moveLeft3() {
              $('#slider3 ul').animate({
                  left: + slideWidth3
              }, 200, function () {
                  $('#slider3 ul li:last-child').prependTo('#slider3 ul');
                  $('#slider3 ul').css('left', '');
              });
          };
      
          function moveRight3() {
              $('#slider3 ul').animate({
                  left: - slideWidth3
              }, 200, function () {
                  $('#slider3 ul li:first-child').appendTo('#slider3 ul');
                  $('#slider3 ul').css('left', '');
              });
          };
      
          $('a.control_prev3').click(function () {
              moveLeft3();
          });
      
          $('a.control_next3').click(function () {
              moveRight3();
          });
  });    

doc.on("click", ".alert", function(e) {
    // Get the record's ID via attribute
  //var id = $(this).attr('data-id');

  $.ajax({
    url: '/GetUserProfile',
    method: 'GET',
    //data: $form.serialize()
}).success(function(response) {
    responseParse = JSON.parse(response);
    // Populate the form fields with the data returned from server
    $('#userForm')
        .find('[name="userName"]').val(responseParse.UserName).end()
        .find('[name="passWord"]').val(responseParse.Password).end()
        .find('[name="firstName"]').val(responseParse.FirstName).end()
        .find('[name="lastName"]').val(responseParse.LastName).end()
        .find('[name="country"]').val(responseParse.Country).end()
        .find('[name="age"]').val(responseParse.Age).end()

    // Show the dialog
    modalUser = bootbox
  .dialog({
      title: 'Hey '+responseParse.UserName+', here you can edit your profile!',
      message: $('#userForm'),
      show: false // We will show it manually later
  })
  .on('shown.bs.modal', function() {
      $('#userForm')
          .show()                             // Show the login form
          //.formValidation('resetForm'); // Reset form
  })
  .on('hide.bs.modal', function(e) {
      // Bootbox will remove the modal (including the body which contains the login form)
      // after hiding the modal
      // Therefor, we need to backup the form
      $('#userForm').hide().appendTo('body');
  })
  .modal('show');
});
});

doc.on('ready', init);
