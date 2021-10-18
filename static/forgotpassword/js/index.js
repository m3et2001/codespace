function maleBlue() {
  $('#set-male').val('Male')
  $('#set-female').val('')
  console.log($('#set-male').val())
  const male = document.getElementsByClassName("male")[0];
  const female = document.getElementsByClassName("female")[0];
  const maleBtn = document.getElementsByClassName("male-blue")[0];
  const femaleBtn = document.getElementsByClassName("female-blue")[0];

  male.style.backgroundColor = "#2867b2";
  maleBtn.style.backgroundColor = "#2867b2";
  maleBtn.style.color = "white";

  female.style.backgroundColor = "#f1f1f1";
  femaleBtn.style.backgroundColor = "#f1f1f1";
  femaleBtn.style.color = "grey";
}
function femaleBlue() {
  
  $('#set-female').val('Female')
  $('#set-male').val('')
  console.log($('#set-female').val())
  const male = document.getElementsByClassName("male")[0];
  const female = document.getElementsByClassName("female")[0];
  const maleBtn = document.getElementsByClassName("male-blue")[0];
  const femaleBtn = document.getElementsByClassName("female-blue")[0];

  female.style.backgroundColor = "#2867b2";
  femaleBtn.style.backgroundColor = "#2867b2";
  femaleBtn.style.color = "white";

  male.style.backgroundColor = "#f1f1f1";
  maleBtn.style.backgroundColor = "#f1f1f1";
  maleBtn.style.color = "grey";
}

// updated script for label

function showFNLbl() {
  first_name_lbl = document.getElementsByClassName("fn__label")[0];
  first_name_lbl.style.display = "block";
  document.getElementsByName("first")[0].placeholder = " ";
}

function showLNLbl() {
  last_name_lbl = document.getElementsByClassName("ln__label")[0];
  last_name_lbl.style.display = "block";
  document.getElementsByName("last")[0].placeholder = " ";
}

function showPhoneLbl() {
  phone_lbl = document.getElementsByClassName("phone__label")[0];
  phone_lbl.style.display = "block";
  document.getElementsByName("phone")[0].placeholder = " ";
}

function showEmailLbl() {
  email_lbl = document.getElementsByClassName("email__label")[0];
  email_lbl.style.display = "block";
  document.getElementsByName("email")[0].placeholder = " ";
}

function showCityLbl() {
  city_lbl = document.getElementsByClassName("city__label")[0];
  city_lbl.style.display = "block";
  document.getElementsByName("city")[0].placeholder = " ";
}

function showStateLbl() {
  state_lbl = document.getElementsByClassName("state__label")[0];
  state_lbl.style.display = "block";
  document.getElementsByName("state")[0].placeholder = " ";
}

function showRegionLbl() {
  region_lbl = document.getElementsByClassName("region__label")[0];
  region_lbl.style.display = "block";
  document.getElementsByName("region")[0].placeholder = " ";
}

function showPasswordLbl() {
  password_lbl = document.getElementsByClassName("password__label")[0];
  password_lbl.style.display = "block";
  document.getElementsByName("password")[0].placeholder = " ";
}

function showConfirmPasswordLbl() {
  confirm_password_lbl = document.getElementsByClassName(
    "confirm_password__label"
  )[0];
  confirm_password_lbl.style.display = "block";
  document.getElementsByName("confirm_password")[0].placeholder = " ";
}

function showConfirmUsernameLbl() {
  username_lbl = document.getElementsByClassName("username__label")[0];
  username_lbl.style.display = "block";
  document.getElementsByName("username_password")[0].placeholder = " ";
}

function showBirthdayLbl() {
  birthday_lbl = document.getElementsByClassName("birthday__label")[0];
  birthday_lbl.style.display = "block";
  document.getElementsByName("birthday")[0].placeholder = " ";
  document.getElementsByClassName("birthday__label")[0].style.marginBottom =
    "-6px";
}
