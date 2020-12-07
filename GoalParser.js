// Iterate over the string
// Use if/else block to check for keywords
// advance pointer if () or (al)

const interpret = function (command) {
    response = "";
    for (var i = 0; i < command.length; i++){
        // console.log(command[i])
        if (command[i] === "G"){
            response += "G";
        } else if (command[i] === "("){
            if (command[i + 1] === ")"){
                response += "o";
                //add pointer advance here
                i++;
            } else if (command[i + 1] === "a"){
                response += "al";
                //add pointer advance here
                i += 3;
            }
        }
    }
    return(response)
}

console.log(interpret("(al)G(al)()()G"))