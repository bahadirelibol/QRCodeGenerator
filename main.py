import customtkinter as ctk
from tkinter import filedialog

import pyqrcode

import os


def generate_qr_code():
    try:
        # Get the URL from the entry widget
        url = url_entry.get()
        # Check if the URL is empty
        if not url:
            raise ValueError("URL cannot be empty.")

        # Generate the QR code
        qr_code = pyqrcode.create(url)

        # Open a file dialog to get the file path to save the QR code
        file_path = filedialog.asksaveasfilename(defaultextension=".svg",
                                                 filetypes=[("SVG files", "*.svg")],
                                                 title="Save QR Code")
        # Check if the file path was provided
        if not file_path:
            status_label.configure(text="Save operation cancelled.", text_color="red")
            return

        # Check if the directory for the file path exists
        if not os.path.dirname(file_path):
            raise FileNotFoundError("Directory for the file path does not exist.")

        # Save the QR code as an SVG file
        qr_code.svg(file_path, scale=10)
        status_label.configure(text="QR Code generated and saved successfully!", text_color="green")
    except ValueError as ve:
        # Handle empty URL error
        status_label.configure(text=str(ve), text_color="red")
    except FileNotFoundError as fe:
        # Handle directory not found error
        status_label.configure(text=str(fe), text_color="red")
    except Exception as e:
        # Handle any other errors
        status_label.configure(text=f"An error occurred: {e}", text_color="red")
    finally:
        # Clear the URL entry field after processing
        url_entry.delete(0, ctk.END)


def close_program():
    root.destroy()


# Set the appearance mode and color theme for the application
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Initialize the main window
root = ctk.CTk()
root.title("QR Code Generator")
root.geometry("600x400")

# Create and place widgets in the main window
title_label = ctk.CTkLabel(root, text="Enter URL to generate QR code:", font=("Arial", 14))
title_label.pack(pady=20)

url_entry = ctk.CTkEntry(root, width=400, placeholder_text="Enter URL here")
url_entry.pack(pady=10)

generate_button = ctk.CTkButton(root, text="Generate QR Code", width=250, command=generate_qr_code)
generate_button.pack(pady=20)

status_label = ctk.CTkLabel(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

close_button = ctk.CTkButton(root, text="Exit", width=50, command=close_program)
close_button.pack(padx=20, pady=20, side='right', anchor='s')

root.mainloop()
