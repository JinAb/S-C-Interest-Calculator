print("Welcome To Interest Finder By JinAB - (Abhishek Vyas)\n")
print('''Which Interest You Want To Find\n
Simple Interest (Type 1)
Compund Interest (Type 2) ''')

Interest = int(input())


pr = int(input("Enter The Principal\n"))
Ra = int(input("Enter The Rate ( In Percentage!! %  Don't use sign)\n"))
ti = int(input("Enter The Time ( In Year )\n"))

if Interest == 1:
    sip = (pr*Ra*ti)/100
    print("This Is Your Simple Interest\n", sip)

elif Interest == 2:
    Ra2 = (Ra/100 + 1)
    Ra3 = Ra2**ti 
    copA =  (pr*Ra3)   
    copC = (copA - pr)
    print("Your Compund Interest is\n", copC)
    print("Your Amonut is\n", copA)

print("Thank You for choosing us ")
