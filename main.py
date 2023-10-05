print("Hello world")
while True:
    d = int(input("ENter ur no. :"))
    d = str(d)
    f = d[::-1]
    if   (d == "0") :
        print("INVALID INPUT")
        
    elif d == f :
        print('This no. is a pallindrom ')   
        break
    else :
        print("THis no. is not a pallindrom ")
        break

