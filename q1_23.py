# ~~~ This is a template for question 1  ~~~

# Imports:

###Part A###
# Implement Stack class:


class Linkedlist:

    def __init__(self, value):
        self.nextnode = 0
        self.value = value


class Stack:

    def __init__(self):
        self.head = 0
        self.size = 0


    def top(self):
        if not self.empty():
            return self.head
        return "Stack is Empty"

    def empty(self):
        if self.size == 0:
            return True
        return False

    def push(self, x):

        e = Linkedlist(x)
        e.nextnode = self.head
        self.head = e
        self.size += 1
        return


    def pop(self):
        if self.empty():
            return "Stack Empty"
        x = self.head
        self.head = x.nextnode
        self.size -= 1
        return x.value


###Part B###


def string_testing(strg):
    try:
        if not isinstance(strg, str):  # making sure user entered a string
            raise ValueError
        if len(strg) == 0:  # empty string was given
            raise ValueError
        stack = Stack()
        iarr = []  # array for storing opened parenthesises' indexes, max size of array is n
        for i in range(len(strg)):
            if strg[i] == "{" or strg[i] == "[" or strg[i] == "(":  # stack pushes open parenthesis types
                stack.push(strg[i])  # pushing to stack
                iarr.append(i)  # saving index to array
            if strg[i] == "}" or strg[i] == "]" or strg[i] == ")":
                if stack.size > 0:  # making sure stack isn't empty
                    el = stack.pop()
                    iarr = iarr[:-1]  # removing the index of last closed element from array
                    if el + strg[i] == "{}" or el + strg[i] == "[]" or el + strg[i] == "()":
                        continue
                if stack.size == 0:  # case of wrong side parenthesis in string - }
                    print("False, Bad parenthesis is {} at index {}".format(strg[i], i + 1))
                    return False
        # case for string ending
        if stack.size > 0 and i + 1 == len(strg):  # case of string ending without a closing parenthesis
            print("False, No closing parenthesis for {} at index {}".format(stack.top.value, iarr[-1] + 1))
            return False
        print("True")
        return True

    except ValueError:
        print("No string or illegal input was given")

    #  time complexity of O(n) - runtime depends on size of string
