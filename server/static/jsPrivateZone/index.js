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
    if(!firstTimeToggle){
        $.ajax({
          url: 'http://127.0.0.1:8888/ChangePlaylistPrivacy',
          type: "POST",
          data: JSON.stringify({"privacy":$(this).prop('checked')}),
          dataType: "json",
          contentType: "application/json"
      })
    }
    else{
      firstTimeToggle = false;
    }
  });

  $(".custom-select").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger">' + 'Decade' + '</span>';
        template += '<div class="custom-options">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option:first-of-type").hover(function() {
    $(this).parents(".custom-options").addClass("option-hover");
  }, function() {
    $(this).parents(".custom-options").removeClass("option-hover");
  });
  $(".custom-select-trigger").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select").removeClass("opened");
    });
    $(this).parents(".custom-select").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option").on("click", function() {
    $(this).parents(".custom-select-wrapper").find("select").val($(this).data("value"));
    $(this).parents(".custom-options").find(".custom-option").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select").removeClass("opened");
    $(this).parents(".custom-select").find(".custom-select-trigger").text($(this).text());

    var decade = $(this).text();
    $.ajax({
      url: 'http://127.0.0.1:8888/GetUserSearchTerm',
      type: 'POST',
      data: JSON.stringify({"Type":'Artist',"Decade":decade}),
      dataType: "json",
      contentType: "application/json"
      }).success(function() {
        $.ajax({
          url: 'http://127.0.0.1:8888/GetTableTimeMachine',
          type: 'GET',
          }).success(function(response) {
            responseParse = JSON.parse(response);
            var node = document.getElementById('five');
            node.innerHTML = '<div class=scrollbox><div class="table-responsive header-fixed" style="text-align:left;height:300px;"><table class="table table-striped "><thead><tr><th>#</th><th>Artist</th></tr></thead><tbody id="artistTable"></tbody></table></div></div>';
            var node = document.getElementById('artistTable');
            var htmlTableInsert = "";
            var index = 1;
            responseParse.forEach(element => {
              htmlTableInsert += "<tr>" +
              "<td class='col-md-1'>"+index+"</td>" +
              "<td class='col-md-8'>"+element['col2']+"</td>" +
              "</tr>"
              index++;
            });
            node.innerHTML = htmlTableInsert;
        });
    });
  });

  $(".custom-select2").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger2">' + 'Decade' + '</span>';
        template += '<div class="custom-options2">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option2 ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper2"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option2:first-of-type").hover(function() {
    $(this).parents(".custom-options2").addClass("option-hover2");
  }, function() {
    $(this).parents(".custom-options2").removeClass("option-hover2");
  });
  $(".custom-select-trigger2").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select2").removeClass("opened");
    });
    $(this).parents(".custom-select2").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option2").on("click", function() {
    $(this).parents(".custom-select-wrapper2").find("select").val($(this).data("value"));
    $(this).parents(".custom-options2").find(".custom-option2").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select2").removeClass("opened");
    $(this).parents(".custom-select2").find(".custom-select-trigger2").text($(this).text());

    var decade = $(this).text();
    $.ajax({
      url: 'http://127.0.0.1:8888/GetUserSearchTerm',
      type: 'POST',
      data: JSON.stringify({"Type":'Song',"Decade":decade}),
      dataType: "json",
      contentType: "application/json"
      }).success(function() {
        $.ajax({
          url: 'http://127.0.0.1:8888/GetTableTimeMachine',
          type: 'GET',
          }).success(function(response) {
            responseParse = JSON.parse(response);
            var node = document.getElementById('six');
            node.innerHTML = '<div class=scrollbox><div class="table-responsive header-fixed" style="text-align:left;height:300px;"><table class="table table-striped "><thead><tr><th>#</th><th>Song</th></tr></thead><tbody id="songTable"></tbody></table></div></div>';
            var node = document.getElementById('songTable');
            var htmlTableInsert = "";
            var index = 1;
            responseParse.forEach(element => {
              htmlTableInsert += "<tr>" +
              "<td class='col-md-1'>"+index+"</td>" +
              "<td class='col-md-8'>"+element['col2']+"</td>" +
              "</tr>"
              index++;
            });
            node.innerHTML = htmlTableInsert;
        });
    });
  });

  $(".custom-select3").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger3">' + 'Decade' + '</span>';
        template += '<div class="custom-options3">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option3 ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper3"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option3:first-of-type").hover(function() {
    $(this).parents(".custom-options3").addClass("option-hover3");
  }, function() {
    $(this).parents(".custom-options3").removeClass("option-hover3");
  });
  $(".custom-select-trigger3").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select3").removeClass("opened");
    });
    $(this).parents(".custom-select3").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option3").on("click", function() {
    $(this).parents(".custom-select-wrapper3").find("select").val($(this).data("value"));
    $(this).parents(".custom-options3").find(".custom-option3").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select3").removeClass("opened");
    $(this).parents(".custom-select3").find(".custom-select-trigger3").text($(this).text());

    var decade = $(this).text();
    $.ajax({
      url: 'http://127.0.0.1:8888/GetUserSearchTerm',
      type: 'POST',
      data: JSON.stringify({"Type":'Genre',"Decade":decade}),
      dataType: "json",
      contentType: "application/json"
      }).success(function() {
        $.ajax({
          url: 'http://127.0.0.1:8888/GetTableTimeMachine',
          type: 'GET',
          }).success(function(response) {
            responseParse = JSON.parse(response);
            var node = document.getElementById('seven');
            node.innerHTML = '<div class=scrollbox><div class="table-responsive header-fixed" style="text-align:left;height:300px;"><table class="table table-striped "><thead><tr><th>#</th><th>Genre</th></tr></thead><tbody id="genreTable"></tbody></table></div></div>';
            var node = document.getElementById('genreTable');
            var htmlTableInsert = "";
            var index = 1;
            responseParse.forEach(element => {
              htmlTableInsert += "<tr>" +
              "<td class='col-md-1'>"+index+"</td>" +
              "<td class='col-md-8'>"+element['col2']+"</td>" +
              "</tr>"
              index++;
            });
            node.innerHTML = htmlTableInsert;
          });
    });
  });

  $(".custom-select4").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger4">' + 'Select' + '</span>';
        template += '<div class="custom-options4">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option4 ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper4"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option4:first-of-type").hover(function() {
    $(this).parents(".custom-options4").addClass("option-hover4");
  }, function() {
    $(this).parents(".custom-options4").removeClass("option-hover4");
  });
  $(".custom-select-trigger4").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select4").removeClass("opened");
    });
    $(this).parents(".custom-select4").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option4").on("click", function() {
    $(this).parents(".custom-select-wrapper4").find("select").val($(this).data("value"));
    $(this).parents(".custom-options4").find(".custom-option4").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select4").removeClass("opened");
    $(this).parents(".custom-select4").find(".custom-select-trigger4").text($(this).text());

    var typeOfSearch = $(this).text();
    $.ajax({
      url: 'http://127.0.0.1:8888/GetUserSearchTerm',
      type: 'POST',
      data: JSON.stringify({"Type":'Artist',"TypeOfSearch":typeOfSearch}),
      dataType: "json",
      contentType: "application/json"
      }).success(function() {
        $.ajax({
          url: 'http://127.0.0.1:8888/GetTableTrending',
          type: 'GET',
          }).success(function(response) {
            responseParse = JSON.parse(response);
            var node = document.getElementById('fiveTrending');
            node.innerHTML = '<div class=scrollbox><div class="table-responsive header-fixed" style="text-align:left;height:270px;"><table class="table table-striped "><thead><tr><th>#</th><th>Artist</th></tr></thead><tbody id="artistsTable"></tbody></table></div></div>';
            var node = document.getElementById('artistsTable');
            var htmlTableInsert = "";
            var index = 1;
            responseParse.forEach(element => {
              htmlTableInsert += "<tr>" +
              "<td class='col-md-1'>"+index+"</td>" +
              "<td class='col-md-8'>"+element['col1']+"</td>" +
              "</tr>"
              index++;
            });
            node.innerHTML = htmlTableInsert;
          });
    });
  });

  $(".custom-select5").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger5">' + 'Select' + '</span>';
        template += '<div class="custom-options5">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option5 ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper5"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option5:first-of-type").hover(function() {
    $(this).parents(".custom-options5").addClass("option-hover5");
  }, function() {
    $(this).parents(".custom-options5").removeClass("option-hover5");
  });
  $(".custom-select-trigger5").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select5").removeClass("opened");
    });
    $(this).parents(".custom-select5").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option5").on("click", function() {
    $(this).parents(".custom-select-wrapper5").find("select").val($(this).data("value"));
    $(this).parents(".custom-options5").find(".custom-option5").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select5").removeClass("opened");
    $(this).parents(".custom-select5").find(".custom-select-trigger5").text($(this).text());

    var typeOfSearch = $(this).text();
    $.ajax({
      url: 'http://127.0.0.1:8888/GetUserSearchTerm',
      type: 'POST',
      data: JSON.stringify({"Type":'Songs',"TypeOfSearch":typeOfSearch}),
      dataType: "json",
      contentType: "application/json"
      }).success(function() {
        $.ajax({
          url: 'http://127.0.0.1:8888/GetTableTrending',
          type: 'GET',
          }).success(function(response) {
            responseParse = JSON.parse(response);
            var node = document.getElementById('sixTrending');
            node.innerHTML = '<div class=scrollbox><div class="table-responsive header-fixed" style="text-align:left;height:270px;"><table class="table table-striped "><thead><tr><th>#</th><th>Song</th></tr></thead><tbody id="songsTable"></tbody></table></div></div>';
            var node = document.getElementById('songsTable');
            var htmlTableInsert = "";
            var index = 1;
            responseParse.forEach(element => {
              htmlTableInsert += "<tr>" +
              "<td class='col-md-1'>"+index+"</td>" +
              "<td class='col-md-8'>"+element['col1']+"</td>" +
              "</tr>"
              index++;
            });
            node.innerHTML = htmlTableInsert;
          });
    });
  });

  $(".custom-select6").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger6">' + 'Select' + '</span>';
        template += '<div class="custom-options6">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option6 ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper6"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option6:first-of-type").hover(function() {
    $(this).parents(".custom-options6").addClass("option-hover6");
  }, function() {
    $(this).parents(".custom-options6").removeClass("option-hover6");
  });
  $(".custom-select-trigger6").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select6").removeClass("opened");
    });
    $(this).parents(".custom-select6").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option6").on("click", function() {
    $(this).parents(".custom-select-wrapper6").find("select").val($(this).data("value"));
    $(this).parents(".custom-options6").find(".custom-option6").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select6").removeClass("opened");
    $(this).parents(".custom-select6").find(".custom-select-trigger6").text($(this).text());

    var typeOfSearch = $(this).text();
    $.ajax({
      url: 'http://127.0.0.1:8888/GetUserSearchTerm',
      type: 'POST',
      data: JSON.stringify({"Type":'Collection',"TypeOfSearch":typeOfSearch}),
      dataType: "json",
      contentType: "application/json"
      }).success(function() {
        $.ajax({
          url: 'http://127.0.0.1:8888/GetTableTrending',
          type: 'GET',
          }).success(function(response) {
            responseParse = JSON.parse(response);
            var node = document.getElementById('sevenTrending');
            node.innerHTML = '<div class=scrollbox><div class="table-responsive header-fixed" style="text-align:left;height:270px;"><table class="table table-striped "><thead><tr><th>#</th><th>Collection</th></tr></thead><tbody id="collectionTable"></tbody></table></div></div>';
            var node = document.getElementById('collectionTable');
            var htmlTableInsert = "";
            var index = 1;
            responseParse.forEach(element => {
              htmlTableInsert += "<tr>" +
              "<td class='col-md-1'>"+index+"</td>" +
              "<td class='col-md-8'>"+element['col1']+"</td>" +
              "</tr>"
              index++;
            });
            node.innerHTML = htmlTableInsert;
          });
    });
  });

  //Inchare of retrieving the recommended data
  $.ajax({
    url: 'http://127.0.0.1:8888/GetRecommendedData',
    method: 'GET',
    }).success(function(response) {
      responseParse = JSON.parse(response);
      songTable = responseParse['songs'];
      artistTable = responseParse['artists'];
      collectionTable = responseParse['collections'];
      var songNode = document.getElementById('songSlideRows');
      var artistNode = document.getElementById('artistSlideRows');
      var collectionNode = document.getElementById('collectionSlideRows');
      var htmlTableInsert1 = "";
      console.log(songTable);
      for (let index = 0; index < songTable.length; index++) {
        const element = songTable[index];
        console.log(element);
        htmlTableInsert1 += "<li>"
        if(element[3] == 1){
          htmlTableInsert1 += "<h1 class='panel__textHeader'>&nbsp;<i class='fa fa-check fa-1x' style='color:#1a1a1a;' aria-hidden='true'></i>&nbsp;&nbsp;"+element[0]+"</h1>"
        }
        else{
          htmlTableInsert1 += "<h1 class='panel__textHeader' id='AddToPlaylist"+element[5]+"'>&nbsp;<a href=# class='AddToPlaylist' data-tooltip='Add to Playlist'><i class='fa fa-plus-square-o fa-lg' style='color:#1a1a1a;' aria-hidden='true'></i></a>&nbsp;&nbsp;"+element[0]+"</h1>"
        }
        htmlTableInsert1 += "<h1 class='panel__text'>&nbsp;Average Rating:&nbsp;"+element[6]+"</h1>" +
        "<h1 class='panel__text'>&nbsp;Collection:&nbsp;"+element[1]+"</h1>" +
        "<h1 class='panel__text'>&nbsp;Artist:&nbsp;"+element[2]+"&emsp;&emsp;Release Date:&nbsp;"+element[8]+"&emsp;&emsp;Genre:&nbsp;"+element[7]+"&emsp;&emsp;Price:&nbsp;"+element[9]+"$</h1>"+
        "<h1 class='panel__text'><audio controls>"+
        "<source src='"+element[4]+"' type='audio/ogg'></audio></h1>"+
        "</li>"
      }
      songNode.innerHTML = htmlTableInsert1;

      var htmlTableInsert2 = "";
      artistTable.forEach(element => {
        htmlTableInsert2 += "<li>" +
        "<h1 class='panel__textHeader__Small'>&nbsp;"+element[0]+"</h1>"+
        "<h1 class='panel__text__Small'>&nbsp;Average Rating::&nbsp;"+element[1]+"&emsp;&emsp;Genre:&nbsp;"+element[2]+"</h1>" +
        "</li>"
      });
      artistNode.innerHTML = htmlTableInsert2;

      var htmlTableInsert3 = "";
      collectionTable.forEach(element => {
        htmlTableInsert3 += "<li>" +
        "<h1 class='panel__textHeader__Small'>&nbsp;"+element[0]+"</h1>" +
        "<h1 class='panel__text__Small'>&nbsp;Artist:&nbsp;"+element[2]+"</h1>" +
        "<h1 class='panel__text__Small'>&nbsp;Release Date:&nbsp;"+element[3]+"&emsp;&emsp;Genre:&nbsp;"+element[4]+"&emsp;&emsp;Price:&nbsp;"+element[1]+"$</h1>" +
        "</li>"
      });
      collectionNode.innerHTML = htmlTableInsert3;
      
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
      title: 'Here you can edit your profile!',
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
