input = [4,5,4,6,5,4]

count = 0

unique = []
output = {}
for i in range(len(input)):
    if input[i] not in unique :
        unique.append(input[i])

for i in range(len(unique)):
    for j in range(len(input)):
        if unique[i] == input[j]:
            count=count+1
        output.update({unique[i]:count})
       
    count = 0



#print(count)
#print(unique)
print(output)

