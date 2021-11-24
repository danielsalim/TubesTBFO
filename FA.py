def state1(c):
    if((ord(c) >= 65 and ord(c) <= 90) or (ord(c) == 95) or (ord(c)>= 97 and ord(c) <= 122)):
        state = 2
    else :
        state = 3
    return state

def state2(c):
    if((ord(c) >= 65 and ord(c) <= 90) or (ord(c) == 95) or (ord(c)>= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57)):
        state = 2
    else :
        state = 3
    return state

def state3(c):
    state = 3
    return state

def state4(c):
    if(ord(c) >= 48 and ord(c) <= 57):
        state = 5
    else :
        state = 6
    return state

def state5(c):
    if(ord(c) >= 48 and ord(c) <= 57):
        state = 5
    else :
        state = 6
    return state

def state6(c):
    state = 6
    return state

def isVariable(s):
    state = 1
    for i in range (len(s)):
        if (state == 1):
            state = state1(s[i])
        if (state == 2):
            state = state2(s[i])
        if (state == 3):
            state = state3(s[i])
    if (state == 2):
        return True
    else :
        return False

def isNumber(s):
    state = 4
    for i in range (len(s)):
        if (state == 4):
            state = state4(s[i])
        if (state == 5):
            state = state5(s[i])
        if (state == 6):
            state = state6(s[i])
    if (state == 5):
        return True
    else :
        return False

# str = "12a"
# if(isNumber(str)):
#     print("Variable accepted")
# else:
#     print("Variable error")
        