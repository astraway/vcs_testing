from prefect import Task
from helpers.auto_initializer import initialize
from prefect import  unmapped, Flow, Parameter
class AddTask(Task):
    @initialize
    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default
        print('init running')

    def run(self, x: int, y: int=None) -> int:
        if y is None:
            y = self.default
        print('run running')
        return x + y

# initialize the task instance
add = AddTask(default=1)

from prefect import Flow

with Flow("My first flow!") as flow:
    z = Parameter('5')
    first_result = add(3, z)
    second_result = add(x=first_result, y=400)

z = 5
state = flow.run(parameters={'5': z})

#this is a comment test
#second change

#this is a branch

#hi here is a nother comment
# and another

