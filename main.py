info = []
info = input("Type in your customer number, ID and units consumed (separated by a space or comma):  ").split()
info[2] = int(info[2])
if info[2] < 200:
  total = info[2] * 1.2
elif info[2] < 400:
  total = info[2] * 1.5
elif info[2] < 600:
  total = info[2] * 1.8
else:
  total = info[2] * 2
if info[2] > 400:
  total *= 1.15
print("---------------------------------")
print("Customer Number:", info[0])
print("Customer ID:", info[1])
print("Total Bill Cost: ", (round(total*100)/100), '$', sep="")