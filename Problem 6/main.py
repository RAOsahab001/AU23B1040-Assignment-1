AS=int(input("Annual Site Profit: "))
CCR=int(input("Current Conversion Rate: "))
ICR=int(input("Improved Conversion Rate: "))
IMC=int(input("Improvemenet Cost: "))
EPL=int(input("Expected Project Life: "))
i=0.05

def Future_gain_from_improvement():
    n = ((AS*(ICR/CCR)))-(AS)*((1+i)**EPL-1)/(i-(IMC*(1+i)**EPL))
    return n

print(Future_gain_from_improvement())

def Total_gain_from_improvement():
    l=Future_gain_from_improvement()/(i+1)**EPL
    return l

def Annnual_gain_from_improvement():
    s=Total_gain_from_improvement()/EPL
    return s

def Annual_ROI():
    a=Annnual_gain_from_improvement()/IMC
    return a

def Total_ROI():
    b=Total_gain_from_improvement()/IMC
    return b
