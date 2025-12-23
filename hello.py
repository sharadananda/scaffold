def toyou(x):
    return f"hi {x}"
    
def subtract(x):
    return x - 1
    
def add(x, y):
    return x + y

#var = 
result = add(1, 2)
# print(f"This is the sum: 1, 2, {result}") # supported python 3.6 and later
print("This is the sum: 1, 2, %s" % result)