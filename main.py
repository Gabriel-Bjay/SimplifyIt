import tkinter as tk
from tkinter import messagebox


class NHIFApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SimplifyIt - NHIF Assistant")
        self.geometry("500x300")
        self.resizable(False, False)

        self.user_data = ["", "", "", "", ""]  # Store inputs

        self.frames = []
        self.current_step = 0

        self.create_steps()
        self.show_frame(0)

    def create_steps(self):
        # Step 1 - Name
        frame1 = self.create_frame("Step 1: Enter your Full Name", 0)
        self.name_entry = self.add_entry(frame1)

        # Step 2 - ID Number
        frame2 = self.create_frame("Step 2: Enter your ID Number", 1)
        self.id_entry = self.add_entry(frame2)

        # Step 3 - Phone Number
        frame3 = self.create_frame("Step 3: Enter your Phone Number", 2)
        self.phone_entry = self.add_entry(frame3)

        # Step 4 - Employment Status
        frame4 = self.create_frame("Step 4: Employment Status", 3)
        self.employment_status = tk.StringVar()
        tk.Radiobutton(
            frame4,
            text="Employed",
            variable=self.employment_status,
            value="Employed"
        ).pack(pady=5)
        tk.Radiobutton(
            frame4,
            text="Self-employed",
            variable=self.employment_status,
            value="Self-employed"
        ).pack(pady=5)

        # Step 5 - Simulated Upload
        frame5 = self.create_frame("Step 5: Simulate Document Upload", 4)
        self.upload_var = tk.IntVar()
        tk.Checkbutton(
            frame5,
            text="I have uploaded required documents",
            variable=self.upload_var
        ).pack(pady=10)

    def create_frame(self, text, step_index):
        frame = tk.Frame(self)
        label = tk.Label(frame, text=text, font=("Arial", 14))
        label.pack(pady=20)

        button_frame = tk.Frame(frame)
        button_frame.pack(side="bottom", pady=20)

        if step_index > 0:
            back_btn = tk.Button(
                button_frame,
                text="Back",
                command=self.prev_step
            )
            back_btn.pack(side="left", padx=10)

        if step_index < 4:
            next_btn = tk.Button(
                button_frame,
                text="Next",
                command=self.next_step
            )
            next_btn.pack(side="right", padx=10)
        else:
            submit_btn = tk.Button(
                button_frame,
                text="Submit",
                command=self.submit
            )
            submit_btn.pack(side="right", padx=10)

        self.frames.append(frame)
        return frame

    def add_entry(self, parent):
        entry = tk.Entry(parent, width=40)
        entry.pack(pady=10)
        return entry

    def show_frame(self, index):
        for frame in self.frames:
            frame.pack_forget()
        self.frames[index].pack(fill="both", expand=True)

    def next_step(self):
        if self.current_step == 0:
            self.user_data[0] = self.name_entry.get()
            if not self.user_data[0]:
                messagebox.showerror("Error", "Please enter your name.")
                return
        elif self.current_step == 1:
            self.user_data[1] = self.id_entry.get()
            if not self.user_data[1].isdigit():
                messagebox.showerror("Error", "ID must be numeric.")
                return
        elif self.current_step == 2:
            self.user_data[2] = self.phone_entry.get()
            if (
                not self.user_data[2].startswith("07")
                or len(self.user_data[2]) != 10
            ):
                messagebox.showerror("Error", "Enter a valid phone number.")
                return
        elif self.current_step == 3:
            self.user_data[3] = self.employment_status.get()
            if not self.user_data[3]:
                messagebox.showerror(
                    "Error",
                    "Please select your employment status."
                )
                return

        self.current_step += 1
        self.show_frame(self.current_step)

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_frame(self.current_step)

    def submit(self):
        if self.upload_var.get() == 0:
            messagebox.showerror("Error", "Please confirm document upload.")
            return
        self.user_data[4] = "Uploaded"
        summary = (
            f"✅ Application Summary:\n"
            f"Name: {self.user_data[0]}\n"
            f"ID: {self.user_data[1]}\n"
            f"Phone: {self.user_data[2]}\n"
            f"Employment: {self.user_data[3]}\n"
            f"Documents: {self.user_data[4]}"
        )
        messagebox.showinfo("Submission Complete", summary)
        self.quit()


# Run App
if __name__ == "__main__":
    app = NHIFApplication()
    app.mainloop()
