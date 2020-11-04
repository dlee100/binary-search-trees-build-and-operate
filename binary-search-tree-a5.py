# Cell 1
class BinarySearchTree():      # BST
    """Simplified linked representation of a binary tree structure - only the essentials included."""

  #-------------------------- nested Node class --------------------------
    class Node:
        """Lightweight, nonpublic class for storing a node."""
        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element #data or key
            self.parent = parent #pointer or None
            self.left = left #point to the left child node or None
            self.right = right #point to the right child node or None

 
  #-------------------------- SLBT constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self.root = None #initially tree root is None by default (tree empty)
        self.size = 0

  #-------------------------- accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self.size
  
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self.root

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        return p.parent

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        return p.left

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        return p.right

    def element(self, p):
        return p.element

    def is_root(self, p):
        if p.parent is None:
            return True
        return False

    def is_leaf (self, p):
        if p.left is None and p.right is None:
            return True
        return False

    def num_children(self, p):
        """Return the number of children of Position p."""
        count = 0
        if p.left is not None:     # left child exists
            count += 1
        if p.right is not None:    # right child exists
            count += 1
        return count

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(p.parent)

  #-------------------------- mutators --------------------------
    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
           Raise ValueError if tree nonempty.
        """
        if self.root is not None:
            raise ValueError('Root exists')
        self.size = 1
        self.root = self.Node(e)
        return self.root

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
           Return the Position of new node.
           Raise ValueError if Position p is invalid or p already has a left child.
        """
        if p.left is not None:
            raise ValueError('Left child exists')
        self.size += 1
        p.left = self.Node(e, parent = p)            # p is the parent
        return p.left

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
           Return the Position of new node.
           Raise ValueError if Position p is invalid or p already has a right child.
        """
        if p.right is not None:
            raise ValueError('Right child exists')
        self.size += 1
        p.right = self.Node(e, parent = p)          # node is its parent
        return p.right

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        old = p.element
        p.element = e
        return old

  #------------------------------- BST utilities -------------------------------
    def subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched.
           Also return True if the key is found in the Tree, otherwise False.  """
        if k == p.element:                                 # found match - return position+True
            return p, True                                         
        elif k < p.element:                                # search left subtree
            if self.left(p) is not None:
                return self.subtree_search(self.left(p), k)   
        else:                                              # search right subtree
            if self.right(p) is not None:
                return self.subtree_search(self.right(p), k)
        return p, False          # signal 'not found' to the caller: position+False

    def insert (self, k):
        """ Insert a node with value 'k' into the correct spot in the tree. """
        addHere, found = self.subtree_search(self.root, k)
        if found:
            raise AlreadyInBST ('Element is already in the tree')  # key value already in the Tree
        elif k < addHere.element:
            self.add_left(addHere, k)
        else:
            self.add_right(addHere, k)

  #---------------------------------------------------------------------------------------------- 
  # Note: You are to provide code for this method - the code to find the node is provided as
  #       well as Docstring comments laying out the cases to be coded. 
  #       Hint: use the find_min function to find the min. element in the right subtree. 
  #       Be sure to adjust the tree size after a successful deletion.
  #----------------------------------------------------------------------------------------------
    def delete (self, k):
        """ Delete a node with value 'k' if it is in the tree. Raise NotInBST if elt. not in tree. """    
        deleteThis, found = self.subtree_search(self.root, k)   # Find node to be deleted

      # Cases: (1) element to be deleted is not in the tree, raise exception +
      #        (2) element has no children, just set it's parent's pointer to None (if e is leaf)
      #        (3) element has one child: reset parent of 'k' to point to child 
      #        (4) element has two children: harder case         
        
      # "The matter is to manipulate the POINTERS correctly."
    
        if not found:
            raise NotInBST ('Element is not in the tree')
        # if element to be deleted is found
        else: 
            # if k (element to be deleted) has no parent node
            if self.is_root == True:  
                # delete node
                deleteThis.replace(k, k.right) # k's right child becomes new root
                # move elements up
                # </> ?
            # if k is not root    
            else: 
                # if k has no children
                if self.is_leaf == True: 
                    # setting parent of k's child pointer to None
                    # -- self.parent.replace(k, None) 
                    # delete node
                    deleteThis.replace(k, None)
                # if not leaf
                else: 
                    # if k (element to be deleted) has one child
                    if self.num_children == 1: 
                        # reset parent node of k to point to k's child as its child
                        # </> ?
                        # delete node
                        deleteThis.replace(k, k.left or k.right)
                    # if k (element to be deleted) has two children
                    elif self.num_children == 2: 
                        # set k's left child as child of k's parent node. set k's right child as child of left node.
                        # </> ?
                        deleteThis.replace(k, k.left)
                        # </>
            # if deleted node had no parent node, set parent's pointer to None
            # if deleted node had one child, reset parent node of deleted node to point to child
            # if deleted node had two children, one sibling becomes a parent?
      
        
    def find_min(self, p):
        """Return key with minimum key (or None if empty)."""
        if len(self) == 0:
            return None
        while p.left is not None:
            p = p.left
        return p, p.element

    def find_max(self, p):
        """Return key with minimum key (or None if empty)."""
        if len(self) == 0:
            return None
        while p.right is not None:
            p = p.right
        return p, p.element


# BST Traversals --------------------------------------------------------- 
            
#-----------------------------------------------------------------
# inorder algorithm (recursive):
#    if tree node is not empty:
#        if the node has a left child call preorder on that node
#        print the node's element
#        if the node has a right child call preorder on that node
#----------------------------------------------------------------
    def inorder (self, pos):
        """ Perform an inorder traversal of the current tree - print the elements. """
        if pos is not None:
            if self.left(pos) is not None:    
                self.inorder (self.left(pos))
            print(self.element(pos))
            if self.right(pos) is not None:
                self.inorder (self.right(pos))            

class AlreadyInBST (Exception):
    pass

class NotInBST (Exception):
    pass

# Cell 2
# Instantiate a BST class object, then build a small tree

# Cell 3
BST = BinarySearchTree()

# Cell 4
BST.add_root(100)

# Cell 5
BST.insert(25)
BST.insert(50)
BST.insert(75)
BST.insert(125)
BST.insert(150)
BST.insert(175)
BST.insert(65)
BST.insert(200)
print('Size of BST = ', len(BST))
BST.inorder(BST.root)

# Cell 6
#The 'parenthesize' function displays a parenthesized version of a tree when given its root node
#Use the following code to print a parenthesized version of a BST.

# Cell 7
def parenthesize(T, p):
    """ Print a parenthesized representation of a subtree of T rooted at p. """
    if p is not None:
        print (p.element, end = '')
        if not T.is_leaf(p):
            first_time = True
            for c in (T.left(p), T.right(p)):
                if first_time:
                    sep = ' ('
                else:
                    sep = ', '
                print (sep, end = '')
                first_time = False
                parenthesize(T, c)
            print(')', end = '')

# Cell 8
parenthesize(BST, BST.root)

# Cell 9
BST.find_min(BST.root)[1]

# Cell 10
RST = BST.root.right
BST.find_min(RST)[1]

# Cell 11
BST.find_min(BST.root.right)[1]
