import tkinter as tk
from tkinter import messagebox


def build_gui():
    """Construct and run the VO2 max calculator GUI."""
    def calculate_vo2max():
        try:
            age = float(age_entry.get())
            rhr = float(rhr_entry.get())
            vo2max = 15.3 * ((208 - (0.7 * age)) / rhr)
            result_label.config(text=f"Estimated VO₂ max: {vo2max:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for age and RHR.")

    # Create main window
    root = tk.Tk()
    root.title("VO₂ Max Calculator")
    root.geometry("350x200")

    # Age input
    tk.Label(root, text="Enter your age:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    age_entry = tk.Entry(root)
    age_entry.grid(row=0, column=1, padx=10, pady=10)

    # RHR input
    tk.Label(root, text="Enter your resting heart rate (RHR):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    rhr_entry = tk.Entry(root)
    rhr_entry.grid(row=1, column=1, padx=10, pady=10)

    # Calculate button
    calc_button = tk.Button(root, text="Calculate VO₂ Max", command=calculate_vo2max)
    calc_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Result label
    result_label = tk.Label(root, text="Estimated VO₂ max: ")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    Byandershallman_label = tk.Label(root, text="Byandershallman")
    Byandershallman_label.grid(row=4, column=0, columnspan=2, pady=5)

    # Run the app
    root.mainloop()


if __name__ == "__main__":
    build_gui()