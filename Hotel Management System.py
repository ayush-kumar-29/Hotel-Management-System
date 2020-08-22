#!/usr/bin/env python
# coding: utf-8

# # HOTEL MANAGEMENT SYSTEM
It is assumed that total number of Rooms in a Hotel is 20.
# In[1]:


class Hotel:
    __rooms_available = 20
    __rooms_reserved = 0
    __booked_rooms = {}

    def __init__(self):
        for i in range(Hotel.__rooms_available):
            Hotel.__booked_rooms.update({i + 1: {}})

    @classmethod
    def get_room_list(cls, total_rooms):
        room_list = list()
        for room_num in Hotel.__booked_rooms:
            if len(Hotel.__booked_rooms[room_num]) == 0 and total_rooms != 0:
                room_list.append(room_num)
                total_rooms -= 1
            if total_rooms == 0:
                break
        print(room_list)
        return room_list

    @classmethod
    def count_available_rooms(cls):
        return cls.__rooms_available

    @classmethod
    def count_reserved_rooms(cls):
        return cls.__rooms_reserved

    @classmethod
    def confirm_booking(cls):
        print("\n", "*" * 12, " New Booking ", "*" * 12, sep='')
        cus_name = input("Enter Name : ")
        cus_num = input("Enter Mobile Number : ")
        total_rooms = input("Enter No. of Room to Book : ")
        while not total_rooms.isnumeric():
            total_rooms = input("Enter No. of Room to Book : ")
        while int(total_rooms) > Hotel.__rooms_available:
            print(total_rooms, "Rooms not available. Try entering less no. of Rooms !")
            total_rooms = input("Enter No. of Room to Book : ")
        stay_dur = input("Enter duration of stay (in days) : ")
        while not stay_dur.isnumeric():
            stay_dur = input("Enter duration of stay (in days) : ")
        room_list = Hotel.get_room_list(int(total_rooms))
        for i in room_list:
            new_room = {i: Hotel.new_booking(cus_name, cus_num, stay_dur, i)}
            Hotel.__booked_rooms.update(new_room)
        Hotel.__rooms_available -= int(total_rooms)
        Hotel.__rooms_reserved += int(total_rooms)
        print("\n", "-" * 6, " Booking Details ", "-" * 6, sep='')
        print(total_rooms, "Rooms Booked !")
        print("Room No. Booked : ", end='')
        print("#", room_list[0], end='', sep='')
        if len(room_list) > 1:
            for i in range(1, len(room_list)):
                print(', #', room_list[i], sep='', end=' ')
        print()
        print("*" * 36)

    @staticmethod
    def search_customer(cus_name):
        flag = False
        for room_detail in Hotel.__booked_rooms.values():
            if len(room_detail) != 0:
                if room_detail['CusName'] == cus_name:
                    flag = True
                    print("\n--- Customer Found ---")
                    print("Name : ", room_detail['CusName'])
                    print("Mobile No. : ", room_detail['CusNumber'])
                    print("Room No. : ", room_detail['RoomNumber'])
                    print("Duration of stay : ", room_detail['StayDuration'], "days")
                    print("\n----------------------")
        if not flag:
            print("No customer found !")

    @staticmethod
    def search_room(room_num):
        for room in Hotel.__booked_rooms.keys():
            if room == room_num:
                if len(Hotel.__booked_rooms[room]) != 0:
                    print("\n--- Booking Found ---")
                    print("Customer Name : ", Hotel.__booked_rooms[room]['CusName'])
                    print("Mobile No. : ", Hotel.__booked_rooms[room]['CusNumber'])
                    print("Duration of stay : ", Hotel.__booked_rooms[room]['StayDuration'], "days")
                    return
                else:
                    print("No Booking Found on this Room No. !")
                    return
        print("Room No. not Found !")

    @staticmethod
    def check_room_availability(room_num):
        for room in Hotel.__booked_rooms.keys():
            if room == room_num:
                if len(Hotel.__booked_rooms[room]) == 0:
                    print("Room is Available !")
                else:
                    print("Room is Booked !")
                return
        print("Room No. not Found !")

    @staticmethod
    def edit_record(room_num):
        for room in Hotel.__booked_rooms.keys():
            if room == room_num:
                if len(Hotel.__booked_rooms[room]) != 0:
                    cus_name = input("Enter New Name : ")
                    cus_num = input("Enter New Mobile Number : ")
                    stay_dur = input("Enter new Duration of Stay : ")
                    while not stay_dur.isnumeric():
                        stay_dur = input("Enter new Duration of Stay : ")
                    new_room = {
                        room: Hotel.new_booking(cus_name, cus_num, stay_dur, room)
                    }
                    Hotel.__booked_rooms.update(new_room)
                    print("Booking Record Updated !")
                    return
                else:
                    print("No Booking found on this Room No. !")
                    return
        print("Room No. not Found !")

    @staticmethod
    def delete_record(room_num):
        for room in Hotel.__booked_rooms.keys():
            if room == room_num:
                if len(Hotel.__booked_rooms[room]) != 0:
                    Hotel.__booked_rooms.update({room_num: {}})
                    print("Booking Record Removed !")
                    if Hotel.__rooms_available < 20:
                        Hotel.__rooms_available += 1
                    if Hotel.__rooms_reserved > 0:
                        Hotel.__rooms_reserved -= 1
                    return
                else:
                    print("No Booking found on this Room No. !")
                    return
        print("Room No. not Found !")

    @staticmethod
    def new_booking(cus_name, cus_num, stay_dur, room_num):
        return {'CusName': cus_name,
                'CusNumber': cus_num,
                'StayDuration': stay_dur,
                'RoomNumber': room_num}


