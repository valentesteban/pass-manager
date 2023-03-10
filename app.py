password = input("What is your access code?: ")

if password != str(1234):
   quit

def view():
   with open("passwords.txt", "r") as f:
      for line in f.readlines():
         data = (line.rstrip())
         user, passw = data.split("|")
         print("User: ", user + " | Password: ", passw)

def add():
   name = input("Please enter your account name: ")
   passwd = input("Plase enter the password: ")

   with open("passwords.txt", "a") as f:
      f.write(name + "|" + passwd + "\n")

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