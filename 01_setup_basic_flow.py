import os
from selenium import webdriver


## Setup
# print(os.getcwd())
os.environ['PATH'] = '/Users/charlie/Documents/YouTube/FreeCodeCamp/SeleniumForBeginners'

## When Executing :
driver = webdriver.Chrome()

## selenium.common.exceptions.WebDriverException:
##   Message: 'chromedriver' executable needs to be in PATH.
##   Please see https://sites.google.com/a/chromium.org/chromedriver/home

## So, Need to :
## 1. download right version of 'chromedriver' from https://sites.google.com/a/chromium.org/chromedriver/home
##   -> before this, check Chrome browser version : Version 94.0.4606.61 (Official Build) (x86_64)
## 2. set the path where chromedriver is : os.environ['PATH'] = ''

################################################################################

## Load
driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
driver.implicitly_wait(10) # time.sleep(10) : seconds

## Find
btn_element = driver.find_element_by_id('downloadButton')

## Action
btn_element.click()

## Find Not Existing Element
# driver.find_element_by_id('something')

## selenium.common.exceptions.NoSuchElementException:
##  Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="something"]"}

################################################################################

## Find by class name
# progress_element = driver.find_element_by_class_name('progress-label')
# print(progress_element.text)
# print(progress_element.text == 'Complete!')

## Starting download...
## False

################################################################################

## 위의 명령이 제대로 실행되기 위해서는 명백하게 대상이 되는 특정 element 가 mount 된 이후여야 함
## 그래서 이번에는 'explicitly wait'가 필요

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    WebDriverWait(driver, 20).until(
        ## Expected Condition ( Element Filtration, Expected Text )
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'progress-label'), 'Complete!')
    )
    progress_element = driver.find_element_by_class_name('progress-label')
    print(progress_element.text)
    print(progress_element.text == 'Complete!')
except Exception as e:
# Deal with Exception
    print(e)
finally:
## End with Closing Browser
    driver.quit()

################################################################################

## 여기까지 간단하게 살펴 본대로 예상되는 바 이런 과정에서 가장 어려운 점은
## 복잡한 웹페이지 구조 속에서 어떻게 필요한 element 에 접근할 것인가 하는 것
## 일반적으로 (크롬)브라우저에서 직접 눈으로 확인하고 Inspect 기능을 이용하여 Elements 탭에서 찾음
## 하지만 좀더 기본적이면서 효율적인 방법은 DOM 구조와 (크롬)브라우저의 JavaScript Console을 이용하여 점점 깊이 파고 드는 것
## ex) hotelList = document.getElementById('hotel-list')
##     hotelNameList = hotelList.getElementsByClassName('hotel-name')
##     ...