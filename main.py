import subprocess
import win32gui
import pyautogui
import os
from time import sleep


def main():

    # ini ファイル読込
    username, password = read_ini()
    if not  username or not password :
        print(f'秘密ID: {username}, パスワード: {password}')
        print('エラー : "user.ini"に、秘密IDかパスワードがありません')
        exit()

    # Pulse Secureを切断する
    os.system(r'"C:\Program Files (x86)\Common Files\Pulse Secure\Integration\pulselauncher.exe" -url rasps.konicaminolta.jp/PC -signout')
    sleep(2)

	# Pulse Secureを起動する
    subprocess.Popen([r'C:\Program Files (x86)\Common Files\Pulse Secure\JamUI\Pulse.exe','-show'],shell=True)
    sleep(1)

	# Pulse Secureをアクティブにする
    psapp = win32gui.FindWindow(None,'Pulse Secure')
    sleep(1)
    win32gui.SetForegroundWindow(psapp)
    sleep(1)

    # Pulse Secure 接続
    pyautogui.press('f')
    pyautogui.press('o')
    pyautogui.press('c')

    sleep(4)

    # パスワード入力
    pyautogui.typewrite(username)
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('enter')


def read_ini() :
    usr, pswd = '',''
    if not os.path.isfile(r'.\user.ini') :
        print('エラー : "user.ini" がありません。')
    else :
        with open('user.ini',encoding="utf-8") as f:
            str = f.read()
            lines = str.split("\n")
            if len(lines) >= 3 :
                usr, pswd = lines[1], lines[2]
    return usr, pswd


if __name__ == '__main__':
    main()