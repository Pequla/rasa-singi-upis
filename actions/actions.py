from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
import requests

# Global variables
default_response = "Nažalost, nisam u mogućnosti da Vam odgovorim na ovo pitanje. Molim Vas da kontaktirate studentski servis na adresi: studije@singidunum.ac.rs"

class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]):
        global default_response
        dispatcher.utter_message(default_response)
        return [UserUtteranceReverted()]
    
class ActionRespondFromAPI(Action):

    def name(self) -> Text:
        return "action_api_response"
    
    async def run(self, dispatcher, tracker, domain):
        global default_response
        intent_name = tracker.latest_message['intent'].get('name')

        api_url = f"https://rasa.singidunum.ac.rs/api/question/intent/{intent_name}"
        
        try:
            response = requests.get(api_url, headers={'x-token': 'e6fcad6c-fd9d-4ab9-bfda-22e45c6b7de7'})
            response.raise_for_status()
            json_data = response.json()
            text_data = json_data.get('answer', default_response)
            dispatcher.utter_message(text_data)

        except requests.exceptions.RequestException as e:
            # Handle exceptions if the request fails
            dispatcher.utter_message(f"Došlo je do greške, pokušajte ponovo kasnije.")
            print('REST Error:', e)
        return []