from collections import deque

stack = deque()

bracketData  = { 
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '|' : '|'
}

def balanced(str):
    #loop through each bracket in str
    for bracket in str:
        #if the bracket is an opening bracket push it onto the stack
        if bracketData[bracket]:
            stack.push(bracket);
        else:
            #if not, then pop a bracket off the stack
            poppedBracket = stack.pop();
        
        if bracketData[poppedBracket] != bracket:
            return False
    
    return stack.len()


            
