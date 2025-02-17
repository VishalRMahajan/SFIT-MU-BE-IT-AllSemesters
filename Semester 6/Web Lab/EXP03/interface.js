var student = /** @class */ (function () {
    function student(PID, first_name, last_name, year) {
        this.PID = PID;
        this.first_name = first_name;
        this.last_name = last_name;
        this.year = year;
    }
    student.prototype.GetPID = function () {
        return this.PID;
    };
    student.prototype.GetName = function () {
        return this.first_name + " " + this.last_name;
    };
    student.prototype.GetYear = function () {
        return this.year;
    };
    return student;
}());
var student_obj = new student(22106, "Vishal", "Mahajan", 4);
console.log("PID of Student is", student_obj.GetPID());
console.log("Name of Student is", student_obj.GetName());
console.log("Year of Student is", student_obj.GetYear());
