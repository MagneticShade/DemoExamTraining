let table:HTMLTableElement=<HTMLTableElement> document.getElementById("adminTable")
let id=localStorage.getItem("id")
if (id) {
    generateTable(id)
}
async function generateTable(id) {

   let roles = await fetch(`http://127.0.0.1:8000/roles`, {
    }).then(res=>{
        return res.json()
    }).then(data=>{
        return data
    })

    fetch(`http://127.0.0.1:8000/admin/users`, {
        headers: {
            'ADMIN-ID': `${id}`,
        }
    }).then(res => {
        return res.json()
    }).then(data => {
        for (let elem of data) {
            let line: HTMLTableRowElement = document.createElement("tr")
            let userLogin: HTMLTableCellElement = document.createElement("td")
            userLogin.textContent = elem.login
            line.appendChild(userLogin)
            let role : HTMLTableCellElement = document.createElement("td")
            let droplist :HTMLSelectElement = document.createElement("select")
            generateOptions(roles,elem.role_id,id,droplist,elem.id)
            line.appendChild(role)
            role.appendChild(droplist)
            table.appendChild(line)
        }
    })
}

function generateOptions(roles,id,admin_id,parent:HTMLSelectElement,user_id){
    let option:HTMLOptionElement
    for( let record of roles){
        option=document.createElement("option")
        option.value=record.id
        if( record.id==id){
            option.selected=true
        }
        option.textContent=record.role_name
        parent.appendChild(option)

    }
    parent.addEventListener("change",function () {
        fetch(`http://127.0.0.1:8000/admin/role/`, {
            method:"PATCH",
            headers: {
                'ADMIN-ID': `${admin_id}`,
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({"id":user_id,"role_id":parent.value})
        })
    })
}