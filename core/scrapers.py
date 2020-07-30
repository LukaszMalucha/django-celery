from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from core.models import NewsItem, ScrapeRecord
import datetime
from dateutil.relativedelta import relativedelta

def scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

    browser.get(url)
    #
    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//article[@class='crayons-story']")
            )
        )
    except TimeoutException:
        print("Timed Out")
        browser.quit()

    try:
        article_elements = browser.find_elements_by_xpath(
            ".//article[@class='crayons-story']"
        )

        for article in article_elements[:50]:
            result = article.find_element_by_xpath(".//h2[@class='crayons-story__title']/a")
            news_item_link = result.get_attribute('href')

            title_result = article.find_element_by_tag_name("h2")
            news_item_title = title_result.text

            # check if not older that two years
            two_years_ago = datetime.date.today() - relativedelta(years=2)

            NewsItem.objects.get_or_create(
                title=news_item_title,
                link=news_item_link,
                source='Dev.to'
            )

        ScrapeRecord.objects.create()

    except:
        pass
