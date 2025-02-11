#colombian peso to usd : 1 colombian peso = 0.00024 usd
#peruvian sol to usd : 1 sol = 0.27 usd
#brazilian reai to usd : 1 reai = 0.16 usd

pesos = int(input("What do you have left in pesos?"))
soles = int(input("What do you have left in soles?"))
reais = int(input("What do you have left in reais?"))

usd = (pesos * 0.00024)+(soles * 0.27)+(reais * 0.16)
print(usd)