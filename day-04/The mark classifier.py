#Day 4 Activity1 :The mark classifier
mark=int (input("Enter student mark"))

if mark<0 and mark>100 :
    print("Invalid mark")
    
elif mark>=80 and mark<=100:
    print("Outstanding")

elif mark>=70 and mark<=70:
    print("Highly competent")

elif mark>=50 and mark<=69:
    print("Competent")

elif mark>=40 and mark<=49:
    print("Not yet competent")
    
if mark>=0 and mark<=39:
    print("Not achieved")




   

    
    