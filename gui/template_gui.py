import PySimpleGUI as sg

"""
    Demo - Multiple layouts in a single window that are swapped in and out

    If you've ever wanted to replace the contents of a window with another layout then perhaps
    this demo is for you.  You cannot actually change the layout of a window dynamically, but what
    you can do is make elements visible and invisible.  
    
    To "swap out" a portion of a window, use a Column element for that portion.  Add multiple Columns
    on the same row and make only 1 of them active at a time
"""

# ----------- Create the 3 layouts this Window will display -----------
layout1 = [[sg.Text('This is layout 1 - It is all Checkboxes')],
           *[[sg.CB(f'Checkbox {i}')] for i in range(5)]]

layout2 = [[sg.Text('This is layout 2')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]

layout3 = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
           *[[sg.R(f'Radio {i}', 1)] for i in range(8)]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')],
          [sg.Button('Cycle Layout'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('Exit')]]

window = sg.Window('Swapping the contents of a window', layout)

layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Cycle Layout':
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 3 else 1
        window[f'-COL{layout}-'].update(visible=True)
    elif event in '123':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
window.close()



#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string

"""
    Basic use of the Table Element
"""

sg.change_look_and_feel('Light Green 1')

# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x]) for x in range(len(data[0]))]

# ------ Window Layout ------
layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25, background_color='lightblue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    tooltip='This is a table')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Change Colors')],
          [sg.Text('Read = read which rows are selected')],
          [sg.Text('Double = double the amount of data in the table')],
          [sg.Text('Change Colors = Changes the colors of rows 8 and 9')]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout)

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break
    if event == 'Double':
        for i in range(len(data)):
            data.append(data[i])
        window['-TABLE-'].update(values=data)
    elif event == 'Change Colors':
        window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))

window.close()