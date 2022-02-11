function sendEmail(){
    Email.send({
        Host : "smtp.gmail.com",
        Username : "admin username",
        Password : "password",
        To : 'admin gmail',
        From : document.getElementById('email').value,
        Subject : "This is the subject",
        Body : "Name: " + document.getElementById('name').value
                + "<br> Email: " + document.getElementById('email').value
                + "<br> Email: " + document.getElementById('email').value
                + "<br> Message: " + document.getElementById('message').value
    }).then(
      message => alert("Message Sent Successfully")
    );
}