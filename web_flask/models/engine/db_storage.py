class DBStorage:
    def close(self):
        self.__session.remove()  # or self.__session.close()
