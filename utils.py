from tkinter import messagebox


def show_summary(data):
    summary = (
        f"✅ Application Summary:\n"
        f"Name: {data[0]}\n"
        f"ID: {data[1]}\n"
        f"Phone: {data[2]}\n"
        f"Employment: {data[3]}\n"
        f"Documents: {data[4]}"
    )
    messagebox.showinfo("Submission Complete", summary)
