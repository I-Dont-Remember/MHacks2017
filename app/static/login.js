$(document).ready(function() {
  var $username = $("#username");
  var $password = $("#password");
  var login_url = '/login';

    $("#login-button").click(function(event){
        console.log("submitting login form")
        event.preventDefault();

        //AJAX CALL TO LOGIN, response is RESPONSE
        var json_data = {
          'username': $username.val(),
          'password': $password.val()
        };

        $.ajax({
          type: 'POST',
          url: login_url,
          // JSON.stringify is a hack, why doesnt it work without it
          data: JSON.stringify(json_data),
          contentType: 'application/json'
        })
          .done(function(response) {
            console.log('Successfully logged in');
            $('form').fadeOut(500);
            $('#info').fadeOut(500);
            $('.wrapper').addClass('form-success');

            //wait for animation then go to account page
            setTimeout(function(response){
                $(".container").fadeOut(1000);
                location.href = '/user/' + json_data.username;
            }, 1000);
          })
          .fail(function() {
              $("#error").css('visibility', 'visible')
              $("#error").attr("value","Invalid username/password");
          });
          event.preventDefault();
        });

    $("#sign-up-button").click(function(event){
        console.log("submitting sign up form")
        event.preventDefault();

        $('form').fadeOut(500);
        $('#info').fadeOut(500);
        $('.wrapper').addClass('form-success');

        //AJAX CALL TO CREATE ACCOUNT, response is RESPONSE

        var RESPONSE = true;
        if (RESPONSE == true) {
            //login success, wait for animation then go to account page
            setTimeout(function(){
                $(".container").fadeOut(1000);
                location.href = "signup";
            }, 1000);
        } else {
            //sign up failed

        }
    });


});
