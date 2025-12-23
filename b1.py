f=open(r"C:\Users\ankita\Desktop\Passport photo.jpeg","rb")
f1=open(r"C:\Users\ankita\Desktop\photo.jpeg","wb")
for i in f:
    f1.write(i)
print("Photo created")
f.close()
f1.close()
