M = int(input("Enter the number of rows:"))
N = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:");
for i in range(M):          # A for loop for row entries
    a =[]
    for j in range(N):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(M):
    for j in range(N):
        print(matrix[i][j], end = " ")
    print()