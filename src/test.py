#!/usr/bin/env python

import sys
from Engine import NexusApi

# The function to be executed at runtime
def main():
    apiKey = input("Enter API Access Key: ")
    nexusMods = NexusApi(apiKey)
    
if __name__ == '__main__':
    main()