class Sfit {
    PID: number;
    constructor(PID:number){
        this.PID = PID
    }
}
class details extends Sfit{
    role: string;
    constructor(PID:number,role: string) {
        super(PID);
        this.role = role;
    }
}

class person extends details{
    name: string;
    constructor (PID:number,role: string, name: string) {
        super(PID, role);
        this.name = name;
    }
    display():void{
        console.log("PID is",this.PID)
        console.log("Role is",this.role)
        console.log("Name of the Person is",this.name)

    }
}
    


const multilevel = new person(221068,"Student","Vishal Mahajan")
multilevel.display()