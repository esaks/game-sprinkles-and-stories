# Resource John Elder's Build Games wiht Python and Pygame Playlist on Youtube

# import pygame
import pygame
import os
import random

# Set directory
direct = os.path.dirname(os.path.abspath(__file__))
os.chdir(direct)

# Setup
pygame.init() # initialize
window_width = 900
window_height = 500
screen=pygame.display.set_mode((window_width, window_height)) # set screen size for the game
pygame.display.set_caption("Bakery Game")
clock = pygame.time.Clock() # set in-game timer, necessary for tracking what happens in the game
running = True # means the game is running

# Set background music
pygame.mixer.music.load("sounds and music/rubyzephyr-sun-through-open-windows-v1-450763.mp3")
pygame.mixer.music.set_volume(0.25) # set vol
pygame.mixer.music.play(-1) #loop indefinitely
# Other cafe sounds

# SOUND EFFECTS 
bread_box_sound = pygame.mixer.Sound("sounds and music/freesound_community-plastic-box-open-close-1-63477.mp3")
frosting_sound = pygame.mixer.Sound('sounds and music/freesound_community-cream-spray-67023.mp3')
frosting_sound.set_volume(0.25)
sprinkles_sound = pygame.mixer.Sound('sounds and music/spinopel-shake-rattle-492020.mp3')
correct_order_sound = pygame.mixer.Sound('sounds and music/freesound_gamestudio-purchase-success-384963.mp3')
correct_order_sound.set_volume(0.25)
trait_unlock_sound = pygame.mixer.Sound('sounds and music/vadim_makes_sound-achievement-badge-pop-sound-1-547860.mp3')


# Will want to adjust background, maybe window showing the cafe, wallpaper

# Will want to create a menu and instructions

# Set background image
raw_cafe_bg = pygame.image.load('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Cafe Backgrounds_021325/Cafe_Interior.jpg')
cafe_bg = pygame.transform.scale(raw_cafe_bg, (window_width, window_height)) #width,height
cafe_bg_rect = cafe_bg.get_rect() 
cafe_bg_rect.topleft = (0,0)

# Create helper function for loading in images
def img_load_with_scale(img_path, scale_factor): # input string path and int scale factor
    raw_img = pygame.image.load(img_path).convert_alpha() 
    transformed_img = pygame.transform.scale_by(raw_img, scale_factor)
    rect_obj = transformed_img.get_rect()
    return transformed_img, rect_obj # return a tuple of the img and its rect

# Load in images that will be in the background
# Counter
counter, counter_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Background/counter.png', .5)
counter_rect.bottomleft = (0, 500) 
# Stove
stove, stove_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Counter/stove.png', .5)
stove_rect.bottomleft = (700, 500)
# Bread box
bread_box, bread_box_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Counter/basket_1.png', .5)
bread_box_rect.bottomleft = (550, 450)
# Cupcake stand
cupcake_stand, cupcake_stand_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/cheese_stand.png', .5)
cupcake_stand_rect.bottomleft = (480, 420)
# Bowls
bowls, bowls_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/bowls.png', .5)
bowls_rect.bottomleft = (100, 410)
# Sugar 
sugar, sugar_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Counter/sugar_bowl.png', .5)
sugar_rect.bottomleft = (650, 470)
# Flowers
flowers, flowers_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/bottom_flowers.png', .5)
flowers_rect.bottomleft = (15, 430)
# Butter (made up of three images together)
class ButterDish:
    def __init__(self):
        self.butter_base, self.butter_base_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/butter_base.png', .5)
        self.butter, self.butter_rect =  img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/butter.png', .5)
        self.butter_glass, self.butter_glass_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/butter_glass.png', .5)
    
        self.butter_base_rect.bottomleft = (80, 450)
        self.butter_rect.bottomleft = (90, 440)
        self.butter_glass_rect.bottomleft = (80, 440)

    def draw(self):
        screen.blit(self.butter_base, self.butter_base_rect)
        screen.blit(self.butter, self.butter_rect)
        screen.blit(self.butter_glass, self.butter_glass_rect)
