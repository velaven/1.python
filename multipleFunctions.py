class AssignmentFunctions():
         
    def Subfields():
        
        lists=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("SubfieldsINAI are:")
        
        for i in lists:
              print(i)  
        
    def OddEven():
        num=int(input("Enter the number:"))
        if(num%2==0):
          print("The given no. is Even number")
          message="Even number"
        
        else:
           print("The given no. is Odd number")
           message="Odd number"
        
           return message
        
    def Percentage():
        subject1=float(input("subject1="))
        subject2=float(input("subject2="))
        subject3=float(input("subject3="))
        subject4=float(input("subject4="))
        subject5=float(input("subject5="))
        
        Total=subject1+subject2+subject3+subject4+subject5
        print(Total)
        percentage=Total/5
        print(percentage)
        msg=percentage
        return
        

    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        
        if((age>=21)and(gender=="Male")):
            print("ELIGIBLE")
        elif((age>=18)and(gender=="Female")):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
        return     
            
        
    def Triangle():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
    
        Area=0.5 * b * h
        print('Area:',Area)
    
        h1=int(input("Height 1:"))
        h2=int(input("Height 2:"))
        b=int(input("Breadth:"))
    
        perimeter= (h1+h2+b)
        print('perimeter:',perimeter)
    
        return