# from booking.constants import a
# print(a)

################################################################################
from booking.booking import Booking

# booking_instance = Booking()
# booking_instance.land_first_page()

################################################################################
## Context Manager : Automatically Closed!
##  So, Declare the 'tear_down' Parameter and Set the value False in booking.py
##  Now, Not Automatically Closed!!

# with Booking() as bot:
#     ## Land First Page
#     bot.land_first_page()
#     # print('Exiting...')
#
#     ## Change Currency
#     # bot.change_currency()
#     bot.change_currency(currency='USD')
#
#     ## Select Place to Go
#     bot.input_place(place='new york')
#
#     ## Select Check in Date and Check out Date
#     bot.select_dates(check_in_date='2021-11-01', check_out_date='2021-11-10')
#
#     ## Select Guests
#     bot.select_guests()
#
#     ## Select Adults
#     # bot.select_adults()
#     # bot.select_adults(adults=1)
#     bot.select_adults(adults=3)
#
#     ## Select Children
#     # bot.select_children()
#     # bot.select_children(children=1) # ValueError
#     # bot.select_children(children=1, age=18) # ValueError
#     bot.select_children(children=1, age=10)
#
#     ## Select Rooms
#     # bot.select_rooms()
#     bot.select_rooms(rooms=2)
#
#     ## Search Results
#     bot.search_results()
#
#     ## Apply Filtration
#     # bot.apply_filtrations(star_rate=5)
#     # bot.apply_filtrations(5)
#     bot.apply_filtrations(3, 4, 5)
#

################################################################################
## booking bot 이 모든 환경에서 정상적으로 작동되는 것은 아님
## 따라서 try except 구문을 활용하여 실행하는 것이 좀더 안정적
try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        ########################################################################
        # bot.input_place(place='new york')
        bot.input_place(place=input('Where do you want to go? '))
        ########################################################################
        # bot.select_dates(
        #     check_in_date='2021-11-01',
        #     check_out_date='2021-11-10'
        # )
        bot.select_dates(
            check_in_date=input('When is the chceck in date? (yyyy-mm-dd) '),
            check_out_date=input('When is the chceck out date? (yyyy-mm-dd) ')
        )
        ########################################################################
        bot.select_guests()
        ########################################################################
        # bot.select_adults(adults=3)
        bot.select_adults(adults=int(input('How many adults? ')))
        ########################################################################
        # bot.select_children(
        #     children=1,
        #     age=10
        # )
        children=int(input('How many children? '))
        if children != 0:
            bot.select_children(
                children=children,
                age=int(input('How old are children? '))
            )
        ########################################################################
        # bot.select_rooms(rooms=2)
        bot.select_rooms(rooms=int(input('How many rooms do you want? ')))
        ########################################################################
        bot.search_results()
        bot.apply_filtrations(3, 4, 5)
        ########################################################################
        bot.refresh() # To let the booking bot to grab the data properly
        bot.report_results()

except Exception as e:
    ## 브라우저 드라이버의 경로 설정에 대한 exception이 발생될 경우 대처
    if 'in PATH' in str(e):
        print('''
            You are trying to run this bot from command line.
            Please add to PATH your right version Selenium Drivers.
            ex) Windows:
                    set PATH=%PATH%;C:\path\to\folder\driver\is
                Linux:
                    PATH=$PATH:/path/to/folder/driver/is

            If you are using MacOS, please type these code in your file for initial setup:
                import os
                os.environ['PATH'] = '/path/to/folder/driver/is'
        ''')
    else:
        raise














