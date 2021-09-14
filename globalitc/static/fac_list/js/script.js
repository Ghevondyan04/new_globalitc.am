let a=false

let items_obj=[
    {name:"Front End Ծրագրավորում",
     img:"./item-img/item1.svg"
    },
    {name:"Back End Ծրագրավորում",
     img:"./item-img/item2.svg"
    },
    {name:"Full Stack Ծրագրավորում",
     img:"./item-img/item3.svg"
    },
    {name:"Ruby",
     img:"./item-img/item4.svg"
    },
    {name:"PHP",
     img:"./item-img/item5.svg"
    },
    {name:"Python (Django)",
     img:"./item-img/item6.svg"
    },
    {name:"Java Script",
     img:"./item-img/item7.svg"
    },
    {name:"Վեբ Դիզայն",
     img:"./item-img/item8.svg"
    },
]
let items_obj2=[
    {name:"Unity",
     img:"./item-img/Unity_Logo.jpg"
    },
    {name:"Java",
     img:"./item-img/java_228.jpg"
    },
    {name:"AI",
    img:"./item-img/adobe.jpg"
    },
    
    {name:"AR/VR",
    img:"./item-img/Virtual_Reality_Logo.jpg"
    },
    {name:"C++",
    img:"./item-img/C++_Logo.svg"
    },
    {name:"C#",
    img:"./item-img/C-Sarp.svg"
    },
    {name:" Android",
     img:"./item-img/Android.jpg"
    },
    {name:"Django",
     img:"./item-img/django-logo.jpg"
    },
]

let items_obj3=[
    {name:"Cinema 4D",
    img:"./item-img/CD.jpg"
    },
    {name:"Autodesk 3D Max",
    img:"./item-img/AD3.jpg"
    },
    {name:"Autodesk Autocad",
     img:"./item-img/AA.jpg"
    },
    {name:"Adobe Illustrator",
     img:"./item-img/adobe.jpg"
    },
    {name:"Adobe Photoshop",
    img:"./item-img/Ps1.svg"
    },
    {name:"Adobe Premier Pro",
    img:"./item-img/Pr.jpg"
    },
    
    {name:"Corel Draw",
    img:"./item-img/CCsvg.svg"
    },
   
    {name:"Autodesk Maya",
    img:"./item-img/Am.jpg"
    },
]

let items_objx=[];


let web= document.getElementById("web")
let it= document.getElementById('it')
let multi= document.getElementById('multi')

let arr=[web,it,multi];

function AddClass(id){
    for(let i=0;i<arr.length;i++){
        if(arr[i].id==id){
            arr[i].classList.add('active');
            if(id=='web'){
                arr[i].classList.add('webx');
            }
            if(id=='it'){
                arr[i].classList.add('itx');
            }
            if(id=='multi'){
                arr[i].classList.add('multix');
            }
        }
        else{
            arr[i].classList.remove('active');
            if(id!='web'){
                arr[i].classList.remove('webx');
            }
            if(id!='it'){
                arr[i].classList.remove('itx');
            }
            if(id!='multi'){
                arr[i].classList.remove('multix');
            }
        }
    }
    if(id=="it"){
        InerItems(items_obj2)
    }
    if(id=="web"){
        InerItems(items_obj)
    }
    if(id=="multi"){
        InerItems(items_obj3)
    }
}

let items=document.getElementById('container')
function InerItems(itemx){
itemx.map((item,index) =>{
})
}
InerItems(items_obj);
let contx=document.querySelector('#img-goop')   
let cont2=document.querySelector('#Facultiesgroop')
let cont2_1=document.getElementById("cont2")

// ============= ashxatume clikov===================

//  contx.addEventListener('click', ()=>{
//     if(a==false)
//     {
//      contx.src="./item-img/Vector (3).svg" 
//      cont2.classList.add("chekgroop")
//       a=true;
//     }
//     else{
//         contx.src="./item-img/Vector (4).svg" 
//         a=false;
//         cont2.classList.remove("chekgroop")
//     }
//     cont2_1.onmouseleave = function(){
//         contx.src="./item-img/Vector (4).svg" 
//         a=false;
//         cont2.classList.remove("chekgroop")
//     }
//     cont2_1.onmousemove = function(){
//         contx.src="./item-img/Vector (3).svg" 
//         a=true;
//         cont2.classList.add("chekgroop")
//     }
  
// })
// ===================================================

contx.onmouseleave = function(){
    contx.src="./item-img/Vector (4).svg" 
    a=false;
    cont2.classList.remove("chekgroop")
}
contx.onmousemove = function(){
    contx.src="./item-img/Vector (3).svg" 
    a=true;
    cont2.classList.add("chekgroop")
}
cont2.onmouseleave = function(){
    contx.src="./item-img/Vector (4).svg" 
    a=false;
    cont2.classList.remove("chekgroop")
}
cont2.onmousemove = function(){
    contx.src="./item-img/Vector (3).svg" 
    a=true;
    cont2.classList.add("chekgroop")
}
cont2_1.onmouseleave = function(){
    contx.src="./item-img/Vector (4).svg" 
    a=false;
    cont2.classList.remove("chekgroop")
}
cont2_1.onmousemove = function(){
    contx.src="./item-img/Vector (3).svg" 
    a=true;
    cont2.classList.add("chekgroop")
}
 

let r1=document.querySelectorAll(".r1")

function Checked(id){
    debugger;
    console.log(id)
    if(id == "radio-5"){
        InerItems(items_obj2)
    }
    if(id=="radio-4"){
        InerItems(items_obj)
    }
    if(id=="radio-6"){
        InerItems(items_obj3)
    }
  for(let i=0; i<r1.length;i++){
     if(r1[i].checked){
      let t = document.querySelector(`#p${i+3}`)
       t.classList.add("white")
     }
     else{
      let d = document.querySelector(`#p${i+3}`)
       d.classList.remove("white");
     }
   }
}
for(let i=0; i<r1.length;i++){
    if(r1[i].checked){
      let t = document.querySelector(`#p${i+3}`)
       t.classList.add("white")
    }
    else{
      let d = document.querySelector(`#p${i+3}`)
       d.classList.remove("white");
    }
}

let r2=document.querySelectorAll(".r-1")

function Checked1(id){
  for(let i=0; i<r2.length;i++){
     if(r2[i].checked){
      let t = document.querySelector(`#p${i}`)
       t.classList.add("white")
     }
     else{
      let d = document.querySelector(`#p${i}`)
       d.classList.remove("white");
     }
   }
}
for(let i=0; i<r2.length;i++){
    if(r2[i].checked){
      let t = document.querySelector(`#p${i}`)
       t.classList.add("white")
    }
    else{
      let d = document.querySelector(`#p${i}`)
       d.classList.remove("white");
    }
}
