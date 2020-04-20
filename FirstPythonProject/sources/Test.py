from sources import MainFunction

# Declaring variable and initializing it
x = 0
print(x)
y='abc'
print(y)
x=str(x)+y
print(x)
def testFunction():
    global x
    x = 100
    print(x)
testFunction()
print(x)
print('Hello')