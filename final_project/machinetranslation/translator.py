import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']

url = os.environ['url']
versionD = os.environ['version']

authenticatorD = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=versionD,
    authenticator=authenticatorD
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    trans = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    frenchText = trans["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    trans = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    englishText = trans["translations"][0]["translation"]
    return englishText
