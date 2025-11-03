import boa 
from script.deploy import deploy, INITIAL_SUPPLY 

RANDOM_USER = boa.env.generate_address("non-owner")

def test_token_supply():
    # ALERT Change to fixture 
    snek_token = deploy()
    assert snek_token.totalSupply() == INITIAL_SUPPLY

def test_token_emits_event():
    # Change to fixture 
    snek_token = deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer(RANDOM_USER, INITIAL_SUPPLY)
        logs = snek_token.get_logs()
        log_owner = logs[0].sender 
        assert log_owner == snek_token.owner()
    assert snek_token.balanceOf(RANDOM_USER) == INITIAL_SUPPLY
