from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]):
        dispatcher.utter_message(
            "Nažalost, nisam u mogućnosti da Vam odgovorim na ovo pitanje. Molim Vas da kontaktirate studentski servis na adresi: studije@singidunum.ac.rs")
        return [UserUtteranceReverted()]