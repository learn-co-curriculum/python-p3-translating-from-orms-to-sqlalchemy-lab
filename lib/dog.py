from models import Dog

## Tips and Tricks
# The bodies of all functions in dog.py except create_table() and save() should be composed of a single line of code.
# Read through the pytest error messages to make sure the input and output for your functions match the tests.
# Remember which attributes are required when designing a SQLAlchemy data model: a __tablename__, a primary_key, and one or more Columns.

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()