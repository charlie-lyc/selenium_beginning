from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    ## 현재는 booking.com 구조가 바뀌어 적용되지는 않지만 이 코드의 의미는
    ## 특정하기 어려운 대상 element 를 바로 찾아가 실행하기 어려우므로
    ## 중간 단계의 parent element 를 우선 선택하고 그 children elements 중에 대상을 특정하는 과정
    # def apply_star_rating(self, *star_rates):
    #     filter_class = self.driver.find_element_by_id('filter_class')
    #     children_elements = filter_class.find_elements_by_css_selector('*')
    #     # print(len(children_elements))
    #     for star_rate in star_rates:
    #         for child_element in children_elements:
    #             element_text = str(child_element.get_attribute('innerHTML')).strip()
    #             if element_text == f'{star_rate} star' or element_text == f'{star_rate} stars':
    #                 child_element.click()

    ## My Solution
    # def apply_star_rating(self, star_rates):
    def apply_star_rating(self, *star_rates):
        ## 처음에는 checkbox element 를 찾는데 오락가락 해서 explicitly wait 를 적용
        ## 그 다음에는 checkbox 가 클릭되지 않아서 element_to_be_clickable() 를 적용해보았으나 작동되지 않는 것으로 확2
        ## 방법을 모색한 결과, checked 값을 확인하는 데만 checkbox 를 이용하고
        ## 클릭은 굳이 checkbox 에 직접 실행하지 않아도 된다는 점에서 착안!!!
        ## 이 후 테스트 실행 과정에서 특정 elements 의 mount 상태가 서로에게 영향을 주는 것 같아 all elements 로 전환
        WebDriverWait(self.driver, 30).until(
            # EC.presence_of_element_located((By.NAME, f'class={star_rate}'))
            # EC.element_to_be_clickable((By.NAME, f'class={star_rate}'))
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '*'))
        )
        for star_rate in star_rates:
            star_rate_class = self.driver.find_element_by_name(f'class={star_rate}')
            # print(star_rate_class.is_selected())
            selected_star_rate = self.driver.find_element_by_css_selector(
                f'div[data-filters-item="class:class={star_rate}"]'
            )
            # print(selected_star_rate.get_attribute('data-filters-item'))
            if not star_rate_class.is_selected():
                selected_star_rate.click()
                self.driver.implicitly_wait(30)

    def apply_lowest_price_first(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '*'))
        )
        lowest_price_first = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        lowest_price_first.click()
        self.driver.implicitly_wait(30)

    def apply_highest_stars_first(self):
        pass

    def apply_lowest_stars_first(self):
        pass










