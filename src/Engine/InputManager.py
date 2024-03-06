# InputManager.py

class InputManager():
    
    def booleanInput(prompt = "User Input (t/f): ",positive = 't',negative = 'f',ignoreCase = True) -> bool:
        """Requests user input and will return a boolean based on it.

        Args:
            prompt (str, optional): The prompt to give the user. Defaults to "User Input (t/f): ".
            positive (str, optional): The input that will result in a positive result. Defaults to 't'.
            negative (str, optional): The input that will result in a negative result. Defaults to 'f'.
            ignoreCase (bool, optional): If the user input should ignore upper/lowercase values. Defaults to True.

        Returns:
            bool: Returns "True" for positive result, "False" for negative result.
        """
        
        positiveResponse = positive
        negativeResponse = negative
        
        userInput = input(prompt)
        
        if (ignoreCase):
            # Convert to lowercase so that the input case doesn't matter
            positiveResponse = positiveResponse.lower()
            negativeResponse = negativeResponse.lower()
            userInput = userInput.lower()
        
        if (userInput == positiveResponse):
            return True
        elif (userInput == negativeResponse):
            return False
        else:
            raise Exception("Invalid user input. Acceptable values: " + positiveResponse + ", " + negativeResponse)
        
    def falsyBooleanInput(prompt = "User Input (t/*): ",positive = 't',ignoreCase = True) -> bool:
        """Requests user input and will return a boolean based on it. If any input other than one matching the positive arg is received, returns False.

        Args:
            prompt (str, optional): The prompt to give the user. Defaults to "User Input (t/*): ".
            positive (str, optional): The input that will result in a positive result. Defaults to 't'.
            ignoreCase (bool, optional): If the user input should ignore upper/lowercase values. Defaults to True.

        Returns:
            bool: Returns "True" for positive result, "False" otherwise.
        """
        
        positiveResponse = positive
        
        userInput = input(prompt)
        
        if (ignoreCase):
            # Convert to lowercase
            positiveResponse = positiveResponse.lower()
            userInput = userInput.lower()
        
        if (userInput == positiveResponse):
            return True
        else:
            return False
        
        
    def truthyBooleanInput(prompt = "User Input (*/f): ",negative = 'f',ignoreCase = True) -> bool:
        """Requests user input and will return a boolean based on it. If any input other than one matching the negative arg is received, returns True.

        Args:
            prompt (str, optional): The prompt to give the user. Defaults to "User Input (*/f): ".
            negative (str, optional): The input that will result in a negative result. Defaults to 'f'.
            ignoreCase (bool, optional): If the user input should ignore upper/lowercase values. Defaults to True.

        Returns:
            bool: Returns "False" for negative result, "True" otherwise.
        """
        
        negativeResponse = negative
        
        userInput = input(prompt)
        
        if (ignoreCase):
            # Convert to lowercase
            negativeResponse = negativeResponse.lower()
            userInput = userInput.lower()
        
        if (userInput == negativeResponse):
            return False
        else:
            return True