import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def sender_vk_spam():
    global browser

    phone = input('Enter your phone or email: ')
    if phone == '':
        phone = ''
        password = ''
        message_file = 'message.txt'


    else:
        password = input('Enter your password: ')
        message_file = input('Enter path to file: ')
        iteration = input('Enter how iteration: ')

    while True:  # зацикливаем авторизацию на случай падения selenium драйвера
        try:
            opts = Options()
            opts.headless = True
            assert opts.headless

            # browser = webdriver.Firefox(options=opts)
            browser = webdriver.Firefox()
            browser.get('https://vk.com/')
            time.sleep(1)
            browser.find_element_by_id('index_email').send_keys(phone)
            browser.find_element_by_id('index_pass').send_keys(password)

            time.sleep(1)
            browser.find_element_by_id('index_login_button').click()
            print('Авторизовался')
            time.sleep(12)
            break
        except Exception as err:
            print('Проблема с авторизацией', err)
            time.sleep(10)
    nbr = 3
    vkl = 1
    while True:
        if nbr == 8:
            nbr = 0
        else:
            pass
        vk_frend_group = ['dobav_like_repost_piar',
                          'tomanyfriends',
                          'dobav_v_druzya_likeme',
                          'club39673900',
                          'official10000friends',
                          'spottsila',
                          'dobav_menya_esli_xochesh',
                          'club77713352',
                          'kamdee',
                          ]

        vkgroup = 'https://vk.com/' + vk_frend_group[nbr]
        browser.execute_script("window.open('{}');".format(vkgroup))
        time.sleep(3)
        browser.switch_to.window(browser.window_handles[vkl])
        time.sleep(3)
        # TODO: Добавить отсчет отправленых сообщений
        # TODO: Добавить поочередное обращение к разным группам
        # TODO: Настроить прокси решение https://coderoad.ru/18719980/%D0%9F%D1%80%D0%BE%D0%BA%D1%81%D0%B8-Selenium-Python-Firefox
        # TODO: библиотека python прокси
        # TODO: написать автоприем друзей
        # TODO: записать поиск боксов в отдельную функцию
        # TODO: написать автоотправку заявок в друзья
        # TODO: добавить время отправки сообщений в лог
        # TODO: добавить отправку своих сообщений в переменно в коментарии и на стены разных групп
        # TODO: Что то с драйвером Message: Element <div id="post_field" class="submit_post_field dark submit_post_inited"> is not clickable at point (661,537) because another element <div id="box_layer_wrap" class="scroll_fix_wrap fixed"> obscures it

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
            print(f'{nbr} сообщение отправлено')
            time.sleep(random.randint(240, 600))
            nbr += 1

        except selenium.common.exceptions.WebDriverException as e:
            print('Что то с драйвером', e)
            nbr += 1
            time.sleep(20)
            continue

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
