class Student:

    collage_name = "DJ COLLAGE"


    def __init__(self , name , age , roll_number , subject , marks):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.subject = subject
        self.marks = marks


    def get_avg(self):
        
        num = 0
        for i in self.marks:
            num +=i
        print(num)

user_input = input("Enter your name :")

student_1 = Student(user_input , 20 , 18 , "SCINCE" , [10,2,67,90])
student_1.get_avg()