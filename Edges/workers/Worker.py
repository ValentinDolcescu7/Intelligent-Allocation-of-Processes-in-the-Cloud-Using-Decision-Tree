class Worker():
    def __init__(self):
        """Initialize Worker class."""
        self.cloudlets = []
        self.bandwidth = 0  # inițializăm cu 0 pentru a putea verifica mai târziu
        self.mips = 0  # similar, presupunem inițializare cu 0
        self.position = 0  # presupunem o poziție inițializată cu 0
        self.timer = 0

    def attachCloudlet(self, cloudlet):
        """Attach cloudlet to worker if bandwidth is not 0."""
        self.cloudlets.append(cloudlet)

    def run(self):
        """Run the cloudlets on workers, prioritizing high_priority cloudlets."""
        for cloudlet in self.cloudlets:
            if cloudlet.high_priority == 1:
                self.execute(cloudlet)

        for cloudlet in self.cloudlets:
            if cloudlet.high_priority == 0:
                self.execute(cloudlet)

    def execute(self, cloudlet):
        """Execute cloudlet on worker, handling division by zero."""
        # Prevenim eroarea de divizare cu zero pentru bandwidth și mips
        if self.bandwidth>0:
           cloudlet.transferTime = cloudlet.size / self.bandwidth

        if self.mips > 0:
            cloudlet.executionTime = cloudlet.instructions / self.mips
        else:
            cloudlet.executionTime = float('inf')  # Asignăm un timp mare dacă mips este 0

        self.timer += cloudlet.executionTime  #cloudlet.transferTime
        
    def log(self):
        """Print details of the transactions."""
        print('\n------------------------------WORKER ' + str(self.position) + '--------------------\n')
        print('Numbers of tasks: ' + str(len(self.cloudlets)))
        print('Position: ' + str(self.position))
        print('MIPS: ' + str(self.mips))
        print('Bandwidth: ' + str(self.bandwidth))
        print('Duration: ' + str(self.timer))

        print("\nTasks:")
        for i, c in enumerate(self.cloudlets, start=1):
            print(f"Task {i}:")
            print('From: ' + #str(c.area) +
                '  |  High priority: ' + str(c.high_priority) +
                '  |  Instructions: ' + str(c.instructions) + ' MI' +
                '  |  Size: ' + str(c.size) + ' MB' +
                '  |  ExecutionTime: ' + #str(round(c.executionTime)) + ' s' +
                '  |  TransferTime: ' #str(round(c.transferTime)) + ' s'
                 )



    def clearHistory(self):
        """Clear worker's timer and attached cloudlets."""
        self.timer = 0
        self.cloudlets.clear()
