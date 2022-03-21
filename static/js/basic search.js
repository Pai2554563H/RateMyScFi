document.getElementsByTagName("input")[0].focus();
// get elements from html page
var oId=document.getElementById("moovie_list");
var aLi=getbyclass("movie_container",oId);



document.onkeyup=function(e){
    // user input to search
    var str=document.getElementsByTagName("input")[0].value;
    
    if(str.length>0){
    // search input
    var re=new RegExp(str,'gi');
    
    for(var i=0;i<aLi.length;i++){
        var t=aLi[i].innerText||aLi[i].textContent;

        if(re.test(t)){
            aLi[i].style.display="block";
        }else{
            aLi[i].style.display="none";
        }
    }
    }

    if(document.activeElement.type=='text'){
        if(str.length==0){
        location.reload(false);
        }
    }
}

// get whole block of data
function getbyclass(oClass,Oparent){
    var oParent=oParent||document;
    if(Oparent.getElementsByClassName){
        return Oparent.getElementsByClassName(oClass)
    }else{
        var re=[];
        var reg=new RegExp("\\b"+oClass+"\\b")
        var ch=oParent.getElementsByTagName("div");
        for(var i=0;i<ch.length;i++){
            var str=ch[i].className;
            if(reg.test(str)){
                re.push(ch[i]);
            }    
        }
        return re;
    }
}