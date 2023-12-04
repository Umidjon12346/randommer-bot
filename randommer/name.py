import requests
from .randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        endpoint = "Name"

        url= self.get_url()+endpoint

        headers={
           "X-Api-Key": api_key
        }
        payload ={
            "nameType": nameType,
            "quantity": quantity
        }
        response =requests.get(url,params=payload,headers = headers)

        if response.status_code == 200:
            return response.json()
        return response.status_code
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        endpoint = "Name/Suggestions"
        
        url= self.get_url()+endpoint

        headers={
           "X-Api-Key": api_key
        }
        payload ={
            "startingWords": startingWords
        }
        response =requests.get(url,params=payload,headers = headers)

        if response.status_code == 200:
            return response.json()
        return response.status_code
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        endpoint = "Name/Cultures"
        
        url= self.get_url()+endpoint

        headers={
           "X-Api-Key": api_key
        }
        
        response =requests.get(url,headers = headers)

        if response.status_code == 200:
            return response.json()
        return response.status_code