class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# get all "layers" breadth
# for each layer add child
# last layer has all NOne

    
def lca(root, n1, n2): 
      
    # Base Case 
    if root is None: 
        return None
  
    # If both n1 and n2 are smaller than root, then LCA 
    # lies in left 
    if(root.info > n1 and root.info > n2): 
        return lca(root.left, n1, n2) 
  
    # If both n1 and n2 are greater than root, then LCA 
    # lies in right  
    if(root.info < n1 and root.info < n2): 
        return lca(root.right, n1, n2) 
  
    return root 
    
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
