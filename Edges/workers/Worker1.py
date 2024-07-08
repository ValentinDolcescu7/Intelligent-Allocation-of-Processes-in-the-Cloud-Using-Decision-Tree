from workers import Worker

class Worker1(Worker.Worker):

    def overrideAttrs(self):
        """ override some attributes

        Returns:
            [Worker1]: returns self object
        """
        self.mips = 2
        self.bandwidth = 60
        self.position = 1
        self.timer = 0

        return self
