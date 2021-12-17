
function changeImage(x){
    let a = document.querySelectorAll('.small-image img')
    let b = a[x-1].getAttribute('src')
    document.querySelector('.big-image img').setAttribute('src', b)
    
   
   

}