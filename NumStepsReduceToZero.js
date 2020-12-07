const numberOfSteps = function (num) {
    steps = 0
    while (num != 0){
        if (num % 2){
            num = num / 2
            steps += 1
        } else {
            num = num - 1
            steps += 1
        }
    }
    return steps
}

console.log(numberOfSteps(14))
