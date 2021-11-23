import argparse
import json
import requests
from prettytable import PrettyTable


class KubernetesCLI(object):

       
    def get_Deployments(self,namespace, api_url='http://localhost:8080/apis/'):

       
        deployments_r = requests.get(api_url + 'apps/v1/namespaces/' + namespace + '/deployments')        
        deployments_json = json.loads(deployments_r.text)

        return deployments_json
               

if __name__ == '__main__':

    # Parse options
    #
    parser = argparse.ArgumentParser(description="Kubernetes CLI",                                     
                                     fromfile_prefix_chars='@')
    parser.add_argument("--namespace","-n",
                        dest="namespace",
                        required=True,
                        help="R|\n"
                             "Namespace to search")
    parser.add_argument("--apiurl",
                        dest="apiurl",
                        required=False,
                        help="R|\n"
                             "API URL")                                                            
    args = parser.parse_args()

    instance = KubernetesCLI()
    if args.apiurl:
        deployments= instance.get_Deployments(args.namespace,args.apiurl)
    else:
        deployments= instance.get_Deployments(args.namespace)
    header = ['DeploymentName','Image','lastUpdateTime' ]
    table_values = PrettyTable(header)    

    for deployment in deployments['items']:
        container_image = []          
        for container in (deployment['spec']['template']['spec']['containers']):
            container_image.append(container['image'])
        
        value = [deployment['metadata']['name'], ', '.join(container_image),deployment['status']['conditions'][-1]['lastUpdateTime']]
        table_values.add_row(value)
    

    print(table_values)
    
            

    
    

       

    

