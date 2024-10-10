class MinStack:

    # stack will internally consist of three values, a map where the key is its current stack index, and value minimum value at that index
    # value 2 is the current stack height
    # when inserting new elements (excepting the first edge case), unless it has value smaller than that, in which case it is inserted with that

    def __init__(self):
        self.stack = {}
        self.current_stack_depth = 0

    def push(self, val: int) -> None:
        self.current_stack_depth += 1
        if self.current_stack_depth == 1:
            self.stack[self.current_stack_depth] = stack_value(val, val)
        elif val < self.stack[self.current_stack_depth - 1].get_min():
            self.stack[self.current_stack_depth] = stack_value(val, val)
        else:
            current_min = self.stack[self.current_stack_depth - 1].get_min()
            self.stack[self.current_stack_depth] = stack_value(val, current_min)

    def pop(self) -> None:
        self.current_stack_depth -= 1
        return self.stack.pop(self.current_stack_depth+1).get_value()

    def top(self) -> int:
        return self.stack[self.current_stack_depth].get_value()

    def getMin(self) -> int:
        return self.stack[self.current_stack_depth].get_min()


class stack_value:
    def __init__(self, value: int, current_min: int):
        self.value = value
        self.current_min = current_min

    def get_min(self):
        return self.current_min

    def get_value(self):
        return self.value
