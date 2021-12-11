//prompt() ve alert() metodlarindan istifade

username = prompt("Adinizi daxil edin: ")
password = prompt("Passwordu daxil edin:")

if(username == "admin" && password == "123456"){
    alert("Tebrikler siz sisteme daxil oldunuz")
}else if(username =='' && password == ''){
    alert("Deyerler bosh ola bilmez!")
}else if(username =="admin" && password!=="123456"){
    alert("Username ve ya passwordu sehvdir")
}else if (username!=="admin" && password =="123456"){
    alert("Username ve ya passwordu sehvdir")
}