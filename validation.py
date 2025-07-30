from tkinter import messagebox


def validate_step_input(app, service):
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
        if service == "NHIF":
            phone = app.phone_entry.get().strip()
            if not (
                phone.startswith("07")
                and len(phone) == 10
                and phone.isdigit()
            ):
                messagebox.showerror("Error", "Enter a valid phone number.")
                return False
            app.user_data[2] = phone
        else:
            email = app.email_entry.get().strip()
            if "@" not in email or "." not in email:
                messagebox.showerror("Error", "Enter a valid email address.")
                return False
            app.user_data[2] = email

    elif step == 3:
        status = app.employment_status.get()
        if not status:
            messagebox.showerror(
                "Error",
                "Please select your employment status."
            )
            return False
        app.user_data[3] = status

    elif step == 4 and service == "NSSF":
        kra = app.kra_entry.get().strip()
        if not kra or len(kra) < 5:
            messagebox.showerror("Error", "Please enter a valid KRA PIN.")
            return False

    return True
