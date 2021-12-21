let second = document.querySelector('.scHand');
let minute = document.querySelector('.mnHand');
let hour = document.querySelector('.hrHand');

let scRotate = 0;
let mnRotate = 0;
let hrRotate = 0;


function clock(){
    second.style.transform = `rotate(${scRotate}deg)`
    scRotate += (360/60)
    minute.style.transform = `rotate(${mnRotate}deg)`
    mnRotate+=(360/3600)
    hour.style.transform = `rotate(${hrRotate}deg)`
    hrRotate+= (360/12 *60*60)
}

setInterval(clock, 1000)

