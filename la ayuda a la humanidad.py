
import readchar
specia=["\r","\x08"]
hystorial=[]
forbiddenWords=["PORN","MILK-CHAN"]
while True:
    tecla=readchar.readkey()
    if tecla and not tecla in specia:
        hystorial.append(tecla)
        hystorialVeredict="".join(hystorial)
        if hystorialVeredict.upper() in forbiddenWords:
            print("Dont give up soldier!")
            hystorial.clear()
        print(hystorial)
        print(hystorialVeredict)
    else:
        if len(hystorial) >= 1 and :
            del hystorial[-1]
        print("no word")