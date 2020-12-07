// Iterate over the string
// Use if/else block to check for keywords
// advance pointer if () or (al)

const interpret = function (command) {
    response = "";

    for (var i = 0; i < command.length; i++){
        // console.log(command[i])
        if (command[i] === "G"){
            response += "G"
        } else if (command[i] === "("){
            if (command[i + 1] === ")"){
                response += "o";
                //add pointer advance here
            } else if (command[i + 1] === "a"){
                response += "al"
                //add pointer advance here
            }
        }
    }
    console.log(response)
    
}

interpret("(al)G(al)()()G")