butterdish = ButterDish()

# Clickable ingredients
# helper tinting function
def tint_image(img, color):
    tinted = img.copy()
    tinted.fill(color, special_flags=pygame.BLEND_RGBA_MULT) #pygame.BLEND_RGBA_MULT) tells it to tint
    return tinted

# frosting bowl class and class objects
class FrostingBowl():
    def __init__(self, bowl_img, frosting_img, pos, color):
        self.bowl, self.bowl_rect = img_load_with_scale(bowl_img, .3)
        self.frosting, self.frosting_rect = img_load_with_scale(frosting_img, .3)# for personal/commercial use from https://anj0la.itch.io/sweet-treats-and-ingredients-bundle
        self.bowl_rect.midbottom = pos
        self.frosting_rect.center = self.bowl_rect.midtop #make it so the frosting sits on top of bowl
        self.color = color
    def draw(self):
        screen.blit(self.frosting, self.frosting_rect)
        screen.blit(self.bowl, self.bowl_rect)

white_frosting_bowl = FrostingBowl(
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/blueberry_bowl.png',
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/assets/sweets/vanilla_cupcake.png',
    pos = (620, 470),
    color= "white"
)

blue_frosting_bowl = FrostingBowl(
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/blueberry_bowl.png',
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/assets/sweets/vanilla_cupcake.png',
    pos = (580, 465),
    color = "blue"
)
blue_frosting_bowl.frosting = tint_image(blue_frosting_bowl.frosting, color="slategray2")

pink_frosting_bowl = FrostingBowl(
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/blueberry_bowl.png',
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/assets/sweets/vanilla_cupcake.png',
    pos = (540, 460),
    color="pink"
)
pink_frosting_bowl.frosting = tint_image(pink_frosting_bowl.frosting, color="palevioletred2")

brown_frosting_bowl = FrostingBowl(
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Shelf/blueberry_bowl.png',
    '/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/assets/sweets/vanilla_cupcake.png',
    pos = (500, 455),
    color="brown"
)
brown_frosting_bowl.frosting = tint_image(brown_frosting_bowl.frosting, color="burlywood4")
frosting_bowls =[
    white_frosting_bowl,
    blue_frosting_bowl,
    pink_frosting_bowl,
    brown_frosting_bowl
]

# Sprinkle shakers
white_sprinkle_shaker, white_sprinkle_shaker_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Counter/salt.png', .5)
white_sprinkle_shaker_rect.bottomleft = (40, 470)

blue_sprinkle_shaker, blue_sprinkle_shaker_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Counter/salt.png', .5)
blue_sprinkle_shaker_rect.bottomleft = (80, 470)
blue_sprinkle_shaker = tint_image(blue_sprinkle_shaker, color="slategray2")

pink_sprinkle_shaker, pink_sprinkle_shaker_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Counter/salt.png', .5)
pink_sprinkle_shaker_rect.bottomleft = (120, 470)
pink_sprinkle_shaker = tint_image(pink_sprinkle_shaker, color="palevioletred2")

brown_sprinkle_shaker, brown_sprinkle_shaker_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/Possible images from itch.io/Sprites/Sprites/Environment/Counter/salt.png', .5)
brown_sprinkle_shaker_rect.bottomleft = (160, 470)
brown_sprinkle_shaker = tint_image(brown_sprinkle_shaker, color="burlywood4")

