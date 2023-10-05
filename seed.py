from app import db,app
from models import User, Veterinary, Services, Pets, PetItems
from datetime import datetime

def seed_database():
    with app.app_context():
        user1 = User(username='Micah', email='micah@gmail.com', password='Password1qsa', phonenumber='1234567890')
        user2 = User(username='Kennedy', email='ken@gmail.com', password='Password2', phonenumber='9876543210')
        db.session.add(user1)
        db.session.add(user2)

    # Add veterinary
        vet1 = Veterinary(name='Vet Clinic 1', location='Location 1', created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        vet2 = Veterinary(name='Vet Clinic 2', location='Location 2', created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add(vet1)
        db.session.add(vet2)

    # Add services
        service1 = Services(services_type='Vaccination', veterinary=vet1, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        service2 = Services(services_type='Surgery', veterinary=vet2, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add(service1)
        db.session.add(service2)

    # Add pets
        pet1 = Pets(name='Fluffy', user_id=user1, veterinary_id=vet1, service_id=service1, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        pet2 = Pets(name='Bella', user_id=user2, veterinary_id=vet2, service_id=service2, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add(pet1)
        db.session.add(pet2)

    # Add pet items
        item1 = PetItems(item='Food', price=200, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        item2 = PetItems(item='Toy', price=100, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        db.session.add(item1)
        db.session.add(item2)

    # Commit the changes
        db.session.commit()
        
if __name__ == '__main__':
    with app.app_context():  
        db.create_all() 
        seed_database()  







