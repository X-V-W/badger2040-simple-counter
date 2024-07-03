import time
import badger2040
import badger_os
import json

# Path to the state file
STATE_FILE_PATH = "/state/counter.json"

# Initialize the Badger2040 display
display = badger2040.Badger2040()
display.set_update_speed(3)
WIDTH, HEIGHT = display.get_bounds()

# Function to read the counter state from a file
def read_counter():
    try:
        with open(STATE_FILE_PATH, 'r') as file:
            data = json.load(file)
            return data.get("counter", 0)
    except (OSError, ValueError):
        return 0

# Function to save the counter state to a file
def save_counter(counter):
    with open(STATE_FILE_PATH, 'w') as file:
        json.dump({"counter": counter}, file)

# Initialize the counter
counter = read_counter()

# Function to display the counter on the screen
def display_counter():
    display.set_pen(0)  # Set pen to white (background)
    display.clear()  # Clear the screen
    display.set_pen(15)  # Set pen to black (text)
    display.set_font("bitmap8")  # Set the font
    counter_str = f"{counter:04d}"  # Format counter as a 4-digit string

    # Calculate text width and height
    text_width = display.measure_text(counter_str, scale=13)
    text_height = 8 * 12  # font height * scale

    # Calculate position to center the text
    x = (WIDTH - text_width) // 2
    y = (HEIGHT - text_height) // 2

    display.text(counter_str, x, y, scale=14)
    display.update()

# Initial display
display_counter()

# Main loop
while True:

    # zero the counter
    if display.pressed(badger2040.BUTTON_UP) and display.pressed(badger2040.BUTTON_DOWN): 
        counter = 0
        save_counter(counter)  # Save the counter state
        display_counter()
        time.sleep(1)  # Debounce delay for zeroing
    
    # add 1000 or substract to the counter
    elif display.pressed(badger2040.BUTTON_A): 
        if display.pressed(badger2040.BUTTON_UP):
            counter += 1000
            save_counter(counter)  # Save the counter state
            display_counter()
            time.sleep(0.2)  # Debounce delay
        elif display.pressed(badger2040.BUTTON_DOWN):
            counter -= 1000
            save_counter(counter)  # Save the counter state
            display_counter()
            time.sleep(0.2)  # Debounce delay
    
    # add or substract 100 to the counter
    elif display.pressed(badger2040.BUTTON_B): 
        if display.pressed(badger2040.BUTTON_UP):
            counter += 100
            save_counter(counter)  # Save the counter state
            display_counter()
            time.sleep(0.2)  # Debounce delay
        elif display.pressed(badger2040.BUTTON_DOWN):
            counter -= 100
            save_counter(counter)  # Save the counter state
            display_counter()
            time.sleep(0.2)  # Debounce delay
    
    # add or substract 10 to the counter
    elif display.pressed(badger2040.BUTTON_C):
        if display.pressed(badger2040.BUTTON_UP):
            counter += 10
            save_counter(counter)  # Save the counter state
            display_counter()
            time.sleep(0.2)  # Debounce delay
        elif display.pressed(badger2040.BUTTON_DOWN):
            counter -= 10
            save_counter(counter)  # Save the counter state
            display_counter()
            time.sleep(0.2)  # Debounce delay
    
    # add 1 to the counter
    elif display.pressed(badger2040.BUTTON_UP):
        counter += 1
        save_counter(counter)  # Save the counter state
        display_counter()
        time.sleep(0.2)  # Debounce delay
    
    # substract 1 from the counter
    elif display.pressed(badger2040.BUTTON_DOWN):
        counter -= 1
        save_counter(counter)  # Save the counter state
        display_counter()
        time.sleep(0.2)  # Debounce delay


    # Short sleep to prevent high CPU usage
    time.sleep(0.05)

def turn_off():
    display.set_pen(15)  # Set pen to white
    display.clear()  # Clear the screen
    display.update()
    badger_os.exit()

turn_off()
