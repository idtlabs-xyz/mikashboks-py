import boto3
import os
import logging

logger = logging.getLogger()
cognito_client = boto3.client('cognito-idp')


def get_user_attribute(user_id, attributes):
    responses = cognito_client.list_users(
        UserPoolId=os.getenv("COGNITO_USERPOOL_ID"),
        AttributesToGet=attributes,
        Limit=1,
        Filter="sub = \"" + user_id + "\""
    )
    user = responses["Users"][0] if responses["Users"] else None
    if not user:
        return None

    for attribute in user['Attributes']:
        if attribute["Name"] == attribute:
            return attribute["Value"]
    logger.error("Could not determine " + attribute + " for user " + user_id)
    return None
