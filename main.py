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

            browser = webdriver.Firefox(options=opts)
            # browser = webdriver.Firefox()
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
    nbr = 0
    vkl = 1
    while True:
        if nbr == 8:
            nbr = 0
            print('Обновил переменную')
            # get_vk_friends()
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
        try:
            vkgroup = 'https://vk.com/' + vk_frend_group[nbr]
            browser.execute_script("window.open('{}');".format(vkgroup))
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[vkl])
            time.sleep(3)
            # TODO: Настроить прокси решение https://coderoad.ru/18719980/%D0%9F%D1%80%D0%BE%D0%BA%D1%81%D0%B8-Selenium-Python-Firefox
            # TODO: написать автоприем друзей
            # TODO: записать поиск боксов в отдельную функцию
            # TODO: написать автоотправку заявок в друзья
            # TODO: добавить время отправки сообщений в лог
            # TODO: Что то с драйвером Message: Element <div id="post_field" class="submit_post_field dark submit_post_inited"> is not clickable at point (661,537) because another element <div id="box_layer_wrap" class="scroll_fix_wrap fixed"> obscures it


            browser.find_element_by_xpath('//*[@id="post_field"]').click()
            print('click')

            time.sleep(3)
            with open(message_file, 'r', encoding='utf=8') as txt_file:  # выбираем сообщение из файла
                post_message = random.choice(txt_file.readlines())

            time.sleep(1)
            browser.find_element_by_id('post_field').send_keys(post_message)

            time.sleep(1)
            browser.find_element_by_id('send_post').click()
            print(f'{nbr} сообщение отправлено в {vk_frend_group[nbr]}')
            time.sleep(random.randint(120, 380))
            nbr += 1
            vkl += 1
            # TODO: блок с автодобавлением друзей
        except selenium.common.exceptions.WebDriverException as e:
            print('Что то с драйвером', e)
            nbr += 1
            vkl += 1
            time.sleep(20)
            continue

        except Exception as e:
            print('Непредвиденная ошибка', e)
            # browser.close()
            # browser.quit()
            time.sleep(3)
            continue

        # finally:
        #     browser.close()
        #     browser.quit()

def get_vk_friends():
        global browser

        # phone = input('Enter your phone or email: ')
        # if phone == '':
        phone = ''
        password = ''

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
        try:
            browser.execute_script("window.open('https://vk.com/friends?section=requests');")
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[1])
            time.sleep(3)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            buttons_add = browser.find_elements_by_class_name('flat_button.button_small')
            time.sleep(3)
            possible_friends = browser.find_elements_by_class_name('friends_possible_link')

            ask = 1
            for button in buttons_add:
                try:
                    button.click()

                    print(f'Принял заявку № {ask}')
                    ask += 1
                    time.sleep(3)
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)
                except Exception:
                    pass
            fri = 1
            for link in possible_friends:
                try:
                    link.click()
                    print(f'Добавил {fri} друга')
                    fri += 1
                    time.sleep(5)
                except Exception as e:
                    print('Проблема в цикле ссылок')



        except Exception as e:
            print(e)
        finally:
            browser.close()
def main():
    # sender_vk_spam()
    get_vk_friends()

if __name__ == '__main__':
    main()
