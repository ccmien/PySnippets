from contextlib import contextmanager
@contextmanager
def debug_logging(level):
       logger = logging.getLogger()
       old_level = logger.getEffectiveLevel()
       logger.setLevel(level)
       try:
           yield
       finally:
           logger.setLevel(old_level)
