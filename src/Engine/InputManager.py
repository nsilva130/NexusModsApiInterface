# InputManager.py

# Initialize logger
import logging
dateFormat = '%Y-%m-%d %H:%M:%S'
logFormat = '[%(asctime)s.%(msecs)03d] %(name)s (%(levelname)s): %(msg)s'
log = logging.getLogger("InputManager")
logging.basicConfig(format=logFormat,datefmt=dateFormat)
# Log Level = INFO
log.setLevel(logging.INFO)

class InputManager():
    """An interface that handles user input and input logging
    """
    def basicInput(prompt = "User Input: ") -> str:
        """Requests input from the user and returns the input as a String

        Args:
            prompt (str, optional): The prompt to provide the user when requesting input. Defaults to "User Input: ".

        Returns:
            str: The input received from the user
        """
        
        log.debug("Arg(s) received: \n\tprompt = \"{0}\"".format(prompt))
        log.info(prompt)
        userInput = input()
        log.debug("Received user input: \n\tuserInput = \"{0}\"".format(userInput))
        log.debug("Returning userInput = \"{0}\"".format(userInput))
        return userInput
    
    def waitInput(prompt = "Press enter to continue...") -> None:
        """Pauses the script to await further input from the user.

        Args:
            prompt (str, optional): The prompt to provide the user. Defaults to "Press enter to continue...".
        """
        log.debug("Arg(s) received: \n\tprompt = \"{0}\"".format(prompt))
        log.info(prompt)
        userInput = input()
        log.debug("waitInput() passed.")
        return
    
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
        
        # Log inputs
        log.debug("Arg(s) received:\n\tprompt = \"{0}\",\n\tpositive = \"{1}\",\n\tnegative = \"{2}\",\n\tignoreCase = \"{3}\"".format(prompt,positive,negative,ignoreCase))
        log.info(prompt)
        userInput = input()
        # Log userInput
        log.debug("Received user input:\n\tuserInput = \"{0}\"".format(userInput))
        if (ignoreCase):
            # Convert to lowercase so that the input case doesn't matter
            log.debug("Converting input and arg(s) to lowercase.")
            positiveResponse = positiveResponse.lower()
            negativeResponse = negativeResponse.lower()
            userInput = userInput.lower()
        
        if (userInput == positiveResponse):
            log.debug("User input matches \"{0}\" (positiveResponse). Returning \"True\"".format(positiveResponse))
            return True
        elif (userInput == negativeResponse):
            log.debug("User input matches \"{0}\" (negativeResponse). Returning \"False\"".format(negativeResponse))
            return False
        else:
            log.error("Received invalid user input. userInput = \"{0}\" does not match \"{1}\" (positiveReponse) or \"{2}\" (negativeReponse)".format(userInput,positiveResponse,negativeResponse))
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
        # Log inputs
        log.debug("Arg(s) received:\n\tprompt = \"{0}\",\n\tpositive = \"{1}\",\n\tignoreCase = \"{2}\"".format(prompt,positive,ignoreCase))
        positiveResponse = positive
        log.info(prompt)
        userInput = input()
        # Log userInput
        log.debug("Received user input:\n\tuserInput = \"{0}\"".format(userInput))
        
        if (ignoreCase):
            # Convert to lowercase
            log.debug("Converting input and arg(s) to lowercase.")
            positiveResponse = positiveResponse.lower()
            userInput = userInput.lower()
        
        if (userInput == positiveResponse):
            log.debug("User input matches \"{0}\" (positiveResponse). Returning \"True\"".format(positiveResponse))
            return True
        else:
            log.debug("User input does not match \"{0}\" (positiveResponse). Returning \"False\" (default falsy).".format(positiveResponse))
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
        
        log.debug("Arg(s) received:\n\tprompt = \"{0}\",\n\negative = \"{1}\",\n\tignoreCase = \"{2}\"".format(prompt,negative,ignoreCase))
        negativeResponse = negative
        log.info(prompt)
        userInput = input()
        # Log userInput
        log.debug("Received user input:\n\tuserInput = \"{0}\"".format(userInput))
        
        if (ignoreCase):
            # Convert to lowercase
            log.debug("Converting input and arg(s) to lowercase.")
            negativeResponse = negativeResponse.lower()
            userInput = userInput.lower()
        
        if (userInput == negativeResponse):
            log.debug("User input matches \"{0}\" (negativeResponse). Returning \"False\"".format(negativeResponse))
            return False
        else:
            log.debug("User input does not match \"{0}\" (negativeResponse). Returning \"True\" (default truthy).".format(negativeResponse))
            return True