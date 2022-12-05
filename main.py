# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import turtle


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    if 5>10:
        print("hello world")
    else:
        print("hi world")

def more_spaces(s: str) -> str:
    custString =", !1"
    s2 = ""
    for i in range(len(s)-1):
        s2 += s[i]
        if s[i] not in custString and s[i+1] not in custString:
            s2+=" "

    s2+=s[i+1]
    return s2


def sort_positives(a: List[int])->List[int]:
    b = sorted([int(x) for x in a if int(x) > 0])
    j = 0
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = b[j]
            j+=1
    return a


def flowers(a: List[int]) -> int:
    count  = 0
    for i in range(0,len(a),1):
        if (i==0 and a[i]== 0 and a[i+1]== 0) or (i==len(a)-1 and a[i]== 0 and a[i-1]== 0):
            count +=1
            a[i] = 1
        elif ((i!= 0) and (i!= len(a)-1) and (a[i]== 0 and a[i+1]== 0) and (a[i]== 0 and a[i-1]== 0)):
            count+=1
            a[i] = 1

    return count

def merge(a: List[int], b: List[int]) -> List[int]:
    res = a+b
    return sorted(res)


def sort_cards(a: List[int]) -> List[int]:
    b1 = sorted([int(x) for x in a if int(x) < 5])
    b2 = sorted([int(x) for x in a if int(x) > 5])
    return b2+b1

def format_str(letters:str, f: str) -> str:
    res = ""
    i=0
    for c in range(0, len(f)):
        if f[c]=='X':
            res+=letters[i].upper()
            i+=1
        elif f[c]=='x':
            res+=letters[i].lower()
            i+=1
        else:
            res+=f[c]
    return res

def doubles(s: str) -> int:
    count = 0
    for i in range(0, len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    return count

def divisible_by_three(a: List) -> List:
    b = []
    for i in a:
        if i%3==0:
            b.append(i)
    return b

def duplicate_and_invert_negative_numbers(a: list[int]) -> list:
    b = []
    for i in a:
        b.append(i)
        if i <0:
            b.append(abs(i))
    return b

def count_positive(a: list[int]) -> int:
    counter = 0
    for i in a:
        if i>0:
            counter+=1
    return counter

def add_hello(s: str) -> str:
    s1 = s.split()
    s1.insert(1,'hello')
    return  " ".join(s1)

def second_is_a(s: str) -> str:
    return s[0] + 'A' + s[2:]


def merge(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = list()
    if len(a)>len(b):
        r = len(a)
    else:
        r = len(b)
    for i in range(0, r):
        if i < len(a):
            c.append(a[i])
        if i < len(b):
            c.append(b[i])
    return c


def draw_house(x:int, y:int):
    # penup() pendown() goto(x,y) forward(steps) left(deg) right(deg) home() speed()
    # draw base
    #initialization
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    turtle.speed(1000)


    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    # draw door
    turtle.penup()
    turtle.setpos(x+20, y+0)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()
    turtle.color("black")
    turtle.setpos(x,y)
    turtle.setheading(0)

    # draw roof
    turtle.penup()
    turtle.setpos(x+100, y+100)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.end_fill()
    turtle.color("black")
    turtle.setpos(x,y)

    # draw window
    turtle.penup()
    turtle.setpos(x+50, y+50)
    turtle.setheading(0)
    turtle.pendown()
    for i in range(4):
        turtle.forward(30)
        turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)

def draw_house2(x: int, y: int):
        # penup() pendown() goto(x,y) forward(steps) left(deg) right(deg) home() speed()

        # initialization
        turtle.penup()
        turtle.setpos(x, y)
        turtle.pendown()
        turtle.speed(1000)

        # draw base
        for i in range(4):
            turtle.forward(60)
            turtle.left(90)
        # draw door
        turtle.penup()
        turtle.setpos(x + 20, y + 0)
        turtle.pendown()
        turtle.color("red")
        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(20)
        turtle.end_fill()
        turtle.color("black")
        turtle.setpos(x, y)
        turtle.setheading(0)

        # draw roof
        turtle.penup()
        turtle.setpos(x + 60, y + 60)
        turtle.pendown()
        turtle.color("brown")
        turtle.begin_fill()
        turtle.left(120)
        turtle.forward(60)
        turtle.left(120)
        turtle.forward(60)
        turtle.end_fill()
        turtle.color("black")
        turtle.setpos(x, y)

        # draw window
        turtle.penup()
        turtle.setpos(x + 30, y + 30)
        turtle.setheading(0)
        turtle.pendown()
        turtle.color("yellow")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(20)
            turtle.left(90)
        turtle.end_fill()
        turtle.color("black")
        for i in range(4):
            turtle.forward(20)
            turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(20)


def twoSum( nums: List[int], target: int) -> List[int]:
     for i in range(len(nums)-1):
         if nums[i]> target:
             del (nums[i])
             i-=1
     for i in range(len(nums)-1):
         if nums[i]- target < 0:
             del(nums[i])
     for i in range(len(nums)-1):
         if target-nums[i] in nums:
             return [nums.index(target-nums[i]), nums[i]]
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    #print(more_spaces('Hello, world!'))
    #print(more_spaces('ABCabc'))
    #print(more_spaces('ABC abc'))
    #print(more_spaces('abc,abc1abc'))
    #print(sort_positives([1, 5, 4, 3, -1, 2, -2]))
    #print(sort_positives([0, -1, -2, -3]))
    #print(sort_positives([2, -1, -2, -3, 1]))
    #print(sort_positives([1, 2, 3, -5, 2, 1]))
    #print(flowers([1, 0, 1, 0, 0]))
    #print(flowers([1, 0, 0, 0, 1]))
    #print(flowers([1, 0, 0, 0, 0, 1]))
    #print(flowers([1, 0, 0, 0, 0, 0, 1]))
    #print(flowers([0, 0, 1, 0, 0]))
    #print(flowers([0, 0, 0, 0, 0]))
    #print(flowers([]))
    #print(flowers([1, 0, 1]))
    #print(flowers([0, 1, 0]))

    #merge([1,3,5,6,8], [2,3,5,6,7])
    #print(sort_cards([1, 2, 3, 6]))
    #print(sort_cards([8, 0, 1, 3, 7, 7]))
    #print(sort_cards([0, 6, 7, 8]))
    #print(format_str('aBcDe', 'Xxxxx!'))
    #print(format_str('helloworld', 'Xxxxx, xxxxx!'))
    #print(format_str('john', 'Hello, XXXX!'))

    #print(doubles('collision'))
    #print(doubles('off road iss funn'))
    #print(doubles('ccddeeff'))
    #print(doubles('ccdd eeff'))
    #print(doubles(''))

    #print (divisible_by_three([1, 2, 3, 4, 5, 6]) )

    #print(duplicate_and_invert_negative_numbers([1, 2, -3, 4, 5 ]))

    #print( count_positive([1,2,3,4,5]))

    #print(add_hello('This is the first test'))

    # print( second_is_a('tttt'))
    # print(second_is_a('abc'))

    # assert merge([1, 2, 3], [4, 5, 6])== [1, 4, 2, 5, 3, 6]
    # assert merge([1, 2, 3], [4, 5])== [1, 4, 2, 5, 3]
    # assert merge([1, 2], [4, 5, 6, 7])==[1, 4, 2, 5, 6, 7]

    # for i in range(5):
    #     for j in range(5):
    #         draw_house2(-350+i*100,200-j*120)

    twoSum([2,7,11,15],9)


    turtle.done()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


