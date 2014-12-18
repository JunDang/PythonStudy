class Queue(object):
    def __init__(self):
        """Create an empty set """
        self.el = []

    def insert(self, e):
        self.el.append(e)

    def remove(self):
        #result = []
        try:
            result = self.el[0]
            for i in range(len(self.el) - 1):
                  self.el[i] = self.el[i+1]
            del self.el[-1]
            return result#result = result.append(self.el[i])       
            #print "I popped" + str(result) + "from"
        except:
            raise ValueError
q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
q1.remove()
q2.remove()