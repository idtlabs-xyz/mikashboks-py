import boto3
import os
import logging

logger = logging.getLogger()
cognito_client = boto3.client('cognito-idp')


def get_user(user_id):
    responses = cognito_client.list_users(
        UserPoolId=os.getenv("COGNITO_USERPOOL_ID"),
        AttributesToGet=[],
        Limit=1,
        Filter="sub = \"" + user_id + "\""
    )
    return responses["Users"][0] if responses["Users"] else None


def get_user_attribute(user_id, attribute):
    user = get_user(user_id)
    if not user:
        return None

    for attribute in user['Attributes']:
        if attribute["Name"] == attribute:
            return attribute["Value"]
    logger.error("Could not determine " + attribute + " for user " + user_id)
    return None
