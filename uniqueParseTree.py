import operator  # Required for 'evaluation' fn


class newNode:
    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Implementation of data structures that were used throughout the algorithm:
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.right = None
        self.left = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRootVal(self):
        return self.key

    def setRootVal(self, val):
        self.key = val

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)


def breadthInTree(parseTree):
    if parseTree is not None:
        print(parseTree.getRootVal())
    current = parseTree
    myQ = Queue()
    while current is not None:
        if current.getLeftChild() is not None:
            print(current.getLeftChild().getRootVal())
            myQ.enqueue(current.getLeftChild())
        if current.getRightChild() is not None:
            print(current.getRightChild().getRootVal())
            myQ.enqueue(current.getRightChild())
        if myQ.isEmpty():
            break
        else:
            current = myQ.dequeue()


def bfs(tree):
    root = tree
    a = []
    b = []
    a.append(root)
    even = True
    while len(a) > 0:
        current = a.pop(0)
        if current.left != None:
            b.append(current.left)
        if current.right != None:
            b.append(current.right)
        if len(a) == 0:
            if even == True:
                even = False
            else:
                even = True
            a = b
            if even == False:
                for i in range(len(b)):
                    if i % 2 != 0:
                        print(b[i].data, end=" ")
            b = []


# Main algorithm, used to solve a non-parenthesized mathematical expression:
def buildUniqueParseTree(expression):
    # Splitting the given expression
    exp = expression.split()

    # Building our main tree using the first sub-expression
    eTree = BinaryTree(exp[1])
    eTree.insertLeft(int(exp[0]))
    eTree.insertRight(int(exp[2]))

    # Defining the precedence of operators
    operators = {"-": 0, "+": 0, "*": 1, "/": 1}

    # Looping through the remaining sub expression
    for i in exp[3:]:
        if i in "+-/*":
            # Building a temporary tree
            t = BinaryTree(i)
            t.insertRight('')

            # Traversing into its right child
            current2 = t
            current2 = current2.getRightChild()

            # Checking the precedence
            if operators[t.getRootVal()] <= operators[eTree.getRootVal()]:
                t.left = eTree
                eTree = t
            else:
                t.left = eTree.right
                eTree.right = t

        else:  # Token is an operand then
            # Storing the given token (operand) into the right child
            current2.setRootVal(int(i))
    return eTree


# Implementing some testing functions
def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


def inOrder(parseTree):
    if parseTree is not None:
        inOrder(parseTree.getLeftChild())
        print(parseTree.getRootVal())
        inOrder(parseTree.getRightChild())


# Testing the whole thing
myexp = input()
myTree = buildUniqueParseTree(myexp)
breadthInTree(myTree)
