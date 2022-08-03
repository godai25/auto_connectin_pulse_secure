# Pulse Secureの自動接続

## ファイル構成

***

1. main.py  -> メインプログラム
1. user.ini  -> Pulse Secureに接続するためのユーザ名/パスワード
1. readme.md  -> このファイル

## 準備

***

- 「user.ini」に秘密IDとパスワードを保持しておくこと

## 実行内容

***

1. iniファイルを読み取り。
1. Pulse Secure のCUIから切断を実行
1. GUIアプリでAlt操作を行い、接続を行う。

## 起動方法

***

- python main.py

## 接続できない場合

***

- コマンドライン（bat）で呼び出しているので、stdoutにエラーを吐いています。
