#Iterables: List, Tuple, set, Dictionary, string
nums =[12, 34, 56, 78, 90, 23, 45, 67, 89]
for item in nums:
    print("item:", item **2)

for a in [75, 38, 79, 24]:
    print("for_in_a:",a * 10)


TUPL = (2, 12, 23, 45, 34)
for b in TUPL:
    print("tupl_b:",b * 78)

for c in (23, 45, 34, 67):
    print("for_in_c:",c - 20)


set = {36, 57, 46, 89, 99}
for d in set:
    print("set_d:",d * 5)

for e in {57, 79, 25, 56}:
    print("for_in_e:",e * 15)



student = {
    "name" : "mahdi hasan",
    "email" : "mahdihasan591315@gmail.com",
    "phone" :"01789726197",
    "Fathher":"md jamal uddin"
}
for k, v in student.items():
    print("dictionary =",k, ":" ,v)

for a, b in {"name" : "mahdi hasan","email" : "mahdihasan591315@gmail.com","phone" :"01789726197","Fathher":"md jamal uddin"}.items():
    print(a,":",b)


js = "mahdihasan591315@gmail.com"
for f in js:
    print("string:",f)

for g in "masnunhasan01789@gmail.com":
    print("for_in_g:",g)

student = ["mahdi","Hasan","masnun","Mahmud"]
for h in student:
    print("student_h:", h.upper())
    


    
    







