import tkinter as tk


def create_step_frames(app, service):
    frames = []

    # Step 1 - Name
    f1 = create_frame(app, "Step 1: Enter your Full Name", app.next_step, None)
    app.name_entry = add_entry(f1)
    frames.append(f1)

    # Step 2 - ID
    f2 = create_frame(
        app,
        "Step 2: Enter your ID Number",
        app.next_step,
        app.prev_step
    )
    app.id_entry = add_entry(f2)
    frames.append(f2)

    # Step 3 - Phone or Email
    f3 = create_frame(
        app,
        "Step 3: Enter your Contact Info",
        app.next_step,
        app.prev_step
    )
    if service == "NHIF":
        app.phone_entry = add_entry(f3)
    else:
        app.email_entry = add_entry(
            f3
        )
    frames.append(f3)

    # Step 4 - Employment
    f4 = create_frame(
        app,
        "Step 4: Select Employment Status",
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

    # Step 5 - Upload or KRA
    if service == "NHIF":
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
    else:
        f5 = create_frame(
            app,
            "Step 5: Enter your KRA PIN",
            app.submit,
            app.prev_step
        )
        app.kra_entry = add_entry(f5)
    frames.append(f5)

    return frames


def create_frame(app, label_text, next_cmd, back_cmd):
    frame = tk.Frame(app, bg="#f5f5f5")
    tk.Label(
        frame,
        text=label_text,
        font=("Arial", 14),
        bg="#f5f5f5"
    ).pack(pady=20)

    button_frame = tk.Frame(frame, bg="#f5f5f5")
    button_frame.pack(side="bottom", pady=20)

    if back_cmd:
        tk.Button(
            button_frame,
            text="Back",
            width=10,
            bg="#ccc",
            command=back_cmd
        ).pack(side="left", padx=10)
    if next_cmd:
        btn_text = "Submit" if next_cmd == app.submit else "Next"
        tk.Button(
            button_frame,
            text=btn_text,
            width=10,
            bg="#4CAF50",
            fg="white",
            command=next_cmd
        ).pack(side="right", padx=10)

    return frame


def add_entry(parent):
    entry = tk.Entry(parent, width=40)
    entry.pack(pady=10)
    return entry
