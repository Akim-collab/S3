import boto3
import torch
from collections import OrderedDict
from torch import tensor

s3_client = boto3.client('s3',
                         endpoint_url='http://localhost:9000',
                         aws_access_key_id='ROOTUSER',
                         aws_secret_access_key='SOME_STRONG_PASSWORD')

response = s3_client.get_object(Bucket='my-bucket', Key='checkpoint.pth')
state = eval(response['Body'].read())

model = torch.nn.Linear(10, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
model.load_state_dict(state['state_dict'])
optimizer.load_state_dict(state['optimizer'])
epoch = state['epoch']

print(state)
