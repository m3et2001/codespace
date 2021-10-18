// updated script for label

function showAllFields() {
  email_lbl = document.getElementsByClassName("email__label")[0];
  password_lbl = document.getElementsByClassName("password__label")[0];
  email_lbl.style.display = "block";
  password_lbl.style.display = "block";
  document.getElementsByName("email-phone")[0].placeholder = " ";
  document.getElementsByName("password")[0].placeholder = " ";
}

function showEmailLbl() {
  email_lbl = document.getElementsByClassName("email__label")[0];
  email_lbl.style.display = "block";
  document.getElementsByName("email-phone")[0].placeholder = " ";
}

function ShowPasswordLbl() {
  password_lbl = document.getElementsByClassName("password__label")[0];
  password_lbl.style.display = "block";
  document.getElementsByName("password")[0].placeholder = " ";
}

// script to show and hide password
function showPassword() {
  var x = document.getElementsByName("password")[0];
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
