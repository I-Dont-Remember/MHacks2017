$(document).ready(function() {


    $("#login-button").click(function(event){
        console.log("submitting login form")
        event.preventDefault();

        //AJAX CALL TO LOGIN, response is RESPONSE

        var RESPONSE = false;
        if (RESPONSE == true) {
            //login success, do animation
            $('form').fadeOut(500);
            $('.wrapper').addClass('form-success');

            //wait for animation then go to account page
            setTimeout(function(){
                $(".container").fadeOut(1000);
                location.href = "account.html";
            }, 1000);
        } else {
            //login failed
            var NO_MATCHING_USER = true;
            if (NO_MATCHING_USER) {
                $("#error").css('visibility', 'visible')
                $("#error").attr("value","Username incorrect");
            } else if (WRONG_PASSWORD) {
                $("#error").css('visibility', 'visible')
                $("#error").attr("value","Password incorrect");
            } else {
                $("#error").css('visibility', 'visible')
                $("#error").attr("value","Login failed");
            }
        }
    });

    $("#sign-up-button").click(function(event){
        console.log("submitting sign up form")
        event.preventDefault();

        $('form').fadeOut(500);
        $('.wrapper').addClass('form-success');

        //AJAX CALL TO CREATE ACCOUNT, response is RESPONSE

        var RESPONSE = true;
        if (RESPONSE == true) {
            //login success, wait for animation then go to account page
            setTimeout(function(){
                $(".container").fadeOut(1000);
                location.href = "account.html";
            }, 1000);
        } else {
            //login failed

        }
    });


});