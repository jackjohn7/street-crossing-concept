# library that makes context appropriate calls (Needs organizing and refactoring)

from twilio.rest import Client
from time import sleep
from keys import *

account_sid = get_sid()
auth_token = get_auth()
client = Client(account_sid, auth_token)

#print(call.sid)
rpt = "Repeating once."
   
def make_call(srvc: str , loc):
    
    #getLoc = loc.geocode
    if srvc == "fire":
        msg = f"There is a fire at {loc}. Requesting the fire department."
    elif srvc == "police":
        msg = f"There is an emergency at {loc}, and the police are needed"
    elif srvc == "emt":
        msg = f"EMT is needed at {loc}. Requesting immediate assistance"
    # formats response in TwiML 
    frmt = f'''
    <Response>
        <Pause length="1"/>
        <Say>Guard dog</Say>
        <Pause length="1"/>
        <Say>{msg}</Say>
        <Pause length="1"/>
        <Say>Again</Say>
        <Pause length="1"/>
        <Say>{msg}</Say>
    </Response>
    '''
    tod = get_my_num()
    fromd = get_t_num()
    call = client.calls.create(
        twiml=frmt,
        to=tod,
        from_=fromd
    )
    # prints to confirm that the call has been placed
    print(call.sid)
# test call functions for each of the services
def test_call_fire():
    make_call('fire', 'Louisiana Tech University')

def test_call_pol():
    make_call('police', 'Louisiana Tech University')

def test_call_emt():
    make_call("emt", "Louisiana Tech university")
