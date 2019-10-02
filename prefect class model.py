from prefect import Task, unmapped, Flow, Parameter
from prefect.engine.executors import DaskExecutor
from prefect.utilities.debug import raise_on_exception
from prefect.engine.executors import LocalExecutor
from helpers.auto_initializer import initialize


# need to inherit from Task
class AddTask(Task):
    # I think you have to init with a dummy default arg so that when you instantiate the
    # class before the flow, it works properly.

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default
    # you must have a run function in the class to make it a flow
    def run(self, x: int, y: int=None) -> int:
        self.x = x
        self.y = y
        self.print_it(x)
        print(self.x + self.y)
        print('run function running')
        return

    def print_it(self,x):
        print('printing  ')
        print(x)


#this line has to happen for the Task super class to properly call the run within the class
a = AddTask(default=1)

with Flow("My Flow") as f:
    x = Parameter('x')
    y = Parameter('y')
    #because a is already defined with a default, we only have to pass in the variables
    #we actually want here
    addition = a(x,y)# t2 != a


x = 1
y = 2

with raise_on_exception():
    f.run(parameters={'x': x, 'y':y})

