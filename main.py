import tkinter as tk

window = tk.Tk()

window.title('Tic Tac Toe')
window.geometry("600x700")
window.configure(bg="Blue")


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
    if not romanNumeralPattern.search(a):  # if you want close copy libary part. just comment line 20,21
        valider = True                   # i can't fix something like IVI and maybe diffrent thing idk.
    # copy libary part ------------------# but calculation code is mine but i know it is not optimal.

    a = a + "*"
    passer = False
    value = 0
    if not valider:
        for b in range(len(a)):
            if not passer:
                if a[b] == "I":
                    if a[b+1] == "V":
                        value = value + 4
                        passer = True
                    elif a[b+1] == "X":
                        value = value + 9
                        passer = True
                    elif a[b+1] in ["L", "C", "D", "M"]:
                        print("returnu bozuk at.")
                    else:
                        value = value + 1
                if a[b] == "V":
                    # v sayı ölçer koy buraya
                    if a[b+1] in ["X", "L", "C", "D", "M"]:
                        print("return bozuk at")
                    else:
                        value = value + 5
                if a[b] == "X":
                    if a[b+1] == "L":
                        value = value + 40
                        passer = True
                    elif a[b+1] == "C":
                        value = value + 90
                        passer = True
                    elif a[b + 1] in ["L", "D", "M"]:
                        print("returnu bozuk at.")
                    else:
                        value = value + 10
                if a[b] == "L":
                    # l sayı ölçer koy buraya
                    if a[b+1] in ["C", "D", "M"]:
                        print("return bozuk at")
                    else:
                        value = value + 50
                if a[b] == "C":
                    if a[b+1] == "D":
                        value = value + 400
                        passer = True
                    if a[b+1] == "M":
                        value = value + 900
                        passer = True
                    else:
                        value = value + 100
                if a[b] == "D":
                    # d sayı ölçer koy buraya
                    if a[b+1] in ["M"]:
                        print("return bozuk at")
                    else:
                        value = value + 500
                if a[b] == "M":
                    # m sayı ölçer koy buraya
                    value = value + 1000
            else:
                passer = False
            if a[b+1] == "*":
                break
    else:
        p2.delete(0, 100)
        p2.insert(0, a[0:-1] + " IS NOT VALID")
    return value


player1 = tk.Label(window, text="Enter Convert Decimal Number", fg="black", bg="blue", font=("Courier", 20, "bold"))
player1.place(x=75, y=100)

player2 = tk.Label(window, text="Converting roman numbers in txt file", fg="black", bg="blue", font=("Courier", 20, "bold"))
player2.place(x=10, y=250)

player3 = tk.Label(window, text="Input name of txt file", fg="white", bg="blue", font=("Courier", 10, "bold"))
player3.place(x=35, y=300)

player4 = tk.Label(window, text="Output name of txt file", fg="white", bg="blue", font=("Courier", 10, "bold"))
player4.place(x=390, y=300)

player5 = tk.Label(window, text="Result", fg="black",bg="blue", font=("Courier", 20, "bold"))
player5.place(x=255, y=500)

p1 = tk.Entry(window)
p1["font"] = "Courier", 15
p1.place(x=180, y=150)

p2 = tk.Entry(window, width=20)
p2["font"] = "Courier", 30
p2.place(x=55, y=550)

p3 = tk.Entry(window)
p3["font"] = "Courier", 15
p3.pack(padx=5, pady=15, side=tk.LEFT)

p4 = tk.Entry(window)
p4["font"] = "Courier", 15
p4.pack(padx=5, pady=15, side=tk.RIGHT)

button1 = tk.Button(master=window, text='Manuel', width=15, height=3, bg='white', relief=tk.RAISED,
                    command=lambda: converter_1())
button1.place(x=250, y=180)

button2 = tk.Button(master=window, text='Auto', width=15, height=3, bg='white', relief=tk.RAISED,
                    command=lambda: converter_2())
button2.place(x=250, y=380)


def converter_1():
    single_input = p1.get()
    if romantoNumber(single_input) != 0:
            p2.delete(0, 100)
            p2.insert(0, romantoNumber(single_input))


def converter_2():
    global txtfile, txtfile1

    try:
        genre = p3.get()
        txtfile = open(genre + ".txt", "r").read().splitlines()
    except OSError as e:
        print(e.errno)
        p2.delete(0, 100)
        p2.insert(0, "file is not defined")

    try:
        genre1 = p4.get()
        txtfile1 = open(genre1 + ".txt", "w")
        txtfile1.write("")
    except OSError as e:
        print(e.errno)
        p2.delete(0, 100)
        p2.insert(0, "file is not defined")
    
    problem = 0
    with txtfile1 as file:
            for i in txtfile:
                if romantoNumber(i) == 0:
                    problem = problem + 1
                    file.write(str(romantoNumber(i)) + "\n")
                else:
                    file.write(str(romantoNumber(i)) + "\n")
            print("---------")
            p2.delete(0, 100)
            p2.insert(0, "Found Problem:" + str(problem))
            print("Found Problem:" + str(problem))


window.mainloop()
