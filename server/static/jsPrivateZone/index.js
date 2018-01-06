var menu = document.querySelector('.nav__list');
var burger = document.querySelector('.burger');
var doc = $(document);
var l = $('.scrolly');
var panel = $('.panel');
var vh = $(window).height();
var modalUser = null;

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
  burger.addEventListener('click', openMenu, false);
  window.addEventListener('scroll', scrollFx, false);
  window.addEventListener('load', scrollFx, false);
  $('a[href^="#"]').on('click',scrolly);
  $.ajax({
    url: 'http://127.0.0.1:8888/GetUserProfile',
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
  
  $('#toggle-trigger').change(function() {
    $.ajax({
      url: 'http://127.0.0.1:8888/ChangePlaylistPrivacy',
      type: "POST",
      data: JSON.stringify({"privacy":$(this).prop('checked')}),
      dataType: "json",
      contentType: "application/json"
  })
  });
}

doc.on("click", ".alert", function(e) {
    // Get the record's ID via attribute
  //var id = $(this).attr('data-id');

  $.ajax({
    url: 'http://127.0.0.1:8888/GetUserProfile',
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
