import argparse
import json
import re
import base64
import urllib3
import requests

http = urllib3.PoolManager()

class KubernetesCLI(object):

    
    def __init__(self):
         
        
        self._api_url = 'http://localhost:8080/apis/'
    
    
    def get_Deployments(self,namespace):

       
        deployments_r = requests.get(self._api_url + 'apps/v1/namespaces/' + namespace + '/deployments')        
        deployments_json = json.loads(deployments_r.text)

        return deployments_json

           
                            
               

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

    instance = KubernetesCLI()
    deployments= instance.get_Deployments(args.namespace)
    
    for a in deployments['items']:
        print(a['metadata']['name'])
        for b in (a['spec']['template']['spec']['containers']):
            print(b['image'])

       

    

