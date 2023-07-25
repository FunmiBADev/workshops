

def calc(operation, a, b):
  if operation == "+":
    return a + b
  elif operation == "-":
    return a - b
  elif operation == "x":
    return a * b
  elif operation == "/":
    if b == 0: 
      return 0
    else: 
      return a/b
  
print(calc("+", 3,5)) 
print(calc("x", 3,5)) 
print(calc("-", 15,5)) 
print(calc("/", 25,5)) 
print(calc("/", 5,0)) 

def file_processor(filename):
  with open(filename, 'r') as f:
    entries = f.read().splitlines()
    
    added_up_results = 0
    
    for entry in entries:
      if entry.startswith("calc"):
        my_entry = entry[len("calc"):].split()
        
        operation = my_entry[0]
        a = int(my_entry[1])
        b = int(my_entry[2])
        result = calc(operation, a, b)
        
        print(f'This is result' + result)
    
        