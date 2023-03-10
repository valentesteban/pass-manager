from cryptography.fernet import Fernet

''' this is to create a key to access to the "program" 

def createKey():
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
      key_file.write(key)

createKey()
'''

def loadKey():
   file = open("key.key", "rb")
   key = file.read()
   file.close()
   return key

key = loadKey()
fer = Fernet(key)

def view():
   with open("passwords.txt", "r") as f:
      for line in f.readlines():
         data = (line.rstrip())
         user, passw = data.split("|")
         print("User: ", user + " | Password: ", 
               fer.decrypt(passw.encode()).decode())

def add():
   name = input("Please enter your account name: ")
   passwd = input("Plase enter the password: ")

   with open("passwords.txt", "a") as f:
      f.write(name + "|" + fer.encrypt(passwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add) press Q to quit? ")
    if mode == "q":
       print("Closing the Password Saver..")
       break
    
    if mode == "view":
      view()
    elif mode == "add":
      add()
    else:
      print("Invalid mode.")
      continue