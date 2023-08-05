def tong(a, b):
    x = a + b
    print(str(a) + " + " + str(b) + " = " + str(x) + "\n")
def hieu(a, b):
    y = a - b
    print(str(a) + " - " + str(b) + " = " + str(y) + "\n")
def tich(a, b):
    z = a*b
    print(str(a) + " * " + str(b) + " = " + str(z) + "\n")
def thuong(a, b):
    c = a / b
    print(str(a) + " / " + str(b) + " = " + str(c) + "\n")

while True:
    print("A. Tong")
    print("B. Hieu")
    print("C. Tich")
    print("D. Thuong")
    print("E. Thoat")
    choice = input("nhap lua chon cua ban: ")

    if choice == "a" or choice == "A":
        print("Tong")
        a = int(input("So thu nhat: "))
        b = int(input("So thu hai: "))
        tong(a, b)
    elif choice == "b" or choice == "B":
        print("Hieu")
        a = int(input("So thu nhat: "))
        b = int(input("So thu hai: "))
        hieu(a, b)
    elif choice == "c" or choice == "C":
        print("Tich")
        a = int(input("So thu nhat: "))
        b = int(input("So thu hai: "))
        tich(a, b)
    elif choice == "d" or choice == "D":
        print("Thuong" )
        a = int(input("So thu nhat: "))
        b = int(input("So thu hai: "))
        thuong(a, b)
    elif choice == "e" or choice == "E":
        print("Chuong trinh ket thuc!")
        quit()