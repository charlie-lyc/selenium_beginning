from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, search_results:WebElement):
        self.search_results = search_results
        self.deal_cards = self.pull_deal_cards()

    def pull_deal_cards(self):
        hotel_cards = self.search_results.find_elements_by_css_selector(
            'div[data-testid="property-card"]'
        )
        return hotel_cards

    def pull_titles(self):
        hotel_titles = []
        for deal_card in self.deal_cards:
            hotel_title = deal_card.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            hotel_titles.append(hotel_title)
        return hotel_titles

    def pull_deal_cards_attributes(self):
        collection = []
        for deal_card in self.deal_cards:
            ## 호텔 이름
            hotel_title = deal_card.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            ####################################################################
            ## 호텔 가격
            hotel_price = deal_card.find_elements_by_css_selector(
                'div[data-testid="price-and-discounted-price"] span'
            )
            ## 검색 결과에 따라 price 와 discounted price 두 가지의 가격이 존재할 수 있음
            if len(hotel_price) == 1:
                price = hotel_price[0].get_attribute('innerHTML').strip()
            elif len(hotel_price) == 2:
                price = hotel_price[1].get_attribute('innerHTML').strip()
            ####################################################################
            ## 세금 별도
            taxes_charges = deal_card.find_element_by_css_selector(
                'div[data-testid="taxes-and-charges"]'
            ).get_attribute('innerHTML').strip().split(' ')[0]
            ####################################################################
            ## 리뷰 점수
            review_score = deal_card.find_elements_by_css_selector(
                'div[data-testid="review-score"] div'
            )
            ## 검색 결과에 따라 review score 가 존재하지 않을 수 있음
            if not review_score:
                score = ''
            else:
                score = review_score[0].get_attribute('innerHTML').strip()
            ####################################################################
            # print(f'{hotel_title}: {price}, {taxes_charges}, {score}Score')
            ## Pretty Table 모듈 이용시 필요한 2차원 구조 리스트 생성
            collection.append([ hotel_title, price, taxes_charges, score ])
        return collection












