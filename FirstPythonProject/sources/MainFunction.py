print('Hello World')

print("I am learning ", end='')
print("Python", end ='***')

def main():
    print('From Main Program')
    
print('From Local Code')

if __name__=="__main__":
    print('Printing message from Main Method')
    main()

if __name__=="sources.MainFunction":
    print('Message printed from Module')
    main()
    
print('Value of the function being called : '+ __name__)