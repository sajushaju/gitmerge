defualt_user="admin"
defualt_password="123456"
username=input("enter your username: ")
password=input("enter your password: ")
if username==defualt_user and password==defualt_password:
    print("login successful")
else:
    print("login failed")