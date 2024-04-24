class State(BaseModel, Base):
    if storage_type != 'db':
        @property
        def cities(self):
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
