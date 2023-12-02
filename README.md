# METRX
an python based CPU indicator.

# 什麼是METRX？
**METRX是一個實用的視覺化CPU使用率指示器，它可以在任何時候，任何地方為你提供CPU的使用率**

# 下載的時候跳出病毒通知，這個東東安全嗎？
**METRX的程式碼完全公開，由於包裝時使用的PyInstaller需要指定的檔案，會導致防毒軟體誤報**

**詳情請見：[Github] <https://github.com/pyinstaller/pyinstaller/issues/5668>**

**若有疑慮，也可以下載`METRX.py`，自行在Code或其他IDE裡面進行編譯運行**

# METRX的架構是什麼？
**METRX是基於Python建置的程式，透過PyInstaller轉譯成.exe檔案在沒有安裝Python的電腦上運行，請安心使用！**

若防毒軟體擋下並偵測到 `Win32/Wacapew.C!ml`，

是因為Python打包成exe時所使用的 `PyInstaller` 需要用到的功能所導致，詳情請見：

https://github.com/pyinstaller/pyinstaller/issues/5668

# v0.1 初代功能：
根據CPU使用率調整視窗大小，超酷超實用

Adjust window size by CPU usage, super cool and useful
