from pymongo import MongoClient
from django.http import HttpResponse

def inserirDados(teste):
    my_client = MongoClient("localhost", 27017)

    dbname = my_client['noticias'] #base de dados
    collection_name = dbname["collection"]

    #duas collections
    medicine_1 = {
        "medicine_id": "RR000123456",
        "common_name" : "Paracetamol",
        "scientific_name" : "",
        "available" : "Y",
        "category": "fever"
    }
    medicine_2 = {
        "medicine_id": "RR000342522",
        "common_name" : "Metformin",
        "scientific_name" : "",
        "available" : "Y",
        "category" : "type 2 diabetes"
    }

    # Insert the documents
    collection_name.insert_many([medicine_1,medicine_2])
    # Check the count
    #count = collection_name.count_documents()
    #print(count)

    # Read the documents
    #med_details = collection_name.find()

    # Print on the view
    #for r in med_details:
    return HttpResponse("oi")


