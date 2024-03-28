from tkinter import *
import requests

# Function to fetch Kanye West quote
def get_quote():
    # Send GET request to Kanye West quote API
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    # Extract quote from JSON response
    quote = response.json()['quote']
    # Update quote text on canvas
    canvas.itemconfig(quote_text, text=quote)

# Create main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create canvas to display background and quote text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Create button to fetch quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Start the tkinter event loop
window.mainloop()
