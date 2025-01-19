import boto3
# Criando uma instância do cliente S3
s3_client = boto3.client('s3')
# Listando buckets
response = s3_client.list_buckets()
# Extraindo informações dos buckets
buckets = response['Buckets']
# Imprimindo os nomes dos buckets
print("Buckets na conta AWS:")
print(response)
for bucket in buckets:
    print(f"- {bucket['Name']}")