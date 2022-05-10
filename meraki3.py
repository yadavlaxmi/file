file=open("swathi.text","w")
list=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(list):
    file.write(list[i])
    file.write("\n")
    i+=1
file.close()