import os
import json
import logging
import random
import pandas as pd

from flask import Flask, request, make_response, Response

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.signature import SignatureVerifier

from slashCommand import Slash
from seedData import SeedData

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

def getSeedData(filepath):
  global seedDataDict

  seedData = SeedData(filepath)
  seedDataJsonString = seedData.csvToJsonString()
  seedDataDictWithoutKeys = seedData.jsonStringToDict(seedDataJsonString)
  seedDataDict = seedData.createDictWithKeysFromDict(seedDataDictWithoutKeys)
  seedDataDict = seedData.formatValues(seedDataDict)

  print("Seed data has been loaded and cleaned from CSV to Dict...")

@app.route("/slack/randomFromSeed", methods=["POST"])
def commandRandomFromSeed():
  if not verifier.is_valid_request(request.get_data(), request.headers):
    return make_response("invalid request", 403)
  info = request.form

  chosenLocation = seedDataDict[random.randint(0, len(seedDataDict) - 1)]

  try:
    response = slack_client.chat_postMessage(
      channel='#{}'.format(info["channel_name"]),
      text=info["user_name"] + " is requesting a random location from the seed data. It is:\n```" + json.dumps(chosenLocation) + "```"
    )
  
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)
    return make_response("", e.response.status_code)

  return make_response("", response.status_code)

@app.route("/slack/displaySeed", methods=["POST"])
def commandDisplaySeed():
  if not verifier.is_valid_request(request.get_data(), request.headers):
    return make_response("invalid request", 403)
  info = request.form

  try:
    response = slack_client.chat_postMessage(
      channel='#{}'.format(info["channel_name"]), 
      text=info["user_name"] + " is requesting the seed data. It is:\n```" + str(seedDataDict) + "```"
    )
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)
    return make_response("", e.response.status_code)

  return make_response("", response.status_code)

@app.route("/slack/test", methods=["POST"])
def commandTest():
  if not verifier.is_valid_request(request.get_data(), request.headers):
    return make_response("invalid request", 403)
  info = request.form

  try:
    response = slack_client.chat_postMessage(
      channel='#{}'.format(info["channel_name"]), 
      text=info["user_name"] + " wants to eat " + info["text"]
    )
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)
    return make_response("", e.response.status_code)

  return make_response("", response.status_code)

# Start the Flask server
if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  SLACK_SIGNATURE = os.environ['SLACK_SIGNATURE']
  slack_client = WebClient(SLACK_BOT_TOKEN)
  verifier = SignatureVerifier(SLACK_SIGNATURE)

  getSeedData("resources/seed.csv")

  app.run()
