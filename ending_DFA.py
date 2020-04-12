def ending():
    n = int(input("Enter the number of input symbols:  "))
    next_bad_state = 0
    alphabets = []
    for i in range(0, n):
        alphabets.append(input("enter the input symbols: "))
    str = input("Enter an ending string for DFA: ")
    l = len(str) + 1
    temp = str
    states = []
    for i in range(0,l):
        states.append(temp[i:])
    transition = []


    current_transition = {}


    for i in range(0, l):#j
        for m in range(0,n):#k
            current = str[0:i] + alphabets[m]
            status = 0
            # Finding next state when we get wrong input
            for j in range(0, l):#m
                p = states[j]
                for k in range(0, len(current)):#p
                    t = current[k:]  # Finding substring of current input which matches with some state
                    if (t + p == str):  # checking whether that substring matches with some state or not
                        next_bad_state = j
                        status = 1
                        break

            if status == 0:
                next_bad_state = 0

            current_transition[alphabets[m]]= next_bad_state

        d = dict(current_transition)
        transition.append(d)

    print("  ",end=" ")
    for i in range(0,n):
        print("    |  {}".format(alphabets[i]),end=" ")
    print(" ")
    print("|-----------------------")

    for k in range(0, l):
        print("|q{}".format(k),end=" ")
        for i in range(0, n):
            print("   |  q{}".format(transition[k][alphabets[i]]), end=" ")
        print("  |")
        print(" ")
        print("|-----------------------")
    stringprocessing(transition, l - 1)

def stringprocessing(transition, l):
        pro = input("Enter the string you want to check:  ")
        lp = len(pro)
        current = 0
        next = 0
        for i in range(0, lp):
            p = pro[i]
            next = transition[current][p]
            current = next
        if current == l:
            print("String accepted")
        else:
            print("String rejected")

