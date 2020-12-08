//create function to count dates from 1900-01-01
//add leap years (if statement?)

const days = function(date){
    //expect correct time format
    //add incorrect format handler
    year = Number(date.slice(0,4) - 1) //need to subtract the current year
    console.log(year)
    // month = Number(date[5..6])
    // day = Number(date[8..9])
    totalDays = 0
    totalLeap = 0
    while (year >= 1900){
        //check if year is a leap year, divisible by 4 or 400 (1900 is not a leap year, 2000 is)
        if (year !== 1900 && year % 4 === 0 || year % 400 === 0){
            // is a leap year
            console.log(`Year ${year} is a leap year`)
            totalDays += 366
            totalLeap += 1
            year --
        }else {
            totalDays += 365
            year --
        }
    }
    console.log("Total leap years:", totalLeap)
    return totalDays
}

console.log(days("2020-10-10"))

var daysBetween = function (date1, date2) {

    
}