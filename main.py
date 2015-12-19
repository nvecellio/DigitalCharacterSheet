import pickle
import sys
import os

class Main():

    def __init__(self):
        player = raw_input(">> Speak your name, adventurer:\n>> ")

        player_data = self.load(player)

    def load(self, name):
        home = os.getenv('HOME')
        file_name = '{name}.p'.format(name=name)
        save_file = '{home}/Documents/CharSheet/{file}'.format(home=home, file=file_name)

        if os.path.isfile(save_file):
            player_data = pickle.load(open(save_file, 'rb'))
            return player_data

        else:
            return False

    def save_dir(self, make_path=False, check_path=False, check_file=False):
        path = '/home/Documents/CharSheet/'
        if check_path:
            return os.path.isdir(path)
        if check_file:
            return os.path.isfile()
        if make_path:
            if not os.path.isdir(path):
                try:
                    os.mkdir(path + name)
                    return True
                except Exception as e:
                    sys.exit(e)
        else:
            return False

