import requests

def upload_code():
  my_header = {'Name':'Bhupesh Sharma','Email':'bs5968@srmist.edu.in','College':'SRM Ramapuram','StudentId':'RA1811003020403','FileName':'apitestfinal.py','Password':'YnM1OTY4QHNybWlzdC5lZHUuaW4='}
  with open(r'C:\Users\Bhupesh Sharma\Downloads\apitestfinal.py', 'rb') as file:
    response = requests.put("https://prod-24.centralindia.logic.azure.com/workflows/78d6df0ed1384ee0b7d04918f1a32b85/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=i6gXuS7-5_fFVf-0u8M4UfymINDULCMifsscfN5cPKM",
                             data = file, headers = my_header)
    print(response.text)
    print(response.status_code)

upload_code()