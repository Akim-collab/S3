import boto3
import torch

s3_client = boto3.client('s3',
                         endpoint_url='http://localhost:9000',
                         aws_access_key_id='ROOTUSER',
                         aws_secret_access_key='SOME_STRONG_PASSWORD')

s3_client.create_bucket(Bucket='my-bucket')

model = torch.nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
state = {
    'state_dict': model.state_dict(),
    'optimizer': optimizer.state_dict(),
    'epoch': 1,
}

print(state)

s3_client.put_object(Bucket='my-bucket', Key='checkpoint.pth', Body=str(state))


