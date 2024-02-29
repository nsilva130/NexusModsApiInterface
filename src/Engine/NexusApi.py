# NexusApi.py

# Imports Required Dependencies
import requests
import json

# All documentation for Nexus Mods API can be found here: https://app.swaggerhub.com/apis-docs/NexusMods/nexus-mods_public_api_params_in_form_data/1.0


class NexusApi:
    '''Interface for the Nexus Mods website API. Requires active user API token for use.'''
    
    # The API URL to access. This is the Base URL for Nexus Mods API
    _api_url = "https://api.nexusmods.com/"
    
    def __init__(self, apiKey: str):
        """Initialize Nexus Mods API interface.

        Args:
            apiKey (str): The API access key to interract with Nexus Mods.

        Raises:
            Exception: If apiKey is not a string (str) or has length = 0.
            Exception: If API key fails validation response.
        """
        
        # Validate apiKey is a non-empty string
        if (not isinstance(apiKey,str)):
            raise Exception("Valid API key not provided. API key value must be string (str).")
        if (apiKey == ""):
            raise Exception("Valid API key not provided. Game cannot be empty string (len = 0).")
        
        
        # Prepare validation API key request
        validation_url = self._api_url + "v1/users/validate.json"
        validation_headers = { "accept": "application/json" , "apikey": apiKey}
        validation_response = requests.get(validation_url, headers=validation_headers)
        
        # Send validation API key request
        validation_response_code = validation_response.status_code
        
        # Check if the response was invalid
        if validation_response_code != 200:
            # If not response code 200, apiKey is invalid
            raise Exception("Validation response error. Response code = " + str(validation_response_code) + ", JSON: " + str(validation_response.json()))
        
        self._apiKey = apiKey


    ################################
    # 
    # Mods
    # Mod specific routes (E.g. retreiving latest mods, endorsing a mod)
    # 
    ################################
    
    def getUpdated(self,game:str,time = "1w"):
        """Returns updated mods for a game in the given period.

        Args:
            game (str): The game domain to use when polling Nexus Mods (e.g. "baldursgate3").
            time (str, optional): The time period to check up to the present. Must be 1d (1 day), 1w (1 week), or 1m (1 month). Defaults to "1w".

        Raises:
            Exception: If the game domain provided is not a string (str) or has length = 0.
            Exception: If the time period provided is not "1d", "1w", or "1m".

        Returns:
            Response: The response information received from the API.
        """
        
        # Validate the game domain string (DOES NOT GUARANTEE VALID RESPONSE)
        if (not isinstance(game,str)):
            raise Exception("Valid game domain not provided. Game value must be string (str).")
        if (game == ""):
            raise Exception("Valid game domain not provided. Game cannot be empty string (len = 0).")
        
        # Validate the time period
        if ((not time == "1d") and (not time == "1w") and (not time == "1m")):
            raise Exception("Valid time not provided. Time must be 1d (1 day), 1w (1 week), or 1m (1 month)")
        
        # Prepare API request
        request_url = self._api_url + "v1/games/" + game + "/mods/updated.json?period=" + time
        request_headers = { "accept": "application/json" , "apikey": self._apiKey}
        
        # Send API request
        response: requests.Response = requests.get(request_url, headers=request_headers)
        
        # Return the response
        return response
    
    
    def getLatestAdded(self,game:str):
        """Returns the 10 latest added mods for a game.

        Args:
            game (str): The game domain to use when polling Nexus Mods (e.g. "baldursgate3").

        Raises:
            Exception: If the game domain provided is not a string (str) or has length = 0.

        Returns:
            Response: The response information received from the API.
        """
        
        # Validate the game domain string (DOES NOT GUARANTEE VALID RESPONSE)
        if (not isinstance(game,str)):
            raise Exception("Valid game domain not provided. Game value must be string (str).")
        if (game == ""):
            raise Exception("Valid game domain not provided. Game cannot be empty string (len = 0).")
        
        # Prepare API request
        request_url = self._api_url + "v1/games/" + game + "/mods/latest_added.json"
        request_headers = { "accept": "application/json" , "apikey": self._apiKey}
        
        # Send API request
        response: requests.Response = requests.get(request_url, headers=request_headers)
        
        # Return the response
        return response
    
    
    def getLatestUpdated(self,game:str):
        """Returns the 10 latest updated mods for a game.

        Args:
            game (str): The game domain to use when polling Nexus Mods (e.g. "baldursgate3").

        Raises:
            Exception: If the game domain provided is not a string (str) or has length = 0.

        Returns:
            Response: The response information received from the API.
        """
        
        # Validate the game domain string (DOES NOT GUARANTEE VALID RESPONSE)
        if (not isinstance(game,str)):
            raise Exception("Valid game domain not provided. Game value must be string (str).")
        if (game == ""):
            raise Exception("Valid game domain not provided. Game cannot be empty string (len = 0).")
        
        # Prepare API request
        request_url = self._api_url + "v1/games/" + game + "/mods/latest_updated.json"
        request_headers = { "accept": "application/json" , "apikey": self._apiKey}
        
        # Send API request
        response: requests.Response = requests.get(request_url, headers=request_headers)
        
        # Return the response
        return response
    
    
    def getTrending(self,game:str):
        """Returns the top 10 trending mods for a game.

        Args:
            game (str): The game domain to use when polling Nexus Mods (e.g. "baldursgate3").

        Raises:
            Exception: If the game domain provided is not a string (str) or has length = 0.

        Returns:
            Response: The response information received from the API
        """
        
        # Validate the game domain string (DOES NOT GUARANTEE VALID RESPONSE)
        if (not isinstance(game,str)):
            raise Exception("Valid game domain not provided. Game value must be string (str).")
        if (game == ""):
            raise Exception("Valid game domain not provided. Game cannot be empty string (len = 0).")
        
        # Prepare API request
        request_url = self._api_url + "v1/games/" + game + "/mods/trending.json"
        request_headers = { "accept": "application/json" , "apikey": self._apiKey}
        
        # Send API request
        response: requests.Response = requests.get(request_url, headers=request_headers)
        
        # Return the response
        return response
    
    
    def getMod(self,game:str,id:int):
        """Returns a specific mod with the matching ID number.

        Args:
            game (str): The game domain to use when polling Nexus Mods (e.g. "baldursgate3").
            id (int): The mod ID to get.

        Raises:
            Exception: If the game domain provided is not a string (str) or has length = 0.
            Exception: If the mod ID is not >0.

        Returns:
            Response: The response information received from the API.
        """
        
        # Validate the game domain string (DOES NOT GUARANTEE VALID RESPONSE)
        if (not isinstance(game,str)):
            raise Exception("Valid game domain not provided. Game value must be string (str).")
        if (game == ""):
            raise Exception("Valid game domain not provided. Game cannot be empty string (len = 0).")
        
        if ((not isinstance(id,int)) and id <= 0):
            raise Exception("Valid mod ID not provided. Mod ID must be value >0")
        
        # Prepare API request
        request_url = self._api_url + "v1/games/" + game + "/mods/"+ str(id) +".json"
        request_headers = { "accept": "application/json" , "apikey": self._apiKey}
        
        # Send API request
        response: requests.Response = requests.get(request_url, headers=request_headers)
        
        # Return the response
        return response
    
    
    ################################
    # 
    # Mod Files
    # File specific routes (E.g. retreiving file information, retreiving download link)
    # 
    ################################
    
    def getModFiles(self,game:str,id:int):
        """Returns the files for a specific mod with the matching ID number.

        Args:
            game (str): The game domain to use when polling Nexus Mods (e.g. "baldursgate3").
            id (int): The mod ID to get.

        Raises:
            Exception: If the game domain provided is not a string (str) or has length = 0.
            Exception: If the mod ID is not >0.

        Returns:
            Response: The response information received from the API.
        """
        
        # Validate the game domain string (DOES NOT GUARANTEE VALID RESPONSE)
        if (not isinstance(game,str)):
            raise Exception("Valid game domain not provided. Game value must be string (str).")
        if (game == ""):
            raise Exception("Valid game domain not provided. Game cannot be empty string (len = 0).")
        
        if ((not isinstance(id,int)) and id <= 0):
            raise Exception("Valid mod ID not provided. Mod ID must be value >0")
        
        # Prepare API request
        request_url = self._api_url + "v1/games/" + game + "/mods/"+ str(id) +"/files.json"
        request_headers = { "accept": "application/json" , "apikey": self._apiKey}
        
        # Send API request
        response: requests.Response = requests.get(request_url, headers=request_headers)
        
        # Return the response
        return response
    
    
    