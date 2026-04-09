class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        result.append(person_obj)

    for person in people:
        obj = Person.people[person["name"]]

        if person.get("wife") is not None:
            name_wife = person["wife"]
            obj.wife = Person.people[name_wife]

        if person.get("husband") is not None:
            name_husband = person["husband"]
            obj.husband = Person.people[name_husband]

    return result