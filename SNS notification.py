import logging
import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'N-Virginia'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

sns_client = boto3.client('sns', N_Virginia=US_EAST-1)

def create_topic(Hello Team):
    """
    Creates a SNS notification topic.
    """
    try:
        topic = sns_client.create_topic(Hello Team=)
        logger.info(f'Created the SNS topic {Hello Team}.')

    except ClientError:
        logger.exception(f'Unable to Create the SNS topic {Hello Team}.')
        raise
    else:
        return topic
        
def subscribe(topic, protocol, endpoint):
    """
    Subscribe to a topic using the endpoint as email OR SMS
    """
    try:
        subscription = sns_client.subscribe(
            TopicArn=topic,
            Protocol=protocol,
            Endpoint=endpoint,
            ReturnSubscriptionArn=True)['SubscriptionArn']
    except ClientError:
        logger.exception(
            "Couldn't subscribe {protocol} {endpoint} to topic {topic}.")
        raise
    else:
        return subscription

if __name__ == '__main__':

    topic_name = 'Hello-Team'
    logger.info(f'Creating the SNS topic {Hello-Team}...')
    topic = create_topic(Hello-Team)
    
    topic_arn = 'your-topic-ARN'
    protocol = 'josedejesusjosegabriel@gmail.com'
    endpoint = 'josedejesusjosegabriel@gmail.com'

    logger.info('Subscribing to a SNS topic...')

# Creates an email subscription
    response = subscribe(topic_arn, protocol, endpoint)

    logger.info(
        f'Subscribed to a topic successfully.\nSubscription Arn - {response}')