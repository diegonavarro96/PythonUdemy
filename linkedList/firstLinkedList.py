import time
import random
MaxNum = 3
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

    def insertStart(self,tag,dispenser,hora,rssi):
        self.size = self.size + 1
        newNode = Node(tag,dispenser,hora,rssi)
        if not self.head:
            self.head = newNode
        else:
            if self.sizeMayorAThresh(MaxNum):
                self.removeLast()
            newNode.nextNode = self.head
            self.head = newNode
    ##size if you do not include size in linked list you do it by iterating the linked list
    def sizeMayorAThresh(self,threshold):
        currentNode = self.head 
        size = 0
        while currentNode is not None:
            size = size + 1
            currentNode = currentNode.nextNode
        return size >= threshold

    def removeLast(self):
        if self.head is None:
            return
        self.size= self.size -1

        currentNode = self.head

        if currentNode.nextNode is None:
            currentNode = None
            return
        while currentNode.nextNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = None
        
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print("tag = ",currentNode.tag)
            print("dispenser = ",currentNode.dispenser)
            print("hora = ",currentNode.hora)
            print("rssi = ",currentNode.rssi)
            print ("\n")
            currentNode = currentNode.nextNode


tagsPrueba = ['0773a3f','0773fff','0772345','077afe4','077eeff','07734ca']  
dispensersPrueba = ['a1a1ae2','a1a1fe2','a1a1acb3','a1a1eb12','a1a1af65','a1a1ab45']       
tags = []
dispensers = []
horas = []
TagsDispenserLinkedList = LinkedList() 

def llegaDisp(disp,hora,rssi):
    global dispensers
    global horas
    global TagsDispenserLinkedList
    if disp not in dispensers:
        dispensers.append(disp)
        dispI = len(dispensers) -1
    else:
        cont = 0
        while dispensers[cont] != disp:
            cont = cont + 1
        dispI = cont
    if hora not in horas:
        horas.append(hora)
        horaI = len(dispensers) -1
    else:
        cont = 0
        while horas[cont] != hora:
            cont = cont + 1
        horaI = cont
    
    TagsDispenserLinkedList.insertStart(-1,dispI,horaI,rssi)


def llegaTag(tag,hora,rssi):
    global tags
    global horas
    global TagsDispenserLinkedList
    if tag not in tags:
        tags.append(tag)
        tagI = len(tags) -1
    else:
        cont = 0
        while tags[cont] != tag:
            cont = cont + 1
        tagI = cont
    if hora not in horas:
        horas.append(hora)
        horaI = len(dispensers) -1
    else:
        cont = 0
        while horas[cont] != hora:
            cont = cont + 1
        horaI = cont
    
    TagsDispenserLinkedList.insertStart(tagI,-1,horaI,rssi)
def llegadispOTag(dispTag,dispTagIndex,hora,rssi):
    global dispensersPrueba
    global tagsPrueba
    if dispTag == 1:
        llegaDisp(dispensersPrueba[dispTagIndex],hora,rssi)
    else:
        llegaTag(tagsPrueba[dispTagIndex],hora,rssi)

def mandarABroker():
    TagsDispenserLinkedList.removeLast()
while True:
    aux1 =random.randint(0,2)
    aux2 = random.randint(0,5)
    aux3 =random.randint(0,23)
    aux4 =random.randint(-78,-50)
    if aux1 == 1:
        print("llego dispenser con ",dispensersPrueba[aux2],'  hora =',aux3, '  rssi =',aux4)
        llegadispOTag(aux1,aux2,aux3,aux4)
    elif aux1 == 0:
        print("llego tag con ",tagsPrueba[aux2],'   hora =',aux3, '  rssi =',aux4)
        llegadispOTag(aux1,aux2,aux3,aux4)
    else:
        print('Mandamos a Broker')
        mandarABroker()

    TagsDispenserLinkedList.printLinkedList()
    print ("tags =",tags)
    print ("Dispensers = ",dispensers)
    print ("horas = ",horas)
    print('-------------------------------------------------------------------')
    time.sleep(5)


TagsDispenserLinkedList.printLinkedList()
print ("tags =",tags)
print ("Dispensers = ",dispensers)
print ("horas = ",horas)



        
        
        
        


        




    


