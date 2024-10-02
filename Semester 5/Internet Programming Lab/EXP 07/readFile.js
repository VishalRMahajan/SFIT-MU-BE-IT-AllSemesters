const http = require('http')
const fs = require('fs')
const prompt = require('prompt-sync')({ sigint: true });


var ch = parseInt(prompt("Enter the Choice: 1. Read File 2.Append Data 3.Copy File. 4.Rename 5.Delete Enter your Choice:   "));
switch (ch) {
    case 1:
        console.log("\n")
        ReadFile("sample.txt")
        break;

    case 2:
        console.log("\n")
        AppendData("sample.txt")
        break;

    case 3:
        console.log("\n")
        CopyFile("sample.txt", "sample2.txt")
        break;

    case 4:
        console.log("\n")
        Rename("sample2.txt", "renamedsample2.txt");
        break;

    case 5:
        console.log("\n")
        Delete("renamedsample2.txt");
        break;

    default:
        "Enter Valid Choice";

}



function ReadFile(filename) {
    fs.readFile(filename, (err, data) => {
        if (err) {
            console.log(err);
        }
        else {
            console.log(data.toString())
        }

    }
    )
}

function AppendData(filename) {
    var appenddata = prompt("Enter the Data to be appended: ")
    fs.appendFile(filename, 'n' + appenddata, (err, data) => {
        if (err) {
            console.log(err);
        }
        else {
            console.log("Data Appended")
        }

    }
    )
}

function CopyFile(from, to) {
    fs.copyFile(from, to, (err, data) => {
        if (err) {
            console.log(err);
        }
        else {
            console.log("Copied File with the content : ")
            fs.readFile('sample2.txt', (err, data) => {
                if (err) {
                    console.log(err);
                }
                else {
                    console.log(data.toString())
                }

            }
            )
        }
    }
    )
}

function Rename(filename, RenamedName) {
    fs.rename(filename, RenamedName, (err) => {
        if (err) {
            throw err;
        }
        console.log(filename,"renamed to",RenamedName);
    });
}

function Delete(filename) {
    fs.unlink(filename, (err, data) => {
        if (err) {
            console.log(err);
        }
        else {
            console.log("File Deleted")
        }

    }
    )
}

