import sys


def laser_cut(seq):
    stick_left = 1
    stack = [seq[0]]
    total_stick = 0
    laser_detected = False
    for cur in seq[1:]:
        if cur == '(':
            stack.append(cur)
            stick_left += 1
        if cur == ')':
            if stack[-1] == '(':
                stick_left -= 1
                total_stick += stick_left
                stack.pop()
            
            # else:
            #     print('popped')
            #     stick_left -= 1
            #     stack.pop()
            #     total_stick += 1
        print(cur, stick_left, total_stick)

    return total_stick

while True:
    seq = input()
    print(laser_cut(seq))
# seq = '()(((()())(())()))(())'
# print(laser_cut(seq))

# seq2 = '(((()(()()))(())()))(()())'
# print(laser_cut(seq2))

            