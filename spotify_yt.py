import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from Secret import usr, passw, usrY, passY
import fileinput


class S_Bot(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://open.spotify.com")
        self.login_btn = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div[1]/header/div[4]/button[2]")
        self.login_btn.click()
        sleep(5)
        self.fb_btn = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/a")
        self.fb_btn.click()
        sleep(3)
        self.email_in = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input")
        self.email_in.send_keys(usr)
        self.passw_in = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input")
        self.passw_in.send_keys(passw)
        sleep(1)
        self.login_final_btn = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button")
        self.login_final_btn.click()
        sleep(5)
        self.click_fav()

    def click_fav(self):
        self.fav = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]/div[2]/nav/div[2]/div/div/div[2]/a/span")
        self.fav.click()

    def s_song(self):
        last_ht, ht = 0, 1
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/div")
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        sleep(1)

        page = self.driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')

        tracks = page_soup.findAll("div", {"class": "tracklist-name ellipsis-one-line"})
        artist = page_soup.findAll("a", {"class": "tracklist-row__artist-name-link"})

        f = open("song_S.txt", "w")

        for track in tracks:
            f.write(str(track))

        f.close()

        f_2 = open("artist_S.txt", "w")

        for art in artist:
            f_2.write(str(art))

        f_2.close()

    def clean_txt(self):

        with fileinput.FileInput("song_S.txt", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace("""<div class="tracklist-name ellipsis-one-line" dir="auto">""", ""), end='')
            for line in file:
                print(line.replace("</div>", "\n"), end='')

        with fileinput.FileInput("artist_S.txt", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(
                    """<a class="tracklist-row__artist-name-link" href="/artist/07YZf4WDAMNwqr4jfgOZ8y" tabindex="-1">""",
                    ""), end='')
        with fileinput.FileInput("song_S.txt", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace("</a>", "\n"), end='')
            for line in file:
                print(line.replace("""<a class="tracklist-row__artist-name-link" href="/artist/""", ""), end='')
            for line in file:
                print(line.replace(""" tabindex="-1">""", ""), end='')
        new_list = []
        list_art = open("artist_S.txt").readlines()
        for art in list_art:
            new_list.append(art[23:])

        f_3 = open("Final_S.txt", "w")

        for art in new_list:
            f_3.write(str(art))
        f_3.close()


class Y_Bot(object):

    def __init__(self, username, password):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('https://music.youtube.com/')
        sleep(1)

    def ad_fav(self, list_1):
        try:
            for song in list_1:
                sleep(1)
                self.driver.find_element_by_xpath(
                    "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div["
                    "1]/paper-icon-button[1]/iron-icon").click()
                sleep(3)
                self.driver.find_element_by_xpath(
                    "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div["
                    "1]/input").send_keys(
                    song)
                sleep(4)
                self.driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/div["
                                                  "3]/ytmusic-search-page/ytmusic-section-list-renderer/div["
                                                  "2]/ytmusic-shelf-renderer[1]/div["
                                                  "1]/ytmusic-responsive-list-item-renderer").click()
                sleep(3)
                self.driver.find_element_by_xpath(
                    "/html/body/ytmusic-app/ytmusic-app-layout/div["
                    "3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div["
                    "1]/ytmusic-responsive-list-item-renderer/ytmusic-menu-renderer/paper-icon-button ").click()
                sleep(2)
                self.driver.find_element_by_xpath("""//html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown
                /div/ytmusic-menu-popup-renderer/paper-listbox/ytmusic-menu-navigation-item-renderer[2]""").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown["
                                                  "2]/div/ytmusic-add-to-playlist-renderer/div["
                                                  "1]/ytmusic-playlist-add-to-option-renderer[1]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div["
                                                  "2]/ytmusic-search-box/div/div[1]/paper-icon-button["
                                                  "2]/iron-icon").click()
                sleep(1)

        except selenium.common.exceptions.WebDriverException:
            print("Error Item Not Found")
        except IndentationError:
            print("Error White Indentation")
        except selenium.common.exceptions.ElementNotInteractableException:
            print("Not Found (SURFACE)")


bot = S_Bot()
bot.login()
sleep(2)
bot.s_song()
sleep(2)
bot.clean_txt()

list_fav = open("Final_S.txt").readlines()

yBot = Y_Bot(usrY, passY)
yBot.ad_fav(list_fav)
