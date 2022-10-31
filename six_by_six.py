# Simulates all the possible addition of two six sided dice rolls 
R = C = 6
# Initialize matrix 
matrix = []
results = [] 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append("({}, {} = {})".format(i+1,j+1, i+j+2))
         results.append(i+j+2)
    matrix.append(a) 

for line in matrix:
    print ('  '.join(map(str, line)))

for i in range(2,max(results)+1):
    print("number of {}'s = {}".format(i, results.count(i)))
