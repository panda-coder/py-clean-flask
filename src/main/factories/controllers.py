
from presentation.controllers import SumController, SubtractController, MultiplyController, DivideController
from use_case import SumAction, SubtractAction, MultiplyAction, DivideAction

def make_sum_controller():
    return SumController(SumAction())

def make_subtract_controller():
    return SubtractController(SubtractAction())

def make_multiply_controller():
    return MultiplyController(MultiplyAction())

def make_divide_controller():
    return DivideController(DivideAction())