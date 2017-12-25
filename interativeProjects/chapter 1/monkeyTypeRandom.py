import string, random

# creates random letters of alphabeat and a space and returns
def monkeypress():
    count = 0
    s = ''
    while count < 28:
        s += random.choice(string.ascii_lowercase + ' ')
        count += 1
    return s

print(monkeypress())

def score(goal, currentext):
    points =0
    for i, k in zip(goal, currentext):
        print(i, k)
        if i == k:
            points +=1
    return points

def main():
    goal = 'methinks it is like a weasel'
    print(goal)
    generatedstring = monkeypress()
    k = score(goal, generatedstring)
    print('You have scored {} out of 27 points'.format(k))

main()

