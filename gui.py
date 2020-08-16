import PySimpleGUI as sg
from task import Task
import webbrowser as wb
from typing import List, Optional
import subprocess

sg.theme('Dark Amber')    # Add some color for fun

# # 1- the layout
# layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]

# # 2 - the window
# window = sg.Window('Pattern 2', layout)

# # 3 - the event loop
# while True:
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#     if event == 'Show':
#         # Update the "output" text element to be the value of "input" element
#         window['-OUTPUT-'].update(values['-IN-'])

#         # In older code you'll find it written using FindElement or Element
#         # window.FindElement('-OUTPUT-').Update(values['-IN-'])
#         # A shortened version of this update can be written without the ".Update"
#         # window['-OUTPUT-'](values['-IN-'])     

# # 4 - the close
# window.close()

SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

def collapse(layout:List[List], key:str) -> sg.pin:
    return sg.pin(sg.Column(layout, key=key))

def show_add_task(layout:List[List], key:str) -> None:
    pass

def display_new_task_form() -> Optional[Task]:
    ADD_TASK_LAYOUT = [[sg.Input('Task Name', k='-NAME?-'), sg.Checkbox('High Priority?', '-PRIORITY?-'), sg.Input('Time to Finish', k='-ETC?-')],
                        [sg.Input('Relevant Link',k='-LINK?-')],
                        [sg.Input('Task Description', k='-DESCRIPTION?-')]
                        ]

    window = sg.Window('ToDo Queue', ADD_TASK_LAYOUT, keep_on_top=True)

    while True:
        event, values = window.read()    
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    if event.startswith('-CREATE TASK-'):
        window.close()
        return Task(name=values['-NAME?-'], description=values['-DESCRIPTION?-'], 
                est_mins_to_finish=values['-ETC-'],
                priority=values['-PRIORITY?-'],link=values['-LINK?-'])


# Remake this more modularly. Should break down into situational event handling.
def display_task(t: Task) -> None: 
    if t.top_priority: x = "!!!Top Priority!!!" 
    else: x = ''

    MAX_TASK_LAYOUT = [[sg.Text(t.rel_link,click_submits=True, key='-LINK-')],
        [sg.Text(t.description)],
        [sg.Button('Add New Task', enable_events=True, key='-NEW TASK-'), sg.Button('Complete Task', enable_events=True, key='-COMPLETE-')]]

    TASK_LAYOUT = [[sg.Text(t.name), sg.Text(t.est_mins_to_finish), sg.T(x), sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN DETAILS-')],
                    [collapse(MAX_TASK_LAYOUT, '-DETAILS-')]]

    
        
    window = sg.Window('ToDo Queue', TASK_LAYOUT, keep_on_top=True)    
    
    opened = True

    while True: # Event Loop
        event, values = window.read()    
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

        if event.startswith('-LINK-'):
            sp = subprocess.Popen([CHROME,t.rel_link], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if event.startswith('-OPEN DETAILS-'):
            opened = not opened
            window['-OPEN DETAILS-'].update(SYMBOL_DOWN if opened else SYMBOL_UP)
            window['-DETAILS-'].update(visible=opened)

        if event.startswith('-NEW TASK-'):
            pass # Switch Layout to Create New Task page

        
        
        if event.startswith('-COMPLETE-'):
            pass    
    window.close()
    return None

if __name__=='__main__':
    task = Task(name='Sample Task', description='Sample Task to test out GUI', est_mins_to_finish=15)
    display_task(task)



    subprocess.Popen([CHROME, t.rel_link], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)" match parameters
  Argument types: (list[Unknown], Literal[True], int, int)Pyright (reportGeneralTypeIssues)
