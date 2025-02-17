interface sfit{
    ID: number
}

interface details{
    name: string
    role: string
}

interface student extends sfit, details{
    year: number
}

let studobj = <student>{}

studobj.ID = 221068
studobj.name = "Vishal"
studobj.role = "Student"
studobj.year = 3

console.log("ID of Student is",studobj.ID)
console.log("Name of Student is", studobj.name)
console.log("Role is", studobj.role)
console.log("Year is",studobj.year)