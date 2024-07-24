import os
from google.oauth2 import service_account
from google.cloud import aiplatform




credentials = service_account.Credentials.from_service_account_file("your_credentials_of_gcp.json")

project_id = 'theta-cell-406519'

def predict_text_classification_single_label_sample(project="your_project_id",location="Your_location", endpoint= "Your_endpoint",content="{user_input}"):

  aiplatform.init(project=project, location=location)
  endpoint = aiplatform.Endpoint(endpoint)
  response = endpoint.predict(instances=[{"content": content}], parameters={})
  print(response)
  names=response[0][0]['displayNames']
  values=response[0][0]['confidences']
  max_index=values.index(max(values))
  

  return names[max_index]

