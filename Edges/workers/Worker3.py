from workers import Worker

class Worker3(Worker.Worker):

    def overrideAttrs(self):
        """ override some attributes

        Returns:
            [Worker3]: returns self object
        """
        self.mips = 2
        self.bandwidth = 10
        self.position = 3
        self.timer = 0

        return self
