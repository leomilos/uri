
class binary_tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def add_value(self,value_to_insert):
        if self.value<value_to_insert:
            if self.right ==None:
                self.right = binary_tree(value_to_insert)
            else:
                self.right.add_value(value_to_insert)
        else:
            if self.left:
                self.left.add_value(value_to_insert)
            else:
                self.left = binary_tree(value_to_insert)
    def pre_fix(self):
    
        print(f' {self.value}',end = '')
        if self.left:
            self.left.pre_fix()
        if self.right:
            self.right.pre_fix()
    def in_fix(self):
    
        if self.left:
            self.left.in_fix()
        print(f' {self.value}',end = '')
        if self.right:
            self.right.in_fix()
    def pos_fix(self):
    
        if self.left:
            self.left.pos_fix()
        if self.right:
            self.right.pos_fix()
        print(f' {self.value}',end = '')



c = int(input().strip())
for i in range(c):
    n = int(input().strip())
    entrada = input().strip()
    values = list(map(int, entrada.split()))
    binary = binary_tree(values.pop(0))
    for value in values:
        binary.add_value(value)

    if i > 0:
        print()  

    print(f"Case {i + 1}:")

    print('Pre.:', end='')
    binary.pre_fix() 
    print()

    print('In..:', end='')
    binary.in_fix()  
    print()

    print('Post:', end='')
    binary.pos_fix()  
    print()

print()
