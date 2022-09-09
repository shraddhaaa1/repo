from selenium import webdriver
from selenium.webdriver.common.by import By

class login_fb():
    def __init__(self,driver):
        self.driver = driver
        self.id_text_id = 'email'
        self.pas_text_id = 'pass'
        self.but_xp = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'

    def usern(self, username):
        self.driver.find_element(By.ID, self.id_text_id).clear()
        self.driver.find_element(By.ID, self.id_text_id).send_keys(username)
    def passw(self,input):
        self.driver.find_element(By.ID, self.pas_text_id).clear()
        self.driver.find_element(By.ID, self.pas_text_id).send_keys(input)
    def login_butt(self):
        self.driver.find_element(By.XPATH, self.but_xp).click()


        #hellow hi
