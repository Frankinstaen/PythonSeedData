from __future__ import annotations
import pandas as pd
from fastapi_utils.guid_type import GUID
from typing import List

from sqlalchemy import ForeignKey, create_engine, String
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, DateTime, Integer


Base = declarative_base()


class Departments(Base):
    __tablename__ = "departments"
    id = sa.Column(Integer, primary_key=True)
    department = sa.Column(String)
    personals = relationship(List["Personal"], back_populates="departments")


class Pc(Base):
    __tablename__ = "pc"
    pc_id = sa.Column(GUID, primary_key=True)
    pc_serial = sa.Column(String)
    pc_mac = sa.Column(String)
    pc_ip = sa.Column(String)
    personal = relationship("Personal", back_populates="pc")


class Personal(Base):
    __tablename__ = "personal"
    user_id = sa.Column(GUID, primary_key=True)
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
    user_id = sa.Column(GUID, ForeignKey("personal.user_id"), primary_key=True)
    pc_id = sa.Column(GUID, ForeignKey("pc.pc_id"), primary_key=True)
    date_time = sa.Column(DateTime)


class Сontracts(Base):
    __tablename__ = "contracts"
    user_id = sa.Column(GUID, ForeignKey("personal.user_id"), primary_key=True)
    date_from = sa.Column(Date)
    date_to = sa.Column(Date)


class Salary(Base):
    __tablename__ = "salary"
    user_id = sa.Column(GUID, ForeignKey("personal.user_id"), primary_key=True)
    month = sa.Column(Integer)
    year = sa.Column(Integer)
    salary = sa.Column(Integer)


Server = 'HOME-PC\SQLEXPRESS'
Database = 'our_organization'
Driver = 'ODBC Driver 17 for SQL Server'
Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'

engine = create_engine(Database_con)

Base.metadata.create_all(bind=engine)
print(1)
"""
personalList = pd.read_excel(r'data.xlsx', sheet_name='personal')
departmentsList = pd.read_excel(r'data.xlsx', sheet_name='departments')
pcList = pd.read_excel(r'data.xlsx', sheet_name='pc')
login_datesList = pd.read_excel(r'data.xlsx', sheet_name='login_dates')
contractsList = pd.read_excel(r'data.xlsx', sheet_name='contracts')
salaryList = pd.read_excel(r'data.xlsx', sheet_name='salary')

with engine.connect() as con:
    personalList.to_sql(
        name='personal',
        con=con,
        index='false',
        chunksize=1200,
        if_exists='replace'
    )
    departmentsList.to_sql(
        name='departments',
        con=con,
        schema=Departments(),
        index='false',
        if_exists='replace'
    )
    pcList.to_sql(
        name='pc',
        con=con,
        schema=Pc(),
        index='false',
        chunksize=1200,
        if_exists='replace'
    )
    login_datesList.to_sql(
        name='login_dates',
        con=con,
        index='false',
        chunksize=1200,
        if_exists='replace'
    )
    contractsList.to_sql(
        name='contracts',
        con=con,
        index='false',
        chunksize=1200,
        if_exists='replace'
    )
    salaryList.to_sql(
        name='salary',
        con=con,
        index='false',
        chunksize=13000,
        if_exists='replace'
    )
"""
