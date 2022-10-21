import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from termcolor import cprint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip


def main(zero, ads_id, seed, password):
    try:

        open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
        close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

        resp = requests.get(open_url).json()

        chrome_driver = resp["data"]["webdriver"]
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)

        url = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'

        driver.get(url)
        time.sleep(3)
        get_started = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]').click()
        time.sleep(3)
        import_wallet = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]').click()
        time.sleep(3)
        agree = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary page-container__footer-button"]').click()
        time.sleep(3)
        pyperclip.copy(seed)
        phrase = driver.find_element(By.XPATH, '//*[@class="MuiInputBase-input MuiInput-input"]').click()
        time.sleep(1)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()

        time.sleep(3)
        pyperclip.copy(password)
        new_password = driver.find_element(By.XPATH, '//*[@id="password"]').click()
        time.sleep(1)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()
        time.sleep(1)
        password_confirm = driver.find_element(By.XPATH, '//*[@id="confirm-password"]').click()
        time.sleep(1)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()
        time.sleep(1)
        agree_terms = driver.find_element(By.XPATH, '//*[@class="check-box far fa-square"]').click()
        time.sleep(3)
        done_import = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary create-new-vault__submit-button"]').click()
        time.sleep(3)
        all_done = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary first-time-flow__button"]').click()
        time.sleep(3)
        
        # ============================= if you don't need to add a network, delete everything below =============================
     
        net_name = 'Optimism'
        rpc = 'https://mainnet.optimism.io'
        chain_id = 10
        symbol = 'ETH'
        explorer = 'https://optimistic.etherscan.io/'

        xpatch = '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div'

        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network')
        time.sleep(5)
        network_name = driver.find_element(By.XPATH, f'{xpatch}[1]/label/input').click()
        time.sleep(1)
        pyperclip.copy(net_name)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()
        time.sleep(1)

        new_rpc = driver.find_element(By.XPATH, f'{xpatch}[2]/label/input').click()
        time.sleep(1)
        pyperclip.copy(rpc)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()
        time.sleep(1)

        chain = driver.find_element(By.XPATH, f'{xpatch}[3]/label/input').click()
        time.sleep(1)
        pyperclip.copy(chain_id)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()
        time.sleep(1)

        currency_symbol = driver.find_element(By.XPATH, f'{xpatch}[4]/label/input').click()
        time.sleep(1)
        pyperclip.copy(symbol)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()
        time.sleep(1)

        explorer_url = driver.find_element(By.XPATH, f'{xpatch}[5]/label/input').click()
        time.sleep(1)
        pyperclip.copy(explorer)
        ActionChains(driver).key_down(u'\ue03d').send_keys('v').perform()
        time.sleep(1)

        save = driver.find_element(By.XPATH, '//*[@class="button btn--rounded btn-primary"]').click()
        time.sleep(3)

        # =======================================================================================================================
        
        driver.quit()
        requests.get(close_url)

        cprint(f'{zero+1}. {ads_id} = done', 'green')

    except Exception as ex:
        cprint(f'{zero+1}. {ads_id} = already done', 'yellow')
        driver.quit()
        requests.get(close_url)


with open("id_users.txt", "r") as f:
    id_users = [row.strip() for row in f]

with open("seeds.txt", "r") as f:
    seeds = [row.strip() for row in f]
        
zero = -1
for ads_id in id_users:
    zero = zero + 1
    seed = seeds[zero]
    password = 'password123'

    main(zero, ads_id, seed, password)

