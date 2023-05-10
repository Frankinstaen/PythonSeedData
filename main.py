from __future__ import annotations
import uuid
from typing import List

import pyodbc
from sqlalchemy import ForeignKey, String
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, DateTime, Integer, Text
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import pandas as pd

Base = declarative_base()

# Server = 'HOME-PC\SQLEXPRESS'
# Database = 'our_organization'
# Driver = 'ODBC Driver 17 for SQL Server'
# Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'

# server='WIN-NLAMS2TV4QH'
# server = ''
# database='our_organization'
# username='sa'
# password='Qq12345678'

# conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' \
#            + server + ';DATABASE=' \
#            + database + ';UID=' + username \
#            + ';PWD=' + password


class Departments(Base):
    __tablename__ = "departments"
    id = sa.Column(Integer, primary_key=True, autoincrement=False, nullable=False)
    department = sa.Column(String, nullable=False)
    personals = relationship(List["Personal"], back_populates="departments")


class Pc(Base):
    __tablename__ = "pc"
    pc_id = sa.Column(Text(36),
                      default=lambda: str(uuid.uuid4()),
                      primary_key=True, nullable=False)
    pc_serial = sa.Column(String, nullable=False)
    pc_mac = sa.Column(String, nullable=False)
    pc_ip = sa.Column(String, nullable=False)
    personal = relationship("Personal", back_populates="pc")


class Personal(Base):
    __tablename__ = "personal"
    user_id = sa.Column(Text(36),
                        default=lambda: str(uuid.uuid4()),
                        primary_key=True, nullable=False)
    first_name = sa.Column(String, nullable=False)
    last_name = sa.Column(String, nullable=False)
    birth_date = sa.Column(Date, nullable=False)
    login = sa.Column(String, nullable=False)
    email = sa.Column(String, nullable=False)
    department_id = sa.Column(ForeignKey("departments.id"), nullable=False)
    department = relationship("Departments", back_populates="personal")
    pc_id = sa.Column(ForeignKey("pc.pc_id"), nullable=False)
    pc = relationship("Pc", back_populates="personal")
    contract = relationship("Сontracts", back_populates="personal")
    login_dates = relationship(List["Login_dates"], back_populates="personal")
    salary = relationship(List["Salary"], back_populates="personal")


class Login_dates(Base):
    __tablename__ = "login_dates"
    login_dates_id = sa.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = sa.Column(Text(36),
                        ForeignKey("personal.user_id"),
                        default=lambda: str(uuid.uuid4()), nullable=False)
    pc_id = sa.Column(Text(36),
                      ForeignKey("pc.pc_id"),
                      default=lambda: str(uuid.uuid4()), nullable=False)
    date_time = sa.Column(DateTime, nullable=False)
    sa.UniqueConstraint(user_id, pc_id, date_time)


class Сontracts(Base):
    __tablename__ = "contracts"
    contracts_id = sa.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = sa.Column(Text(36),
                        ForeignKey("personal.user_id"),
                        default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    date_from = sa.Column(Date, nullable=False)
    date_to = sa.Column(Date, nullable=False)


class Salary(Base):
    __tablename__ = "salary"
    salary_id = sa.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = sa.Column(Text(36),
                        ForeignKey("personal.user_id"),
                        default=lambda: str(uuid.uuid4()), nullable=False)
    month = sa.Column(Integer, nullable=False)
    year = sa.Column(Integer, nullable=False)
    salary = sa.Column(Integer, nullable=False)
    sa.UniqueConstraint(user_id, month, year, salary)


# engine = create_engine(Database_con)

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
    try:
        print("Введите название сервера:")
        server = input()
        print("Введите имя пользователя:")
        username = input()
        print("Введите пароль:")
        password = input()
        database = 'our_organization'
        conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
        cnxn = pyodbc.connect(conn_str)
        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(conn_str))
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine, checkfirst=True)
        create_departments()
        create_pc()
        create_personal()
        create_contracts()
        create_salary()
        create_login_dates()
        print("Нажмите Enter для завершения")
        input()
    except pyodbc.OperationalError:
        print("Ошибка при подключении к базе данных")
