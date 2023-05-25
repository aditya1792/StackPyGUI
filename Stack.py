'''
Stack In Python
'''

def PUSH():
    global stk
    global top
    
    print('\n Enter a number:')
    n = int(input())
    
    top += 1
    stk.insert(top, n)
    
def DISP():
    global stk
    global top
    
    print('\n Stack: ')
    if(stk == []):
        print('\n Stack is Empty.')
    else:
        for i in range(top, -1, -1):
            print(stk[i])

def PEEK():
    global stk
    global top
    
    if(stk == []):
        print('\n Stack is empty.')
    else:
        print('\n PEEK = ', stk[top])
    
def POP():
    global stk
    global top
    
    if(stk == []):
        print('\n Stack is empty.')
    else:
        stk.pop(top)
        top -= 1

stk=[]
top=-1

while(True):
    print('\n'*4)
    print('1] PUSH ')
    print('2] DISP ')
    print('3] PEEK ')
    print('4] POP ')
    print('5] EXIT ')

    print('\n Enter your choice : ')
    choice = int(input())

    if(choice == 1):
        PUSH()
        DISP()
    elif(choice == 2):
        DISP()        
    elif(choice == 3):
        PEEK()
    elif(choice == 4):
        POP()
        DISP()
    elif(choice == 5):
        print('\n EXIT ')
        break
    else:
        print('\n INVALID INPUT')