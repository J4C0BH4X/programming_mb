const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter your age: ", function(age) {
    if (age >= 18 && age <= 64) {
        rl.question("Enter your weight in kg: ", function (weight) {
            rl.question("Enter your height in meters: ", function (height) {
                let bmi = weight / (height * height);
                console.log(`BMI is ${bmi}`);
                if (bmi > 24) console.log("You are overweight");
                else if (bmi < 19) console.log("You are underweight");
                else console.log("You are right where you should be");
                rl.close();
            });
        });
    }
    else {
        console.log("BMI is not valid for your age group");
        rl.close();
    }
});

rl.on("close", function() {
    console.log("\nBYE BYE !!!");
    process.exit(0);
});
