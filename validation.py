from tkinter import messagebox


def validate_step_input(app):
    step = app.current_step

    if step == 0:
        name = app.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter your full name.")
            return False
        app.user_data[0] = name

    elif step == 1:
        id_number = app.id_entry.get().strip()
        if not id_number.isdigit():
            messagebox.showerror("Error", "ID must be numeric.")
            return False
        app.user_data[1] = id_number

    elif step == 2:
        phone = app.phone_entry.get().strip()
        if not (
            phone.startswith("07")
            and len(phone) == 10
            and phone.isdigit()
        ):
            messagebox.showerror(
                "Error",
                "Enter a valid phone number (e.g., 07XXXXXXXX)."
            )
            return False
        app.user_data[2] = phone

    elif step == 3:
        status = app.employment_status.get()
        if not status:
            messagebox.showerror(
                "Error",
                "Please select your employment status."
            )
            return False
        app.user_data[3] = status

    return True
