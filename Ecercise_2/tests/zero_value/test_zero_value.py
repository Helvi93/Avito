from Ecercise_2.helper.helper import Helper

def test_check(driver):
    helper = Helper(driver)

    driver.get("https://www.avito.ru/avito-care/eco-impact")

    helper.scroll_to_elem('//h2[@class="desktop-item-title-LkZqW"]')
    helper.get_screenshot_by_elem('//div[@class="desktop-impact-items-F7T6E"]', 'zero_value')
