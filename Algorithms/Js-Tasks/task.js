//Emr 01 - Ekranın arxa fon rəngini dəyiş.

function changeBackColor(){
document.querySelector('html').setAttribute('style', 'background-color: blue');
}

//Emr 02 - Başlığın rəngini dəyişin.

function changeHeadColor(){
    document.querySelector('h1').setAttribute('style', 'color: red');
}

//Emr 03 - Mətnin rəngini dəyişin

function changeTextColor(){
   let x =  document.querySelectorAll('p, li');
   let i;
    for(let i=0;i<x.length;i++){
        x[i].style.color = 'green';
    }
}

//Emr 04 - Mətnin daxilində neçə hərf olduğunu nəticə ifadəsinin qarşısında göstərsin.
/*function looksUp() { 
   var word = document.getElementById('demo').value;
   var count = 0;
   var x = word.x("");
   for(i = 0; i<x.length; i++){
       if (x[i] != ""){
           count+=1
       }
   }
   document.getElementById('demo').innerHTML = count;
  }
  */

  let say = [];
  function looksUp(){
      let x=document.querySelector('.card p').innerHTML
      return this.length
  }
  



//Emr 05 - Mətnin daxilində neçə söz olduğunu nəticə ifadəsinin qarşısında göstərsin

//Emr 06 - Mətnin daxilində proqramçı sözünün olub olmadığını nəticə ifadəsinin qarşısında göstərsin


//Emr 07 - Şəklin ətrafına çərçivə əlavə edilsin.

function addBorder(){
    document.querySelector('img').setAttribute('style','border: 1px solid yellow');
}

//Emr 08 - Şəkli Bu şəkil ilə əvəz edin.

function changeImg(){
    document.querySelector('img').setAttribute('src', 'images/book.jpeg')

}