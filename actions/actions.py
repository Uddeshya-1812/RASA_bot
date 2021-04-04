# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted,FollowupAction


class ActionAfterOrderCompletion(Action):
    def name(self) -> Text:
        return 'action_reservation'

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        seat = tracker.get_slot('seat_number')
        if tracker.get_slot("air_condition") is None:
            ac_status = tracker.get_slot('non_aircondition')
        else:
            ac_status = tracker.get_slot('air_condition')
        time = tracker.get_slot('time')
        _, time = tracker.get_slot('time').split('T')
        hour = int(time[:2])
        if 19 <= hour < 22:
            time = time.split('.')[0]
            dispatcher.utter_message(template="utter_book_info",
                                 seats=seat,
                                 ac_status=ac_status,
                                 booking_time = time
                                 )
            return []
        else: 
            dispatcher.utter_message(text="We are not open at that time. We are only open from 7pm to 10pm \nWhen would you like to book a reservation? (We are only open from 7pm to 10pm)")       
            UserUtteranceReverted()
            FollowupAction('action_reservation')
            return []