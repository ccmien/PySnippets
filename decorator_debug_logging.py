from contextlib import contextmanager
@contextmanager
def debug_logging(level, name):
       logger = logging.getLogger(name)
       old_level = logger.getEffectiveLevel()
       logger.setLevel(level)
       try:
           yield logger
       finally:
           logger.setLevel(old_level)
