count=0
for i in range(2,11):
    for j in range(2,11):
        for k in range(2,11):
            if i+j+k==10:
                print(i,j,k)
                count+=1
print(count)