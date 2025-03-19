import boto3
import json
import argparse

def get_rds_instances(region):
    # Initialize boto3 client for RDS
    client = boto3.client('rds', region_name="eu-north-1")

    try:
        response = client.describe_db_instances()
        instances = response.get('DBInstances', [])

        rds_metadata = []
        for instance in instances:
            metadata = {
                'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
                'Engine': instance['Engine'],
                'Status': instance['DBInstanceStatus'],
                'Endpoint': instance['Endpoint']['Address'] if 'Endpoint' in instance else 'N/A'
            }
            rds_metadata.append(metadata)

        return json.dumps(rds_metadata, indent=4)
    except Exception as e:
        return json.dumps({'error': str(e)}, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrieve AWS RDS metadata')
    parser.add_argument('region', type=str, help='AWS region to query')
    args = parser.parse_args()

    print(get_rds_instances(args.region))
