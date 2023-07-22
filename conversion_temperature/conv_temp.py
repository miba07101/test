import math
f_list = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650]

def to_celsius(x):
    # return round(((x - 32) * 5/9))
    return round(math.ceil((x - 32) * 5/9),0)

def to_fahrenheit(x) :
    return round(math.ceil((x * 9/5) + 32),-1)

c_list = []
for temp in f_list:
    c_list.append(to_celsius(temp))

fc_list = []
for temp in c_list:
    fc_list.append(to_fahrenheit(temp))

print(f_list)
print(c_list)
print(fc_list)
