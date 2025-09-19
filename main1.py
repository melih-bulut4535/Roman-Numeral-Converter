import tkinter as tk
from collections import OrderedDict
import collections
window = tk.Tk()

window.title('Tic Tac Toe')
window.geometry("600x700")
window.configure(bg="red")


player1 = tk.Label(window, text="Enter Convert Decimal Number", fg="black", bg="white", font=("Courier", 20))
player1.place(x=75, y=10)

p1 = tk.Entry(window)
p1["font"] = "Courier", 15
p1.place(x=335, y=150)

p2 = tk.Entry(window, width=20)
p2["font"] = "Courier", 30
p2.place(x=55, y=450)

p3 = tk.Entry(window, width=20)
p3["font"] = "Courier", 30
p3.place(x=55, y=550)

text = tk.Text(window, height=18, width=40)
scroll = tk.Scrollbar(window)
text.configure(yscrollcommand=scroll.set)
text.place(x=5, y=100)

scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

player1 = tk.Label(window, text="Shortest spelling of roman numeral", fg="black", bg="white", font=("Courier", 15, "bold"))
player1.place(x=80, y=520)

player2 = tk.Label(window, text="Repeating roman numeral", fg="black", bg="white", font=("Courier", 15, "bold"))
player2.place(x=155, y=420)

button1 = tk.Button(master=window, text='Manuel', width=15, height=3, bg='white', relief=tk.RAISED,
                    command=lambda: start())
button1.place(x=400, y=200)

txtfile = open("txtfile.txt", "r").read().splitlines()




def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


def romantoNumber(b):
    a = b
    # copy libary part ----------------------
    import re
    valider = False
    romanNumeralPattern = re.compile("""
        ^                   # beginning of string
        M{0,4}              # thousands - 0 to 4 M's
        (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                            #            or 500-800 (D, followed by 0 to 3 C's)
        (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                            #        or 50-80 (L, followed by 0 to 3 X's)
        (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                            #        or 5-8 (V, followed by 0 to 3 I's)
        $                   # end of string
        """, re.VERBOSE)
    if not romanNumeralPattern.search(a):
        valider = True
    
    a = a + "*"
    passer = False
    value = 0
    if not valider:
        for b in range(len(a)):
            if not passer:
                if a[b] == "I":
                    if a[b + 1] == "V":
                        value = value + 4
                        passer = True
                    elif a[b + 1] == "X":
                        value = value + 9
                        passer = True
                    elif a[b + 1] in ["L", "C", "D", "M"]:
                        print("returnu bozuk at.")
                    else:
                        value = value + 1
                if a[b] == "V":
                    # v sayı ölçer koy buraya
                    if a[b + 1] in ["X", "L", "C", "D", "M"]:
                        print("return bozuk at")
                    else:
                        value = value + 5
                if a[b] == "X":
                    if a[b + 1] == "L":
                        value = value + 40
                        passer = True
                    elif a[b + 1] == "C":
                        value = value + 90
                        passer = True
                    elif a[b + 1] in ["L", "D", "M"]:
                        print("returnu bozuk at.")
                    else:
                        value = value + 10
                if a[b] == "L":
                    # l sayı ölçer koy buraya
                    if a[b + 1] in ["C", "D", "M"]:
                        print("return bozuk at")
                    else:
                        value = value + 50
                if a[b] == "C":
                    if a[b + 1] == "D":
                        value = value + 400
                        passer = True
                    if a[b + 1] == "M":
                        value = value + 900
                        passer = True
                    else:
                        value = value + 100
                if a[b] == "D":
                    # d sayı ölçer koy buraya
                    if a[b + 1] in ["M"]:
                        print("return bozuk at")
                    else:
                        value = value + 500
                if a[b] == "M":
                    # m sayı ölçer koy buraya
                    value = value + 1000
            else:
                passer = False
            if a[b + 1] == "*":
                break
    else:
        print(a[0:-1] + " IS NOT VALID")
    return value


def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num


def start():
    decimal_number = int(p1.get())
    same_number = []
    for i in txtfile:
        if romanToInt(i) == decimal_number:
            same_number.append(i)
    
    p2.delete(0, 100)
    p2.insert(0, same_number)
    
    print(same_number)
    
    for j in range(0, len(same_number)):
        romantoNumber(same_number[j])

    p3.delete(0, 100)
    p3.insert(0, write_roman(decimal_number))

for i in txtfile:
    insert_text = []
    insert_text.append(romanToInt(i))
    insert_text.append("\n")
    text.insert(tk.END, insert_text)

window.mainloop()
