def main():
    print('From Main Program')
    
print('From Local Code')

if __name__=="__main__":
    print('Printing message from Main Method')
    main()
    
print('Value of the function being called : '+ __name__)