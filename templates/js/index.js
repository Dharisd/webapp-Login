$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
   )
});


$(document).ready(function(){
$('#sgnup').click()(function(){
    console.log("click")
    user = $("#username").val()
    pass = $("#password").val()
    if ((user  || pass) != ""){
        fetch("/signup",{
            method: "POST",
            headers:{'Content-Type':'application/x-www-form-urlencoded',},
            body: "user="+user+"&pass="+pass

        })
    }
    else{
        alert("please fill the fields")
    }

})
})