from todo_manager import ToDo, ToDoManager
from task import get_task_type, Task
import random

"""Focused Time-Based Queue Prioritization Manager

    A To-Do Queue for focused automatic task prioritization, with filing based on time to complete and a staggered next task manager
    which prioritizes low-effort items to keep their number low.  

    Will need to add GUI Component. GUI Will be a shrinkable window, holding name. When expanded, 
    will show description, relevant link if there is one, and possibly a timer implemented to track completion time, 
    though the timer should not update in real time. 

    Be able to add tasks to complete, should have basic description of task with some details and a descriptive name. 
    Currently Queue is only broken down by estimated time to completion, but may add another distinction for Task Streams based on project. 
"""

class TimeQueueManager(ToDoManager):
    def __init__(self):
        self.TDQ_ID = 'TQ:'+str(random.getrandbits(32))
        self.small = ToDo('SM:TQ:'+str(self.TDQ_ID))
        self.mid = ToDo('MD:TQ:'+str(self.TDQ_ID))
        self.big = ToDo('LG:TQ:'+str(self.TDQ_ID))
        self.small_count = 0
        self.mid_count = 0
        self.total = 0
        self.current : Task

    def add_task(self, task:Task) -> None:
        t = get_task_type(task)
        if t == 1:
            if task.top_priority: self.small.add_priority(task)
            else: self.small.add(task)
        elif t == 2:
            if task.top_priority: self.mid.add_priority(task)
            else: self.mid.add(task)
        elif t == 3: 
            if task.top_priority: self.big.add_priority(task)
            else: self.big.add(task)

    def get_next(self) -> None:
        if len(self.small.todo) > 0 and len(self.small.todo) <= 3:
            self.small_count += 1
            self.current = self.small.todo.pop()
        elif len(self.mid.todo) > 0 and len(self.mid.todo) <= 2:
            self.mid_count += 1
            self.current = self.mid.todo.pop()
        else:
            self.small_count = 0
            self.mid_count = 0 
            self.current = self.big.todo.pop()

    def get_total(self) -> int:
        s,m,l = len(self.small.todo), len(self.small.todo), len(self.small.todo)
        self.total = s + m + l
        return self.total

    def loadQueue(self, filepath: str='.\\TimeToDoQueue.pickle') -> None:
        with open(filepath, 'rb') as load_file:
            deque_dict = pickle.load(load_file)
        self.small = deque_dict['small']
        self.mid = deque_dict['mid']
        self.big = deque_dict['big']

    def saveQueue(self, filename:str='.\\TimeToDoQueue.pickle') -> None:
        deque_dict = {
            'small': self.small,
            'mid' : self.mid,
            'big' : self.big
        }
        with open(filename, 'wb+') as save_file:
            pickle.dump(obj=deque_dict, file=save_file)

    def manage(self) -> None:
        while self.get_total() > 0:
            if self.current.complete: 
                self.get_next()
            x = display_task(self.current)
            if isinstance(x, Task):
                self.add_task(x)
        #Display GUI 
        print("All Tasks have been completed. Please pass a new task")
