let modal:HTMLDialogElement=<HTMLDialogElement>document.getElementById("modal")
let formLogin:HTMLFormElement=<HTMLFormElement>document.getElementById("login")
let formRegis:HTMLFormElement=<HTMLFormElement>document.getElementById("regis")
let close:HTMLButtonElement=<HTMLButtonElement>document.getElementById("close")

formLogin.addEventListener("submit",(e)=>{
    e.preventDefault()
    let data=Object.fromEntries(new FormData(formLogin).entries())
    fetch("http://127.0.0.1:8000/user/login/",{
        method:"POST",
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(data),
    }).then(response=>{
        if (response.ok) {
            return response.json();
        }
        throw new Error();
    }).then(result=>{
        localStorage.setItem("id",result.id)
        window.location=window.location+result.path
    }).catch(e=>{
        modal.showModal()
    })
})

formRegis.addEventListener("submit",(e)=>{
    e.preventDefault()
    let data=Object.fromEntries(new FormData(formRegis).entries())
    fetch("http://127.0.0.1:8000/user/create/",{
        method:"POST",
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(data),
    }).then(response=>{
        if (response.ok) {
            return response.json();
        }
        throw new Error();
    }).then(result=>{
        localStorage.setItem("id",result.id)
        window.location=window.location+result.path
    }).catch(e=>{
        let name:HTMLInputElement =<HTMLInputElement> formRegis.querySelector("#name")
        let login:HTMLInputElement = <HTMLInputElement> formRegis.querySelector("#login_regis")
        let password:HTMLInputElement = <HTMLInputElement> formRegis.querySelector("#password_regis")
        name.value=""
        login.value=""
        password.value=""
    })
})
close.addEventListener("click", (e)=>{
    modal.close()
})