# Create BakingCupcake class for the cupcake that players will decorate
# Load frosting images
white_frosting_img, white_frosting_rect = img_load_with_scale("frosting_white.png", .5)
blue_frosting_img, blue_frosting_rect = img_load_with_scale("frosting_blue.png", .5)
pink_frosting_img, pink_frosting_rect = img_load_with_scale("frosting_pink.png", .5)
brown_frosting_img, brown_frosting_rect = img_load_with_scale("frosting_brown.png", .5)
frostings = {
    "white" : white_frosting_img,
    "blue": blue_frosting_img,
    "pink": pink_frosting_img,
    "brown": brown_frosting_img
}
# Load sprinkles images
white_sprinkles_img, white_sprinkles_rect = img_load_with_scale("sprinkles_white.png", .25)
blue_sprinkles_img, blue_sprinkles_rect = img_load_with_scale("sprinkles_blue.png", .25)
blue_sprinkles_img.set_colorkey((255, 255, 255)) # make pure white transparent
pink_sprinkles_img, pink_sprinkles_rect = img_load_with_scale("sprinkles_pink.png", .25)
pink_sprinkles_img.set_colorkey((255, 255, 255))
brown_sprinkles_img, brown_sprinkles_rect = img_load_with_scale("sprinkles_brown.png", .25)
brown_sprinkles_img.set_colorkey((255, 255, 255))
sprinkles_options = {
    "white": white_sprinkles_img,
    "blue": blue_sprinkles_img,
    "pink": pink_sprinkles_img,
    "brown": brown_sprinkles_img
}
class BakingCupcake(): 
    def __init__(self, frosting=None, sprinkles=None):
        self.cupcake, self.cupcake_rect = img_load_with_scale('/Users/emily/Personal programming projects/pygame bakery game/muffin_edited.png', .5) # edited original image to have a blue wrapper
        self.cupcake_rect.bottomleft = (300, 450 ) #position
        # Visual features
        self.frosting = frosting
        self.sprinkles = sprinkles
    def draw(self):
        screen.blit(self.cupcake, self.cupcake_rect) #draw the plain muffin
        if self.frosting: #if player clicked on a frosting bowl
            frosting_img = frostings[self.frosting] #get correct colored image
            frosting_rect = frosting_img.get_rect() 
            frosting_rect.midbottom = (self.cupcake_rect.centerx, self.cupcake_rect.top + 40) #position relative to cupcake
            screen.blit(frosting_img, frosting_rect) 
        if self.sprinkles:
            sprinkles_img = sprinkles_options[self.sprinkles] 
            sprinkles_rect = sprinkles_img.get_rect() 
            sprinkles_rect.midbottom = (self.cupcake_rect.centerx, self.cupcake_rect.top + 20) 
            screen.blit(sprinkles_img, sprinkles_rect) 

# Create general cupcake object
class CupcakeObj():
    def __init__(self, frosting=None, sprinkles=None):
        self.frosting = frosting
        self.sprinkles = sprinkles
    def __eq__(self,other): #override the equality operator, checks if cupcakes have the same components
        if self.frosting == other.frosting and self.sprinkles == other.sprinkles:
            return True
        else:
            return False

# Create customer class
class Customer:
    def __init__(self, name, sprite, scale_fac, fav_frosting, fav_sprinkles, traits, spawn_weight):
        self.name = name
        self.sprite = sprite

        self.img, self.img_rect = img_load_with_scale(sprite, scale_fac)
        self.img_rect.bottomleft = (20, 600) #position

        self.visits = 0
        self.friendship = 0
        self.story_stage = 0
        self.spawn_weight = spawn_weight

        self.order = None

        self.favorite_cupcake = CupcakeObj(frosting=fav_frosting, sprinkles=fav_sprinkles)
        self.traits = traits
    def draw(self):
        screen.blit(self.img, self.img_rect)

