import os
from selenium import webdriver


# print(os.getcwd())
# os.environ['PATH'] = '/Users/charlie/Documents/YouTube/FreeCodeCamp/SeleniumForBeginners'

# driver = webdriver.Chrome()
# driver.get('https://www.google.com')
# driver.implicitly_wait(10)


################################################################################
from booking.constants import DEFAULT_DRIVER_PATH, BASE_URL # 프로젝트 폴더를 Root Directory 기준으로!!!
from selenium.webdriver.support.select import Select
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=DEFAULT_DRIVER_PATH, tear_down=False):
        self.driver_path = driver_path
        self.tear_down = tear_down
        os.environ['PATH'] = driver_path
        ################################
        # webdriver.Chrome.__init__(self)
        ################################
        super().__init__()
        ################################
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb): # Using PyCharm IDE
        if self.tear_down:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)
        self.implicitly_wait(30)

    def change_currency(self, currency=None):
        ### 모든 경우에 id 가 주어주면 좋겠지만 실제로는 그렇지 않은 경우가 훨씬 많음
        ### class 를 이용하기도 하지만 디자인적인 요소로써 자주 반복되기 때문에 파악하기 힘듦
        ### 이런 경우에 아래와 같이 element 의 특이한 attribute (button 의 실행 함수, 또는 텍스트 등) 일부분을 그대로 선택자로 활용할 수 있음
        ### ex) driver.find_element_by_css_selector('<element>[<attribute>="<value>"]')
        currency_change_btn = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_change_btn.click()
        if currency != None: # if 문이 없이도 currency=None 이면 실행되지 않으나, 명시적으로 표현함
            selected_currency_elm = self.find_element_by_css_selector(
                # 'a[data-modal-header-async-url-param="changed_currency=1;selected_currency={}"]'.format(currency)
                f'a[data-modal-header-async-url-param="changed_currency=1;selected_currency={currency}"]'
            )
            selected_currency_elm.click()

    def input_place(self, place):
        place_to_go = self.find_element_by_id('ss')
        place_to_go.clear()
        place_to_go.send_keys(place)
        first_of_autocompletions = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_of_autocompletions.click()

    def select_dates(self, check_in_date, check_out_date):
        selected_check_in_date = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        selected_check_in_date.click()
        selected_check_out_date = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        selected_check_out_date.click()

    def select_guests(self):
        guests_toggle = self.find_element_by_id('xp__guests__toggle')
        guests_toggle.click()

    def select_adults(self, adults=2):
        adults_decrease_btn = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        adults_increase_btn = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        while True:
            group_adults = self.find_element_by_id('group_adults')
            value_of_adults = group_adults.get_attribute('value')
            if int(value_of_adults) > adults:
                adults_decrease_btn.click()
            elif int(value_of_adults) < adults:
                adults_increase_btn.click()
            else:
                break

    def select_children(self, children=0, age=None):
        if children != 0 and age == None:
            raise ValueError('You need to select children age!')
        elif age != None and (0 > age or age > 17):
            raise ValueError('Children age is between 0 and 17!')
        elif children != 0 and age != None:
            children_decrease_btn = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Children"]'
            )
            children_increase_btn = self.find_element_by_css_selector(
                'button[aria-label="Increase number of Children"]'
            )
            while True:
                group_children = self.find_element_by_id('group_children')
                value_of_children = group_children.get_attribute('value')
                if int(value_of_children) > children:
                    children_decrease_btn.click()
                elif int(value_of_children) < children:
                    children_increase_btn.click()
                else:
                    break
            children_age = Select(self.find_element_by_name('age'))
            children_age.select_by_value(str(age))

    def select_rooms(self, rooms=1):
        rooms_decrease_btn = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Rooms"]'
        )
        rooms_increase_btn = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Rooms"]'
        )
        while True:
            group_rooms = self.find_element_by_id('no_rooms')
            value_of_rooms = group_rooms.get_attribute('value')
            if int(value_of_rooms) > rooms:
                rooms_decrease_btn.click()
            elif int(value_of_rooms) < rooms:
                rooms_increase_btn.click()
            else:
                break

    def search_results(self):
        search_btn = self.find_element_by_css_selector(
            'button[data-sb-id="main"]'
        )
        search_btn.click()
        self.implicitly_wait(30)

    ############################################################################

    # def apply_filtrations(self, star_rates):
    def apply_filtrations(self, *star_rates):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(*star_rates)
        filtration.apply_lowest_price_first()

    ############################################################################

    def report_results(self):
        search_results = self.find_element_by_id('search_results_table')
        ########################################################################
        report = BookingReport(search_results)
        # print(report.pull_titles())
        # print(report.pull_deal_cards_attributes())
        ########################################################################
        table = PrettyTable(
            field_names=['Hotel Name', 'Hotel Price', 'Taxes and Charges', 'Review Score']
        )
        table.add_rows(report.pull_deal_cards_attributes())
        print(table)

    def export_csv(self):
        pass

















