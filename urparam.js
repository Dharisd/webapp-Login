


function get_param(url){
    var c = url.split("?");
    var furl = c[1].split("=");
    return furl
}

var error = get_param("?error=incorrect")
console.log(furl[0])