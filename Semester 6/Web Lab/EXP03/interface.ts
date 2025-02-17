interface sfit_college{
    PID: number;
    first_name : string;
    last_name : string;
    year : number;
    GetPID():number
    GetName():string
    GetYear():number
}

class student implements sfit_college{
    PID: number;
    first_name : string;
    last_name : string;
    year : number;
    GetPID():number{
        return this.PID;
    }
    GetName():string{
        return this.first_name + " " + this.last_name;
    }
    GetYear(): number {
        return this.year;
    }

    constructor(PID:number,first_name:string,last_name:string,year:number){
        this.PID = PID;
        this.first_name = first_name;
        this.last_name = last_name;
        this.year = year;
    }
}

let student_obj = new student(22106,"Vishal", "Mahajan",4)
console.log("PID of Student is", student_obj.GetPID());
console.log("Name of Student is",student_obj.GetName())
console.log("Year of Student is",student_obj.GetYear());