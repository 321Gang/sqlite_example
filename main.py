from src.Repo import Repo
from src.Model import Person

repo = Repo()

repo.createPerson("Loc")
repo.createPerson("Tung")
repo.createPerson("Linh")
repo.createPerson("Max")
repo.createPerson("Khanh")
repo.createPerson("Huy")
people: list[Person] = repo.getAllPeople()
for person in people:
    print(person.name)
