class MinStack(object):

    def __init__(self):
     
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            
            self.stack.append((val, val))
        else:
            # Pega o mínimo atual do topo
            current_min = self.stack[-1][1]
            # Calcula o novo mínimo
            new_min = min(val, current_min)
            self.stack.append((val, new_min))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1][1]




if __name__ == "__main__":
    ms = MinStack()

    ms.push(5)
    ms.push(2)
    ms.push(8)
    ms.push(1)

    print("Topo:", ms.top())       # 1
    print("Min:", ms.getMin())     # 1

    ms.pop()
    print("Topo após pop:", ms.top())   # 8
    print("Min após pop:", ms.getMin()) # 2