student = {
    "Name"          :"Mahdi Hasan" "\n" "masnun",
    "Age"           :"16",
    "Phone"         :"01789726197",
    "Email"         :"mahdihasan591315@gmail.com",
    "Cuntry"        :"BD",
    "Father's name" :"MD Jamal Uddin",
    "Mother's name" :"Razia",
    "Address"       :"Pirojpur",
    "Date of Birth" :"01-01-2005",
    "Facebook_ID"   :"MAHDI HASAN" 

}

profile ={
    "Name"         : "MASNUN HASAN",
    "Twitter_ID"   : "@MAHDIHASAN95",
    "YouTube_ID"   : "VIERAITIS VIDEOS",
    "Instgram_ID"  : "MAHDIHASAN833"
}
print(type(student))
print(student["Name"])
print(student.get("Email"))
student_cp = student.copy()
print(student_cp)



student_ID = {
    "MAHDI HASAN"  : """NAME          = 'MAHDI HASAN' 
                        Father's Name = 'MD Jamal Uddin' 
                        Mother's Name = 'Razia'
                        Age           = '16'
                        Date of Birth = '01-01-2005'
                        Address       = 'Pirojpur'
                        Email         = 'mahdihasan591315@gmail.com'
                        Phone         = '01789726197'
                        Cuntry        = 'BD' """,
    
    "MASNUN HASAN" : """NAME          = 'MASNUN HASAN'
                        Father's Name = 'MD Jamal Uddin'
                        Mother's Name = 'Razia'
                        Age           = '14'
                        Date of Birth = '03-07-2007'
                        Address       = 'Dhaka'
                        Email         = 'masnunhasan01789@gmail.com'
                        Phone         = '01709120939'
                        Cuntry        = 'BD' """, 
    
    "MAHMUD HASAN" : """NAME          = 'MAHMUD HASAN'
                        Father's Name = 'MD Jamal Uddin'
                        Mother's Name = 'Razia'
                        Age           = '23'
                        Date of Birth = '02-05-1998'
                        Address       = 'Dhaka'
                        Email         = 'mahmudhasan5406@gmail.com'
                        Phone         = '01988466511'
                        Cuntry        = 'BD' """,                                      
}
print("         ")
print("         ")
print("Student ID of School")
print("         ")
print("                      :",student_ID.get("MAHMUD HASAN"))
#print(student_ID.items())

print(student.keys())
print(student.values())
student["Class"] = "Eight"
del student["Date of Birth"]
student.pop("Facebook_ID")
print("Student_of_ID:",student)
student.update(profile)
print(student)
new_student_dict = {**student,**profile}
print(new_student_dict)
print(student | profile)
student |= profile

