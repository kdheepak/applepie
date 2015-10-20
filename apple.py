import logging

class AppleScript(object):
    def __init__(self):
        self.logger = kwargs.get('logger', logging.getLogger(__name__))
        self.logger.debug("Initializing AppleScript")
