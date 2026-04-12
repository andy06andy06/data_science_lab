from ssl import VERIFY_DEFAULT
import numpy as np
from requests import delete

def swap_rows(x, r1, r2):
    # no return values needed
    # no loops allowed
    # do not declare new variables, manipulate x directly
    x[[r1,r2],:] = x[[r2,r1],:]

def most_value(x):
    # no loops allowed
    most_value = np.argmax(np.bincount(x))
    return most_value

def top_n(x, n):
    ind = np.argpartition(x, -n)[-n:]
    tops = abs(np.sort(-x[ind]))
    # no loops allowed
    return tops
    
def pythagorean(x):
    p = np.zeros((int(x.size/2),1))
    if x.size==4:
        for i in range(x.shape[0]):
            p[i] = (x[i,0]**2+x[i,1]**2)**0.5
    elif x.shape[0]==1:
        p[0] = (x[0,0]**2+x[0,1]**2)**0.5
    else:
        p[0] = (x[0]**2+x[1]**2)**0.5
    return p

def replace_me(v, a, b=None, c=None):
    for i in v:
        if i==a and b!=None and c!=None:
            v = np.setdiff1d(v,i)
            v = np.insert(v,i-1,[b,c])
        elif i==a and b!=None and c==None:
             v = np.setdiff1d(v,i)
             v = np.insert(v,i-1,[b,b])
        elif i==a and b==None and c==None:
            v = np.setdiff1d(v,i)
            v = np.insert(v,i-1,[0,0])
    return v


# You may test your function here
def main():

    # Lab04_C1 Swap rows
    print('Lab04_C1 Swap rows:')
    x1 = np.arange(9).reshape(3, 3)
    swap_rows(x1, 0, 1)
    print(x1, '\n')

    # Lab04_C2 Find most frequent value
    print('Lab04_C2 Find most frequent value:')
    x2 = np.array([1, 2, 2, 1, 3, 2, 4, 1, 2])
    print('The most frequent value is: ', most_value(x2), '\n')

    # Lab04_C3 top n
    print('Lab04_C3 Top n:')
    x3 = np.array([1, 0, 3, 5, 7, 3, 2, 8, 9, 2, 8])
    print('The 3 largest values are: ', top_n(x3, n=3), '\n')

    # Lab04_C4 pythagorean
    print('Lab04_C4 pythagorean:')
    x4 = np.array([[3, 4],[5, 12]])
    print(pythagorean(x4))

    try:
        pythagorean(np.array([12]))
        print('If you see this line, you may not check the input array', '\n')
    except:
        print('\n')

    # Lab04_C5 replace_me
    print('Lab04_C5 replace_me:')
    x5 = np.array([1, 2, 3])
    print(replace_me(x5, 2, 4, 5), '\n')

if __name__ == "__main__":
    main()