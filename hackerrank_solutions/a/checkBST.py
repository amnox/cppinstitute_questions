""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def checkLeft(nut,pivot):
    current = pivot
    l_small = nut[pivot][0]
    stack = []
    stack.append(l_small)
    bl = []
    while(len(stack)!=0):
        current = stack.pop()
        bl.append(current)
        if(max(bl)>=pivot):
            return False
        if(current not in nut.keys()):
            continue
        #check right is greater and left is smaller
        if(nut[current][0]>=current or nut[current][1]<=current):
            return False
        stack.extend(nut[current])
    return True

def checkRight(nut,pivot):
    current = pivot
    l_small = nut[pivot][1]
    stack = []
    stack.append(l_small)
    bl = []
    while(len(stack)!=0):
        current = stack.pop()
        bl.append(current)
        if(min(bl)<=pivot):
            return False
        if(current not in nut.keys()):
            continue
        #check right is greater and left is smaller
        if(nut[current][0]>=current or nut[current][1]<=current):
            return False
        stack.extend(nut[current])
    return True
    
def checkBST(root):
    stack = []
    nut  = {}
    stack.append(root)
    level = 1
    current = root
    left = True
    while(len(stack)!=0):
        nut[current.data] = []
        if(current.right is not None):
            stack.insert(0, current.right)
            nut[current.data].insert(0,current.right.data)
        if(current.left is not None):
            stack.insert(0, current.left)
            nut[current.data].insert(0,current.left.data)
        if((current.left is None) and (current.right is None)):
            del nut[current.data]
        current = stack.pop(0)
        level+=1
    pivot = root.data

    return checkLeft(nut,pivot) and checkRight(nut,pivot)
    