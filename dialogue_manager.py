# import modules
import random
import pygame
from dialogue_data import dialogues

# set max story stage
max_story_stage = 4


# Determine whether to advance story stage
# in the game loop, call this and if true increase customer.story_stage += 1
def should_advance_story_stage(customer):
    friendship_points = customer.friendship
    if customer.story_stage == 0:
        return True
    elif customer.story_stage == 1 and friendship_points >= 2:
        return True
    elif customer.story_stage  == 2 and friendship_points >= 10:
        return True
    elif customer.story_stage  == 3 and friendship_points >= 20:
        return True
    elif customer.story_stage  == 4 and friendship_points >= 28:
        return False
    else:
        return False

# Determine visit type
def choose_visit_type(customer):
    if customer.story_stage < max_story_stage:
        chance_of_progression = 0.75
    elif customer.story_stage == max_story_stage:
        chance_of_progression = 0
    visit_type = random.choices(
        ["regular", "progression"],
        [1-chance_of_progression, chance_of_progression]
    )
    return visit_type[0]

# Dialogue retrieval functions
def get_order_dialogue(customer, order):
    chosen_frosting=order.frosting #retrieve characteristics of order
    chosen_sprinkles=order.sprinkles

    customer_dialogue_data = dialogues[customer.name] # get all of the character's possible dialouges

    orders = customer_dialogue_data["Orders"] # get the character's order and reaction dialogues
    reactions = customer_dialogue_data["Order Reactions"]

    selected_order_dialogue = []

    if chosen_sprinkles is None:
        selected_lines = orders["frosting_only"]
    else:
        selected_lines = orders["frosting_and_sprinkles"]
    
    for line in selected_lines:
        filled_in_line = str(line).format(frosting=chosen_frosting, sprinkles=chosen_sprinkles)
        selected_order_dialogue.append(filled_in_line)
                                                
    return selected_order_dialogue

def get_reaction_dialogue(customer, order_result):
    customer_dialogue_data = dialogues[customer.name]
    reactions = customer_dialogue_data["Order Reactions"]
    if order_result == "success":
        selected_reaction_dialogue = reactions["success_reaction"]
    elif order_result == "failure":
        selected_reaction_dialogue = reactions["fail_reaction"]
    return  selected_reaction_dialogue


def get_progression_dialogue(customer):
    stage_dialogue = dialogues[customer.name][str(customer.story_stage)] # will return a dictionary
    return stage_dialogue


class DialogueManager:
    def __init__(self):
        self.current_stage_node = None #tracks the part of the dialogue dictionary for this stage
        self.current_phase= None #tracks stage of conversation
        
        self.current_lines = [] 
        self.page_index = 0

        self.showing_choices = False
        self.response_rects = []

        self.phase_index =0


    def start_dialogue(self, customer):
        if customer.name not in dialogues:
             print(f"No dialogue written for {customer.name}")
             return
        else:
            self.current_stage_node = dialogues[customer.name][str(customer.story_stage)] # retrieve section of dialogue dictionary for this stage
            self.current_phase = "text"
            self.load_phase()

    def load_phase(self):
        phase_data = self.current_stage_node[self.current_phase]

        if self.current_phase == "text":
            self.current_lines = phase_data
            self.showing_choices = False

        elif self.current_phase in ["trait_prompt", "prompt"]:
            self.current_lines = phase_data
            self.showing_choices = True
            self.create_response_rects()

        elif self.current_phase in ["trait_responses", "responses"]:
            self.showing_choices = False

        elif self.current_phase == "reactions":
            self.load_reaction()

    def advance_phase(self):
        phases = ["text", "trait_prompt", "trait_responses", "prompt", "responses", "reactions"]
        while self.phase_index < len(phases) -1:
            self.phase_index +=1
            self.current_phase = phases[self.phase_index]

            phase_data =self.current_stage_node[self.current_phase]
            if phase_data:
                self.load_phase()
                self.page_index = 0
                break

    def create_response_rects(self):
        self.response_rects = []
        self.response_rects.clear()

        if self.current_phase == "trait_prompt":
            responses = self.current_stage_node["trait_responses"]
        elif self.current_phase == "prompt":
            responses = self.current_stage_node["responses"]
        else:
            return
    
        y=250
        for key, text in responses.items(): #return tuples of diciontary keys and values
            rect = pygame.Rect(220, y, 450, 30)
            self.response_rects.append((rect, key, text))
            y+=20
        return self.response_rects
        

    def choose_response(self, choice_key): #takes in choice and stores which dialogue they chose
        self.choice = choice_key

        if self.current_phase == "trait_prompt":
            self.current_phase = "trait_responses"

        elif self.current_phase == "prompt":
            self.current_phase = "responses"

        self.showing_choices = False

    def load_reaction(self):
        reaction_key = "reaction" + self.choice
        self.current_lines = self.current_stage_node["reactions"][reaction_key]
        self.page_index = 0
        self.showing_choices = False

    def get_current_page(self):
        start = self.page_index
        end = start + 4
        return self.current_lines[start:end]
