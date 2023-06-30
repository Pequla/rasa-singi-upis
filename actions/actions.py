from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionDefaultFallback(Action):

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "Na žalost, nisam u mogućnosti da Vam odgovorim na ovo pitanje. Molim Vas da kontakrite studentski servis na adresi: studije@singidunum.ac.rs")
        return []


class ActionUnlikelyIntent(Action):

    def name(self):
        return "action_unlikely_intent"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "Na žalost, nisam u mogućnosti da Vam odgovorim na ovo pitanje. Molim Vas da kontakrite studentski servis na adresi: studije@singidunum.ac.rs")
        return []
