#number pad with 2d lists and nested loops

num_pad=[[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         ["*", 0, "#"]]

#print(num_pad)

#for row in num_pad:
#    print(row)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()    
