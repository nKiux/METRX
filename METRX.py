import tkinter as tk
import psutil
import asyncio
import time

async def windowcontrol():
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
    await windupdt()
    await time.sleep(100)

async def windupdt():
    root.geometry(f"{leng}x0")
    await windowcontrol()

root = tk.Tk()
root.call('wm', 'attributes', '.', '-topmost', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"+0+0")
root.iconbitmap('MX.ico')
asyncio.run(windowcontrol())
asyncio.run(windupdt())
root.mainloop()


