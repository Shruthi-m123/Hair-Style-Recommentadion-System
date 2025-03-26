import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image  # Pillow library for handling images

selected_file_path = ""  # Global variable to store the selected file path

# Function to handle file selection
def select_image():
    global selected_file_path  # Access the global variable
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        selected_file_path = file_path  # Update the global variable with selected file path
        display_image(selected_file_path)
        process_image(selected_file_path)

# Function to display selected image
def display_image(file_path):
    image = Image.open(file_path)
    image = image.resize((300, 300))  # Resize image as needed
    img_tk = ImageTk.PhotoImage(image)

    # Update label with the selected image
    label.config(image=img_tk)
    label.image = img_tk  # Keep a reference to the image to prevent garbage collection

# Function to process the selected image file path
def process_image(file_path):
    # Replace this with your custom image processing logic
    print("Selected file path:", file_path)

# Function to close the Tkinter window
def close_window():
    root.destroy()

# Create Tkinter application window
root = tk.Tk()
root.title("Image Uploader")

# Create a button to select image
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=20)

# Create a label to display the selected image
label = tk.Label(root)
label.pack()

# Create an "OK" button to close the window
ok_button = tk.Button(root, text="OK", command=close_window)
ok_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# After the Tkinter event loop ends (window closed), you can access selected_file_path
print("Final selected file path:", selected_file_path)

