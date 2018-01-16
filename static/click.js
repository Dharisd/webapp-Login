$(document).ready(function(){
    $("#sbmt").click(function(){
        user = $("#username").val();
        password = $("#password").val();
        if ((user == "" && password== "") || (user == "" || password== "")){
            alert("please fill the fields")
        } 
        else{
            console.log("sending")
        } 
    })
})