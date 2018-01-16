$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
   $("#response").hide(); 
   //console.log(window.location.search)
   
});

function get_param(url){
    if (url != null){
        var c = url.split("?");
        var furl = c[1].split("=");
        return furl
    }


}
$(document).ready(function(){
    url = window.location.search
    console.log(url)
    if (url != ""){
        param = get_param(url)
        if ((param[0] == "error") && (param[1] == "incorrect")){
            $("#response").html("Invalid password or username")
            $("#response").show();
        }
    }
    
})




$(document).ready(function(){
    
$("#login").submit(function(event){
    user = $("#user").val()
    pass = $("#pass").val()
    if ((user &&  pass ) != ""){
        console.log("sent")
        
    }
    else{
        event.preventDefault();
        $("#response").html("please fill all fields")
        
    }

})
})


$(document).ready(function(){
    $('#sgnup').click(function(){
    console.log("click")
    user = $("#username").val()
    pass = $("#password").val()
    if ((user  || pass) != ""){
        fetch("/signup",{
            method: "POST",
            headers:{'Content-Type':'application/x-www-form-urlencoded',},
            body: "user="+user+"&pass="+pass

        }).then(function(response){
            return response.text();
        }).then(function(data){
            result = JSON.parse(data)
            if (result == "1"){
                $("#stat").html("account created,you will be redirected soon")
                t1 = window.setTimeout(function(){
                    window.location.replace("/");
                },5000)
            }
        })
    }
    else{
        console.log("invaild for")
        $("#stat").html("please fill all fields")
    }
    

})


})