// sade login yaradilmasi

username = prompt('Adinizi daxil edin: ')
password = prompt('Kodunuzu daxil edin:')

if(username == 'admin' && password == '123456'){
    alert('Xosh gelmisiniz')
}else if(username!= 'admin' && password == '123456'){
    alert('Username i sehv daxil etmisiniz')
}else if(username == 'admin' && password!= '123456'){
    alert('Passwordu sehv yazmisiniz')
}else if(username!= 'admin' && password!='123456'){
    alert('Melumatlar sehvdir')
}