def starting():
    str = input("Enter an starting string for DFA: ")
    l = len(str) + 1
    transition = []
    for i in range(0,l-1):
        good = str[i]

        if good == 'a':
            bad = 'b'
        else:
            bad ='a'

        d = {good:i+1,bad: -1}
        transition.append(d)

    transition.append({'a': l-1,'b': l-1})

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
