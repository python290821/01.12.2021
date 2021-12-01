from datetime import datetime
from User import User
from sqlalchemy import text
from db_cofig import local_session, create_all_entities

# NOTE THAT IN ORDER TO RECOGNIZE NEW ENTITY CLASSES FOR CREATION
# YOU NEED TO IMPORT THEM SO PYTHON RUNS THEIR MODULES!
create_all_entities()

# repo = UserRepository(local_session)

#local_session.add(User(username='bob', email='bob@bob.com'))
#local_session.commit()
# users = repo.get_all()
# print(users)
#
#
#users = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
#local_session.add_all(users)
#local_session.commit()
# users = repo.get_all()
# print(users)
# users = repo.get_all()

local_session.query(User).filter(User.id == 2).delete(synchronize_session=False)
local_session.commit()

users = local_session.query(User).all()
print(users)
