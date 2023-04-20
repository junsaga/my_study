numbers= [1,2,3,5,4,6,1,2,3,4,5,6]
counter ={}

for number in numbers:
    if number in counter:
        counter[number] =counter[number]+1
    else:
        counter[number] =1

#최중출력
print(counter)