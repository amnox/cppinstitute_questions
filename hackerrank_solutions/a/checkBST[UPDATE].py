INT_MAX = 4294967296
INT_MIN = -4294967296
  
def checkBST(node): 
    return (isBSTUtil(node, INT_MIN, INT_MAX)) 
  
# Retusn true if the given tree is a BST and its values 
# >= min and <= max 
def isBSTUtil(node, mini, maxi): 
      
    # An empty tree is BST 
    if node is None: 
        return True
  
    # False if this node violates min/max constraint 
    if node.data < mini or node.data > maxi: 
        return False
  
    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi)) 