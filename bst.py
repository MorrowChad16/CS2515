'''
Created on 2 Nov 2018

@author: Chad Morrow
'''

import re
    
class BSTNode:
    """ An internal node for a BST .    """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

            The string will be created by an in-order traversal.
        """
        return BSTNode.printInorder(self)
        
    def printInorder(self): #compiles the inOrder traversal to be used in the __str__ method
        inorderString = []
        if self.hasLeft():
            inorderString.append(str(self._leftchild.printInorder()))
        inorderString.append(str(self._element))
        if self.hasRight():
            inorderString.append(str(self._rightchild.printInorder()))
        return ', '.join(inorderString)
    
            
    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))
    
  
    def search(self, item):
        """ Return the first subtree containing item, or None. """
        if item > self._element:
            if self.hasRight() == False:
                return None
            return self._rightchild.search(item)
        elif item < self._element:
            if self.hasLeft() == False:
                return None
            return self._leftchild.search(item)
        else:
            return self
    
    def add(self, item):
        """ Add item to the tree, maintaining BST properties.
            Note: if item is already in the tree, this does nothing.
        """
        if self == None:
            node = BSTNode(item)
            self = node
        elif item > self._element: #right subtree
            if self._rightchild == None:
                node = BSTNode(item)
                self._rightchild = node
                node._parent = self
            else: #recursively call the add method, but move the current value to the right
                return self._rightchild.add(item)
        elif item < self._element: #left subtree
            if self._leftchild == None:
                node = BSTNode(item)
                self._leftchild = node
                node._parent = self
            else: #recursively call the add method, but move the current value to the left
                return self._leftchild.add(item)
        else: # equal to a value in the tree already
            return None
                

    def findmin(self):
        """ Return the minimal element below this node. """
        if self.hasLeft(): #Go to farthest left node possible and return its element
            return self._leftchild.findmin()
        return self._element
            

    def _findminnode(self):
        """ Return the BSTNode with the minimal element below this node. """
        if self.hasLeft():
            return self._leftchild.findmin()
        return self

    def findmax(self): #Go to the farthest right node and return its element
        """ Return the maximal element below this node. """
        if self.hasRight():
            return self._righchild.findmax()
        return self._element

    def _findmaxnode(self):
        """ Return the BSTNode with the maximal element below this node. """
        if self.hasRight():
            return self._righchild.findmax()
        return self
    
    def height(self): #compare right and left branches of a node. The branch with more nodes expanding on each other is the depth
        """ Return the height of this node.

            Note that with the recursive definition of the tree the height
            of the node is the same as the depth of the tree rooted at this
            node.
        """
        leftheight = -1
        rightheight = -1
        if self.hasLeft():
            leftheight = self._leftchild.height()
        if self.hasRight():
            rightheight = self._rightchild.height()
        return (1 + max(leftheight, rightheight)) 

    def size(self): #traverses across the entire tree and returns how many nodes are in it
        """ Return the size of this subtree.

            The size is the number of nodes (or elements) in the tree.
        """
        size = 1
        if self.hasLeft():
            size += self._leftchild.size()
        if self.hasRight():
            size += self._rightchild.size()
        return size

    def hasLeft(self): #returns True if the current node has a left child
        if self._leftchild != None:
            return True
        return False
    
    def hasRight(self): #returns True if the current node has a right child
        if self._rightchild != None:
            return True
        return False
    
    def numChildren(self): #returns the number of children of the current node for later methods
        numChildren = 0
        if self.hasRight():
            numChildren += 1
        if self.hasLeft():
            numChildren += 1
        return numChildren
    
    def leaf(self): #the current node has no children
        """ Return True if this node has no children. """
        if self.numChildren() == 0:
            return True
        return False
    
    def semileaf(self): #current node only has one child. Doesn't say left or right though
        """ Return True if this node has exactly one child. """
        if self.numChildren() == 1:
            return True
        return False

    def full(self): #current node has 2 children
        """ Return true if this node has two children. """
        if self.numChildren() == 2:
            return True
        return False

    def internal(self): #current node has 1-2 children
        """ Return True if this node has at least one child. """
        if self.numChildren() >= 1:
            return True
        return False
    
    def root(self): #current node is the root
        if self._parent == None:
            return True
        return False       
            
    def remove(self, item):
        """ Remove and return item from the tree rooted at this node.

            Maintains the BST properties.
        """
        node = self.search(item)
        if node != None:
            if node.leaf(): #removes the leaf node by deleting all connections to the parent if not the root, then deletes its element
                if node._parent:
                    if node._parent._leftchild == node:
                        node._parent._leftchild = None
                    else:
                        node._parent._rightchild = None
                    del node
                else:
                    node._element = None
                return item
            elif node.semileaf(): #removes the semi leaf by checking if it has a right or left child. If the node has a parent its
                #connections are made. Otherwise the current node is connected to the child
                if node.hasLeft():
                    child = node._leftchild
                    node._leftchild = None
                else:
                    child = node._rightchild
                    node._rightchild = None
                if node._parent:
                    if node._parent._leftchild == node:
                        node._parent._leftchild = child
                        child._parent = node._parent
                    else: 
                        node._parent._rightchild = child
                        child._parent = node._parent
                    node._parent = None
                    node._element = None
                else:
                    node._leftchild = child._leftchild
                    if node._leftchild != None:
                        node._leftchild._parent = node
                    node._rightchild = child._rightchild
                    if node._rightchild != None:
                        node._rightchild._parent = node
                    node._element = child._element
                    child._leftchild = None
                    child._rightchild = None
                    child._parent = None
                    child._element = None
                return item
            if node.full(): #removes the full node by going left once and as far right as possible and putting that node in the current one. Then deletes the other node
                parent = node
                temp = node._leftchild
                #loops through the tree until the farthest ride node is found
                while temp.hasRight():
                    parent = temp
                    temp = temp._rightchild
                node._element = temp._element
                #if the prev node(parent)'s right child is the node to be switched then have the parent call this nodes left child
                if parent._rightchild == temp:
                    parent._rightchild = temp._leftchild
                    #checks if the parent's child call is anything to finish the connection upward
                    if parent._rightchild != None:
                        temp._leftchild._parent = parent
                #if the prev node(parent)'s left child is the node to be switched then have the parent call this nodes left child
                if parent._leftchild == temp:
                    parent._leftchild = temp._leftchild
                    #checks if the parent's child call is anything to finish the connection upward
                    if parent._leftchild != None:
                        temp._leftchild._parent = parent
                #Cleans up old node that has replaced the removed one   
                temp._element = None
                temp._leftchild = None
                temp._parent = None
                return item
        return None

    def _remove_node(self):
        """ (Private) Remove this BSTBode from its tree.

            Maintains the BST properties.
        """
        #if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild up into its place, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild up into its place, and clean up
            #return the original element
        # method body goes here

    def _pullup(self, node):
        """ Pull up the data from a child (subtree) node into this BSTNode.

            Note: rather than updates the links so that the child node takes
            the place of the removed semileaf, instead, we will copy the
            child's element into the semileaf, and then readjust the links, and
            then remove the now empty child node. This means that when we remove
            a root semileaf, the code that called the remove method still
            maintains a reference to the root of the tree, and so can continue
            processing the tree (otherwise, if we removed the actual BSTNode
            that was the root, the calling code would lose all reference to
            the tree). 
        """
        # method body goes here

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if self._isthisapropertree() == False:
            print("ERROR: this is not a proper tree. +++++++++++++++++++++++")
        outstr = str(self._element) + '(' + str(self.height()) + ')['
        if self._leftchild:
            outstr = outstr + str(self._leftchild._element) + ' '
        else:
            outstr = outstr + '* '
        if self._rightchild:
            outstr = outstr + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '*]'
        if self._parent:
            outstr = outstr + ' -- ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- *'
        print(outstr)
        if self._leftchild:
            self._leftchild._print_structure()
        if self._rightchild:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False          
        if self._parent:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok
    
    def myTest2(): #REMOVE 21 AND ASK WHY IT IS AN INPROPER TREE
        node = BSTNode(10)
        node.add(20)
        node.add(21)
        node.add(15)
        node.add(13)
        node.add(12)
        node.add(14)
        print(node._print_structure())
        node.remove(10)
        print(node._print_structure())
        print("----------------------------------------------------------")
         
          
    def _testadd():
        node = BSTNode('mushroom')
        node._print_structure()
        print('> adding greenbean')
        node.add('greenbean')
        node._print_structure()
        print('> adding radish')
        node.add('radish')
        node._print_structure()
        print('> adding pea')
        node.add('pea')
        node._print_structure()
        print('> adding pepper')
        node.add('pepper')
        node._print_structure()
        print('> adding parsnip')
        node.add('parsnip')
        node._print_structure()
        return node
    
    def _test():
        node = BSTNode(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 0)
        node.add(0)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 0)
        node.remove(0)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 6)
        node.add(6)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 1)
        node.remove(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 4)
        node.add(4)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 3)
        node.add(3)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 5)
        node.add(5)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 4)
        node.remove(4)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 3)
        node.remove(3)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 5)
        node.remove(5)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 12)
        node.add(12)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 8)
        node.add(8)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 9)
        node.add(9)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 7)
        node.add(7)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 12)
        node.remove(12)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 8)
        node.remove(8)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 9)
        node.remove(9)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 7)
        node.remove(7)
        print('Ordered:', node)
        node._print_structure()
        print(node)



def wordbst(filename):
    file = open(filename, 'r')  # open the file
    fulltext = file.read()  # read it all into one big string
    stripped = re.sub('[^a-zA-Z\s]+', '',
                      fulltext)  # remove non-letters or -spaces
    wordlist = stripped.split()  # split the string on white space into words in a list
    print(len(wordlist), 'words in total')
    bst = BSTNode(wordlist[0])
    for word in wordlist:
        bst.add(word)
    return bst


def test_books():
    filenames = ['testfile.txt',
                 'drMoreau.txt',
                 'frankenstein.txt',
                 'dracula.txt']
    words = ['blood', 'screaming', 'science']
    for name in filenames:
        print('Reading file', name)
        tree = wordbst(name)
        print('bst has stats', tree._stats())
        for word in words:
            node = tree.search(word)
            if node:
                print(word, ': (', node._stats(), ')')
                print(node)
            else:
                print(word, 'is not in', name)
                

# BSTNode._testadd()
# print("-------------------------------------------------------------------")
BSTNode._test()
# print("-------------------------------------------------------------------")
# print(test_books())





