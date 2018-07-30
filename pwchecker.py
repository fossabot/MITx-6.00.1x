pw_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*() "

pw = input('Enter a password: ')

pw_iterator = 0 # iterates through the password checking for acceptable letters

while pw_iterator < len(pw):
    char = pw[pw_iterator]
    if char in pw_letters:
        pw_iterator += 1
        if pw_iterator == len(pw):
            print('Creating your account...') 
    else:
        print (char + " is not an acceptable character.")
        pw = input('Enter your password: ') # if the password has an unnacceptable letter
                                            # it will prompt again for a password