def home_menu():
    choice = None
    while choice != '0':
        print("\n###### Home Menu ######")
        print("1 -> Booking\n2 -> Enquiry\n0 -> Exit")
        choice = input("Enter your choice : ")
        while choice not in ['0', '1', '2']:
            choice = input("Enter your choice : ")
        if choice == '0':
            print("###### THANK YOU ! ######")
            break
        elif choice == '1':
            booking_menu()
        elif choice == '2':
            enquiry_menu()


def booking_menu():
    choice = None
    while choice != '0':
        print("\n###### Booking Menu ######")
        print("1 -> New Booking ")
        print("2 -> No. of Rooms Available")
        print("3 -> No. of Rooms Reserved")
        print("0 -> Go back to Main Menu")
        choice = input("Enter your choice : ")
        while choice not in ['0', '1', '2', '3']:
            choice = input("Enter your choice : ")
        if choice == '0':
            break
        elif choice == '2':
            print("\n", "*" * 35, sep='')
            print("No. of Rooms Available : ", Hotel.count_available_rooms(), "Rooms")
            print("*" * 35, end='\n')
        elif choice == '3':
            print("\n", "*" * 35, sep='')
            print("No. of Rooms Reserved : ", Hotel.count_reserved_rooms(), "Rooms")
            print("*" * 35, end='\n')
        elif choice == '1':
            Hotel.confirm_booking()


def enquiry_menu():
    choice = None
    while choice != '0':
        print("\n###### Enquiry Menu ######")
        print("1 -> Search with Customer Name")
        print("2 -> Search with Room Number")
        print("3 -> Check Room for Availability")
        print("4 -> Edit a Booking Record")
        print("5 -> Delete a Booking Record")
        print("0 -> Go back to Main Menu")
        choice = input("Enter your choice : ")
        while choice not in ['0', '1', '2', '3', '4', '5']:
            choice = input("Enter your choice : ")
        if choice == '0':
            break
        elif choice == '1':
            print("\n", "*" * 6, " Search Customer ", "*" * 6, sep='')
            cus_name = input("Enter name of customer : ")
            Hotel.search_customer(cus_name)
            print("*" * 35, end='\n')
        elif choice == '2':
            print("\n", "*" * 8, " Search Room ", "*" * 8, sep='')
            room_num = input("Enter Room No. : ")
            while not room_num.isnumeric():
                room_num = input("Enter Room No. : ")
            Hotel.search_room(int(room_num))
            print("*" * 35, end='\n')
        elif choice == '3':
            print("\n", "*" * 6, " Room Availability ", "*" * 6, sep='')
            room_num = input("Enter Room No. : ")
            while not room_num.isnumeric():
                room_num = input("Enter Room No. : ")
            Hotel.check_room_availability(int(room_num))
            print("*" * 35, end='\n')
        elif choice == '4':
            print("\n", "*" * 9, " Edit Record ", "*" * 9, sep='')
            room_num = input("Enter Room No. to Edit : ")
            while not room_num.isnumeric():
                room_num = input("Enter Room No. to Edit : ")
            Hotel.edit_record(int(room_num))
            print("*" * 35, end='\n')
        elif choice == '5':
            print("\n", "*" * 8, " Remove Record ", "*" * 8, sep='')
            room_num = input("Enter Room No. to Delete : ")
            while not room_num.isnumeric():
                room_num = input("Enter Room No. to Delete : ")
            Hotel.delete_record(int(room_num))
            print("*" * 35, end='\n')


# Driver Code
hotel = Hotel()
home_menu()
del hotel