# Customer spawner
customer_templates = [
    {"name": "Zoe", "sprite": "Possible images from itch.io/Budget-Characters/16f.png", "scale_fac": 0.2,  "fav_frosting": "white", "fav_sprinkles": "blue", "traits": ["neurotic","extroverted"], "spawn_weight": .10},
    {"name": "Marcus", "sprite": "Possible images from itch.io/Budget-Characters/16m.png", "scale_fac": 0.2,  "fav_frosting": "brown", "fav_sprinkles": "brown", "traits": ["introverted", "awkward"], "spawn_weight": .10},
    {"name": "Justin", "sprite": "Possible images from itch.io/Budget-Characters/16mb.png", "scale_fac": 0.2, "fav_frosting": "brown", "fav_sprinkles": "blue", "traits": ["relaxed", "cool"], "spawn_weight": .10},
    {"name": "Crystal", "sprite": "Possible images from itch.io/Budget-Characters/19fb.png", "scale_fac": 0.2,  "fav_frosting": "blue", "fav_sprinkles": "pink", "traits": ["cool", "closed"], "spawn_weight": .10},
    {"name": "Michael", "sprite": "Possible images from itch.io/Budget-Characters/19m.png", "scale_fac": 0.2,  "fav_frosting": "blue", "fav_sprinkles": "None", "traits": ["introverted", "sensitive"], "spawn_weight": .10},
    {"name": "Samantha", "sprite": "Possible images from itch.io/Budget-Characters/22f.png", "scale_fac": 0.2,  "fav_frosting": "white", "fav_sprinkles": "pink", "traits": ["relaxed", "sensitive"], "spawn_weight": .10},
    {"name": "Ted", "sprite": "Possible images from itch.io/Budget-Characters/22m.png", "scale_fac": 0.2,  "fav_frosting": "white", "fav_sprinkles": "brown", "traits":["blunt", "awkward"], "spawn_weight": .10},
    {"name": "Joyce", "sprite": "Possible images from itch.io/Budget-Characters/banker-f.png", "scale_fac": 0.2,  "fav_frosting": "pink", "fav_sprinkles": "white", "traits":["sensitive", "open"], "spawn_weight": .10},
    {"name": "Arthur", "sprite": "Possible images from itch.io/Budget-Characters/banker-m.png", "scale_fac": 0.2,  "fav_frosting": "white", "fav_sprinkles": None, "traits": ["extroverted", "open"], "spawn_weight": .10},
    {"name": "Diana", "sprite": "Possible images from itch.io/Budget-Characters/mom.png", "scale_fac": 0.2,  "fav_frosting": "pink", "fav_sprinkles": None, "traits":["blunt", "open"], "spawn_weight": .10}
]
# Traits explained:
# Introversion vs. extroversion controls how talkative the customer is and somewhat energy/cheerfulness
# Open vs. closed controls how much they open up about themselves, curiosity
# Relaxed vs. neurotic controls how much they appear to be relaxed or more of a worrying type
# Cool vs. awkward determines their interactional style, either being smooth and self confident, or speaking awkwardly
# Sensitive vs. blunt is whether they tend to communicate with high emotional sensitivity or very directly

# Create versions of the customers for each game so that their stats carry over each time they appear
customers = []
for template in customer_templates:
    customers.append(Customer(**template)) #take the template arguments and pass them into customer for their initial versions

# Select customer
def enter_customer():
    current_weights = []
    return customers[0]
    #FOR TEST ONLY ZOE
    # for customer in customers:
    #     current_weights.append(customer.spawn_weight)
    # return random.choices(
    #     customers,
    #     weights = current_weights,
    #     k=1
    # )[0]

# Set max story stage
max_story_stage = 4
    
# ORDER SYSTEM
# Create function to randomly generate order combinations
def generate_order():
    frostings = ["white", "blue", "pink", "brown"]
    sprinkles = [None, "white", "blue", "pink", "brown"]
    return CupcakeObj(frosting= random.choice(frostings), sprinkles=random.choice(sprinkles))

# Create regular dialogue box
reg_dialogue_box = pygame.Rect(220,150,420,60) #surface, color, (x coordinate of top left corner, y coordinate of top left corner, width,height)
# print(pygame.font.get_fonts())

# Create dialogue box for longer progression interactions
prog_dialogue_box = pygame.Rect(220,150,450,100) #surface, color, (x coordinate of top left corner, y coordinate of top left corner, width,height)


# fonts
dialogue_font = pygame.font.SysFont('applegothic', 16) 
responses_font = pygame.font.SysFont('applegothic', 14) 

