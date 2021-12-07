/* Birinci tapshiriq
prompt() istifadə edərək ad və soyad tələb edin və 
bu daxil edilən məlumatlardan istifadə edərək alert() metodu ilə
 ekrana "Memmed Hesenov sən xoş gəlmisən" formatında yazı çıxarın . 
 Template Literal mövzusu faydalı ola bilər. (Yazılan kodlar ad.js faylında olmalıdır)

//prompt() ve alert() metodlarindan istifade etdim

username = prompt("Adinizi daxil edin: ")
surname = prompt("Soyadinizi daxil edin")

if (username=="admin" && surname == "admin"){
    alert("Memmed Hesenov sən xoş gəlmisən")
}else{
    alert("Yeniden cehd edin")
}
*/

/* Ikinci tapshiriq
prompt vasitəsi ilə istifadəçidən username və password 
tələb olunmalıdır. bu daxil olunan məlumatlara əsasən aşağıdakı işlər görülməlidir
-Əgər username və ya password bos buraxılıbsa ekrana alert 
vasitəsi ilə 'Deyerler bos ola bilmez' yazısı çıxsın
-Əgər username 'admin' ve password '123456'-dirsa ekrana alert vasitesi ile 
'Tebrikler siz sisteme daxil oldugunuz'
-Daxil edilen deyerlerden her hansi biri duz deyilse ona uygun mesaj cixsin. Meselen username duz deyil

//prompt() ve alert() metodlarindan istifade

username = prompt("Adinizi daxil edin: ")
password = prompt("Passwordu daxil edin:")

if(username == "admin" && password == "123456"){
    alert("Tebrikler siz sisteme daxil oldunuz")
}else if(username == '' && password == ''){
    alert("Deyerler bosh ola bilmez!")
}else if(username =="admin" && password!=="123456"){
    alert("Username ve ya passwordu sehvdir")
}else if (username!=="admin" && password =="123456"){
    alert("Username ve ya passwordu sehvdir")
}
*/