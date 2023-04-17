from __future__ import annotations
import uuid
from typing import List
from sqlalchemy import ForeignKey, String
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, DateTime, Integer, Text
from sqlalchemy import create_engine
from Data.DBConfig import Database_con

Base = declarative_base()


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
    user_id = sa.Column(Text(36),
                        ForeignKey("personal.user_id"),
                        default=lambda: str(uuid.uuid4()),
                        primary_key=True,
                        autoincrement=False)
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

