correct_password = "python123"
attempts_used = 0

while attempts_used < 3:
    password = input("Enter correct password: ")
    attempts_used += 1

    if (password == correct_password):
        login_successful = "Access granted!"
        print(login_successful)
        print(attempts_used)
    
    else:
        login_successful = "Access denied!"       
        print(login_successful)
        print(attempts_used)
