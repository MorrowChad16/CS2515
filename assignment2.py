'''
Created on 28 Sep 2018

@author: cm80
'''
import stackA
from stackA import Stack
import random
from random import randint
import sys 
import time
from _ast import operator

givenStack = Stack()

givenStack.push('C')
givenStack.push('H')
givenStack.push('A')
givenStack.push('D')
givenStack.push('M')
givenStack.push('O')
givenStack.push('R')
givenStack.push('R')
givenStack.push('O')
givenStack.push('W')

givenString = '()(6+5){6[5(4+3)]})'

def reverseStack(givenStack):
    newStack = Stack()
    while givenStack.length() != 0: #& isinstance(obj, stackA):
        newStack.push(givenStack.pop())
    return newStack

def correctBracket(givenString):
    charStack = Stack()
    for char in givenString:
        if char == '{' or char == '[' or char == '(':
            charStack.push(char)
        elif char == '}':
            if charStack.top() != '{':
                return 'INCORRECT'
            charStack.pop()
        elif char == ']':
            if charStack.top() != '[':
                return 'INCORRECT'
            charStack.pop()
        elif char == ')':
            if charStack.top() != '(':
                return 'INCORRECT'
            charStack.pop()
    return 'ITS CORRECT'


def color_tetris(stacks, colours, rounds, th, secs):
    """ Play multi-stack colour tetris.

    Args:
        stacks - (int) number of stacks
        colours - (int) number of colours
        rounds - (int) number of blocks to be generated
        th  - (int) threshold height for a stack (if any stack exceeds this
              height, the game is over)
        secs - (int) number of seconds available for each move.
    """
    stacklist = []
    for i in range(stacks):
        stacklist.append(Stack())
    charstr = 'RGBOYIV'

    #generate the list of blocks
    blocklist = []
    for i in range(rounds):
        blocklist.append(charstr[random.randint(0,colours-1)])
    i = 0
    matches = 0
    threshold = True

    #reveal each block in turn, until exhausted or threshold breached
    while i < len(blocklist) and threshold:
        block = blocklist[i]
        i = i+1
        #display the block and get the user response
        output = str(i) + ': ' + block + '?'
        clocktime0 = time.time()
        ans = input(output)
        clocktime1 = time.time()
        elapsed = clocktime1 - clocktime0
        #now propcess the user response
        if elapsed > secs:
            print('TOO LATE (', elapsed, ' sec), block add to stack 1')
            ans = '1'
        if ans in['1','2','3','4']:
            value = int(ans)-1
        else:
            value = 0
        #now try to match the block with the top of the user's chosen stack
        if stacklist[value].top() == block:   #successful match
            stacklist[value].pop()
            print(' ******************************** ')
            matches = matches + 1
        else:                                 #failed match, so grow the stack
            stacklist[value].push(block)
        if stacklist[value].length() >= th:
            threshold = False
        else:
            j = 0
            while j < len(stacklist):
                print((j+1), ':', stacklist[j])
                j = j+1
    if threshold:
        print('Congratulations! You beat the system, and made', matches, 'matches.')
    else:
        print('You lasted for', i, 'rounds, and made', matches, 'matches.')

def infixConverter(equationString):
    numStack = Stack()
    numList = []
#     operatorValues = {"/":2, "*":2, "+":1, "-":1}
    
    for variable in equationString:
        try: 
            int(variable)
            numList.append(variable)
        except ValueError:
            if variable == "(":
                numStack.push(variable)
            elif variable == ")":
                while numStack.top() != "(":
                    numList.append(numStack.pop())
                numStack.pop()
            elif (variable == "*" or variable == "/"):
                if numStack.top() == "*" or numStack.top() == "/":
                    numList.append(numStack.pop())
                    numStack.push(variable)
                else:
                    numStack.push(variable)
            elif (variable == "+" or variable == "-"):
                numStack.push(variable)
    while numStack.length() != 0:
        numList.append(numStack.pop())
    s = " "
    print(s.join(numList)) 
    
# infixConverter("(7 / 8 + 4) / 3 * 5")
# tetrisGame(NUMBER OF COLORS, NUMBER OF STACKS, TIME LIMIT, MAX HEIGHT)                   
# tetrisGame(5, 2, 10, 5)    
# print(correctBracket(givenString))
# print(reverseStack(givenStack))

