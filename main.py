from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def main():

    driver = webdriver.Chrome()
    driver.get("https://mcc.live")
    assert "MCC" in driver.title
    time.sleep(2)
    elem = driver.find_element(By.ID, 'app-body')
    elem = elem.find_element(By.ID, 'app-root')
    elem = elem.find_element(By.CLASS_NAME, 'container')
    elem = elem.find_element(By.CLASS_NAME, 'flexbox')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]')
    elem = elem.find_element(By.TAG_NAME, 'div')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]')
    elem = elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul')
    elem = elem.find_element(By.CLASS_NAME, 'statistic')
    # player 1

    player1 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[1]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[1]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[1]/span[2]/p').text]

    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]
    player2 = [
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/h1').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[1]/p').text,
        elem.find_element(By.XPATH, '//*[@id="app-root"]/div[4]/div/div[2]/div/div[3]/div[2]/div/ul/div[2]/span[2]/p').text]

    print(player1)
    print(player2)

    assert "No results found." not in driver.page_source
    driver.close()


if __name__ == '__main__':
    main()


