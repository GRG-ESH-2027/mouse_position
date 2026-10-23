import tkinter as tk
import pyautogui
import time

def get_position():
    # الانتظار 5 ثواني قبل أخذ الإحداثيات
    time.sleep(5)
    x, y = pyautogui.position()
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    entry_x.insert(0, str(x))
    entry_y.insert(0, str(y))

# إنشاء النافذة
root = tk.Tk()
root.title("الحصول على إحداثيات الماوس")

# تكبير حجم الفورم
root.geometry("400x200")  # العرض × الطول

# إعداد الخط
font_style = ("Arial", 16, "bold")

# مربعات النص
tk.Label(root, text="قيمة X:", font=font_style).grid(row=0, column=0, padx=10, pady=10)
entry_x = tk.Entry(root, font=font_style)
entry_x.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="قيمة Y:", font=font_style).grid(row=1, column=0, padx=10, pady=10)
entry_y = tk.Entry(root, font=font_style)
entry_y.grid(row=1, column=1, padx=10, pady=10)

# زر التنفيذ
btn = tk.Button(root, text="احصل على الإحداثيات", command=get_position, font=font_style)
btn.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()


