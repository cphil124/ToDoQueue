from abc import ABC, abstractclassmethod

class Task(ABC):
    def __init__(self, name:str, description:str, est_mins_to_finish:int, priority:bool=False, link:str=None) -> None:
        self.name = name
        self.rel_link = link 
        self.description = description
        if est_mins_to_finish < 1:
            self.est_mins_to_finish = 0
        else:
            self.est_mins_to_finish = est_mins_to_finish
        self.complete = False
        self.completion_notes = None
        self.top_priority = priority

    def complete_task(self, note:str) -> None:
        self.completion_notes = note
        # Send logging message about task completion
        self.complete = True

    def update_name(self, name:str) -> None:
        self.name = name
    
    def update_desc(self, descr:str) -> None:
        self.description = descr

    def update_etd(self, mins:int) -> None:
        self.est_mins_to_finish = mins

    def reopen_task(self, note:str) -> None:
        self.complete = False
        self.completion_notes += "  <<<REOPENING>>>: " + note

def get_task_type(task: Task) -> int:
    etd = task.est_mins_to_finish
    if etd < 8:
        return 1
    elif etd > 7 and etd < 26:
        return 2
    else:
        return 3