# import dialogue_data and dialogue_manager
from dialogue_data import dialogues
import dialogue_manager


    
# Further dialogue/story arcs
#Information:
#Zoe: Age: teen, Arc: School dance is coming up, but wonders if she is atypical for having no one to go with. MC provides emotional reassurance that soothes her neuroticism. End: She takes a step toward accepting that her trajectory unfolds at its own pace. 
#Marcus: Age: teen, Arc: Because he is shy/awkward, he is worried about socially transitioning to college. He learns to feel more optimistic about his chance of making friends. End: Joined clubs, took a few semesters, but made at least 2 good friends
#Justin: Age: teen, Arc: Wants to play baseball, but his parents don't think it's a stable career choice. He learns to find a middle ground. End: Continues playing on the high school team, doing trainings, applying to colleges that have semi-competitive teams and strong computer science departments
#Crystal: Age: college, Arc: Acts like everything is fine, but reveals that she's finding it hard to balance everything in college: getting good grades, taking care of herself and having a social life. Slowly learns strategies, trial and error, learning to prioritize her health through her classes. End: Joins a support group, improved happiness next semester
#Michael: Age: college, Arc: Worried about choosing a major stuck between music and math and whats more practical. End: Engages in both and learns that the college major is not the end all be all
#Samantha: Age: 20s, Arc: Works at a local store, but her boss is often really rude to her and she doesn't know how to handle it. Learns about HR policies and brings it up responsibly. End: Her boss is reprimanded but nothign changes, but she believes in herself enough to apply for other jobs and goes somewhere better
#Ted: Age: 30s, Arc: Feeling depressed about his love life from dating apps. Takes a break, adopts a new perspective, shits to in person events. End: Eventually ends up meeting a great girl in real life at a hockey game
#Joyce: Age: 40s, Arc: Teaches English at the local university but frustrated with student behavior (cheating, AI, not coming to class). Attends events/learns strategies. End: Keeps teaching and adjusts syllabi
#Arthur: Age: 60s, Arc: Recently retired and unsure what to do with himself and his wife says he should do something. Worried about doing something new at his age but auditions for a local choicr and enjoys it. End: Happily singing
#Diana: Age: 50s, Arc: Typically feels sure, but is currently struggling with how to talk to her two boys about their grandmother dying. Realizes maybe she struggles with this kind of thing, learns to be open wiht her own emotions without putting pressure, leaving space open to talk. End: Some months later, one of her kids did suddenly ask about her mother, and she told him and it felt good.

# Reputation system
bar_x = 850
bar_y = 25
bar_width = 20
bar_height= 150
max_reputation = 100
min_reputation = 0
# box
reputation_box = pygame.Rect(bar_x, bar_y, bar_width, bar_height) 

# text label

# print(pygame.font.get_fonts())
# Ending System


# State tracking variables
active_cupcake = None
active_customer1 = None
is_dragging = False
order_result = None
current_dialogue = None

money_count = 0
reputation= 50

game_state = "waiting" #game states are waiting, ordering, reacting
customer_wait = 0 # initialize at 0 so that each frame, time is added until it reaches the wait_time, before spawning
wait_time = random.uniform(0.5,5) # select time interval before next customer spawns

order_reaction_timer = 0
reaction_duration = 3 



