from abc import ABC, abstractclassmethod
from collections import deque

import pickle
import random
from task import Task, get_task_type


class ToDo(ABC):
    def __init__(self, id:str):
        self.id = id
        self.todo = deque()

    def add(self, task:Task) -> None:
        self.todo.append(task)

    def add_priority(self, task:Task) -> None:
        self.todo.appendleft(task)

    def get_next(self) -> Task:
        return self.todo.pop()


# Save in SQLite Database save ToDo Manager Object 
class ToDoManager(ABC):
    def __init__(self):
        self.TDQ_ID = str(random.getrandbits(32))

    @abstractclassmethod
    def add_task(self, task: Task) -> None:
        """Add Task to the Queue Manager. The manager 
            will then sort the task and add it to the end 
            of  the appropriate queue.

        Args:
            task (Task): Newly created and added task. 
        """
        pass

    @abstractclassmethod
    def get_next(self) -> None:
        """
            Implement sorting algorithm here. With whatever number 
            of Queues you have implemented for the subclass, determine 
            in what order they'll be passed to the user.
        """
        pass

    @abstractclassmethod
    def loadQueue(self, filepath : str) -> None:
        """
            Read file containing saved Queues back into Todos.
            Will have a different reading implementation for each Queue configuration
        """
        pass

    @abstractclassmethod
    def saveQueue(self) -> None:
        """
            Saves any queues currently in use to disc. Should be used before close.
            Could open window to allow
        """
        pass

    @abstractclassmethod
    def manage(self) -> None:
        """
            Driver method for TodoQueue usage. 
            Runs a while loop to maintain Queue instance while in use.

        """
        pass

    



if __name__ == '__main__':
    tq = TimeQueueManager()
    tq.manage()
