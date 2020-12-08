//create function to count dates from 1900-01-01
//add leap years (if statement?)

const days = function(date){
    //expect correct time format
    //add incorrect format handler
    year = Number(date.slice(0,4)) //need to subtract the current year, month, day?
    month = Number(date.slice(5,7))
    day = Number(date.slice(8,10))
    // console.log(year, month, day)
    const daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDays = 0
    totalLeap = 0

    for (currentMonth = 1; currentMonth <= month - 1; currentMonth ++){
        if (currentMonth === 2 && (((year % 4 === 0) && (year % 100 !== 0)) || (year % 400 === 0))){
            //leap year
            totalDays += daysInMonth[currentMonth] + 1
        } else{
            totalDays += daysInMonth[currentMonth]
        }
    }

    for (currentYear = 1900; currentYear <= year - 1; currentYear ++){
        if (((currentYear % 4 === 0) && (currentYear % 100 !== 0)) || (currentYear % 400 === 0)){
            //leap year
            totalDays += 366
        } else{
            totalDays += 365
        }
    }
    console.log('days here', totalDays)
    // return totalDays + day
}

days("2020-12-07")

var daysBetween = function (date1, date2) {
    num = days(date1) - days(date2)
    return (num < 0) ? num * -1 : num; //check if number is negative, ensures return of positive integer
}

// console.log(daysBetween("2020-01-15", "2019-12-31"))

// console.log(daysBetween("2009-08-18", "2080-08-08"))
