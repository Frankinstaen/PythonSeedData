from Entity.Models import Base, engine
from orm import create_salary,\
    create_contracts,\
    create_personal,\
    create_departments,\
    create_pc,\
    create_login_dates

if __name__ == '__main__':
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine, checkfirst=True)
    create_departments()
    create_pc()
    create_personal()
    create_contracts()
    create_salary()
    create_login_dates()
