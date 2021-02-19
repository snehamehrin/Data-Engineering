import boto3
import setup

def run_jobs():
    client = boto3.client('emr', region_name='us-east-1')
    response = client.list_clusters(

        ClusterStates=['WAITING'
                       ],

    )
    for cluster in response['Clusters']:
        cluster_id=cluster['Id']
        response = client.add_job_flow_steps(
            JobFlowId=cluster_id,
            Steps=[
                {
                    'Name': 'Execute Script',
                    'ActionOnFailure': 'CANCEL_AND_WAIT',
                    'HadoopJarStep': {
                        'Jar': 'command-runner.jar',
                        'Args': ['bash', '/home/hadoop/Execute.sh']
                    }
                }

            ]
        )
        print(response)

run_jobs()
