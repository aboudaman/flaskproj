Installing Venv for flask

$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.

#Activating
$ . venv/bin/activate

#Deactivating
$ deactivate

# Before instally flask and sqlalchemy
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

#Installing Flask
$ pip3 install Flask

#Install SQLAlchemy 
$ pip3 install sqlalchemy

#Install pylint
$ pip3 install pylint

#Adding a record manually
>>> from sqlalchemy.orm import sessionmaker
>>> from database_setup import Base, Student, Classes
>>> engine = create_engine('sqlite:///students.db')
>>> Base.metadata.bind = engine
>>> DBSession = sessionmaker(bind=engine)
>>> session = DBSession()
>>> firstStudent = Student(name="Krypton")
>>> session.add(Student)
>>> session.commit()

<!-- Query -->
session.query(Student).all()

<!-- Find all employees -->
employees = session.query(Employee).all()

<!-- Loop through and output names-->
for employee in employees:
    print employee.name