from __future__ import annotations
import uuid
from typing import List
from sqlalchemy import ForeignKey, String
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, DateTime, Integer, Text
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import pandas as pd

Base = declarative_base()

Server = 'HOME-PC\SQLEXPRESS'
Database = 'our_organization'
Driver = 'ODBC Driver 17 for SQL Server'
Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'

class Departments(Base):
    __tablename__ = "departments"
    id = sa.Column(Integer, primary_key=True, autoincrement=False)
    department = sa.Column(String)
    personals = relationship(List["Personal"], back_populates="departments")


class Pc(Base):
    __tablename__ = "pc"
    pc_id = sa.Column(Text(36),
                      default=lambda: str(uuid.uuid4()),
                      primary_key=True,
                      autoincrement=False)
    pc_serial = sa.Column(String)
    pc_mac = sa.Column(String)
    pc_ip = sa.Column(String)
    personal = relationship("Personal", back_populates="pc")


class Personal(Base):
    __tablename__ = "personal"
    user_id = sa.Column(Text(36),
                        default=lambda: str(uuid.uuid4()),
                        primary_key=True,
                        autoincrement=False)
    first_name = sa.Column(String)
    last_name = sa.Column(String)
    birth_date = sa.Column(Date)
    login = sa.Column(String)
    email = sa.Column(String)
    department_id = sa.Column(ForeignKey("departments.id"))
    department = relationship("Departments", back_populates="personal")
    pc_id = sa.Column(ForeignKey("pc.pc_id"))
    pc = relationship("Pc", back_populates="personal")
    contract = relationship("Сontracts", back_populates="personal")
    login_dates = relationship(List["Login_dates"], back_populates="personal")
    salary = relationship(List["Salary"], back_populates="personal")


class Login_dates(Base):
    __tablename__ = "login_dates"
    login_dates_id = sa.Column(Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(Text(36),
                        ForeignKey("personal.user_id"),
                        default=lambda: str(uuid.uuid4()))
    pc_id = sa.Column(Text(36),
                      ForeignKey("pc.pc_id"),
                      default=lambda: str(uuid.uuid4()))
    date_time = sa.Column(DateTime)
    sa.UniqueConstraint(user_id, pc_id, date_time)


class Сontracts(Base):
    __tablename__ = "contracts"
    contracts_id = sa.Column(Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(Text(36),
                        ForeignKey("personal.user_id"),
                        default=lambda: str(uuid.uuid4()), unique=True)
    date_from = sa.Column(Date)
    date_to = sa.Column(Date)


class Salary(Base):
    __tablename__ = "salary"
    salary_id = sa.Column(Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(Text(36),
                        ForeignKey("personal.user_id"),
                        default=lambda: str(uuid.uuid4()))
    month = sa.Column(Integer)
    year = sa.Column(Integer)
    salary = sa.Column(Integer)
    sa.UniqueConstraint(user_id, month, year, salary)


engine = create_engine(Database_con)

personalList = pd.read_excel(r'data.xlsx', sheet_name='personal')
departmentsList = pd.read_excel(r'data.xlsx', sheet_name='departments')
pcList = pd.read_excel(r'data.xlsx', sheet_name='pc')
login_datesList = pd.read_excel(r'data.xlsx', sheet_name='login_dates')
contractsList = pd.read_excel(r'data.xlsx', sheet_name='contracts')
salaryList = pd.read_excel(r'data.xlsx', sheet_name='salary')


def create_departments():
    try:
        with engine.connect() as con:
            departmentsList.to_sql(
                name='departments',
                con=con,
                if_exists='append',
                index=False
            )
            print(f"departments data added successfully")
    except IntegrityError as e:
        print(e.orig)
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating departments: {e}")


def create_pc():
    try:
        with engine.connect() as con:
            pcList.to_sql(
                name='pc',
                con=con,
                chunksize=1200,
                if_exists='append',
                index=False
            )
            print(f"pc data added successfully")
    except IntegrityError as e:
        print(e.orig)
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating pc: {e}")


def create_personal():
    try:
        with engine.connect() as con:
            personalList.to_sql(
                name='personal',
                con=con,
                chunksize=1200,
                if_exists='append',
                index=False
            )
            print(f"personal data added successfully")
    except IntegrityError as e:
        print(e.orig)
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating personal: {e}")


def create_contracts():
    try:
        with engine.connect() as con:
            contractsList.to_sql(
                name='contracts',
                con=con,
                chunksize=1200,
                if_exists='append',
                index=False
            )
            print(f"contracts data added successfully")
    except IntegrityError as e:
        print(e.orig)
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating contracts: {e}")


def create_salary():
    try:
        with engine.connect() as con:
            salaryList.to_sql(
                name='salary',
                con=con,
                chunksize=13000,
                if_exists='append',
                index=False
            )
            print(f"salary data added successfully")
    except IntegrityError as e:
        print(e.orig)
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating salary: {e}")


def create_login_dates():
    try:
        with engine.connect() as con:
            login_datesList.to_sql(
                name='login_dates',
                con=con,
                chunksize=1200,
                if_exists='append',
                index=False
            )
            print(f"login_dates data added successfully")
    except IntegrityError as e:
        print(e.orig)
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating login_dates: {e}")


if __name__ == '__main__':
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine, checkfirst=True)
    create_departments()
    create_pc()
    create_personal()
    create_contracts()
    create_salary()
    create_login_dates()
    input()
