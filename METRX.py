import tkinter as tk
import psutil
import asyncio
import time

async def windowcontrol():
    while True:
        global leng
        global usuage
        usuage = psutil.cpu_percent(1)
        leng = int(screen_width * usuage / 100)
        print(usuage)
        if leng < 240:
            leng = 240
        root.title(f"CPU:{usuage}% || METRX")
        root.update()
        #root.after(10, windowcontrol)
        time.sleep(0.1)
        root.geometry(f"{leng}x0")
        await windowcontrol()

root = tk.Tk()
root.call('wm', 'attributes', '.', '-topmost', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"+0+{screen_height - 100}")
#root.iconbitmap('MX.ico')
asyncio.run(windowcontrol())
root.mainloop()


