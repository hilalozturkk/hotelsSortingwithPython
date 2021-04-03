/*let price = 100
let tax= 0.18
let priceTax = price * tax
let total = price + priceTax
console.log(
    "fiyat:",price,
    "kdv oranı:",tax,
    "kdv tutarı:",priceTax,
    "fiyat:",total
    )
  
let counter = 320
counter ++; 
console.log(counter);  

console.log("kalan ürün sayisi:", 18 % 8);

console.log("2üssü4:", 2**4 );

console.log("aşağı yuvarlama",Math.floor(2.9) );

console.log("yukarı yuvarlama",Math.ceil(3.2) );

console.log("yakına yuvarlama",Math.round(1.3) );

let stringNumber = "11"
console.log(stringNumber);
let newNumber = Number(stringNumber)
//Number numaraya çevrien bir fonk. 
console.log(newNumber);

let isActive = false

let userName;
let isUserName = Boolean(userName)

//boolean eğer o değer varsa ve atama yoksa true olarak gelir  

console.log(isActive)//false
//"0" true gelirken 0 false geliyor 
const b = "0";
console.log(Boolean("0"))
console.log(Boolean(1n));
console.log(Boolean(-1n));
console.log(Boolean(Infinity));
console.log(Boolean({}));
console.log(Boolean(Symbol()));
console.log( Boolean(b))

let number1 = "11";
number1 = parseInt(number1);
console.log(number1 + typeof(number1));

let number2 = 55

number2 = number2.toString();

console.log(number2 , typeof(number2));
*//*
let username = "hakan";
const DOMAIN = "kodluyoruz.com";

let email = username + "@" + DOMAIN
//console.log("Mehaba", username,"sitemize hoşgeldin", "mail adresin : " , email)

 let info = `Merhaba ${username} sitemize hoşgeldin... mailin: ${email}
kısa isminiz : ${username[0]}.
mail adresinin uzunlugu: ${email.length}
borcunuz. ${2+3*5}
gunun saat bilgisi : ${new Date().getHours()}
 ` 
console.log(info)*/
let email = "hilal@gmail.com"
let firstName = "hakan"
let lastName = "YALINKAYA"

console.log( email.length )
console.log(firstName[0])
console.log(firstName.charAt(0))
firstName = firstName.toUpperCase()
console.log(firstName)
firstName = firstName.toLowerCase()
console.log(firstName)

console.log(email.search("@"))
console.log(email[5])
console.log(email.search("olmayan"))

console.log(email.slice(0,10))
console.log(email.slice(5))

let DOMAIN =email.slice( email.search("@") + 1)
console.log(DOMAIN)
console.log(DOMAIN.indexOf("."))

console.log(
    DOMAIN.slice(0,DOMAIN.indexOf("."))
    )

email = email.replace("gmail.com","kodluyoruz.org")    
console.log(email)


console.log(email.includes("@"))

console.log(email.endsWith("org"))

let fullName = `
${firstName[0].toUpperCase()}${firstName.slice(1).toLocaleLowerCase()} ${lastName[0].toUpperCase()}${lastName.slice(1).toLocaleLowerCase()}
`

console.log(fullName)

let url = "www.kodluyoruz.org";

url = url.slice(4)
console.log(url)
//console.log(document.URL)
//document.write("merhaaba")
//document.body.style.backgroundColor = "red";
//document.body.style.color="black"

let title = document.getElementById(title)
console.log(title)

let title = document.getElementById("title")
console.log(title.innerHTML)
title.innerHTML = "Değişen bilgi"//html dökümanındada değişti 
console.log(title.innerHTML)

let link = document.querySelector("#aa")//o etikete ulaşıyorsun

console.log(link)
console.log(link.innerHTML)//İNNERhtml ile içindeki yazıyı alıyorum

link.innerHTML += " Değişen"
console.log(link)

link.style.color = "red" //css özellikleride verilebilri
link.classList.add("btn")

console.log(link)
//let uyari = prompt("isminizi girin")//promt ile kullanıcıdan bilgi aldık
//console.log(uyari)
/*
let aa2 = document.querySelector("#aa2")//aa2 selectoru alıp atadık
aa2.innerHTML = `${aa2.innerHTML} <small>${uyari}</small>`  
*//*
let lastChild = document.querySelector("ul#list2>li:last-child")
lastChild.innerHTML = "son öge değiştir"

let firstChild = document.querySelector("ul#list2>li:first-child")
firstChild.innerHTML = "ilk öğe değişti"

let ulDOM = document.querySelector("ul#list2")

let liDOM = document.createElement('li')//li elementi oluşturduk

liDOM.innerHTML = "oluşturdum"//için ebunu yazdık

ulDOM.prepend(liDOM) //ulDOM selektörüne liDOM selektörünü ekledik

let greeting = document.querySelector("#aa2")//aa2 idli selector al

greeting.classList.add("title")//slectore title clası ekeldim
greeting.classList.add("title2")//slectore title clası ekeldim
console.log(greeting.classList)
greeting.classList.remove("title")//slectore title clası sildim
console.log(greeting.classList)


console.log(!!2)*/