# Main game loop start
while running: #shorthand for while running==TRUE. This is the game loop.

    # Tick the clock at the beginning of the loop
    dt = clock.tick(60)  # limits game to 60 frames per second and returns how many milliseconds passed since the previous frame
    dt_seconds = dt/1000.0 #seconds

    # Pick screen color
    screen.fill((255, 240, 245))

    # Draw background imag
    screen.blit(cafe_bg, cafe_bg_rect)

    # Draw reputation bar
    pygame.draw.rect(screen, "antiquewhite1", reputation_box)
    fill_height = (reputation/max_reputation) * reputation_box.height
    fill_rect = pygame.Rect(
        reputation_box.x, # top left corner x coordinate
        reputation_box.bottom - fill_height, #top left y coordinate
        reputation_box.width -2, # width
        fill_height #height
    )
    pygame.draw.rect(screen, "palevioletred2", fill_rect) # draw fill
    pygame.draw.rect(screen, "burlywood4", reputation_box, width=2) # draw outline
    rep_text = dialogue_font.render("Reputation", True, "saddlebrown") # render text label
    screen.blit(rep_text, (reputation_box.x - 55, reputation_box.y-20))

    # Game State (game states and timers go before deciding what to draw)
    if game_state == "reacting":
        active_cupcake = None # Cupcake has been delivered, so immediately make it disappear
        order_reaction_timer += dt_seconds # add time elapsed each frame
        if order_reaction_timer >= reaction_duration: 
            # After 3 seconds, reset values
            active_customer1 = None 
            order_result = None
            current_dialogue = None

            game_state = "waiting" #update game state. Now dialogue rendering if statements below evaluate to False so no dialogue appears

            order_reaction_timer = 0 # reset reaction timer
            customer_wait = 0 # reset customer timer
            # Sound effect 
            # Money added
            # Relationship stats updated

    
    # Render customer drawing (must be behind the counter visually)
    if active_customer1 is not None: # if there is a customer and order not completed
        active_customer1.draw()


    # Customer spawn/order/dialogue
    if game_state == "waiting":  
        customer_wait += dt_seconds # create random interval between customers
        current_dialogue = None
        if customer_wait >= wait_time:
            active_customer1 = enter_customer() #customer spawns
            
            met_stage_requirement = dialogue_manager.should_advance_story_stage(active_customer1) # determine if customer has the right stats to trigger the next story stage event

            if met_stage_requirement == True:
                current_visit_type = dialogue_manager.choose_visit_type(active_customer1) # determine whether visit is regular or one that progresses the charcter's storyline
                if current_visit_type == "progression":
                     dialogue_tracker = dialogue_manager.DialogueManager()
                     game_state = "progression_event"
                     dialogue_tracker.start_dialogue(active_customer1) 

            elif met_stage_requirement == False:
                current_visit_type = "regular"
                game_state = "ordering"
                active_customer1.order = generate_order()
                current_dialogue = dialogue_manager.get_order_dialogue(active_customer1, active_customer1.order)
            

            wait_time = random.uniform(0.5,5) # set a new random wait_time to reach for the next customer


    # Draw other props in background
    screen.blit(counter, counter_rect)
    screen.blit(stove, stove_rect)
    screen.blit(bread_box, bread_box_rect)
    screen.blit(cupcake_stand, cupcake_stand_rect)
    screen.blit(bowls, bowls_rect)
    screen.blit(flowers, flowers_rect)
    screen.blit(sugar, sugar_rect)

    butterdish.draw()

    screen.blit(brown_sprinkle_shaker, brown_sprinkle_shaker_rect)
    screen.blit(pink_sprinkle_shaker, pink_sprinkle_shaker_rect)
    screen.blit(blue_sprinkle_shaker, blue_sprinkle_shaker_rect)
    screen.blit(white_sprinkle_shaker, white_sprinkle_shaker_rect)

    white_frosting_bowl.draw()
    blue_frosting_bowl.draw()
    pink_frosting_bowl.draw()
    brown_frosting_bowl.draw()

    # Baking loop
    for event in pygame.event.get(): #poll for events, if pygame.QUIT meaning user X'd out of the game, stop the game
        if event.type == pygame.QUIT:
            running = False
        if active_customer1 != None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1: #left click
                    if game_state == "ordering":
                        # BAKING
                        # Clicking ingredients
                        if bread_box_rect.collidepoint(event.pos): # if click on bread box, spawn plain cupcake
                            pygame.mixer.Sound.play(bread_box_sound, maxtime=500) 
                            active_cupcake = BakingCupcake() #generate new cupcake
                        if active_cupcake is not None and order_result is None:
                            # Clicking on frostings
                            for bowl in frosting_bowls:
                                if bowl.bowl_rect.collidepoint(event.pos) or bowl.frosting_rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(frosting_sound, maxtime=200)
                                    active_cupcake.frosting= bowl.color
                            # Clicking on sprinkles
                            if active_cupcake.frosting:
                                if white_sprinkle_shaker_rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(sprinkles_sound, maxtime=200)
                                    active_cupcake.sprinkles = "white"
                                if blue_sprinkle_shaker_rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(sprinkles_sound, maxtime=200)
                                    active_cupcake.sprinkles = "blue"
                                if pink_sprinkle_shaker_rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(sprinkles_sound, maxtime=200)
                                    active_cupcake.sprinkles = "pink"
                                if brown_sprinkle_shaker_rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(sprinkles_sound, maxtime=200)
                                    active_cupcake.sprinkles = "brown"
                        # Click on active cupcake
                            if active_cupcake.cupcake_rect.collidepoint(event.pos): # if player clicks on the active cupcake
                                is_dragging = True

                    # Click through dialogues boxes for progression events
                    if game_state == "progression_event":
                        if prog_dialogue_box.collidepoint(event.pos):
                            if  not dialogue_tracker.showing_choices: #text not prompt
                                if dialogue_tracker.current_phase == "reactions":
                                    game_state = "ordering"
                                    active_customer1.order = generate_order()
                                    current_dialogue = dialogue_manager.get_order_dialogue(active_customer1, active_customer1.order)
                                if dialogue_tracker.page_index + 4 < len(dialogue_tracker.current_lines): # if still dialogue lines left to be read
                                    dialogue_tracker.page_index += 4
                                else:
                                    dialogue_tracker.advance_phase()
                                   
                        if dialogue_tracker.showing_choices:
                            for rect, key, text in dialogue_tracker.response_rects:
                                if rect.collidepoint(event.pos):
                                    dialogue_tracker.choose_response(key)
                                    
            # Click and drag order result
            if event.type == pygame.MOUSEMOTION and is_dragging:
                active_cupcake.cupcake_rect.center = event.pos # imag follows the mouse's position
            if event.type == pygame.MOUSEBUTTONUP: 
                if is_dragging == True:
                    is_dragging = False
                    if active_cupcake.cupcake_rect.colliderect(active_customer1.img_rect):
                        finished_cupcake = CupcakeObj(frosting=active_cupcake.frosting, sprinkles=active_cupcake.sprinkles)
                        if finished_cupcake == active_customer1.order:
                            pygame.mixer.Sound.play(correct_order_sound, maxtime=2000)
                            order_result = "success"
                            game_state = "reacting"
                            order_reaction_timer = 0
                            current_dialogue = dialogue_manager.get_reaction_dialogue(active_customer1, order_result) # update customer's dialogue to now be the appropriate reaction
                            if reputation < max_reputation:
                                reputation += 1
                        else:
                            order_result = "failure"
                            game_state = "reacting" 
                            order_reaction_timer = 0
                            current_dialogue = dialogue_manager.get_reaction_dialogue(active_customer1, order_result)
                            if reputation > min_reputation:
                                reputation -= 1
           
                
    
    # DRAW/RENDER
    if active_cupcake != None: 
        active_cupcake.draw()
    
    if game_state == "ordering" and current_dialogue is not None: 
        pygame.draw.rect(screen, "antiquewhite1", reg_dialogue_box) # draw dialogue box onto surface screen, color antiquwhite
        x=230
        y=160
        for line in current_dialogue:
            surf_text = dialogue_font.render(line, True, "saddlebrown")
            screen.blit(surf_text, (x,y))
            y +=20

    elif game_state == "reacting" and current_dialogue is not None:           
        pygame.draw.rect(screen, "antiquewhite1", reg_dialogue_box) # same dialogue box
        x=230
        y=160
        for line in current_dialogue: # render text line by line from list
            surf_text = dialogue_font.render(line, True, "saddlebrown")
            screen.blit(surf_text, (x,y))
            y +=20

    # Progression event rendering
    if game_state == "progression_event":
        pygame.draw.rect(screen, "antiquewhite1", prog_dialogue_box)
        x=230
        y=160
        for line in dialogue_tracker.get_current_page():
            surf_text = dialogue_font.render(line, True, "saddlebrown")
            screen.blit(surf_text, (x, y))
            y +=20

        if dialogue_tracker.showing_choices == True:
            for rect, key, text in dialogue_tracker.response_rects:
                pygame.draw.rect(screen, "burlywood", rect)
                surf=responses_font.render(text[0], True, "antiquewhite1")
                screen.blit(surf, (rect.x + 10, rect.y + 5))
        
    
    # eventualolyneed to end progression event

    pygame.display.flip() #update display


pygame.quit()