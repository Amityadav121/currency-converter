print("Hello")
a=input("Enter the currency converted from: ")
b=input("Enter the currency coonverted to: ")
p=int(input("Enter the Amount: "))
#Convertng From INR
if a=="INR" :
  if b=="USD":
    cr=0.012
    print("Current Rates:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="GBP":
    cr:0.011
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="EUR":
    cr=1/83.55
    print("Current Rate:",format(cr,".4f"))
    print(a,"to",b,":",int(cr*p))
  elif b=="JPY":
    cr=1.72
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CNY":
    cr=0.088
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="RUB":
    cr=0.75
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CAD":
    cr=0.016
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
#Converting From USD
if a=="USD" :
  if b=="INR":
    cr=1/0.012
    print("Current Rates:",format(cr,".2f"))
    print(a,"to",b,":",int(cr*p))
  elif b=="GBP":
    cr=0.85
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="EUR":
    cr =0.96
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="JPY":
    cr=138.80
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CNY":
    cr=7.11
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="RUB":
    cr=60.77
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CAD":
    cr=1.33
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
#Converting from GBP
if a=="GPB" :
  if b=="USD":
    cr=1.18
    print("Current Rates:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="INR":
    cr=95.14
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="EUR":
    cr=1.14
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="JPY":
    cr=163.95
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CNY":
    cr=8.40
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="RUB":
    cr=71.52
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CAD":
    cr=1.56
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
#Converting From EUR
if a=="EUR" :
  if b=="USD":
    cr=1.04
    print("Current Rates:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="INR":
    cr=83.55
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="GBP":
    cr=0.88
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="JPY":
    cr=143.95
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CNY":
    cr=7.37
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="RUB":
    cr=62.81
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CAD":
    cr=1.37
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))

#Converting to JPY
if a=="JPY" :
  if b=="USD":
    cr=0.0072
    print("Current Rates:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="INR":
    cr=0.58
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="EUR":
    cr=0.0069
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="GBP":
    cr=0.0061
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CNY":
    cr=0.051
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="RUB":
    cr=0.44
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CAD":
    cr=0.0095
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
#Converting From CYN
if a=="CNY" :
  if b=="USD":
    cr=0.14
    print("Current Rates:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="INR":
    cr=11.33
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="EUR":
    cr=0.14
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="JPY":
    cr=19.53
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="GBP":
    cr=0.12
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="RUB":
    cr=8.53
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CAD":
    cr=0.19
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
#Converting From RUB
if a=="RUB" :
  if b=="USD":
    cr=0.016
    print("Current Rates:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="INR":
    cr=1.33
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="EUR":
    cr=1/62.81
    print("Current Rate",format(cr,".4f"))
    print(a,"to",b,":",int(cr*p))
  elif b=="JPY":
    cr=2.29
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="GBP":
    cr=0.014
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CNY":
    cr=0.12
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CAD":
    cr=0.022
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
#Converting from CAD
if a=="CAD" :
  if b=="USD":
    cr=0.75
    print("Current Rates:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="INR":
    cr=60.70
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="EUR":
    cr=0.73
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="JPY":
    cr=104.59
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="GBP":
    cr=0.64
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="RUB":
    cr=45.63
    print("Curret Rate:",cr)
    print(a,"to",b,":",int(cr*p))
  elif b=="CNY":
    cr=5.36
    print("Current Rate:",cr)
    print(a,"to",b,":",int(cr*p))