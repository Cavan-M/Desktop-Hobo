import tkinter as tk
from win32api import GetMonitorInfo, MonitorFromPoint
from tom import Tom

monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
work_area = monitor_info.get("Work")

window = tk.Tk()
window.geometry("{}x{}".format(work_area[2], work_area[3]))
window.resizable(False, False)
window.overrideredirect(True)
window.attributes('-topmost', True)
window.configure(background='white')
window.wm_attributes('-transparentcolor', 'white')
window.update()

mainFrame = tk.Canvas(master=window, height=window.winfo_height(), width=window.winfo_width(), bg="white", highlightbackground="white")
mainFrame.pack(fill=tk.BOTH, side=tk.TOP)

tom = Tom(mainFrame, window.winfo_width()*0.1, window.winfo_height()-66)

window.mainloop()
