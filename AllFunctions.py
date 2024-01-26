class Allfunctions():
    def Subfields():
        Field1="Machine learning"
        Field2="Neural Networks"
        Field3="Vision"
        Field4="Robotics"
        Field5="Speech Processing"
        Field6="Natural Language Processing"
        print("Sub-fields in AI are:")
        print(Field1)
        print(Field2)
        print(Field3)
        print(Field4)
        print(Field5)
        print(Field6)

    def OddEven():
        Num=int(input("Enter a number: "))
        if (Num%2)==0:
            print(Num,"is Even number")
            result="Even number"
        else:
            print(Num,"is Odd number")
            result="Odd number"
        return result  

    def Eligible():
        Gender=input("Enter Gender: ")
        Age=int(input("Enter Age: "))
        if(Gender=="Male"):
            if(Age>=21):
                print("ELIGIBLE")
                status="ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                status="NOT ELIGIBLE"
        if(Gender=="Female"):
            if(Age>=18):
                print("ELIGIBLE")
                status="ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                status="NOT ELIGIBLE"
        return status   
    
    def percentage():
        Sub1=int(input("Subject1: "))
        Sub2=int(input("Subject2: "))
        Sub3=int(input("Subject3: "))
        Sub4=int(input("Subject4: "))
        Sub5=int(input("Subject5: "))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        Percent=(Total/500.0)*100
        print("Total : ",Total)
        print("Percentage : ", Percent)
        
    def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        Area=(Height*Breadth)/2
        print("Area formula=(Height*Breadth)/2")
        print("Area of Triangle: ",Area)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))
        Perimeter=Height1+Height2+Breadth
        print("Perimeter formula= Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Perimeter)