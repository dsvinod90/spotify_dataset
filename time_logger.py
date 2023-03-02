import time


class TimeLogger:
    def __init__(self):
        self.log_start, self.log_end = None, None

    def start(self):
        """ Start logging time
        A timer to keep track of the processing times for various stages
        of creating and populating the database.
        This method will start the timer.
        """
        if not self.log_start:
            self.log_start = time.time()
        else:
            print("A timer has already been started!")

    def end(self):
        """ End logging time
        A timer to keep track of the processing times for various stages
        of creating and populating the database.
        This method will end the timer and print the execution time.
        """
        if self.log_start:
            self.log_end = time.time()
            diff = self.log_end - self.log_start
            if diff > 60:
                print(f"Execution Time = {round(diff/60, 2)} minutes\n")
            else:
                print(f"Execution Time = {round(diff, 2)} seconds\n")
        # re-setting the start and end time to None so that the timer can
        # be used by another function
        self.reset()

    def reset(self):
        self.log_start, self.log_end = None, None
