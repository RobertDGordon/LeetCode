# Loop through string until end
#     record integer = x
#     If "[" found
#         Loop until "]"
#             add next character to temp string
#         add temp string to new string x times

# ... oorrrr parse

# def decodeString(self, s: str) -> str:
#     new_string = ""
#     for char in s:
#         x = 0
#         if type(char) == int:
#             x = char
#         if char == "[":

def decodeString(s: str) -> str:
    new_string = ""
    code = s.replace("]","[")
    new_code = code.split("[")
    print(new_code)
    for index, char in enumerate(new_code):
        if char.isnumeric():
            letters = new_code[index + 1]
            # print("letters before if", letters)
            if any(letr.isdigit() for letr in letters):
                sec_mult = 0
                sec_letters = ""
                for ltr in letters:
                    if ltr.isdigit():
                        sec_mult = int(ltr)
                if sec_mult > 0:
                    sec_letters = new_code[index + 2] * sec_mult
                letters = "".join([ltr for ltr in letters if not ltr.isdigit()])
                print(sec_mult, letters, sec_letters)
                new_string = new_string + (letters + sec_letters) * int(char)
            else:
                new_string = new_string + new_code[index + 1] * int(char)
    return new_string

a = "2[ba]4[adfg]"
b = "3[a2[c]]"

print(decodeString(b))