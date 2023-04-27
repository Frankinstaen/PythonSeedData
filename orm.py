# from sqlalchemy.exc import IntegrityError, SQLAlchemyError
# import pandas as pd
# from logger import logger
#
# from Entity.Models import engine
#
# personalList = pd.read_excel(r'data.xlsx', sheet_name='personal')
# departmentsList = pd.read_excel(r'data.xlsx', sheet_name='departments')
# pcList = pd.read_excel(r'data.xlsx', sheet_name='pc')
# login_datesList = pd.read_excel(r'data.xlsx', sheet_name='login_dates')
# contractsList = pd.read_excel(r'data.xlsx', sheet_name='contracts')
# salaryList = pd.read_excel(r'data.xlsx', sheet_name='salary')
#
#
# def create_departments():
#     try:
#         with engine.connect() as con:
#             departmentsList.to_sql(
#                 name='departments',
#                 con=con,
#                 if_exists='append',
#                 index=False
#             )
#             logger.info(f"departments data added successfully")
#     except IntegrityError as e:
#         logger.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         logger.error(f"Unexpected error when creating departments: {e}")
#         raise e
#
#
# def create_pc():
#     try:
#         with engine.connect() as con:
#             pcList.to_sql(
#                 name='pc',
#                 con=con,
#                 chunksize=1200,
#                 if_exists='append',
#                 index=False
#             )
#             logger.info(f"pc data added successfully")
#     except IntegrityError as e:
#         logger.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         logger.error(f"Unexpected error when creating pc: {e}")
#         raise e
#
#
# def create_personal():
#     try:
#         with engine.connect() as con:
#             personalList.to_sql(
#                 name='personal',
#                 con=con,
#                 chunksize=1200,
#                 if_exists='append',
#                 index=False
#             )
#             logger.info(f"personal data added successfully")
#     except IntegrityError as e:
#         logger.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         logger.error(f"Unexpected error when creating personal: {e}")
#         raise e
#
#
# def create_contracts():
#     try:
#         with engine.connect() as con:
#             contractsList.to_sql(
#                 name='contracts',
#                 con=con,
#                 chunksize=1200,
#                 if_exists='append',
#                 index=False
#             )
#             logger.info(f"contracts data added successfully")
#     except IntegrityError as e:
#         logger.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         logger.error(f"Unexpected error when creating contracts: {e}")
#         raise e
#
#
# def create_salary():
#     try:
#         with engine.connect() as con:
#             salaryList.to_sql(
#                 name='salary',
#                 con=con,
#                 chunksize=13000,
#                 if_exists='append',
#                 index=False
#             )
#             logger.info(f"salary data added successfully")
#     except IntegrityError as e:
#         logger.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         logger.error(f"Unexpected error when creating salary: {e}")
#         raise e
#
#
# def create_login_dates():
#     try:
#         with engine.connect() as con:
#             login_datesList.to_sql(
#                 name='login_dates',
#                 con=con,
#                 chunksize=1200,
#                 if_exists='append',
#                 index=False
#             )
#             logger.info(f"login_dates data added successfully")
#     except IntegrityError as e:
#         logger.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         logger.error(f"Unexpected error when creating login_dates: {e}")
#         raise e
