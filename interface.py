import tkinter as tk
import bruh
import chatbot

# Create Tk Window.
root = tk.Tk()
root.title('**BRUH Converter**')

# Create a Frame which can expand according to size of Window.
pane = tk.Frame(root)
# Shove Frame onto screen.
pane.pack(expand = True)

# Initialize color variables for GUI Widgets.
main_button_bg = '#0D4BC5'

general_button_bg = '#0DC5B5'
general_label_bg = '#09F90D'
general_entry_bg = '#F79C09'

#######################################
########## GUI Functions ##############
#######################################

# Method that Sets up Screen 
def initScreen() :
    nameButton = tk.Button(pane, text = 'Hi. What is your name?', bg = general_button_bg, 
        fg = 'black', bd = 5, borderwidth = 2, command = lambda : startConversion(str(input_field.get())))
    # Position Button Widget onto Screen.
    nameButton.grid(row = 0, column = 0)

    # 'Hacky' Way of Spacing Apart Widgets.
    empty_label = tk.Label(pane, text = ' ')
    empty_label.grid(row = 0, column = 1)

    # Create an Entry Widget.
    input_field = tk.Entry(pane, width = 30, bg = general_entry_bg, 
        fg = 'black', bd = 5, borderwidth = 2)
    # Position Entry Widget onto Screen.
    input_field.grid(row = 0, column = 2, padx = 10, pady = 10)
    # Insert Default Text to Entry Widget.
    input_field.insert(0, 'Enter Your Name')

# Method to Trigger and Display First Bruh Conversion
def startConversion(name) :
    # 'Hacky' Way of Spacing Apart Widgets.
    empty_label = tk.Label(pane, text = ' ')
    empty_label.grid(row = 1, column = 0)

    # Conduct initial 'BRUH' conversion.
    prepare_conversion = tk.Label(pane, text = f'Hello {name}. I have something to tell you. ', 
        bg = general_label_bg, fg = 'black', anchor = tk.E, bd = 5, borderwidth = 2)
    prepare_conversion.grid(row = 2, column = 0, padx = 10, pady = 10)

    message_to_console = bruh.converter(name)

    print_conversion = tk.Label(pane, text = message_to_console, 
        bg = general_label_bg, fg = 'black', anchor = tk.E, bd = 5, borderwidth = 2)
    print_conversion.grid(row = 2, column = 2)
    
    if (message_to_console != 'Cannot BRUH-ify. Your name is too short.') :
        # 'Hacky' Way of Spacing Apart Widgets.
        empty_label.grid(row = 3, column = 0)

        prepare_reduced = tk.Button(pane, text = 'Do you want to BRUH-ify again? ', bg = general_button_bg, 
            fg = 'black', bd = 5, borderwidth = 2, command = lambda : continueConversion(message_to_console, 0, False))
        prepare_reduced.grid(row = 4, column = 0, padx = 10, pady = 10)


# Method to Continue Bruh Conversions Until Not Possible
def continueConversion(phrase, continue_count, stop_conversion) :
            end_of_bruh = stop_conversion

            empty_label = tk.Label(pane, text = ' ')

            # Reduce 'BRUH' phrase if possible.
            if (not end_of_bruh) :
                # Conduct further 'BRUH' conversion.
                reduced_bruh = bruh.reducer(phrase)
                
                print_reduced = tk.Label(pane, text = reduced_bruh, bg = general_label_bg, 
                    fg = 'black', anchor = tk.E, bd = 5, borderwidth = 2)
                print_reduced.grid(row = 4 + continue_count, column = 2)

                continue_count += 1

                if (reduced_bruh == 'Cannot be BRUH-ified further.') :
                    continueConversion(reduced_bruh, continue_count + 1, True)
                else :
                    # 'Hacky' Way of Spacing Apart Widgets.
                    empty_label.grid(row = 4 + (continue_count), column = 0)

                    duplicate_prepare_reduced = tk.Button(pane, text = 'Do you want to BRUH-ify again? ', 
                        bg = general_button_bg, fg = 'black', bd = 5, borderwidth = 2, 
                        command = lambda : continueConversion(reduced_bruh, continue_count + 1, end_of_bruh))
                    duplicate_prepare_reduced.grid(row = 4 + (continue_count + 1), column = 0, padx = 10, pady = 10)
            # Give Options to Exit Program, Reset Converter, or Snake Game
            else :
                # 'Hacky' Way of Spacing Apart Widgets.
                empty_label.grid(row = 4 + (continue_count), column = 0)

                exitButton = tk.Button(pane, text = 'Exit Program', bg = main_button_bg, fg = 'white',
                    bd = 5, borderwidth = 5, command = root.quit)
                exitButton.grid(row = 4 + (continue_count + 1), column = 0, padx = 10, pady = 10)

                resetButton = tk.Button(pane, text = 'Reset Converter', bg = main_button_bg, 
                    fg = 'white', bd = 5, borderwidth = 5, command = resetScreen)
                resetButton.grid(row = 4 + (continue_count + 1), column = 1, padx = 10, pady = 10)

                continueButton = tk.Button(pane, text = 'Chat Bot', bg = main_button_bg, 
                    fg = 'white', bd = 5, borderwidth = 5, command = chatbot.start_chat)
                continueButton.grid(row = 4 + (continue_count + 1), column = 2, padx = 10, pady = 10)

def resetScreen() :
    # Destroy all Widgets from Frame
    for widget in pane.winfo_children():
       widget.destroy()

    initScreen()

#######################################
#######################################
#######################################

# Main Method of Program -> Triggered by startButton 
def main() :
    # Remove Widget from TopLevel by Rendering Invisible and Removing Position.
    startButton.forget()

    initScreen()

# Create a Button Widget.
startButton = tk.Button(pane, text = 'START BRUH', bg = main_button_bg, 
    fg = 'white', bd = 5, borderwidth = 5, command = main)
startButton.pack(anchor = tk.CENTER, expand = True)

# Infinite Loop -> Interrupted by Keyboard or Mouse
root.mainloop()







