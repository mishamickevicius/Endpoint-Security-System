import hashlib
import requests as rq

from dotenv import load_dotenv
import os

from ollama import chat, ChatResponse

def compute_file_hash(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read the file in chunks of 8192 bytes
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def generate_report(data):
    """This function will call the Llama 3.1 Model 
    to generate a report if a virus is found"""
    sys_prompt = '''
    You are an report generator. You will recieve json data from a public api about some known 
    malicious file and generate a report that can help the user. Do basic things like explain 
    what the malicious file is and some suggestions on how to not be effected.
    '''
    response: ChatResponse = chat(model='llama3.1:8b', messages=[
    {'role': 'system', 'content': sys_prompt},
    {'role': 'user', 'content': str(data)}
        ])
    
    return response.message.content

def main():
    ## Read in file path
    # file_path = input("Enter the path to the file: ")
    file_path = 'main/test.txt'
    ## Get Hash for file
    file_hash = compute_file_hash(file_path)

    #### Test Malware Hash
    file_hash = 'cada223faa617fb038a5d6040d6bbe318a8d6a455377fbc5362ad82f0b741e2e'
    ####

    ## Make request to api to lookup hash
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    ## Read in API Key
    load_dotenv()
    api_key = os.getenv('VIRUSTOTAL_API_KEY')

    headers = {"accept": "application/json",
               "x-apikey": api_key}

    response = rq.get(url=url, headers=headers)
    ## Extract score
    reputation_score = int(response.json()['data']['attributes']['reputation'])
    
    if reputation_score == -1:
        print("Known Virus\n")
        print("Report: \n")
        print(generate_report(response.json()['data']))
    else:
        print("Not a known virus")

if __name__ == '__main__':
    main()

