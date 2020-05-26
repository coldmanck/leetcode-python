# Leetcode 359: Logger Rate Limiter

# Given a message and a timestamp (in seconds granularity), return true 
# if the message should be printed in the given timestamp, otherwise returns false.
# It is possible that several messages arrive roughly at the same time.

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue = deque()
        self.cache = set()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if timestamp > 10:
            while self.queue and timestamp - self.queue[0][1] >= 10:
                self.cache.remove(self.queue.popleft()[0])
        if message in self.cache:
            return False
        self.cache.add(message)
        self.queue.append((message, timestamp))
        return True

logger = Logger()

# // logging string "foo" at timestamp 1
print(logger.shouldPrintMessage(1, "foo")) # ; returns true;

# // logging string "bar" at timestamp 2
print(logger.shouldPrintMessage(2,"bar")) # ; returns true;

# // logging string "foo" at timestamp 3
print(logger.shouldPrintMessage(3,"foo")) # ; returns false;

# // logging string "bar" at timestamp 8
print(logger.shouldPrintMessage(8,"bar")) # ; returns false;

# // logging string "foo" at timestamp 10
print(logger.shouldPrintMessage(10,"foo")) # ; returns false;

# // logging string "foo" at timestamp 11
print(logger.shouldPrintMessage(11,"foo")) # ; returns true;