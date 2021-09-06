let armenia_1_320 = document.getElementById('armenia-1-320')
 armenia_1_320.onclick = function() {
	 
	document.getElementById('body').classList.toggle('body-light')
	
	  if(toggle === true){
		armenia_1_320.src = '../image/dark-font.svg';
		 
	  
	  }
	  else{
		
		  armenia_1_320.src = '../image/light-font.svg';
	  }
   
   
	toggle = !toggle ;
 } ;
 let light = document.getElementById('armenia-1');


light.onclick = function (){
 
  document.getElementById('body').classList.toggle('body-light');
 
    if(toggle === true){
		light.src = '../image/dark-font.svg';
		
	
	}
	else{
		
		light.src = '../image/light-font.svg';
	}
 
 
  toggle = !toggle ;
};
let coll = document.getElementById('coll')

coll.onclick = function () {
  document.getElementById('cool-registration').classList.toggle('cool-registration-on')
  document.getElementById('signup_4').classList.remove('signup-block-onclick')
  document.getElementById('search').classList.remove('search-hover')
}

let coll_on = document.getElementById('coll-registration-hover')
coll_on.onclick = function (){
  document.getElementById('cool-registration').classList.remove('cool-registration-on')
  document.getElementById('signup_4').classList.remove('signup-block-onclick')
  document.getElementById('search').classList.remove('search-hover')
}
let manu_320_open = document.getElementById('manu-320-open')
manu_320_open.onclick = function() {
	document.getElementById('menu-320').classList.toggle('manu-320-onclick-block')
	document.getElementById('signup_4').classList.remove('signup-block-onclick')
	document.getElementById('search').classList.remove('search-hover')
}
let manu_320_open_1 = document.getElementById('door-open-350')
manu_320_open_1.onclick = function() {
	document.getElementById('signup_4').classList.add('signup-block-onclick')
	document.getElementById('signup_1').classList.remove('signup-block-onclick')
	document.getElementById('signup_2').classList.remove('signup-block-onclick')
	document.getElementById('signup_3').classList.remove('signup-block-onclick')
	$("html, body").animate({scrollTop:0},1000)
	document.getElementById('signup_4').classList.remove('signup-block-onclick')
	document.getElementById('search').classList.remove('search-hover')
}
let coll_on_1 = document.getElementById('coll-registration-hover-1')
coll_on_1.onclick = function (){
  document.getElementById('menu-320').classList.remove('manu-320-onclick-block')
  document.getElementById('search').classList.remove('search-hover')
  document.getElementById('signup_4').classList.remove('signup-block-onclick')
}
 let search_on = document.getElementById('search-on')
 search_on.onclick = function () {
   document.getElementById('search').classList.toggle('search-hover')
   document.getElementById('signup_4').classList.remove('signup-block-onclick')
   document.getElementById('cool-registration').classList.remove('cool-registration-on')
 } 
 document.getElementById('armenia').onclick = function () {
   document.getElementById('list-country').classList.toggle('list-country')
 }
 let signup_registration_dor = document.getElementById('sign-up-registration-onclick')
signup_registration_dor.onclick = function () {
	document.getElementById('signup_4').classList.add('signup-block-onclick')
	document.getElementById('signup_1').classList.remove('signup-block-onclick')
	document.getElementById('signup_2').classList.remove('signup-block-onclick')
	document.getElementById('signup_3').classList.remove('signup-block-onclick')
	$("html, body").animate({scrollTop:0},1000)
	document.getElementById('search').classList.remove('search-hover')
}

