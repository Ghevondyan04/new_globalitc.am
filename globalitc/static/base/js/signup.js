document.getElementById('inner-btn').innerHTML = `

    <div class="signupinnerhtml-2">
    <div class="signup-innerhtml-container-2">
       <button type="button" class="sign-up-registrarion facebook facbook-google-1"  onclick="signup_1()"><img src="../img/student-img.svg" alt=""><p> Ուսանող</p> </button>
       <button type="button" class="sign-up-registrarion google facbook-google-1" onclick="signup_2()"><img src="../img/teacher-img.svg" alt=""><p>Դասախոս</p> </button>
       <button type="button"class="sign-up-registrarion google facbook-google-1"onclick="signup_3()"><img src="../img/hyur.svg" alt=""><p>Հյուր</p> </button>
    </div>
    <div class="signup-innerhtml-container-2">
       <button type="button" href="" class="sign-up-registrarion facebook facbook-google-1"onclick="signup_4()"><img src="../img/university-img.svg" alt=""> <p>Ուս․ հաստատություն</p> </button>
       <button type="button" href="" class="sign-up-registrarion google facbook-google-1"onclick="signup_5()"><img src="../img/finance-img.svg" alt=""><p>Ֆրիլանսեր / Գործատու</p> </button>
       <button type="button" href="" class="sign-up-registrarion google facbook-google-1"onclick="signup_6()"><img src="../img/colective-img.svg" alt=""><p>Գործընկեր</p> </button>
    </div>
</div>
    `
    document.getElementById('b-1').classList.add('btn_color')
    document.getElementById('line-6').classList.add('line-block')
 function btn_1() {
    document.getElementById('b-1').classList.add('btn_color')
    document.getElementById('b-2').classList.remove('btn_color')
    document.getElementById('line-6').classList.add('line-block')
    document.getElementById('line-7').classList.remove('line-block')
    document.getElementById('inner-btn').innerHTML = `

    <div class="signupinnerhtml-2">
    <div class="signup-innerhtml-container-2">
       <button  type="button" class="sign-up-registrarion facebook facbook-google-1" onclick="signup_1()"><img src="../img/student-img.svg" alt=""><p> Ուսանող</p> </button>
       <button type="button" class="sign-up-registrarion google facbook-google-1"onclick="signup_2()"><img src="../img/teacher-img.svg" alt=""><p>Դասախոս</p> </button>
       <button type="button" class="sign-up-registrarion google facbook-google-1"onclick="signup_3()"><img src="../img/hyur.svg" alt=""><p>Հյուր</p> </button>
    </div>
    <div class="signup-innerhtml-container-2">
       <button type="button" class="sign-up-registrarion facebook facbook-google-1"onclick="signup_4()"><img src="../img/university-img.svg" alt=""> <p>Ուս․ հաստատություն</p> </button>
       <button type="button" class="sign-up-registrarion google facbook-google-1"onclick="signup_5()"><img src="../img/finance-img.svg" alt=""><p>Ֆրիլանսեր / Գործատու</p> </button>
       <button type="button" class="sign-up-registrarion google facbook-google-1"onclick="signup_6()"><img src="../img/colective-img.svg" alt=""><p>Գործընկեր</p> </button>
    </div>
</div>
    `
}
let back_1 = document.getElementById('back-1')
back_1.onclick = function() {
   document.getElementById('signup_1').classList.remove('signup-block-onclick')
   document.getElementById('signup_4').classList.add('signup-block-onclick')
   document.getElementById('search').classList.remove('search-hover')
}
let back_2 = document.getElementById('back-2')
back_2.onclick = function() {
   document.getElementById('signup_2').classList.remove('signup-block-onclick')
   document.getElementById('signup_4').classList.add('signup-block-onclick')
   document.getElementById('search').classList.remove('search-hover')
}
let back_3 = document.getElementById('back-3')
back_3.onclick = function() {
   document.getElementById('signup_3').classList.remove('signup-block-onclick')
   document.getElementById('signup_4').classList.add('signup-block-onclick')
   document.getElementById('search').classList.remove('search-hover')
}
let back_4 = document.getElementById('back-4')
back_4.onclick = function() {
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
   document.getElementById('search').classList.remove('search-hover')
   
}
let back_5 = document.getElementById('back-5')
back_5.onclick = function() {
   document.getElementById('signup_6').classList.remove('signup-block-onclick')
   document.getElementById('signup_4').classList.add('signup-block-onclick')
}
let back_6 = document.getElementById('back-6')
back_6.onclick = function() {
   document.getElementById('signup_5').classList.remove('signup-block-onclick')
   document.getElementById('signup_4').classList.add('signup-block-onclick')
}
let back_7 = document.getElementById('back-7')
back_7.onclick = function() {
   document.getElementById('signup_7').classList.remove('signup-block-onclick')
   document.getElementById('signup_4').classList.add('signup-block-onclick')
}
let x_1 = document.getElementById('x')
x_1.onclick = function (){
   document.getElementById('signup_1').classList.remove('signup-block-onclick')
}
let x_2 = document.getElementById('x-2')
x_2.onclick = function (){
   
   document.getElementById('signup_2').classList.remove('signup-block-onclick')
}
let x_3 = document.getElementById('x-3')
x_3.onclick = function (){
   document.getElementById('signup_3').classList.remove('signup-block-onclick')
}
let x_4 = document.getElementById('x-4')
x_4.onclick = function (){
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
}
let x_5 = document.getElementById('x-5')
x_5.onclick = function (){
   document.getElementById('signup_6').classList.remove('signup-block-onclick')
}
let x_6 = document.getElementById('x-6')
x_6.onclick = function (){
   document.getElementById('signup_5').classList.remove('signup-block-onclick')
}
let x_7 = document.getElementById('x-7')
x_7.onclick = function (){
   document.getElementById('signup_7').classList.remove('signup-block-onclick')
}
function signup_1(){
     document.getElementById('signup_3').classList.add('signup-block-onclick')
     document.getElementById('signup_4').classList.remove('signup-block-onclick')
     $("html, body").animate({scrollTop:0},1000)
}
function signup_2(){
   document.getElementById('signup_6').classList.add('signup-block-onclick')
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
   $("html, body").animate({scrollTop:0},1000)
   document.getElementById('search').classList.remove('search-hover')
}
function signup_4(){
   document.getElementById('signup_2').classList.add('signup-block-onclick')
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
   $("html, body").animate({scrollTop:0},1000)
   document.getElementById('search').classList.remove('search-hover')
}
function signup_6(){
   document.getElementById('signup_1').classList.add('signup-block-onclick')
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
   $("html, body").animate({scrollTop:0},1000)
   document.getElementById('search').classList.remove('search-hover')
}

function signup_5(){
   document.getElementById('signup_5').classList.add('signup-block-onclick')
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
   $("html, body").animate({scrollTop:0},1000)
   document.getElementById('search').classList.remove('search-hover')
}
function signup_3(){
   document.getElementById('signup_7').classList.add('signup-block-onclick')
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
   $("html, body").animate({scrollTop:0},1000)
   document.getElementById('search').classList.remove('search-hover')
}
function btn_2()  {
    document.getElementById('b-2').classList.add('btn_color')
    document.getElementById('b-1').classList.remove('btn_color')
    document.getElementById('line-7').classList.add('line-block')
    document.getElementById('line-6').classList.remove('line-block')
    document.getElementById('inner-btn').innerHTML = `

    <div class="signup-inputs-select">
    <input type="text" placeholder="Հեռախոսահամար / Էլ․ փոստ">
    <input type="password" placeholder="Գաղտնաբառ">
    <a href="" class="sign-up-registrarion">Գրանցվել</a>
   </div>
    `
}