from typing import Any, Text, Dict, List

from rasa_sdk import Action
from rasa.shared.core.events import ConversationPaused, UserUtteranceReverted


class ActionDefaultFallback(Action):

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "Nažalost, nisam u mogućnosti da Vam odgovorim na ovo pitanje. Molim Vas da kontaktirate studentski servis na adresi: studije@singidunum.ac.rs")
        return [ConversationPaused(), UserUtteranceReverted()]