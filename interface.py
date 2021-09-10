import tkinter as tk
from tkinter.font import Font

import bruh

# Create Tk Window.
root = tk.Tk()
root.title('BRUH Converter')

# Initialize customization variables for GUI Widgets.
main_button_bg = '#0D4BC5'
main_button_font = Font(family = 'Arial', size = 12, weight = 'bold')

general_button_label_bg = '#09F90D'
general_button_font = Font(family = 'Arial', size = 10, weight = 'bold')
general_label_font = Font(family = 'Ubuntu Mono', size = 8, weight = 'normal')

general_entry_bg = '#0DC5B5'
general_entry_font = Font(family = 'Ubuntu Mono', size = 8, weight = 'normal')


#######################################
########## GUI Functions ##############
#######################################

# Method that Sets up Screen.
def initScreen() :
    # Create a Frame for Bruh Conversion.
    global conversion_pane
    conversion_pane = tk.Frame(root)
    # Position Frame onto Screen.
    conversion_pane.grid(row = 0, column = 0, sticky = tk.N + tk.E + tk.S + tk.W)

    nameButton = tk.Button(conversion_pane, text = 'Hi. What is your name?', bg = general_button_label_bg, fg = 'black',
        font = general_button_font, borderwidth = 2, command = lambda : startConversion(str(input_field.get())))
    # Position Button Widget onto Screen.
    nameButton.grid(row = 0, column = 0, padx = (10, 5), pady = (10, 5))

    # Create an Entry Widget.
    input_field = tk.Entry(conversion_pane, width = 30, bg = general_entry_bg, fg = 'black',
        font = general_entry_font, borderwidth = 2)
    # Position Entry Widget onto Screen.
    input_field.grid(row = 0, column = 1, padx = (0, 10), pady = (10, 5))
    # Insert Default Text to Entry Widget.
    input_field.insert(0, 'Enter Your Name')

# Method to Trigger and Display First Bruh Conversion.
def startConversion(name) :
    # Conduct initial 'BRUH' conversion.
    prepare_conversion = tk.Label(conversion_pane, text = f'Hello {name}. I have something to tell you. ',
        bg = general_button_label_bg, fg = 'black', font = general_label_font, anchor = tk.E, borderwidth = 2)
    prepare_conversion.grid(row = 1, column = 0, padx = 5, pady = 5)

    message_to_console = bruh.converter(name)

    print_conversion = tk.Label(conversion_pane, text = message_to_console,
        bg = general_button_label_bg, fg = 'black', font = general_label_font, anchor = tk.E, borderwidth = 2)
    print_conversion.grid(row = 1, column = 1, padx = 5, pady = 5)

    if (message_to_console != bruh.name_too_short) :
        prepare_reduced = tk.Button(conversion_pane, text = 'Do you want to BRUH-ify again? ', bg = general_button_label_bg, fg = 'black',
            font = general_button_font, borderwidth = 2,
            command = lambda : continueConversion(message_to_console, 0, False))
        prepare_reduced.grid(row = 2, column = 0, padx = 5, pady = 5)


# Method to Continue Bruh Conversions Until Not Possible.
def continueConversion(phrase, continue_count, stop_conversion) :
            end_of_bruh = stop_conversion

            # Reduce 'BRUH' phrase if possible.
            if (not end_of_bruh) :
                # Conduct further 'BRUH' conversion.
                reduced_bruh = bruh.reducer(phrase)

                print_reduced = tk.Label(conversion_pane, text = reduced_bruh, bg = general_button_label_bg, fg = 'black',
                    font = general_label_font, anchor = tk.E, borderwidth = 2)
                print_reduced.grid(row = 2 + continue_count, column = 1, padx = 5, pady = 5)

                continue_count += 1

                if (reduced_bruh == bruh.reduction_finished) :
                    continueConversion(reduced_bruh, continue_count, True)
                else :
                    duplicate_prepare_reduced = tk.Button(conversion_pane, text = 'Do you want to BRUH-ify again? ', bg = general_button_label_bg, fg = 'black',
                        font = general_button_font, borderwidth = 2,
                        command = lambda : continueConversion(reduced_bruh, continue_count, end_of_bruh))
                    duplicate_prepare_reduced.grid(row = 2 + continue_count, column = 0, padx = 5, pady = 5)
            # Give Options to Continue to Chat Bot, Reset Converter, or Exit Program.
            else :
                # Create a Frame for End Buttons.
                global end_pane
                end_pane = tk.Frame(root)
                # Position Frame onto Screen.
                end_pane.grid(row = 1, column = 0, sticky = tk.N + tk.E + tk.S + tk.W)

                resetButton = tk.Button(end_pane, text = 'Reset Converter', bg = main_button_bg,
                    font = main_button_font, fg = 'white', borderwidth = 5, command = resetScreen)
                resetButton.grid(row = 1, column = 0, padx = 10, pady = 10)

                # continueButton = tk.Button(end_pane, text = 'Chat Bot', bg = main_button_bg,
                #     font = main_button_font, fg = 'white', borderwidth = 5, command = chatbot.start_chat)
                # continueButton.grid(row = 1, column = 1, padx = 10, pady = 10)

                exitButton = tk.Button(end_pane, text = 'Exit Program', bg = main_button_bg, fg = 'white',
                    font = main_button_font, borderwidth = 5, command = root.quit)
                exitButton.grid(row = 1, column = 2, padx = 10, pady = 10)


def resetScreen() :
    # Destroy all Widgets from Conversion and End Frames.
    for widget in conversion_pane.winfo_children() :
       widget.destroy()

    for widget in end_pane.winfo_children() :
        widget.destroy()

    initScreen()

#######################################
#######################################
#######################################

# Main Method of Program -> Triggered by startButton.
def main() :
    # Remove Widget from TopLevel by Rendering Invisible and Removing Position.
    startButton.forget()

    initScreen()

# Create a Button Widget.
startButton = tk.Button(root, text = 'START BRUH', bg = main_button_bg, fg = 'white',
    font = main_button_font, borderwidth = 5, command = main)
startButton.pack(anchor = tk.CENTER, fill = tk.BOTH, expand = True)

# Infinite Loop -> Interrupted by Keyboard or Mouse
root.mainloop()
