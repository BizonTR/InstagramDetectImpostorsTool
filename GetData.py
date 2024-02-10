from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
import os
import datetime
#from App import LoginCorrectMessage,LoginIncorrectMessage

class InstagramTool():
    def __init__(self,userName,password):
        self.browser = webdriver.Chrome()
        self.actions = ActionChains(self.browser)
        self.userLink = f"https://www.instagram.com/{userName}/"
        self.userFollowersLink = f"https://www.instagram.com/{userName}/followers/"
        self.userFollowingsLink = f"https://www.instagram.com/{userName}/following/"
        self.loginLink = "https://www.instagram.com/"
        self.userName = userName
        self.password = password


    def Login(self):
        self.browser.get(self.loginLink)
        time.sleep(2)
        userNameXpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        passwordXpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        userNameInput = self.browser.find_element('xpath', userNameXpath)
        passwordInput = self.browser.find_element('xpath', passwordXpath)

        userNameInput.send_keys(self.userName)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(7)

        #try-catch daha mantıklı gibi üstünde düşünülür
        # wrongDataInfo = self.browser.find_element('xpath','//*[@id="loginForm"]/span/div')

        # if wrongDataInfo:
        #     print("incorrect.")
        #     # LoginIncorrectMessage()
        #     # self.Close()
        # else:
        #     # LoginCorrectMessage()
        #     print("login successful.")

    def GetFollowers(self):
        targetFolderPath = os.path.join("./", "output", str((datetime.date.today().strftime("%d_%m_%Y"))))
        os.makedirs(targetFolderPath, exist_ok=True)
        targetTxtPath = os.path.join(targetFolderPath, "followers.txt")
        with open(targetTxtPath, "w") as followersTxt:
            pass

        self.browser.get(self.userFollowersLink)
        time.sleep(5)

        dialog_window = self.browser.find_element("xpath","//*[@role='dialog']")
        main_div = self.browser.find_element(By.CLASS_NAME, "_aano")
        sub_divs = main_div.find_elements(By.TAG_NAME, "div")
        target_div1 = sub_divs[0]
        sub_divs2 = target_div1.find_elements(By.TAG_NAME,"div")
        target_div2 = sub_divs2[0]
        followers = target_div2.find_elements("xpath","./div")
        followerCount = len(followers) #12

        while True:
            self.actions.move_to_element(dialog_window).perform()
            scroll_origin = ScrollOrigin.from_element(dialog_window)
            self.actions.scroll_from_origin(scroll_origin, 0, 5000).perform()  # 550 piksel aşağı kaydır

            time.sleep(6)

            followers = target_div2.find_elements("xpath","./div")
            newCount = len(followers)

            if followerCount != newCount:
                followerCount = newCount
                print("newcount: " + str(newCount))
            else:
                break
        with open(targetTxtPath, "w") as followersTxt:
            for widget in followers:
                follower = widget.find_element(By.TAG_NAME,"a")

                if len(str(follower.get_attribute("href"))) == 0:
                    follower = widget.find_element(By.TAG_NAME,"span")
                    # print(str(follower.text))
                    nickName = follower.text
                    followersTxt.write(nickName + "\n")
                    time.sleep(0.5)
                else:
                    # print(str(follower.get_attribute("href")))
                    nickName = str.split(follower.get_attribute("href"),"/")[-2]
                    followersTxt.write(nickName + "\n")
                    time.sleep(0.5)

    def GetFollowings(self):
        targetFolderPath = os.path.join("./", "output", str((datetime.date.today().strftime("%d_%m_%Y"))))
        os.makedirs(targetFolderPath, exist_ok=True)
        targetTxtPath = os.path.join(targetFolderPath, "followings.txt")
        with open(targetTxtPath, "w") as followingsTxt:
            pass
        self.browser.get(self.userFollowingsLink)
        time.sleep(3)

        dialog_window = self.browser.find_element(By.CLASS_NAME,"_aano")
        main_div = self.browser.find_element(By.CLASS_NAME, "_aano")
        sub_divs = main_div.find_elements(By.TAG_NAME, "div")
        target_div1 = sub_divs[0] #hesabı takip edenlerin columnu
        sub_divs2 = target_div1.find_elements(By.TAG_NAME,"div")
        target_div2 = sub_divs2[0]
        followings = target_div2.find_elements("xpath","./div")
        followingsCount = len(followings) #12

        while True:
            self.actions.move_to_element(dialog_window).perform()

            # element_width = dialog_window.size['width']
            # element_height = dialog_window.size['height']
            # middle_x = element_width / 2
            # middle_y = element_height / 2

            scroll_origin = ScrollOrigin.from_element(dialog_window)

            self.actions.scroll_from_origin(scroll_origin, 0, 5000).perform()  # 550 piksel aşağı kaydır

            time.sleep(6)

            followings = target_div2.find_elements("xpath","./div")
            newCount = len(followings)

            if followingsCount != newCount:
                followingsCount = newCount
                print("newcount: " + str(newCount))
            else:
                break
        with open(targetTxtPath, "w") as followingsTxt:
            for widget in followings:
                follower = widget.find_element(By.TAG_NAME,"a")

                if len(str(follower.get_attribute("href"))) == 0:
                    follower = widget.find_element(By.TAG_NAME,"span")
                    # print(str(follower.text))
                    nickName = follower.text
                    followingsTxt.write(nickName + "\n")
                    time.sleep(0.5)
                else:
                    # print(str(follower.get_attribute("href")))
                    nickName = str.split(follower.get_attribute("href"),"/")[-2]
                    followingsTxt.write(nickName + "\n")
                    time.sleep(0.5)

    def Scan(self):
        self.Login()
        self.GetFollowings()
        self.GetFollowers()
        return(str((datetime.date.today().strftime("%d_%m_%Y"))))
        
    def Close(self):
        self.browser.close()


    def Idle(self):
        while True:
            pass
        

# instagramTool = InstagramTool()
# instagramTool.Scan()
#instagramTool.idle()