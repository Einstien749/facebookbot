from requests import post

def login():
    email = input("Enter Your Mail :")
    password = input("Enter Your Password :")
    login_url = "https://www.facebook.com/login"
    my_data = {"email":email, "pass":password}
    try:
        b = post(login_url, json=my_data)
        print(b.text)
    except:
        print("Invalid Credentials")
        

def Register():
    firstname = input("Enter Your First Name :")
    firstname = input("Enter Your Last Name :")
    reg_email__ = input("Enter Your Mail :")
    reg_password__ = input("Enter Your Password :")
    birthday_day = int(input("Enter Your Birth Day :"))
    birthday_month = int(nput("Enter Your Birth Month :"))
    birthday_year = int(input("Enter Your Birth Year :"))
    sex = int(input("Enter Your Sex. 1 for Male, 2 For Female :"))
    #password = input("Enter Your Password :")
    register_url = "https://www.facebook.com/login"
    my_data = {"firstname":firstname, "pass":password, "reg_email__":reg_email__,"reg_password__":reg_password__, "birthday_day":birthday_day,"birthday_month":birthday_month, "birthday_year":birthday_year, "sex":sex}
    try:
        post(register_url, json=my_data)
    except:
        print("Invalid Credentials")


login()

        
        
