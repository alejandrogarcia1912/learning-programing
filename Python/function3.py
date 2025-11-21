def showGreeting2(userName):
    msg = "Hello " + userName + ", welcome"
    
    return msg

# Main
print("Enter your name: ")
userName = input()
message = showGreeting2(userName)
print(message)