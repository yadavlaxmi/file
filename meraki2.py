obj=open("swathi.txt","r")
count=0
for line in obj:
    if obj!="\n":
        count+=1
print(count)
obj.close()

    