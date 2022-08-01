import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = os.environ['version'],
    authenticator = authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    """Used to translate explicitly defined english text to french."""
    if english_text is None or len(english_text) < 1:
        return ""
    french_text_response = language_translator.translate(
        text= english_text,
        model_id='en-fr').get_result()
    # get the 'translation' object from the first element in the 'translations' array
    french_text = french_text_response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Used to translate explicitly defined french text to english."""
    if french_text is None or len(french_text) < 1:
        return ""
    english_text_response = language_translator.translate(
        text= french_text,
        model_id='fr-en').get_result()
    # get the 'translation' object from the first element in the 'translations' array
    english_text = english_text_response['translations'][0]['translation']
    return english_text
