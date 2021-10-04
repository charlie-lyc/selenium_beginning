import os
from selenium import webdriver


# print(os.getcwd())
os.environ['PATH'] = '/Users/charlie/Documents/YouTube/FreeCodeCamp/SeleniumForBeginners'
driver = webdriver.Chrome()

################################################################################

driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(10)

################################################################################

## Deal with Exception

# no_button = driver.find_element_by_class_name('at-cm-no-button')
# no_button.click()

# try:
#     no_button = driver.find_element_by_class_name('at-cm-no-button')
#     no_button.click()
# except Exception as e:
#     print('No element with this class name. Skipping ...')
#     print(e)

################################################################################

### Firstly, Inspect Every Elements to Need
## Enter Message : id="user-message"
## Show Message : form id="get-input" > button class="btn btn-default"
## Enter a : id="sum1"
## Enter b : id="sum2"
## Get Total : form id="gettotal" > button class="btn btn-default"


### 1. Show Message
usr_msg = driver.find_element_by_id('user-message')
usr_msg.send_keys('Hello World')

## JavaScript 에서 주로 사용되는 CSS Selector 개념이 그대로 적용
# show_btn = driver.find_element_by_css_selector('form#get-input button')
show_btn = driver.find_element_by_css_selector('form#get-input > button')
show_btn.click()


### 2. Get Total
from selenium.webdriver.common.keys import Keys

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')
# sum1.send_keys(12)
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD2)
sum2.send_keys(12)

# ttl_btn = driver.find_element_by_css_selector('form#gettotal button')
### 모든 경우에 id 가 주어주면 좋겠지만 실제로는 그렇지 않은 경우가 훨씬 많음
### class 를 이용하기도 하지만 디자인적인 요소로써 자주 반복되기 때문에 파악하기 힘듦
### 이런 경우에 아래와 같이 element 의 특이한 attribute (button 의 실행 함수, 또는 텍스트 등) 일부분을 그대로 선택자로 활용할 수 있음
### ex) driver.find_element_by_css_selector('<element>[<attribute>="<value>"]')
ttl_btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
ttl_btn.click()








