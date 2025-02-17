class SFIT {
    PID: number;
    constructor(PID:number){
        this.PID = PID
    }
}
class Student_details extends SFIT{
    stud_name: string;
    year: number;
    constructor(PID:number,stud_name: string, year: number) {
        super(PID);
        this.stud_name = stud_name;
        this.year = year
    }
    display():void{
        console.log(this.PID)
        console.log(this.stud_name)
        console.log(this.year)

    }
}

let SFITobj = new Student_details(221068,"Vishal Mahajan", 3)
SFITobj.display()