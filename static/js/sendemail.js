function sendMail() {
    var templateParams = {
      from_name: document.getElementById("name").value,
      Email: document.getElementById("emailaddress").value,
      message: document.getElementById("msg").value,
    };
  
    emailjs.send("gmail", "template_besheraj", templateParams).then(
      function (response) {
        alert("Your message has been sent.");
        document.getElementById("name").value = "";
        document.getElementById("msg").value = "";
        document.getElementById("emailaddress").value = "";
      },
      function (error) {
        alert("FAILED... please try again later!");
      }
    );
    return false;
  }