from workers import Worker

class Worker2(Worker.Worker):

    def overrideAttrs(self):
        """ override some attributes

        Returns:
            [Worker2]: returns self object
        """
        self.mips = 2
        self.bandwidth = 23
        self.position = 2
        self.timer = 0

        return self

