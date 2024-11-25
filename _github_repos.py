import requests

class Github:
    def __init__(self):
        self.api_url='https://api.github.com'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getrepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    
github = Github()

while True:
    secim= input('1- find user\n2- get repositories\n3- Exit\nSeçim:')

    if secim=='3':
        break
    else:
        if secim=='1':
            username=input('username: ')
            result = github.getUser(username)
            print(f"name:{result['name']} public repos:{result['public_repos']} follower:{result['followers']}")
        elif secim=='2':
            username=input('username: ')
            result = github.getrepositories(username)
            for repo in result:
                print(repo['name'])
        else:
            print('yanlış seçim')