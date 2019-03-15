def Hanoi(n,x=[],y=[],z=[],order=[1,2,3]):
    # input n as number of levels
    # x,y,z are the arrays representing the rims on the poles
    # x is the pole holding the original rims
    # y is the pole used to move rims
    # z is the target pole to pile the rims
    # order represents the order of the poles. e.g. [1,2,3] means [x,y,z], [2,3,1] means [y,z,x]
    if n<1:
        print('error input!')
    else:
        if len(x)==0 and len(y) == 0 and len(z)==0:
            # means the initialization of arrays
            for i in range(1,n+1):
                x.append(i)
            Draw(x,y,z,order)
        if n==1:
            # only when n=1, it will make movement of rims
            z.insert(0,x.pop(0))
            Draw(x,y,z,order)
            return [x,y,z]

        if n>1:
            # when n>1, it will use iteration
            # 1. pile the top (n-1) rims to the pole y
            A = Hanoi(n-1,x,z,y,Swap(order,1,2))
            order = Swap(order,1,2)
            x = A[0]
            y = A[2]
            z = A[1]
            # 2. remove the bottom nth rim from pole x to pole z
            z.insert(0,x.pop(0))
            Draw(x,y,z,order)
            # 3. pile the (n-1) rims on pole y to pole z
            B = Hanoi(n-1,y,x,z,Swap(order,0,1))
            order = Swap(order,0,1)
            x = B[1]
            y = B[0]
            z = B[2]
            return [x,y,z]

def Swap(order,a,b):
    # change the order for printing purpose
    c = order[a]
    order[a] = order[b]
    order[b] = c
    return order

def Blow(copy,width):
    # fill the arrays with 0s until the length of arrays is equivalent to n
    # will only be used in Draw method at bottom. Has nothing to do with the real arrays x,y,z
    ''' view the poles like buildings, which have floors
        each floor represents one rim
        the empty floor represents the rim with 0 width,
        which fill the array with 0'''
    for array in copy:
        if len(array) == width:
            continue
        else:
            for i in range(0,width-len(array)):
                array.insert(0,0)
    return copy
        

def PrintOut(x,y,z,order):
    # decide the order of printing out image
    if order[0] == 1:
        if order[1] == 2:
            return [x,y,z]
        else:
            return [x,z,y]
    if order[0] == 2:
        if order[1] == 1:
            return [y,x,z]
        else:
            return [z,x,y]
    if order[0] == 3:
        if order[1] == 2:
            return [z,y,x]
        else:
            return [y,z,x]

def Draw(x,y,z,order):
    # draw the images using PrintingOut and Blow methods
    data = PrintOut(x,y,z,order)
    width = max([max(x,default = 0),max(y,default = 0),max(z,default = 0)])
    copy = [data[0][:],data[1][:],data[2][:]]
    copy = Blow(copy,width)   
    line = ' '*(width+2)+'||'+' '*(width+2)*2+'||'+' '*(width+2)*2+'||'
    print(line)
    for i in range(0,len(copy[0])):
        [line1,line2,line3] = ['','','']
        if copy[0][i] == 0:
            line1 = ' '*(width+2)+'||'+' '*(width+2)
        else:
            line1 = ' '*(width+2-copy[0][i])+'*'*(copy[0][i]+1)*2+' '*(width+2-copy[0][i])
        if copy[1][i] == 0:
            line2 = ' '*(width+2)+'||'+' '*(width+2)
        else:
            line2 = ' '*(width+2-copy[1][i])+'*'*(copy[1][i]+1)*2+' '*(width+2-copy[1][i])
        if copy[2][i] == 0:
            line3 = ' '*(width+2)+'||'+' '*(width+2)
        else:
            line3 = ' '*(width+2-copy[2][i])+'*'*(copy[2][i]+1)*2+' '*(width+2-copy[2][i])
        line = line1+line2+line3
        print(line)
    baseline = (" "+"="*(width+2)*2+" ")*3
    print(baseline)
    print(baseline)
            
n = int(input('the level of tower:'))
Hanoi(n)
input()
