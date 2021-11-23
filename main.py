import argparse
import json
import re
import base64
import requests

class KubernetesCLI(object):

    
    def __init__(self):
         
        
        self._api_url = 'http://http://localhost:8080/apis/'

           
                            
               

if __name__ == '__main__':

    # Parse options
    #
    parser = argparse.ArgumentParser(description="Kubernetes CLI",                                     
                                     fromfile_prefix_chars='@')
    parser.add_argument("--namespace",
                        dest="namespace",
                        required=False,
                        help="R|\n"
                             "Application to search")                                 
    args = parser.parse_args()
       

    

