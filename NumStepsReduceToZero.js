const numberOfSteps = function (num) {
    steps = 0
    while (num != 0){
        console.log(num, steps)
        if (num % 2 === 0){
            num = num / 2
            steps += 1
        } else {
            num = num - 1
            steps += 1
        }
    }
    return steps
}

console.log(numberOfSteps(123))
