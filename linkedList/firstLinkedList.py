class Node(object):
    def __init__(self,tag,dispenser,hora,rssi):
        self.tag = tag
        self.dispenser = dispenser
        self.hora = hora
        self.rssi = rssi
        self.nextNode = None

class LinkedList (object):
    def __init__ (self):
        self.head = None
        self.size = 0

    def insertStart(self,tag,dispenser,hora,rssi):
        self.size = self.size + 1
        newNode = Node(tag,dispenser,hora,rssi)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    ##size if you include a size in linked list
    def size (self):
        return self.size
    ##size if you do not include size in linked list you do it by iterating the linked list
    def size2(self):
        currentNode = self.head 
        size = 0
        
        while currentNode.nextNode is not None:
            size = size + 1
            currentNode = currentNode.nextNode
        return size
    def insertEnd(self, tag,dispenser,hora,rssi):
        self.size = self.size + 1
        newNode = Node(tag,dispenser,hora,rssi)
        actualNode = self.head
        if not self.head:
            self.head = newNode
        else:
            while actualNode.nextNode is not None:
                actualNode = actualNode.nextNode
            actualNode.nextNode = newNode

    def removeTag(self,tag):
        if self.head is None:
            return
        self.size= self.size -1

        currentNode = self.head
        previousNode = None
        while currentNode.tag != tag:
            if currentNode.nextNode is None:
                return print("Data not in linked list")
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None: 
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def removeDispenser(self,dispenser):
        if self.head is None:
            return
        self.size= self.size -1

        currentNode = self.head
        previousNode = None
        while currentNode.dispenser != dispenser:
            if currentNode.nextNode is None:
                return print("Data not in linked list")
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None: 
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print("tag = ",currentNode.tag)
            print("dispenser = ",currentNode.dispenser)
            print("hora = ",currentNode.hora)
            print("rssi = ",currentNode.rssi)
            print ("\n\n")
            currentNode = currentNode.nextNode


tags = []
dispensers = []
hora = []
TagsDispenserLinkedList = LinkedList() 

TagsDispenserLinkedList.insertEnd('2324344','343432434',12,-75)
TagsDispenserLinkedList.insertEnd('1234','5678',12,-75)
TagsDispenserLinkedList.printLinkedList()
print('\n')
TagsDispenserLinkedList.removeTag('1234')
TagsDispenserLinkedList.removeDispenser ('23243542325')
print('new list \n')
TagsDispenserLinkedList.printLinkedList()



        
        
        
        


        




    


