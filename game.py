import config as cfg
import pg_interface as _if
class game:
    def __init__(self):
        self._if = _if.interface(self)

    def run(self):
        self._if.run()
        
    def close(self):
        self._if.close()

myGame = game()
myGame.run()
myGame.close()
