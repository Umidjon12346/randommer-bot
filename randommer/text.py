import requests
from .randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        endpoint ="Text/LoremIpsum"
        url = self.get_url()+endpoint
        headers={
            "X-Api-Key": api_key
        }
        payload = {
            "loremType": loremType,
            "type": type,
            "number": number
        }
        response = requests.get(url,params = payload,headers = headers)
        if response.status_code == 200:
            return response.json()

        return response.status_code

    
    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        endpoint ="Text/Password"
        url = self.get_url()+endpoint
        headers={
            "X-Api-Key": api_key
        }
        payload = {
           "length" : length,
           "hasDigits": hasDigits,
           "hasUppercase" : hasUppercase,
           "hasSpecial" : hasSpecial
        }
        response = requests.get(url,params = payload,headers = headers)
        if response.status_code == 200:
            return response.json()

        return response.status_code
