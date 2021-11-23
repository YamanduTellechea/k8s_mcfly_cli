import argparse
import json
import re
import base64
import urllib3
import requests
from prettytable import PrettyTable


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

    header = ['DeploymentName','Image','lastUpdateTime' ]
    table_values = PrettyTable(header)    

    for deployment in deployments['items']:
        container_image = []          
        for container in (deployment['spec']['template']['spec']['containers']):
            container_image.append(container['image'])
        
        value = [deployment['metadata']['name'], str(container_image),deployment['status']['conditions'][-1]['lastUpdateTime']]
        table_values.add_row(value)
    

    print(table_values)
    
            

    
    

       

    

