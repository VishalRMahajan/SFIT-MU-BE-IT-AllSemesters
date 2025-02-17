var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var SFIT = /** @class */ (function () {
    function SFIT(PID) {
        this.PID = PID;
    }
    return SFIT;
}());
var Student_details = /** @class */ (function (_super) {
    __extends(Student_details, _super);
    function Student_details(PID, stud_name, year) {
        var _this = _super.call(this, PID) || this;
        _this.stud_name = stud_name;
        _this.year = year;
        return _this;
    }
    Student_details.prototype.display = function () {
        console.log(this.PID);
        console.log(this.stud_name);
        console.log(this.year);
    };
    return Student_details;
}(SFIT));
var SFITobj = new Student_details(221068, "Vishal Mahajan", 3);
SFITobj.display();
