let form:HTMLFormElement = <HTMLFormElement> document.getElementById("form");
let login:HTMLInputElement=<HTMLInputElement> document.getElementById("login_login");
let password:HTMLInputElement=<HTMLInputElement> document.getElementById("password_login");

form.addEventListener("submit",(e)=>{
  e.preventDefault();
  let object={"login":login.value, "password":password.value}
  fetch("http://localhost:8000/login/",{
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(object)
  })
})