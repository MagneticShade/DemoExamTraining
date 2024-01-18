let login:HTMLInputElement =<HTMLInputElement> document.getElementById("login_login")
let password:HTMLInputElement=<HTMLInputElement>document.getElementById("password_login")

document.getElementById("login").addEventListener("submit",(e)=>{
    e.preventDefault()
    let obj={"login":`${login.value}`,"password":`${password.value}`}

    fetch("http://127.0.0.1:8000/login/",{
        method:"POST",
        body:JSON.stringify(obj),
        headers: {
            "Content-type": "application/json"
        }
    }).then((res)=>{
        if(res.redirected){
            document.location=res.url
        }
    })

} )