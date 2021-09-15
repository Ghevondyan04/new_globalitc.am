
// =====================================================================================================================
let include_obj=[
    {
        name:`Շաբաթական անձնական խորհրդատվություններ մենթորի հետ`,
        img:"./front-img/Group 1.svg",
    },
    {
        name:"24 խմբակային պրակտիկ դասընթացներ մենթորի հետ",
        img:"./front-img/Group 2.svg",
       
    },
    {
        name:"96 Վիդեոկուրսեր ",
        img:"./front-img/Group 3.svg",
    },
    {
        name:"5 մեծ սեմինարներ դասախոսների հետ",
        img:"./front-img/Group 4.svg",
    },
    {
        name:"5 մեծ ավարտական պռոեկտներ",
        img:"./front-img/Group 5.svg",
    },
    {
        name:"Դուք 6 ամսից ավարտում եք կուրսը և կարող եք արդեն սկսել ձեր կարիերան",
        img:"./front-img/Group 6.svg",
    },
]
let include_obj_2=[
    {
        name:`Մենք շուկայում ենք 2017 թվականից։ Այսօր 
        մենք զբաղվում ենք բազմաթիվ աշակերտների
        մասնագիտական կրթությամբ և ունենք բազում ավարտած ուսանողներ որոնք գտել են իրենց տեղը շուկայում։
        `,
        img:"./front-img/Group item1.svg",
        txt:"Փորձառու Մասնագետներ"
       
    },
    {
        name:"Ոչ մի անհետաքրքիր և ոչ էֆեկտիվ դասընթացներ։ GLOBAL IT - ում դասընթացները անցկացվելու են այնպիսի միջավայրում, որ ոչ մի վարկյան ձանձրալի չթվա։",
        img:"./front-img/Groupitem2.svg",
        txt:"Ընտանեկան Միջավայր"
       
    },
    {
        name:"Մենք շատ խիստ ենք վերաբերվում ուսուցման որակին և դրանով իսկ ապահովում ձեր բարձորակ ուսուցումը։ Դուք կունենաք անձնական մենթոր ով կուղեքցի ձեզ ամբողջ դասընթացի ընթացքում։",
        img:"./front-img/Groupitem3.svg",
        txt:"Լավագույն Մենթոդները "
    },
]

//================================================================================================================================
let item_front=document.getElementById("item_front");
let item_inc=document.getElementById("item_inc");
let leson_front= document.getElementById("leson_front")


//// =====================================================================================================================
include_obj.map(item=>{
    item_inc.innerHTML+=`
    <div class="item_f item_in"">
               <img src="${item.img}" alt="f1">
               <p>${item.name}</p>
      </div>
    `
})




// =====================================================================================================================
let program=document.getElementById("col1")
let col2 =  document.getElementById("col2");


// =====================================================================================================================
let colx=document.getElementById('colx')


// =====================================================================================================================
function VideoX(el){

  let vido_ob1 =document.querySelectorAll(".vido_ob1")
  for(let i=0; i<vido_ob1.length; i++){
   vido_ob1[i].classList.remove("vid-2-onclick")
   vido_ob1[i].pause();
  }

	var kids1 = document.getElementById('stag0').children;
	for(var i = 0; i <kids1.length; i++){
        kids1[i].className = "v_l";

    }
    el.className='class2' 
    el.nextElementSibling.classList.add("contx_x")
    
  }
  function VideoX1(el){

    let vido_ob1 =document.querySelectorAll(".vido_ob1")
    for(let i=0; i<vido_ob1.length; i++){
     vido_ob1[i].classList.remove("vid-2-onclick")
     vido_ob1[i].pause();
    }
  
    var kids1 = document.getElementById('stag1').children;
    for(var i = 0; i <kids1.length; i++){
          kids1[i].className = "v_l";
  
      }
      el.className='class2' 
      el.nextElementSibling.classList.add("contx_x")
      
    } 
// =====================================================================================================================
let x=true;

function addClass(a){
  let vido_ob1 =document.querySelectorAll(".col1_1")
  for(let i=0; i<vido_ob1.length; i++){
   vido_ob1[i].lastElementChild.lastElementChild.classList.remove("plus")
  }

   btn =  a.nextElementSibling
   btn.classList.add('plus')
  
 
}


let item_inc_2=document.getElementById('item_inc_2')
include_obj_2.map(item=>{
    item_inc_2.innerHTML+=`
    <div class="item_f item_in"">
               <img src="${item.img}" alt="f1">
               <h4>${item.txt}</h4>
               <p>${item.name}</p>
      </div>
    `
})



function ActivLog1(el){
  var kids1 = document.getElementById("log-ul-1").children;
	 for(var i = 0; i <kids1.length; i++){
        kids1[i].className = "";
    }
    el.className='clsss_li_log' 
}
function ActivLog2(el){
  var kids1 = document.getElementById("log-ul-2").children;
	 for(var i = 0; i <kids1.length; i++){
        kids1[i].className = "";
    }
    el.className='clsss_li_log' 
}
function ActivLog3(el){
  var kids1 = document.getElementById("log-ul-3").children;
	 for(var i = 0; i <kids1.length; i++){
        kids1[i].className = "";
    }
    el.className = 'clsss_li_log' 
}

let set=false;
function SetComent(){
  let studentx = document.getElementById('student')
  let p_st=document.getElementById('p-St')
  console.log(p_st)
   if(set==false){
       studentx.classList.add('setAll')
       set=true;
       p_st.innerHTML=`Թաքցնել`
   }
   else{
     studentx.classList.remove('setAll');
     p_st.innerHTML=`Դիտել Ավելին`
     set=false;
   }
}

function VideoBlog(){
    let vid=document.getElementById("Vid2")
     vid.classList.add("vid-2-onclick")
     document.getElementById('play-id').classList.add('play-id-onclinc')
}
function VideoBlog1(el){  
    
    let vido_ob1 =document.querySelectorAll(".vido_ob1")
     for(let i=0; i<vido_ob1.length; i++){
      vido_ob1[i].classList.remove("vid-2-onclick")
      vido_ob1[i].pause();
     }
    el.nextElementSibling.classList.add("vid-2-onclick");
    el.nextElementSibling.classList.remove("poxos");
}