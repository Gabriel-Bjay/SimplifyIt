import tkinter as tk


def create_step_frames(app):
    frames = []

    # Step 1: Full Name
    f1 = create_frame(app, "Step 1: Enter your Full Name", app.next_step, None)
    app.name_entry = add_entry(f1)
    frames.append(f1)

    # Step 2: ID Number
    f2 = create_frame(
        app,
        "Step 2: Enter your ID Number",
        app.next_step,
        app.prev_step
    )
    app.id_entry = add_entry(f2)
    frames.append(f2)

    # Step 3: Phone Number
    f3 = create_frame(
        app,
        "Step 3: Enter your Phone Number",
        app.next_step,
        app.prev_step
    )
    app.phone_entry = add_entry(f3)
    frames.append(f3)

    # Step 4: Employment Status
    f4 = create_frame(
        app,
        "Step 4: Employment Status",
        app.next_step,
        app.prev_step
    )
    tk.Radiobutton(
        f4,
        text="Employed",
        variable=app.employment_status,
        value="Employed"
    ).pack(pady=5)
    tk.Radiobutton(
        f4,
        text="Self-employed",
        variable=app.employment_status,
        value="Self-employed"
    ).pack(pady=5)
    frames.append(f4)

    # Step 5: Simulated Upload
    f5 = create_frame(
        app,
        "Step 5: Confirm Document Upload",
        app.submit,
        app.prev_step
    )
    tk.Checkbutton(
        f5,
        text="I have uploaded required documents",
        variable=app.upload_var
    ).pack(pady=10)
    frames.append(f5)

    return frames


def create_frame(app, label_text, next_cmd, back_cmd):
    frame = tk.Frame(app)
    tk.Label(frame, text=label_text, font=("Arial", 14)).pack(pady=20)

    button_frame = tk.Frame(frame)
    button_frame.pack(side="bottom", pady=20)

    if back_cmd:
        tk.Button(
            button_frame,
            text="Back",
            command=back_cmd
        ).pack(side="left", padx=10)
    if next_cmd:
        tk.Button(
            button_frame,
            text="Next" if next_cmd != app.submit else "Submit",
            command=next_cmd
        ).pack(side="right", padx=10)

    return frame


def add_entry(parent):
    entry = tk.Entry(parent, width=40)
    entry.pack(pady=10)
    return entry
