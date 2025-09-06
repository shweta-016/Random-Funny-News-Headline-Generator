#Step 1-Import Random Module
import random
#step 2-create subject
subjects=[
    "shahrukh khan",
    "Virat kohli",
    "A Mumbai Cat",
    "Nirmala Sitharaman",
    "A group of monkeys",
    "Prime minister Modi",
    "Auto Rikshaw driver from Delhi"
]
actions=[
    'launches',
    'cancels',
    'dances with',
    'eats',
    'declares war on',
    'orders',
    'celebrates'
]
places_or_things=[
    'at red fort',
    'in mumbai local train',
    'a plate of samosa',
    'inside parliment',
    'at ganga ghat',
    'during IPL match',
    'at India Gate'
]
#step 3-start the headline generation loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    places_or_thing=random.choice(places_or_things)
#using formatted string
    headline= f"BREAKING NEWS : {subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input=input("Do you want another headline? yes or no").strip().lower()
    if user_input=='no':
     break
    
#printing goodbye message
print("\nThanks for using this")
