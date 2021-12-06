## Cavablar
- display:flex xüsusiyyətinin əsas neçə alt xüsusiyyəti var və bunlar nə işə yarayır?
-  Flex lə containerin içindəki itemləri rahatlıqla üfüqi və horiontal hərəkət etdirə bilərik. display:flex'in flex-direction, flex-wrap,flex-flow, justify-content, align-items, align-content kimi bir sıra alt xüsusiyyətləri vardır. Flex-direction containerin flex qutuları hansı istiqamətdə yerləşdirməsini müəyyən edir 
- display:grid xüsusiyyətinin alt xüsusiyyətləri hansılardır və qısaca nə işə yaradığını yazın
-  display: grid lə container içərisində asanlıqla sətir və sütun yarada bilərik. Bundan başqa grid-template-columns, grid-template-rows, grid-gap kimi bir sıra alt funksiyalar mövcuddur 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## UI- Lesson11 (Sual-Cavab)
**1.display:inline və display:inline-block arasında fərqlər nədir?**
- display:inline elementi daxili element kimi eyni sırada göstərir. Yerləşdiyi konteynerin mümkün ölçüsü qədər yer tutduğundan sonradan verilən en və uzunluğun elementə heç bir təsiri olmur.
- display:inline-block bunun əksinə ölçüləndirmə olur, margin və padding tətbiq etmək mümkündür və elementi eyni səviyyəli block konteyneri olaraq göstərir.

**2.semantik veb nə deməkdir izah edin.**
- *Semantik veb dedikdə istifadə etdiyimiz və qurduğumuz saytın strukturu tərtibatı başa düşülür.*


**3.HTML taq ve attribute arasındakı fərqlər nələrdir?**
- HTML taqları HTML elementlərinin başlanğıc və bitiş yerini göstərir. Qısacası elementlər taqların içərisində yerləşir. Açar söz rolunu oynayaraq hər bir taqın öz mənası var.
- Atributlar isə HTML elementinin xarakterisitikasını təyin etmək üçün işlədilir. Onlar əlavə məlumat hissəsini təşkil edirlər. Daim başlanğıc taqın içərisində yerləşir və elementlərə əlavə üslub verir.

**4.<!DOCTYPE html> nədir? Nə üçün istifadə edilir?**
-The HTML document type declaration və Doctype brauzerlər tərəfindən verilərək HTMLin hansı versiyasında veb saytın yazıldığını bəyan edir. Bu brauzerlərə  dokumentin necə izah olunmasına köməklik göstərir. Doctype nə element nə də taq olmamaqla yanaşı ən yuxarıda yerləşir.

**5.css-də istifadə olunan inherit və initial ifadələrinin mənasını araşdırın yazın.**
- initial açar sözü verilmiş elementin CSS xüsusiyyətindən özünün ilkin dəyərini(default value) götürməyini təyin edir. Məsələn: <p style="text-align:center"; color: red>This is initial keyword</p> verilsə də CSS də taqa :initial açar sözünün verilməsi şriftin rənginin qırmızı yox ilkin qara rəngdə olmasını təmin edəcək.
- inherit açar sözü elementin öz dəyərini default value yox əksinə valideyndən götürməsini təmin edir.

**5.HTML-in köhnə versiyaları ilə HTML5 arasında ən əhəmiyyətli fərqlər nələrdir?**
- Köhnə versiyalar audio və videonu flash player olmadan dəstəkləmədiyi halda HTML5 <audio> and <video> taqları vasitəsiylə audio və videonu dəstəkləyir.
- Köhnə versiyalar dataları müvəqqəti depolamaq üçün cookies işlədirdisə HTML5 dataları offline depolamaq üçün SQL məlumat bazasından istifadə edir.
- Əvvəlkilər brauzerdə JavaScript işə salmağa qoymurdularsa HTML5 background da işə salmağa icazə verir.
- Əvvəllər drag və drop effectlər işlətmək olmurdusa da indi yenidə artıq mümkündür.
-  Old versiyalarda dairə, dördbucaqlı, üçbucaqlı və s. kimi formalar çəkmək mümkün deyildisə yeni versiya bunlar mümkündür.
-  Köhnə versiyalar bütün köhnə brauzerlərlə işləyir. Ancaq yeni Firefox, Mozilla, Chrome, Safari və s. kimi yeni brauzerlər tərəfindən dəstəklənir.
- HTML5 dili digərlərinə nəzərən daha çox mobil-friendly olmuşdur.



**Javascript haqqında ilkin anlayışlar**

*Javascript* - proqramlaşdırma dilidir. Ona script dil də deyirlər.
İstifadə zamanı comlile a ehtiyacı yoxdur. Brauzerlərlə birgə işləyir.
- Javascript proqramlaşdırma dilini *Java* ilə qarışdırmaq olmaz.
- 1995-ci ildə yaradılıb. İlk adı Moko olmuşdur. Javascript adlandırlımasına səbəb adının geniş  istifadə olunan Java proqramlaşdırma dilinə uyğunlaşdırılaraq popularlaşdırılmasıdır. Etma şirkəti tərəfindən yenilənərək təkmilləşdirilir. 
- *Javascript* düşünüldüyündən daha artıq çoxşaxəlidir. Beləki, ilkin olaraq sadə işlər - _karusellər, qalireyalar,_ eləcə də, buttonlara müxtəlif məzmun və effektlər verməkdə görülsə də, dili dərindən mənimsədikdən sonra *oyunlar, 2D-3D animasiyalı qrafiklər, habelə məlumat bankına əsaslanan apps və bir çox şeyləri onun köməyilə qurmaq olar.* 


**Javascriptin Htmlə əlaqələndirilməsi**

Bunun üçün iki üsul var:

1. Html faylında </body> teqindən əvvəldə <script></script> teqi arasında Javascript kodlarını yazmaq;
2. Əgər .js sonluğu ilə bitən ayrıca JS faylı yaradılıbsa, <script></script> teqi yazılaraq başlanğıc teqin içərisində atributlar verilərilərək fayllar ələqələndirilir.*Məsələn:*
 
 <script type="text/Javascript" language="Javascript" scr="app.js"></script> kimi yazılır.



