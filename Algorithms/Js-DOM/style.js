
function changeImage(x){
    //a deyishenine butun small-img leri massiv sheklinde yaziriq
    let a = document.querySelectorAll('.small-image img')
    //b deyishenine cari sheklin src ni yaziriq
    //cari shekil [x-1] indeksi ile teyin olunur
    let b = a[x-1].getAttribute('src')
    //big-image deki shekilde oxudugumuz src teyin edirik.  
    document.querySelector('.big-image img').setAttribute('src', b)
}