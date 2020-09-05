import PySimpleGUI as sg
from task import Task
from Typing import List
from abc import ABC

def collapse(layout, key:str) -> sg.pin:
    return sg.pin(sg.Column(layout, key=key))

class ToDoGUI(ABC):
    """Layouts:
            1) Intro Page: Load Saved Queue, or Add New Task? Filename input box
                - Loading Saved Queue will load Queue and take 
            2) Current Task Page: Min + Max Layout with varyinhg degrees of detail. Add New Task + Complete Task Buttons
            3) Add New Task Page: Task Input boxes for each field needed for a task
            4) View list of On-Hold Tasks to Un-Freeze (Add to head of stack)
            5) View list of completed tasks to Reopen (Add to bottom of stack)
            6) View list of all tasks

    Args:
        ABC ([type]): [description]
    """

    ADD_TASK_LAYOUT = [[sg.Input('Task Name', k='-NAME?-'), sg.Checkbox('High Priority?', '-PRIORITY?-'), sg.Input('Time to Finish', k='-ETC?-')],
                        [sg.Input('Relevant Link',k='-LINK?-')],
                        [sg.Input('Task Description', k='-DESCRIPTION?-')]
                        ]
    SYMBOL_UP =    '▲'
    SYMBOL_DOWN =  '▼'

    LOAD_QUEUE_LAYOUT = [[sg.Input('Queue File:')],
                            [sg.Button('Submit')]]
    def __init__(self):
        self.window = sg.Window('ToDo Queue', ToDoGUI.LOAD_QUEUE_LAYOUT, keep_on_top=True)
        while True:
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break



    def display_task(self, task:Task) -> None:
        if task.top_priority: x = "!!!Top Priority!!!" 
        else: x = ''

        MAX_TASK_LAYOUT = [[sg.Text(task.rel_link,click_submits=True, key='-LINK-')],
        [sg.Text(task.description)],
        [sg.Button('Add New Task', enable_events=True, key='-NEW TASK-'), sg.Button('Complete Task', enable_events=True, key='-COMPLETE-')]]

        MIN_TASK_LAYOUT = [[sg.Text(task.name), sg.Text(task.est_mins_to_finish), sg.T(x), sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN DETAILS-')],
                    [collapse(MAX_TASK_LAYOUT, '-DETAILS-')]]
        
        while True:
            event, values = self.window.read()
            print(event, values)
            if event in (None, 'Exit'):
                break
        self.window.close()