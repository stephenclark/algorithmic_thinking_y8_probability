# Simulates all the possible addition of two six sided dice rolls 
rows = 6
columns = 6

# Initialize matrix 
matrix = []
results = [] 
for r in range(rows):          # A for loop for row entries 
    a =[] 
    for c in range(columns):      # A for loop for column entries 
         a.append("({}, {} = {})".format(r+1,c+1, r+c+2))
         results.append(r+c+2)
    matrix.append(a) 

for line in matrix:
    print ('  '.join(map(str, line)))

for i in range(2,max(results)+1):
    print("number of {}'s = {}".format(i, results.count(i)))
