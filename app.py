import tkinter as tk
from tkinter import messagebox
from steps import create_step_frames
from validation import validate_step_input
from utils import show_summary


class SimplifyItApp(tk.Tk):
    def __init__(self, service_name):
        super().__init__()
        self.title(f"SimplifyIt - {service_name} Assistant")
        self.geometry("550x320")
        self.configure(bg="#f5f5f5")

        self.service = service_name
        self.user_data = [""] * 5
        self.frames = []
        self.current_step = 0

        self.name_entry = None
        self.id_entry = None
        self.phone_entry = None
        self.email_entry = None
        self.kra_entry = None
        self.employment_status = tk.StringVar()
        self.upload_var = tk.IntVar()

        self.frames = create_step_frames(self, self.service)
        self.show_frame(0)

    def show_frame(self, index):
        for frame in self.frames:
            frame.pack_forget()
        self.frames[index].pack(fill="both", expand=True)

    def next_step(self):
        if not validate_step_input(self, self.service):
            return
        self.current_step += 1
        self.show_frame(self.current_step)

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_frame(self.current_step)

    def submit(self):
        if self.service == "NHIF" and self.upload_var.get() == 0:
            messagebox.showerror("Error", "Please confirm document upload.")
            return
        if self.service == "NHIF":
            self.user_data[4] = "Uploaded"
        else:
            self.user_data[4] = self.kra_entry.get()
        show_summary(self.user_data, self.service)
        self.quit()
