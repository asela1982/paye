
function validateForm(){
    var fields = ["incomeInput"]
  
    var i, l = fields.length;
    var fieldname;
    for (i = 0; i < l; i++) {
      fieldname = fields[i];
      if (document.forms["application"][fieldname].value === "") {
        alert(fieldname + " can not be empty");
        return false;
      }
    }
    return true;
  };
  