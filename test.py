from func import show_type_coffee, show_menu_coffee

print("----- WELCOME TO Vending-Machine -----")
print("----- ค่าเฟอัตโนมัติ 24 ชั่วโมง -----")


type_menu = show_type_coffee()

if type_menu == 1 or type_menu == 2 or type_menu == 3 or type_menu == 4:
    print(type_menu)
    if type_menu == 1:
        
        menu_coffee = show_menu_coffee()
        if menu_coffee == 1:
            print("----- คุณได้เลือก มคค่า ยอดรวม 45 บาท -----")