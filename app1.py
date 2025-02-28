from sqlalchemy.orm import sessionmaker

from model import engine,user

# is used to create database session object that interact with databases
Session=sessionmaker(bind=engine)
session=Session()

users=session.query(user).all()
user1=users[0]

print(user1.name)

# User=user(id=1,name="Mohan",age=25)
# user2=user(id=2,name="Rohan",age=26)
# user3=user(id=3,name="Sohan",age=27)
# user4=user(id=4,name="Gohan",age=28)

# session.add_all([User,user2,user3,user4])

session.commit()