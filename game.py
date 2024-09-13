class GamePlayer:
 
    def __init__(self, _id):
        # initial dummy rank -1
        self._id = _id
        # starting position for every player is 1
        self.rank = -1
        self.position = 1
 
    def set_position(self, pos):
        self.position = pos
 
    def set_rank(self, rank):
        self.rank = rank
 
    def get_pos(self):
        return self.position
 
    def get_rank(self):
        return self.rank
