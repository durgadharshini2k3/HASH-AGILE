import pysolr
import requests
import pandas as pd
import json



def createCollections(p_collection_name):
    parameters = {
        "action": "CREATE",
        "name": p_collection_name,
        "numShards": 1
    }

    CONNECTION_URL = 'http://localhost:8989/solr/admin/collections'
    response = requests.get(CONNECTION_URL, params=parameters)


    if response.status_code == 200:
        print(f"Collection {p_collection_name} created successfully!")

    else:
        print(f"Something went wrong, Unable to create collection {p_collection_name}")
        print(f"Error: {response.text}")


def indexData(p_collection_name, p_exclude_column):
    employee_data = pd.read_csv("C:/Users/BALAJI/Desktop/Solr-task/Employee.csv")
    selected_data = employee_data.drop(columns=[p_exclude_column],axis=1)
    data_dict = selected_data.to_dict(orient='records')
    CONNECTION_URL = f"http://localhost:8989/solr/{p_collection_name}/"
    solr = pysolr.Solr(CONNECTION_URL, always_commit=True)
    
    try:
        solr.add(data_dict)
        print(f"Data indexed successfully inside {p_collection_name} collection")
    
    except pysolr.SolrError as e:
        print(f"Error in indexing data")
        print(f"Error : {e}")


def SearchByColumn(p_collection_name, p_column_name, p_column_value):
    CONNECTION_URL = f"http://localhost:8989/solr/{p_collection_name}/"
    solr = pysolr.Solr(CONNECTION_URL, always_commit=True)
    try:

        results = solr.search(f"{p_column_name}:{p_column_value}")

        if results:
            for result in results:
                print(result)
    
        else:
            print("Results Not Found")

    except pysolr.SolrError as e:
        print(f"{p_column_name} is not indexed")

def getEmpCount(p_collection_name):
    CONNECTION_URL = f"http://localhost:8989/solr/{p_collection_name}"
    solr = pysolr.Solr(CONNECTION_URL, always_commit=True)
    params = {
        'q': "*:*",
        'rows': 0,
        'wt': 'json'
    }

    try:
        response = solr.search(**params)
        num_found = response.hits

        print(f"Number of Employees is {num_found}")

    except pysolr.SolrError as e:
        print(f"Something went wrong")
        print(f"Error: {e}")


def getDepFacet(p_collection_name):
    CONNECTION_URL = f"http://localhost:8989/solr/{p_collection_name}"
    solr = pysolr.Solr(CONNECTION_URL, always_commit=True)
    try:
        results = solr.search(**{
        'q': '*:*',
        'facet': 'true',
        'facet.field': 'Department'
        })
        facet_counts = results.facets ['facet_fields']['Department']
        print(facet_counts)
        
    except pysolr.SolrError as e:
        print("something went wrong")
        print(f"Error : {e}")

def delEmpById(p_collection_name, p_employee_id):
    CONNECTION_URL  = f'http://localhost:8989/solr/{p_collection_name}'

   
    solr = pysolr.Solr(CONNECTION_URL, always_commit=True)

    try:
        solr.delete(q=f"Employee_ID:{p_employee_id}")
        print(f"Details of employee with employee ID {p_employee_id} has been removed")
        
    except pysolr.SolrError as e:
        print(f"Some thing went wrong, May be due to invalid employee ID")


v_nameCollection = "Hash_Durgapriyadharshini"

v_phoneCollection = "Hash_5734"

createCollections(v_nameCollection)

createCollections(v_phoneCollection)

getEmpCount(v_nameCollection)

indexData(v_nameCollection, 'Department')

indexData(v_phoneCollection, 'Gender')

getEmpCount(v_nameCollection)

delEmpById(v_nameCollection, 'E02003')

getEmpCount(v_phoneCollection)

SearchByColumn(v_nameCollection, 'Department', 'IT')

SearchByColumn(v_nameCollection, 'Gender', 'Male')

SearchByColumn(v_phoneCollection,'Department', 'IT')

getDepFacet(v_nameCollection)

getDepFacet(v_phoneCollection)