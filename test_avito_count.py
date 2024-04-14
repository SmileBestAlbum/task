from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pytest
import os

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_first_counter(driver):
    driver.get("https://www.avito.ru/avito-care/eco-impact")

    try:
        first_counter = driver.find_element(By.XPATH, '//div[@class="desktop-impact-items-F7T6E"]/div[2]')
        assert first_counter.is_displayed()

        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Making directory in case it does not exists
        output_folder = os.path.join(current_directory, "output")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        first_counter_screenshot_path = os.path.join(output_folder, "first_counter.jpg")

        if os.path.exists(first_counter_screenshot_path):
            os.remove(first_counter_screenshot_path)
        first_counter.screenshot(first_counter_screenshot_path)

        print("Первый счетчик сохранен как first_counter.jpg")

    except NoSuchElementException:
        with open("BUGS.md", "a") as bugs_file:
            bugs_file.write(f"Ошибка при поиске первого счетчика: {str(NoSuchElementException)}\n")
            print(f"Сообщение об ошибке сохранено в файл BUGS.md: {str(NoSuchElementException)}")


def test_second_counter(driver):
    driver.get("https://www.avito.ru/avito-care/eco-impact")

    try:
        scnd_counter = driver.find_element(By.XPATH, '//div[@class="desktop-impact-items-F7T6E"]/div[4]')
        assert scnd_counter.is_displayed()

        current_directory = os.path.dirname(os.path.abspath(__file__))

        output_folder = os.path.join(current_directory, "output")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        scnd_counter_screenshot_path = os.path.join(output_folder, "scnd_counter.jpg")

        if os.path.exists(scnd_counter_screenshot_path):
            os.remove(scnd_counter_screenshot_path)

        scnd_counter.screenshot(scnd_counter_screenshot_path)
        print("Второй счетчик сохранен как scnd_counter.jpg")

    except NoSuchElementException:
        with open("BUGS.md", "a") as bugs_file:
            bugs_file.write(f"Ошибка при поиске второго счетчика: {str(NoSuchElementException)}\n")
            print(f"Сообщение об ошибке сохранено в файл BUGS.md: {str(NoSuchElementException)}")


def test_third_counter(driver):
   driver.get("https://www.avito.ru/avito-care/eco-impact")

   try:
        thrd_counter = driver.find_element(By.XPATH, '//div[@class="desktop-impact-items-F7T6E"]/div[6]')
        assert thrd_counter.is_displayed()

        current_directory = os.path.dirname(os.path.abspath(__file__))

        output_folder = os.path.join(current_directory, "output")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        thrd_counter_screenshot_path = os.path.join(output_folder, "thrd_counter.jpg")

        if os.path.exists(thrd_counter_screenshot_path):
            os.remove(thrd_counter_screenshot_path)

        thrd_counter.screenshot(thrd_counter_screenshot_path)
        print("Третий счетчик сохранен как thrd_counter.jpg")

   except NoSuchElementException:
        with open("BUGS.md", "a") as bugs_file:
            bugs_file.write(f"Ошибка при поиске третьего счетчика: {str(NoSuchElementException)}\n")
            print(f"Сообщение об ошибке сохранено в файл BUGS.md: {str(NoSuchElementException)}")
