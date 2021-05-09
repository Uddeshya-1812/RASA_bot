# Objective - 
Simple chatbot for a restaurant.
following basic functionalities are handled by the bot
- Make a Reservation
- Handle FAQs

# Installation

`python 3.6` is recommended for use with Rasa!

# Flows
## Book Reservation

### Sample Flows

**Flow 1: Booking an AC room at an allowed time**

<ins>Step 1</ins>

User: I want to reserve a table

Bot: How many seats would you like to reserve

<ins>Step 2</ins>

User: 2 seats

Bot: Which section would you like to book
- AC
- Non-AC

<ins>Step 3</ins>

User: (Clicks on Button 1)

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

<ins>Step 4</ins> (Assuminig conversation time is 7:10pm)

User: In half an hour

Bot: You have reserved 2 seats in our AC section for 7:30pm. Thanks!

---

**Flow 2: Booking a Non-AC room at a disallowed time**

<ins>Step 1+2</ins>

User: I want to reserve a table for a party of 4

Bot: Which section would you like to book
- AC
- Non-AC

<ins>Step 3</ins>

User: (Clicks on Button 2)

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

<ins>Step 4</ins> (Assuminig conversation time is 5pm)

User: In half an hour

Bot: We are not open at that time. We are only open from 7pm to 10pm

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

User: 7:30 pm

Bot: You have reserved 4 seats in our Non-AC section for 7:30pm. Thanks!


## FAQs
```
User: What are your timings?
Bot: The restaurant opens at 7pm and closes at 10pm.

User: What days are you open?
Bot: The restaurant is open each and every day.

User: How do I cancel a reservation?
Bot: To cancel a reservation, simply call us at [helpline number]  and cancel your reservation

User: What are the specials?
Bot: Our chef is a master of the Italian cuisine. Our core speciality is our pasta, which is renowned throughout the city.
```
**Sample Flow**

User: I want to reserve a table for 4

Bot: Which section would you like to book

- AC
- Non-AC

User: (Clicks on Button 1)

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

User: Are you open today?

Bot: The restaurant is open each and every day.

Bot: When would you like to book a reservation? (We are only open from 7pm to 10pm)

User: At 8pm

Bot: You have reserved 4 seats in our AC section for 8pm. Thanks!

 
## How it works
Following Servers required to run while application proceeds -

* Rasa Server
* Rasa Action Server
* DucklingHTTPExtractor 

Please Configure DucklingHTTPExtractor Using this link: https://medium.com/@adboio/using-duckling-to-extract-dates-and-times-in-your-rasa-chatbot-7687f4fde2e0

