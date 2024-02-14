let table:HTMLTableElement=<HTMLTableElement>document.getElementById("orders")
if(localStorage.getItem("id")){
    fetch(`http://127.0.0.1:8000/commisions/${localStorage.getItem("id")}`).
    then(res=>{
        return res.json()
    }).then(data=>{
        for (let elem of data){
            let line:HTMLTableRowElement=document.createElement("tr")
            for(let key in elem){
                let td:HTMLTableCellElement=document.createElement("td")
                td.textContent=elem[key]
                line.appendChild(td)
            }
            table.appendChild(line)
        }
    })
}