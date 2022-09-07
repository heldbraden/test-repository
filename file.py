#A simple, yet polite, program for your pleasure :) 
def greetings ():
    print ("May I please have your name? ")
    name = input()
    print ("Welcome " + name + "! Thank you for your name. Are you doing well today? (Y/N)")
    response = input() 
    if response == "Y":
        print ("I am glad to hear!")
    elif response == "N": 
        print ("I am sorry to hear that :(")
    else: 
        print ("I don't know what " + response + " means. Sorry.")

greetings() 