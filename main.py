from func import *
import time

print("----- WELCOME TO Vending-Machine -----")
print("----- ค่าเฟอัตโนมัติ 24 ชั่วโมง -----")

type_menu = show_type_coffee()

if type_menu == 1 or type_menu == 2 or type_menu == 3 or type_menu == 4:
    
    if type_menu == 1:
        menu_coffee = show_menu_coffee()
        if menu_coffee == 1:
            print("----- คุณได้เลือก มคค่า ยอดรวม 45 บาท -----")
        elif menu_coffee == 2:
            print("----- คุณได้เลือก กาแฟชาไทย ยอดรวม 45 บาท -----")
        elif menu_coffee == 3:
            print("----- คุณได้เลือก ลาเต้ ยอดรวม 45 บาท -----")
        elif menu_coffee == 4:
            print("----- คุณได้เลือก คาปูชิโน่ ยอดรวม 50 บาท -----")
        else:
            print("----- คุณได้เลือก อเมริกาโน่ ยอดรวม 50 บาท -----")
        
        print("")
        payment = int(input("กรุณาใส่จำนวนเงิน: "))
        if menu_coffee == 1 or menu_coffee == 2 or menu_coffee == 3 or menu_coffee == 4:
            while True:
                if payment >= 45:
                    sum = payment - 45
                    phone_number(input("กรุณาใส่เบอร์โทร: "))
                    print("เงินทอน :%d " %sum)

                    time.sleep(5)
                    ascii()
                    print("------------------------------------")
                    print("เครื่องดื่มของคุณเสร็จเรียบร้อยแล้ว")
                    break
                else:
                    print("เกิดข้อผิดพลาด")
                    payment = int(input("กรุณาใส่จำนวนเงิน: "))
                    
        else:
            while True:
                if payment >= 50:
                    sum = payment - 50
                    break
                else:
                    print("เกิดข้อผิดพลาด")
                    payment = int(input("กรุณาใส่จำนวนเงิน: "))
    
    elif type_menu == 2:
        menu_milk = show_menu_milk()
        if menu_milk == 1:
            print("----- คุณได้เลือก มคค่า ยอดรวม 45 บาท -----")
        elif menu_milk == 2:
            print("----- คุณได้เลือก กาแฟชาไทย ยอดรวม 45 บาท -----")
        elif menu_milk == 3:
            print("----- คุณได้เลือก ลาเต้ ยอดรวม 45 บาท -----")
        elif menu_milk == 4:
            print("----- คุณได้เลือก คาปูชิโน่ ยอดรวม 50 บาท -----")
        else:
            print("----- คุณได้เลือก อเมริกาโน่ ยอดรวม 50 บาท -----")
        
        print("")
        payment = int(input("กรุณาใส่จำนวนเงิน: "))
        if menu_milk == 1 or menu_milk == 2 or menu_milk == 3:
            while True:
                if payment >= 45:
                    sum = payment - 45
                    break
                else:
                    print("เกิดข้อผิดพลาด")
                    payment = int(input("กรุณาใส่จำนวนเงิน: "))
        else:
            while True:
                if payment >= 50:
                    sum = payment - 45
                    break
                else:
                    print("เกิดข้อผิดพลาด")
                    payment = int(input("กรุณาใส่จำนวนเงิน: "))