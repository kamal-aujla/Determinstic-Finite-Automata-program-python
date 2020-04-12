def substring():
    str = input("Enter an substring for DFA: ")
    l = len(str) + 1
    temp = str
    states = []
    for i in range(0, l):
        states.append(temp[i:])

    transition = []
    # Transitions for all non-finals states
    next_good_state = 0
    next_bad_state = 0
    good = 'p'  # good will denote the input at a state which will be required to move on to next state
    bad = 'q'  # bad will denote the input at a state which will spoil our current progress of string processing

    for i in range(0, l - 1):
        good = temp[i]
        if good == 'a':
            bad = 'b'
        else:
            bad = 'a'

        next_good_state = i + 1
        current = str[0:i] + bad
        status = 0

        for j in range(0, l - 1):
            p = states[j]
            for k in range(0, len(current)):
                t = current[k:]
                if (t + p == str):
                    next_bad_state = j
                    status = 1
                    break

        if status == 0:
            next_bad_state = 0

        d = {good: next_good_state, bad: next_bad_state}
        transition.append(d)

    transition.append({'a': l - 1, 'b': l - 1})

    print("         a          b        ")
    print("-------------------------")
    for k in range(0, l):
        print("q{} |    q{}         q{}            ".format(k, transition[k]['a'], transition[k]['b']))
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
