import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def sender_vk_spam():
    global browser
    phone = input('Enter your phone or email: ')
    if phone == '':
        phone = '+79870674092'
        password = 'Berserkdao11'
        message_file = 'message.txt'
        iteration = 1000

    else:
        password = input('Enter your password: ')
        message_file = input('Enter path to file: ')
        iteration = input('Enter how iteration: ')


    try:
        opts = Options()
        opts.headless = True
        assert opts.headless

        browser = webdriver.Firefox()
        browser.get('https://vk.com/')
        time.sleep(1)
        browser.find_element_by_id('index_email').send_keys(phone)
        browser.find_element_by_id('index_pass').send_keys(password)

        time.sleep(1)
        browser.find_element_by_id('index_login_button').click()
        print('Авторизовался')

        time.sleep(12)
        browser.execute_script("window.open('https://vk.com/go2friends');")
        time.sleep(3)
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(3)
        # TODO: Добавить отсчет отправленых сообщений
        # TODO: Добавить поочередное обращение к разным группам
        # TODO: Настроить прокси решение https://coderoad.ru/18719980/%D0%9F%D1%80%D0%BE%D0%BA%D1%81%D0%B8-Selenium-Python-Firefox
        # TODO: библиотека python прокси
        # TODO: написать автоприем друзей
        # TODO: написать автоотправку заявок в друзья
        # TODO: добавить время отправки сообщений в лог
        for i in range(1, iteration):
            try:
                browser.find_element_by_xpath('//*[@id="post_field"]').click()
                print('click')

                time.sleep(3)
                with open(message_file, 'r', encoding='utf=8') as txt_file:  # выбираем сообщение из файла
                    post_message = random.choice(txt_file.readlines())

                time.sleep(1)
                browser.find_element_by_id('post_field').send_keys(post_message)

                time.sleep(1)
                browser.find_element_by_id('send_post').click()
                print(f'{i} сообщение отправлено')
                time.sleep(random.randint(120, 480))

            except selenium.common.exceptions.WebDriverException as e:
                print('Что то с драйвером', e)
                time.sleep(20)
                continue
    except KeyboardInterrupt:
        browser.close()
        browser.quit()
        print('Программа закрыта пользователем')
    except Exception as e:
        print('Непредвиденная ошибка', e)
        browser.close()
        browser.quit()

    finally:
        browser.close()
        browser.quit()
def main():
    sender_vk_spam()


if __name__ == '__main__':
    main()
