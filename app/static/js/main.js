
$(document).ready(function() {
  
  $('.signup-form input#inputEmail3').popover({
    'animation': true,
    'content': 'Required. Must be a valid email address.',
    'placement': 'right',
    'trigger': 'focus',
  });
  $('.signup-form input#inputUsername3').popover({
    'animation': true,
    'content': 'Required. Must be at least 3 characters long.',
    'placement': 'right',
    'trigger': 'focus',
  });
  $('.signup-form input#inputPassword3').popover({
    'animation': true,
    'content': 'Required. Must be at least 5 characters long.',
    'placement': 'right',
    'trigger': 'focus',
  });
  $('.signup-form input#inputConfirmPassword3').popover({
    'animation': true,
    'content': 'Required. Must be the same as the above password.',
    'placement': 'right',
    'trigger': 'focus',
  });

  var signupButtonInt = setInterval(setSignupButton, 500);

  $('.signup-form').validate({
    showErrors: function(error, element) {
    },
    rules: {
      email: {
        required: true,
        checkEmail: true
      },
      username: {
        required: true,
        checkUser: true
      },
      password: {
        required: true,
        checkPass: true
      },
      confirmpassword: {
        required: true,
        confirmPass: true
      }
    }
  });
});

jQuery.validator.addMethod('checkEmail', function(value, element) {
  var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  var $form = $('.signup-form .form-group:nth-of-type(1)');
  if (!re.test(value) || value.length == 0) {
    $form.addClass('has-error');
    $form.removeClass('has-success');
  }
  else {
    $form.addClass('has-success');
    $form.removeClass('has-error');
  }
}, '');
jQuery.validator.addMethod('checkUser', function(value, element) {
  var $form = $('.signup-form .form-group:nth-of-type(2)');
  if (value.length < 3) {
    $form.addClass('has-error');
    $form.removeClass('has-success');
  }
  else {
    $form.addClass('has-success');
    $form.removeClass('has-error');
  }
}, '');
jQuery.validator.addMethod('checkPass', function(value, element) {
  var $form = $('.signup-form .form-group:nth-of-type(3)');
  if (value.length < 5) {
    $form.addClass('has-error');
    $form.removeClass('has-success');
  }
  else {
    $form.addClass('has-success');
    $form.removeClass('has-error');
  }
}, '');
jQuery.validator.addMethod('confirmPass', function(value, element) {
  var $form = $('.signup-form .form-group:nth-of-type(4)');
  if (value != $('.signup-form input#inputPassword3').val() || $('.signup-form input#inputConfirmPassword3').val().length == 0) {
    $form.addClass('has-error');
    $form.removeClass('has-success');
  }
  else {
    $form.addClass('has-success');
    $form.removeClass('has-error');
  }
}, '');

function setSignupButton() {
  var email = $('.signup-form .form-group:nth-of-type(1)').hasClass('has-success');
  var user = $('.signup-form .form-group:nth-of-type(2)').hasClass('has-success');
  var pass = $('.signup-form .form-group:nth-of-type(3)').hasClass('has-success');
  var confirmPass = $('.signup-form .form-group:nth-of-type(4)').hasClass('has-success');

  if (email && user && pass && confirmPass && checkSignupLengths()) {
    $('#signup-button').removeClass('disabled');
  }
  else {
    $('#signup-button').addClass('disabled');
  }
}

function checkSignupLengths() {
  var formgroups = $('.signup-form .form-group');
  for (var i = 1; i <= formgroups.length; i++) {
    var input = $('.signup-form .form-group:nth-of-type(' + i + ') input');
    if (input.val().length == 0) {
      return false;
    }
  }
  return true;
}
