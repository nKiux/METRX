import tkinter as tk
import psutil

def windowscontrol():
    usuage = psutil.cpu_percent(1)
    leng = int(screen_width * usuage / 100)
    print(usuage)
    if leng < 200:
        root.geometry(f"240x0")
    else:
        root.geometry(f"{leng}x0")
    root.title(f"CPU:{usuage}% || METRX")
    
    root.after(50, windowscontrol)

root = tk.Tk()
root.call('wm', 'attributes', '.', '-topmost', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"+0+0")
root.iconbitmap('MX.ico')
windowscontrol()
root.mainloop()