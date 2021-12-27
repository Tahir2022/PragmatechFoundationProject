function check(){
    let mail=document.getElementById('mail').value; //checking email addres if that contains of '@'
    
    if (mail.indexOf('@')<0){
        alert('You must add "@"')
    }else {
        alert('Correct')
    }
    let phone = document.getElementById('phone').value; // checking number if that starts with '+994' and consists of 13 figures
    if (phone.includes('+994') && phone.length == '13') {
        document.write('Please add "+994" at begining and number must consist of 13')
    }else{
        alert('Correct')
    }

    /*let birthday = document.getElementById('birthday').value; Find out if entered birthday date not elder than 15 years
    let year = new Date().getFullYear()
    if ('#'){
        alert('small')
    }*/
}