# Create a tree similar to dialogue data which contains information about:
# Friendship points and spawn weights to be applied based on player responses
friendship_values ={
    "Zoe": {
        "0": {
            "responses": {
                "1": 4,
                "2": 2
                },
        },
        "1":{
            "responses": {
                "1": 4,
                "2": 2,
                "3": 0
            },
        },
        "2": {
            "trait_responses": {
                "1": 4,
                "2": 2,
                "3": 0
            },
            "responses": {
                "1": 4,
                "2": 2,
                "3": 0
            },
        },
        "3": {
            "trait_responses": {
                "1": 4,
                "2": 2,
                "3": 0
            },
            "responses": {
                "1": 4,
                "2": 2,
                "3": 0
            },
        },        
        "4": {
            "responses" : {
                "1": 2
            }
        }
    }
}


# Update friendship points
def update_friendship(customer, dialoguemanager):
    choice_key= dialoguemanager.choice
    section = dialoguemanager.current_phase

    current_friendship= customer.friendship
    stage_key = str(customer.story_stage)
    customer_name = customer.name

    adj = friendship_values[customer_name][stage_key][section][choice_key]

    return current_friendship + adj

# Apply spawn weight consequences
def update_spawn_weight(customer, dialoguemanager):
    current_weight = customer.spawn_weight
    stage_key = str(customer.story_stage)

    # Story stage weights
    if stage_key == "1":
        current_weight *= 1.025
    elif stage_key == "2":
        current_weight *= 1.05
    elif stage_key == "3":
        current_weight *= 1.25

    return current_weight

# Trait discovery
def trait_discovered(customer, dialoguemanager):
    choice_key= dialoguemanager.choice
    section = dialoguemanager.current_phase

    response_score = friendship_values[customer.name][customer.story_stage][section][choice_key]

    if section == "trait_responses" and response_score == max(friendship_values[customer.name][customer.story_stage][section]):
        return True
# update traits in profile UI
# update friendship heart sprites in profile UI
#def update_traits(customer, dialoguemanager):

