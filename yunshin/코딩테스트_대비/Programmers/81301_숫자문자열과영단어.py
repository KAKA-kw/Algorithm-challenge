from collections import defaultdict
def solution(s):
    dictionary = defaultdict(str)
    dictionary["zero"] = "0"
    dictionary["one"] = "1"  
    dictionary["two"] = "2"  
    dictionary["three"] = "3"  
    dictionary["four"] = "4"  
    dictionary["five"] = "5"  
    dictionary["six"] = "6"  
    dictionary["seven"] = "7"  
    dictionary["eight"] = "8"  
    dictionary["nine"] = "9"  
    dictionary["0"] = "0" 
    dictionary["1"] = "1" 
    dictionary["2"] = "2" 
    dictionary["3"] = "3" 
    dictionary["4"] = "4" 
    dictionary["5"] = "5" 
    dictionary["6"] = "6" 
    dictionary["7"] = "7" 
    dictionary["8"] = "8" 
    dictionary["9"] = "9" 

    stack = []
    answer = []
    for char in list(s):
        stack.append(char)
        if (dictionary["".join(stack)]):
            answer.append(dictionary["".join(stack)])
            stack = []
            continue
    
    return int("".join(answer))