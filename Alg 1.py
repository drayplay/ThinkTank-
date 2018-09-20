class Stack:
    def __init__(self):
        self.items = [] # This initializes the list/stack
        
    def push(self,data):
         self.items.append(data) #Will add data to the stack
         
    def pop(self):
         self.items.pop() # Function that pops the last thing on the stack out 
         
    def empty(self):
         return self.items == []
    def show(self):
        return self.items
    
    def peek(self):
        return self.items[len(self.items)-1]        
# Shirt list is S, Pants is P, Undergarnment is U
U = Stack()
S = Stack()
P = Stack()
#Initialize our 

#Input statements for stacks
s = int(input("How many shirts do you have: "))
u = int(input("How many misc. items do you have: "))
p = int(input("How many pants do you have: "))

print("Now we need to know the total of items you have.")
#total number of 
so = int(input("How many total shirts do you have: "))
uo = int(input("How many total misc. items do you have: "))
po = int(input("How many total pants do you have: "))

U.push(u)
S.push(s)
P.push(p)
po = u*s*p
to = so*uo*po
ao = to//po 
print(to)
print(ao)

if ao in range(0,10):
    print("Wash your clothes on Sunday") 
elif ao in range(11,20):
    print("Wash your clothes on Monday")
elif ao in range(21,30):
    print("Wash your clothes on Tuesday")
elif ao in range(31,40):
    print("Wash your clothes on Wednesday")
elif ao in range(41,50):
    print("Wash your clothes on Thursday")
elif ao in range(51,60):
    print("Wash your clothes on Friday")
elif ao in range(61,70):
    print("Wash your clothes on Saturday")
elif ao in range(71,80):
    print("Wash your clothes on Sunday")
elif ao in range(81,90):
    print("Wash your clothes on Monday")
elif ao in range(91,100):
    print("Wash your clothes on Tuesday")
elif ao in range(100,300):
    print(-1)
   
