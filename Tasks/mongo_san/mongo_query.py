from query_generator import *

def mongo_query(mycol, query_agg):
    if isinstance(query_agg, list):
        print(query_agg)
        documents = []
        try:
            for document in  mycol.aggregate(query_agg):
                if len(document)==0:
                    continue
                documents.append(document)
            return documents
        except Exception as e:
            return e 