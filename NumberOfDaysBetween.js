//create function to count dates from 1900-01-01
//add leap years (if statement?)

const days = function(date){
    //expect correct time format
    //add incorrect format handler
    year = Number(date.slice(0,4) - 1) //need to subtract the current year, month, day?
    month = Number(date.slice(5,7) - 1)
    day = Number(date.slice(8,10))
    // console.log(year, month, day)
    totalDays = 0
    totalLeap = 0
    while (year >= 1900){
        //check if year is a leap year, divisible by 4 or 400 (1900 is not a leap year, 2000 is)
        if (year !== 1900 && year % 4 === 0 || year % 400 === 0){
            // is a leap year
            // console.log(`Year ${year} is a leap year`)
            totalDays += 366
            totalLeap += 1
        }else {
            totalDays += 365
        }
        year --
    }
    while (month > 0){
        thirtyOne = [1,3,5,7,8,10,12]
        thirty = [4,6,9,11]
        if (thirtyOne.includes(month)){
            totalDays += 31
        } else if (thirty.includes(month)){
            totalDays += 30
        } else if (month === 2){
            //Leap year day already added in year
            totalDays += 28
        }
        month --

    }
    // console.log("Total leap years:", totalLeap)
    return totalDays + day
}

// console.log(days("2020-12-08"))

var daysBetween = function (date1, date2) {
    num = days(date1) - days(date2)
    return (num < 0) ? num * -1 : num; //check if number is negative, ensures return of positive integer
}

console.log(daysBetween("2020-12-05", "2020-12-05"))