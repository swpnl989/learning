  
# #  sqlquery = func.in_(column).label(id)
#                 # print(sqlquery,"-----------------------------------------------------")
#                 #search_args = [col.ilike('%%%s%%' % search_key) for col in ['col1', 'col2', 'col3']]
#                 #query = Query(table).filter(or_(*search_args))
#                 #session.execute(query).fetchall()
#                 # query = func.in_()
#                 # print(query,"-------------------------------------------------------------") 
#                 # query5.append(query)



import sqlalchemy as db

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine('postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB')

# CREATE THE METADATA OBJECT TO ACCESS THE TABLE
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)

# GET THE `actor` TABLE FROM THE METADATA OBJECT
clinic_table = meta_data.tables['clinic_data']

# SELECT COUNT(*) FROM clinic_data
result = db.select([db.func.count()]).select_from(clinic_table).scalar()

print("Count:", result)

