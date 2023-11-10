# Chatbot_using_SementicSearch_for_QA_from_webpage_through_Elasticsearch_Indexing
Chatbot that used elasticsearch for indexing webpage

### Steps for creating Chatbot using Sementic Search for Question Answering. 
Due to file uploading limit i could not upload my_venv foler of this project. 

1. Create Virtual Environment for the folder
   
  a.  open command prompt and write the following commands 
  
  b.  cd path_for_folder
  c.  python -m venv my_venv
Now activate virtual Environment
  d. my_venv\Scripts\activate
Now perform installations
 pip install transformers
 pip install requests
 pip install elasticsearch
 pip install openai
3. Scrap the web page article
   wikipedia page (copy link of web page)
4. Now open vscode open the folder in vscode  and make a file data.py
    now in data.py file write code and give the link of web page in line
   import requests
   data = requests.get("web page link")
   print(data.text)
   now run command in vscode terminal
   python data.py
#### 4. Now go to Elasticsearch webpage make account and save username and password as these will be used in our code files
5. create deployment (copy cloud Id )
   go to home and click vectorsearch
6.  Now again go to VSCode and make a new file name datasearch.py
   write the following code and place cloud id and password in the code
cloud_id = "paste the cloud id copied from first deploymentand"
Basic_auth =("elastic" , "password")   # here in the code we placed the password of elasticsearch account
complete the code that is placed in our datasearch.py and run the command in vscode terminal
                                 python datasearch.py
pip install sentence_transformers
[we uninstalled transformers as it was not giving response]
after this we created the function for url in data.py and called it in datasearch.py
After entering url = weburl run the command
                python datasearch.py
    
    After running python datasearch.py indexes will start running
    we run indexes only one and then comment them
    now make Query data function

8. Now make a file in vscode op_ai.py file and write code for chatbot and copy the key from openai and place that key in this code where written in the file.
   Now run the code by writing

   python datasearch.py
   
   we have set temperature = 0
   
   chatbot will answer only from the webpage from which we have given link not from other websites
   write a question and get answers from the webpage 
