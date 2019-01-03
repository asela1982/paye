
function validateFormSalary() {
  var x = document.forms["application"]["incomeInput"].value;

  if (x == "") {
    alert("Gross Income Amount must be filled out");
    return false;
  }
}


function validateFormBonus() {
  var x = document.forms["application"]["incomeInput"].value;
  var y = document.forms["application"]["lumpsumInput"].value;

  if (x == "") {
    alert("Gross Income Amount must be filled out")
    return false
  }
  else if (y == "") {
    alert("Bonus Amount must be filled out")
    return false
  }
} 