import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get().strip()
    mobile = entry_mobile.get().strip()
    email = entry_email.get().strip()
    gender = gender_var.get()
    topics = [listbox.get(i) for i in listbox.curselection()]
    satisfaction = satisfaction_var.get()
    newsletter = newsletter_var.get()
    feedback = text_feedback.get("1.0", tk.END).strip()

    if not name or not email or not mobile or not gender:
        messagebox.showwarning("Input Error", "Please fill in Name, Mobile Number, Email, and select Gender.")
        return

    result = f"""
    Name: {name}
    Mobile: {mobile}
    Email: {email}
    Gender: {gender}
    Topics: {', '.join(topics)}
    Satisfaction: {satisfaction}
    Subscribe: {'Yes' if newsletter else 'No'}
    Feedback: {feedback}
    """
    messagebox.showinfo("Submitted Data", result)

def clear_form():
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    listbox.selection_clear(0, tk.END)
    gender_var.set("")
    satisfaction_var.set("")
    newsletter_var.set(False)
    text_feedback.delete("1.0", tk.END)

root = tk.Tk()
root.title("Feedback Form")

# Name
tk.Label(root, text="Name:").pack(anchor="w")
entry_name = tk.Entry(root, width=40)
entry_name.pack()

# Mobile Number
tk.Label(root, text="Mobile Number:").pack(anchor="w")
entry_mobile = tk.Entry(root, width=40)
entry_mobile.pack()

# Email
tk.Label(root, text="Email:").pack(anchor="w")
entry_email = tk.Entry(root, width=40)
entry_email.pack()

# Gender
tk.Label(root, text="Gender:").pack(anchor="w")
gender_var = tk.StringVar()
for gender in ["Male", "Female", "Other"]:
    tk.Radiobutton(root, text=gender, variable=gender_var, value=gender).pack(anchor="w")

# Topics You Liked
tk.Label(root, text="Topics You Liked:").pack(anchor="w")
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=3)
for topic in ["Python", "Java", "C"]:
    listbox.insert(tk.END, topic)
listbox.pack()

# Satisfaction
tk.Label(root, text="Satisfaction:").pack(anchor="w")
satisfaction_var = tk.StringVar()
for level in ["Excellent", "Good", "Average", "Poor"]:
    tk.Radiobutton(root, text=level, variable=satisfaction_var, value=level).pack(anchor="w")

# Newsletter
newsletter_var = tk.BooleanVar()
tk.Checkbutton(root, text="Subscribe to Newsletter", variable=newsletter_var).pack(anchor="w")

# Feedback
tk.Label(root, text="Feedback:").pack(anchor="w")
text_feedback = tk.Text(root, height=4, width=40)
text_feedback.pack()

# Submit and Clear Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Submit", command=submit_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear", command=clear_form).pack(side=tk.LEFT, padx=5)

root.mainloop()
