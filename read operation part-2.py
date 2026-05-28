file_read = open('Codingal.txt','r')
print("File in read.read -")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt','w')

file_write.write("File in write mode .....")
file_write.write("Hi! I am Penguin. I am 1 ")
file_wrtie.close()

file_append = open('Codingal.txt','a')

file_append.write("\n file in append mode .............")
filea_append.write("Hi! I am penguiin")
file_append.close()