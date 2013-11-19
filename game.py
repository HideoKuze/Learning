class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def update(self, key):
    	return self.paths.update(key)

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


class RoomTwo(object):
	def confirm_description(self, describe):
		return describe

this = Room('Gold room', "its gold")
print this.update({'its gold': 'hello'})
print this.go("its gold")
