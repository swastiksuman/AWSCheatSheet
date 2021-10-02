import boto3

statuses = ['ROLLBACK_COMPLETE', 'CREATE_COMPLETE', 'UPDATE_COMPLETE']
cf = boto3.resource('cloudformation')
stacks = [stack for stack in cf.stacks.all() if stack.stack_status in statuses]
print(stacks)
cfn = boto3.client('cloudformation')
for stack in stacks:
    print(cfn.delete_stack(StackName=stack.name))
