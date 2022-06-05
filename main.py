pesel = "76112809756"

year = pesel[0:2]
month = int(pesel[2:4])
day = int(pesel[4:6])
gender = pesel[9]

if day > 31:
    print("askfdl;j;alsdkjf")
    exit()

if month > 12 % 20:
    print("niepoprawny miesiac urodzenia")
    exit()
print("nr pesel jest ok")
#jescze troche kodu

#jakaś kolejna linia kodu

#zmiana atrakcyjna dla wszystkich branczy

