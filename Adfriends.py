import time
import random
import selenium
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config import phone, password

# TODO: сделать отдельный метод авторизации после которого можно будет запускать остальные методы
class Adfriends:

    def sender_vk_spam(self, min_pause=100, max_pause=260,
                       only_accepts_friends=False,
                       add_possible_friends=False,
                       only_delete_sub=False,
                       debug=False):
        """
        Функция для отправки сообщений в группы вк из файла
        :return: запускает get_vk_friends
        """
        global browser

        message_file = 'message.txt'
        pause_random = random.randint(min_pause, max_pause)
        while True:  # зацикливаем авторизацию на случай падения selenium драйвера
            try:
                opts = Options()
                opts.headless = True
                assert opts.headless
                if debug:
                    browser = webdriver.Firefox()
                else:
                    browser = webdriver.Firefox(options=opts)  # скрываем браузер от пользователя

                browser.get('https://vk.com/')  # открываем страницу
                time.sleep(1)

                browser.find_element_by_id('index_email').send_keys(phone)
                browser.find_element_by_id('index_pass').send_keys(password)
                time.sleep(1)

                browser.find_element_by_id('index_login_button').click()
                print('Авторизовался')
                time.sleep(10)
                break
            except KeyboardInterrupt:
                print('Закрыл браузер')
                browser.close()
                browser.quit()
            except Exception as err:
                print('Проблема с авторизацией', err)
                time.sleep(10)

        self.delete_subscribers(only_delete_sub)

        nbr = 19
        while True:
            if nbr == 19 and only_accepts_friends:
                nbr = 19
                print('Режим приема заявок в друзья')
                self.get_vk_friends(add_possible_friends)  # Запускаем ф-цию для приема заявок в друзья
            elif nbr == 19:
                nbr = 0
                print('Обновил переменную')
                self.get_vk_friends(add_possible_friends)  # Запускаем ф-цию для приема заявок в друзья

            vk_frend_group = ['dobav_like_repost_piar',
                              'tomanyfriends',
                              'dobav_v_druzya_likeme',
                              'club39673900',
                              'likefriends123',
                              'club59721672',
                              'club50061797',
                              'club164908452',
                              'club111702311',
                              'gooovdr',
                              'official10000friends',
                              'spottsila',
                              'dobav_menya_esli_xochesh',
                              'club77713352',
                              'kamdee',
                              'club100292512',
                              'club58787677',
                              'topchik_piarchik',
                              'club39130136']
            try:
                vkgroup = 'https://vk.com/' + vk_frend_group[nbr]
                browser.execute_script("window.open('{}');".format(vkgroup))
                time.sleep(3)

                browser.switch_to.window(browser.window_handles[0])
                browser.close()

                browser.switch_to.window(browser.window_handles[-1])
                time.sleep(3)

                browser.find_element_by_xpath('//*[@id="post_field"]').click()
                print('click')

                time.sleep(3)
                with open(message_file, 'r', encoding='utf=8') as txt_file:  # выбираем сообщение из файла
                    post_message = random.choice(txt_file.readlines())
                time.sleep(1)

                browser.find_element_by_id('post_field').send_keys(post_message)  # печатаем сообщение в группу
                time.sleep(1)

                browser.find_element_by_id('send_post').click()  # отправляем сообщение
                now = datetime.datetime.now()
                print(f'{nbr} сообщение отправлено в {vk_frend_group[nbr]} [{now.hour}:{now.minute}]')
                time.sleep(pause_random)

                nbr += 1  # прибавляем к счетчику
            except KeyboardInterrupt:
                print('Закрыл браузер')
                browser.close()
                browser.quit()
            except selenium.common.exceptions.WebDriverException as e:
                print('Что то с драйвером', e)
                nbr += 1
                time.sleep(15)
                continue

            except Exception as e:
                print('Непредвиденная ошибка', e)
                time.sleep(3)
                continue

    def get_vk_friends(self, add_possible_friends):
        """
        Функция приема заявок в друзья и добавление  возможных друзей
        """
        # global browser
        try:
            time.sleep(5)
            browser.execute_script("window.open('https://vk.com/friends?section=requests');")

            time.sleep(17)

            browser.switch_to.window(browser.window_handles[-1])
            time.sleep(7)

            for i in range(10):  # скроллим вниз
                try:
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)
                except KeyboardInterrupt:
                    print('Закрыл браузер')
                    browser.close()
                    browser.quit()
                except Exception as el:
                    print(el)

            buttons_add = browser.find_elements_by_class_name('flat_button.button_small')  # все кнопки "принять заявку"
            time.sleep(3)

            possible_friends = browser.find_elements_by_class_name('friends_possible_link')  # возможные друзья

            ask = 1
            for button in buttons_add:  # принимаем заявки в друзья
                try:
                    button.click()
                    print(f'Принял заявку № {ask}')
                    ask += 1
                    time.sleep(5)
                except KeyboardInterrupt:
                    print('Закрыл браузер')
                    browser.close()
                    browser.quit()
                except Exception:
                    pass

            if add_possible_friends:  # если значение аргумента ф-ции True
                fri = 1
                for link in possible_friends:  # добавляем возможных друзей
                    try:
                        link.click()
                        print(f'Добавил {fri} друга')
                        fri += 1
                        time.sleep(5)
                    except KeyboardInterrupt:
                        print('Закрыл браузер')
                        browser.close()
                        browser.quit()
                    except Exception as e:
                        print('Проблема в цикле ссылок')
        except KeyboardInterrupt:
            print('Закрыл браузер')
            browser.close()
            browser.quit()
        except TypeError:
            print('Не прогрузился')

        except Exception as e:
            print(e)

    def delete_subscribers(self, only_delete_sub):
        """
        Функция для отказа от подписок
        :return:
        """
        browser.execute_script("window.open('https://vk.com/friends?section=out_requests');")
        time.sleep(5)

        browser.switch_to.window(browser.window_handles[-1])
        time.sleep(7)

        for i in range(10):  # скроллим вниз
            try:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
            except KeyboardInterrupt:
                print('Закрыл браузер')
                browser.close()
                browser.quit()
            except Exception as ek:
                print(ek)

        out_buttons = browser.find_elements_by_class_name('flat_button.button_small.fl_r')
        time.sleep(5)

        out = 1
        for button in out_buttons:  # отписываемся
            try:
                button.click()
                print(f'Отписался № {out}')
                out += 1
                time.sleep(5)
            except KeyboardInterrupt:
                print('Закрыл браузер')
                browser.close()
                browser.quit()
            except Exception as e:
                print(e)
        if only_delete_sub:
            print('Закончили отписку')
            browser.close()
            browser.quit()
            exit()
        else:
            pass
#
# if __name__ == '__main__':
#     try:
#         examle = Adfriends()
#         examle.sender_vk_spam(debug=True)
#     except KeyboardInterrupt:
#         print('Закрыл браузер')
#         browser.close()
#         browser.quit()
