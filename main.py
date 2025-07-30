from app import SimplifyItApp
import tkinter as tk


def launch_service(service_name):
    menu.destroy()
    app = SimplifyItApp(service_name)
    app.mainloop()


# Simple Menu UI
menu = tk.Tk()
menu.title("SimplifyIt - Choose Service")
menu.geometry("400x250")
tk.Label(
    menu,
    text="Choose a Service to Begin",
    font=("Arial", 16)
).pack(pady=30)
tk.Button(
    menu,
    text="Apply for NHIF",
    width=20,
    command=lambda: launch_service("NHIF")
).pack(pady=10)
tk.Button(
    menu,
    text="Apply for NSSF",
    width=20,
    command=lambda: launch_service("NSSF")
).pack(pady=10)
tk.Button(menu, text="Exit", width=20, command=menu.quit).pack(pady=10)
menu.mainloop()
