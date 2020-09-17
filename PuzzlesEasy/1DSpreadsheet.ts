//needs improvement
const N: number = parseInt(readline());
const spreadsheet = []
for (let i = 0; i < N; i++) {
    var inputs: string[] = readline().split(' ');
    const operation: string = inputs[0];
    const arg1: string = inputs[1];
    const arg2: string = inputs[2];
    if (operation==="VALUE") {spreadsheet.push(arg1)}
    else {spreadsheet.push({operation, arg1, arg2})}
}

let i=0
while(spreadsheet.some(i=> typeof i !=="number")){
    const input=spreadsheet[i] 
    if (typeof input ==="string")
        spreadsheet[i]=parseInt(input)
    else if (typeof input !=="number"){
        const arg1 = input["arg1"][0]==="$"?spreadsheet[parseInt(input["arg1"].substring(1))]:input["arg1"]
        const arg2 = input["arg2"][0]==="$"?spreadsheet[parseInt(input["arg2"].substring(1))]:input["arg2"]
        if (!isNaN(arg1) && !isNaN(arg2))
        {if (input["operation"]==="ADD") {
            spreadsheet[i]=parseInt(arg1)+parseInt(arg2)
        }
        if (input["operation"]==="SUB") {
            spreadsheet[i]=parseInt(arg1)-parseInt(arg2)
        }
        if (input["operation"]==="MULT") {
            spreadsheet[i]=parseInt(arg1)*parseInt(arg2)
        }}
    }
    i+=1 
    i=i%N
}
spreadsheet.forEach(ans=>console.log(ans))
