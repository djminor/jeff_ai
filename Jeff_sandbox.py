from asyncio import subprocess
from inspect import walktree
from more_itertools import take
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = '9fee242a-9569-4ac9-ac6d-1a049257d875'
api_instance = cloudmersive_nlp_api_client.LanguageTranslationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.LanguageTranslationRequest("How are you?")
try: 
    api_response = api_instance.language_translation_translate_eng_to_rus(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageTranslationApi->language_translation_translate_eng_to_rus: %s\n" % e)
