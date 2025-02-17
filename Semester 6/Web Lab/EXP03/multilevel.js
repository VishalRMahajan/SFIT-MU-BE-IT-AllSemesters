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
var Sfit = /** @class */ (function () {
    function Sfit(PID) {
        this.PID = PID;
    }
    return Sfit;
}());
var details = /** @class */ (function (_super) {
    __extends(details, _super);
    function details(PID, role) {
        var _this = _super.call(this, PID) || this;
        _this.role = role;
        return _this;
    }
    return details;
}(Sfit));
var person = /** @class */ (function (_super) {
    __extends(person, _super);
    function person(PID, role, name) {
        var _this = _super.call(this, PID, role) || this;
        _this.name = name;
        return _this;
    }
    person.prototype.display = function () {
        console.log("PID is", this.PID);
        console.log("Role is", this.role);
        console.log("Name of the Person is", this.name);
    };
    return person;
}(details));
var multilevel = new person(221068, "Student", "Vishal Mahajan");
multilevel.display();
