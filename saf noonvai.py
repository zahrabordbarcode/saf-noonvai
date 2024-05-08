def dequeue_i(self,i):
    if self.num == 0:
        raise exeception("queue empty")
    item == self.q[i]
    del self.q[i]
    index = [(self.num + self.first) % self.max_size]
    self.q.insert(0,index)
    self.num -= 1
    return item
