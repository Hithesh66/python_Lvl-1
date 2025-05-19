#after a south african trip,calculating the money left in us dollars
#money is in colombian pesos,peruvian soles,brazilian reais 

cp = float(input("the money left in colombian pesos:"))
ps = float(input("the money left in peruvian soles:"))
br = float(input("the money left in brazilian reais:"))

pesos = cp/4000 #value in USD =cp/exchange rate of currency ,1 USD=4000pesos
soles = ps*0.27 #here it is * because it is USD per foreign,1 peruvian soles=0.27USD
reais = br*0.20

usd = pesos+soles+reais
print(f"colombian pesos in USD={pesos:.2f}")
print(f"peruvian soles in USD={soles:.2f}")
print(f"brazilian reais in USD={reais:.2f}")

print(f"the total money left in USD={pesos}+{soles}+{reais}={usd}")

inr = usd*80.50
print(f"usd in indian rupees={inr}")