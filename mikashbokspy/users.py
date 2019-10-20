import boto3
import os
import logging

logger = logging.getLogger()
cognito_client = boto3.client('cognito-idp')


def get_user_attribute(user_id, attributes):
    responses = cognito_client.list_users(
        UserPoolId=os.getenv("COGNITO_USERPOOL_ID"),
        AttributesToGet=attributes if isinstance(attributes, list) else [attributes],
        Limit=1,
        Filter="sub = \"" + user_id + "\""
    )
    user = responses["Users"][0] if responses["Users"] else None
    if not user:
        return None

    res = {}

    for attribute in user['Attributes']:
        res[attribute["Name"]] = attribute["Value"]

    return res[attributes[0]] if len(res) == 1 else res
