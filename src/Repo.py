from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.Model import Person, Base


class Repo:
    def __init__(self):
        engine = create_engine('sqlite:///public.db')
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def createPerson(self, name):
        self.session.add(Person(name=name))
        self.session.commit()

    def getAllPeople(self) -> list[Person]:
        people = self.session.query(Person).all()
        self.session.commit()
        return people
