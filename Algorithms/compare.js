// 1. iki ededin muqayise olunmasi

/*function compare(a,b){
    if(a>b){
        console.log(`[${a}]-Birinci eded [${b}]-ikinciden boyukdur`)
    }else if(a<b){
        console.log(`[${b}]-Ikinci eded [${a}]-birinciden boyukdur`)
    }else if(a=b){
        console.log(`[${a}]-Birinci ve [${b}]-ikinci ededler beraberdir`)
    }
}

compare(10,5)
*/

// 2. uc ededin muqayise olunmasi

/*function compare (a,b,c){
    if (a>b, a>c){
        console.log(`[${a}] - ededi en boyukdur`)
    }else if (a<b, a<c){
        console.log(`[${a}] - ededi en kicikdir`)
    }else if (b>a, b>c){
        console.log(`[${b}] - ededi en boyukdur`)
    }else if (c>a, c>b){
        console.log(`[${c}] - ededi en boyukdur`)
    }
}
compare(5,10,20)
*/


// 3. ededin musbet,menfi ve ya 0 a beraber olmasini mueyyen etmek
/*
function checknum (a){
    if (a>0) {
        console.log(`[${a}] - ededi musbetdir`)
    }else if (a<0){
        console.log(`[${a}] - ededi menfidir`)
    }else if (a == 0){
        console.log(`[${a}] - ededi sifra beraberdir`)
    }else{
        console.log(false)
    }
}
checknum(0)
*/

// 4. ededin 5-e, 11-e ve ya hec birine bolunmemesi

/*function divNum (a){
    if (a%5 == 0 && a%11 == 0){
        console.log(`[${a}] - ededi 5 ve 11-e tam bolunur`)
    }else if (a%5 == 0){
        console.log(`[${a}] - ededi 5-e tam bolunur`)
    }else if (a%11 == 0){
        console.log(`[${a}] - ededi 11-e tam bolunur`)
    }else{
        console.log(`[${a}] - ededi 5 ve 11-e bolunmur`)
    }
}
divNum(2561487455)
*/

// 5. ededin tek ve ya cut oldugunu yoxlamaq

/*function typeofNum (a){
    if (a%2 == 1) {
        console.log(`[${a}] - ededi tek ededdir`)
    }else {
        console.log(`[${a}] - ededi cut ededdir`)
    }
}

typeofNum(20)
*/

// 6. check if entered year is leap or common year

/*let year = 2020

if (year%4 == 0 && year%100!= 0 //&& year%400 == 0) {
    console.log(`[${year}] - enter year is LEAP YEAR`)
}else{
    console.log(`[${year}] - entered year is COMMON YEAR`)
}
*/