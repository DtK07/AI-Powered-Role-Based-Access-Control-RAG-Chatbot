from services.router import router
from services.query import process_user_query
import json
import pandas as pd

global_df = pd.read_csv("C:/Users/DINESH/Downloads/Codebasics_Project/resources/data/hr/hr_data.csv")
def orchestrator (query: str, employee_id: str, role: str) -> str:
    emp_df = global_df[global_df["employee_id"] == employee_id]
    query_type = json.loads(router(query))
    #print(query_type) 
    if query_type["access_violation"]:
        return f"Your query cannot be processed due to security reasons"
    else: 
        if 'dataframe' in query_type['route']:
            data = {}
            for field in query_type['fields']:
                if field == "manager_id":
                    manager_id = emp_df["manager_id"].iloc[0]
                    value = global_df.loc[global_df["employee_id"] == manager_id, "full_name"].iloc[0]
                else:
                    value = emp_df.loc[emp_df["employee_id"] == employee_id, field].iloc[0]
                data[field] = value
            response = query_type['response_template'].format(**data)
        else:
            response = ""
        if 'vector' in query_type['route']:
            query = query_type['semantic_query']
            semantic_response = process_user_query(query, role)
        else:
            semantic_response = ""
        final_response = response + semantic_response
        return final_response
#result = orchestrator("What is the revenue", "FINEMP1000", "finance")
#print(result)
#"What is the profit and financial goals?"

#query = orchestrator("What is the profit and financial goals", "FINEMP1000", "finance")