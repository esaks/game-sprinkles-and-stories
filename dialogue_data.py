# Friendship Levels: 0 = not met, up to 4 hearts
# Friendship increases through 1) correct cupcake orders 2) dialogue choices 3) learning customer's favorite cupcake which gives extra friendship
# The first time a customer appears, it will trigger Stage 0, the introoduction conversation, followed by a dialogue choice. If player indicates a more open response, it will increase friendship more
# The second time the customer appears, they will start to explain their problem, followed by a dialogue choice. If Mc indicates wanting to know, they will be told more and friendship will increase
# The third time the customer apepars, they will explain what has developed. MC will be asked to make an inference about the customer's hidden trait. Next, they will be able to provide a reaction. If they correctly guessed the trait, they will get a trait discovered message, profile will be updated. This should help them answer the reaction question.
# The fourth time, the customer explains the choice they are debating. MC again is aksed to infer a trait. Then they have to provide an advice option. if they select correclty, friendship increases
# The last time, the customer just tells them what happens, and thanks them for their help.

# Brief calculations
# +1 reputation for a correct order, -1 for incorrect (out of 100)
# Friendship increases: 2 to 36 pts possible from dialogue, +2 for correct order, (possible: extra +3 for the favorite cupcake)
# Friendship level/hearts: With 36 points max, 1 heart =12 points
# The second time someone visits, player chooses whether to invest in them or not. If they do, their weighted probability goes to 20%
# For the last ~30 rounds, the weighted probabilities are in play
    # If they focus on no characters probabilities remain equal
    # EAch person they chose will be weighted 20% so they will see them on average 6 times in the last 30 rounds
    # 3 of those times will be stage dialogue 2-4. The other times will be "regular" interactions.
    # Once friendship level is hit, it will be the stage dialogue. if not, regular.
    # Need to make it so the regular interactions get them about halfway to the next unlock


# Story stage - automatically advance unless MC fails stage 1, but unlock based on friendship
# Stage 0 - initial introduction - MC is more/less open (Friendship +2 or +4, Order +0 or +2)
# Stage 1 - introduce conflict - MC indicates they want to know more/or more netural (Friendship 0, or 4, Order +0 or +2) - if MC chooses no, relationship does not progress 
# At this point customer has visited about 2 in 20 rounds so that would be 2 successful visits (+0,2,4) plus (+2,4,8) friendship points from dialogue
# Stage 2 - conflict develops - chance to learn trait - MC provides reaction (Friendship +0,2,4, Order +(0,2)) (unlocks at 12 friendship immediately)
# Stage 3 - climax - chance to learn trait - MC provides advice (Friendship +0,2,4, Order +0,2) plus  (unlocks at 20 friendship, need 1 regular order min)
# Stage 4 - resolution - (Friendship +4 for reaching automatically, Order +(0,2)) (unlocks at 30 friendship, need 2 regular orders min)
# End max friendship 36
# Min visits to complete 8, or  6 in the last 30 rounds

# Endings 
# If reputation > 80
    # Default: "Successful Baker" - You've done a good job with the bakery.
    # If they got at least one character to 20 points -> "Chosen Confidant" - The bakery is a success and at least one person in town counts you among their close friends.
    # If they get more than two characters to 20 points -> "Putting Down Roots" - The bakery is a success and your friends in town hope you're here to stay.
    # If they get 3 characters to 20 points -> "Rising Star" - You've proven yourself — as a baker and as a friend.
# If reputation between 50 and 80
    # Default: "Up-and-coming Baker" - The bakery is doing well enough.
    # If they got at least one character to 16 points -> "Newcomer" - The bakery is doing well and you've made at least one friend.
    # If they got at least one character to 20 points -> "Friend to One" - The bakery is doing well, and someone in town counts you among their good friends.
    # If they get more than two characters to 20 points -> "Reliable Friend" - The bakery is doing well, and people in town really seem to appreciate that you've taken the time to get to know them.
# If reputation below 50
    # If they got at least one character to 16 points -> "Amateur" - The bakery's reputation could be better, but at least you've made a friend in town.
    # If they didn't -> "Struggling Baker" - You might not be able to run this business much longer without making some kind of change.

# Later refinemenets
# Decide about discovering fav cupcake and make it so it gives extra points
# Make it harder to advance for closed characters
# Make weighting increase on subsequent interactions

# Dialogue tree
dialogues ={
    "Zoe": {
        "Orders": {
            "frosting_and_sprinkles" : ["I'd like a cupcake with {frosting} frosting and {sprinkles} ",
                        "sprinkles."],
            "frosting_only": ["This time I'd like a cupcake with {frosting} frosting."]
        },
        "Order Reactions": {
            "success_reaction" : ["Yay, thanks!"],
            "fail_reaction" : ["Um, are you sure you got that right?"]
        },
        "0": {
            "text": ["Hi! I don't think we've met yet. This is a cute place! ",
                     "I'm Zoe. I love cupcakes, so I'm glad there's a new bakery  ",
                     "in town. Ugh, it's so hard to decide! ",
                     "Why am I like this?"],
            "trait_prompt": {},
            "trait_responses": {},
            "prompt": ["Anyway, I'm glad I stopped in."],
            "responses": {
                "1": ["I'm glad you wandered in today, too."],
                "2": ["Mm."],
            },
            "reactions": {
                "reaction1": ["Thanks!"],
                "reaction2": ["..."]
            }
        },
        "1":{
            "text": {},
            "trait_prompt": {},
            "trait_responses": {},
            "prompt": ["Hi, again! I could really use something sweet. ",
                     "My mom's taking me to go dress shopping this weekend for the school ",
                     "dance. There are some styles I have in mind, but I'm stuck between like ",
                     "four options. I'm nervous because it's the first dance I've been to. ",
                     "Maybe there's nothing to be nervous about...Sorry, am I talking too much? ",
                     "You probably just want to take my order."],
            "responses": {
                "1": ["Not at all. That sounds exciting and being nervous is pretty normal. "],
                "2": ["Don't worry about it."],
                "3": ["Yeah, actually...just let me know when you want to order."]
            },
            "reactions": {
                "reaction1": ["Thanks! Yeah, I guess it is pretty normal. "],
                "reaction2": ["Thanks."],
                "reaction3": ["...Okay."]
            }
        },
        "2": {
            "text": ["Hi! I'm excited for another of your cupcakes. ",
                     "At school today, I saw someone give a really elaborate proposal ",
                     "inviting their date to the dance. It made me think... ",
                     "I mean it would be scary to have everyone looking at you like that, ",
                     "but at the same time, I think it's sweet."],
            "trait_prompt": ["Hm, so far, I get the sense that Zoe is..."],
            "trait_responses": {
                "1": "extroverted",
                "2": "awkward",
                "3": "closed"
            },
            "prompt": ["Do you think it's weird that I'm going to the dance alone?"],
            "responses": {
                "1": ["I don't think that's weird. Lots of people aren't in relationships ",
                      "and you can still have a good time at the dance."],
                "2": ["Not really."],
                "3": ["It's a little weird."]
            },
            "reactions" : {
                "reaction1": ["You're right! I can definitely still have a good time."],
                "reaction2": ["Yeah, you're right. It's not that weird..."],
                "reaction3": ["Oh..."]
            }
        },
        "3": {
            "text": ["I'm back! You know, the dance is next week. I know I'll still have fun ",
                     "going alone and everything...but I'm realizing how everyone will have ",
                     "their couple photos before and there will be those slow dances where ",
                     "everyone watches from the sidelines or they try to mimic it with their friends ",
                     "even though it doesn't really feel the same. Maybe it's not even about the dance. ",
                     "Maybe it's just that I wonder if that kind of connection will ever happen for me."],
            "trait_prompt": ["Hm, so far, I get the sense that Zoe is..."],
            "trait_responses": {
                "1": ["neurotic"],
                "2": ["curious"],
                "3": ["cool"]
            },
            "prompt": ["I lot of people in my grade are in relationships. It makes me think I'm... ",
                       "behind, or something."],
            "responses": {
                "1": ["I understand that. But things happen for different people at different times. ",
                      "The number of relationships you have now doesn't say anything about the kinds ",
                      "of relationships you'll have in the future. And I think someone like you who seems "
                      "to really care about forming those connections actually has a good chance of meeting "
                      "someone who wants that with you, too."],
                "2": ["It'll happen. You've got years ahead of you."],
                "3": ["It'll happen or it won't. Relationships aren't all they're cracked up to be anyway."]
            },
            "reactions" : {
                "reaction1": ["Thanks, that means a lot! And you're right. Things happen at different times. ",
                              "Besides, I don't want to rush to get into a relationship with someone ",
                              "I don't actually like just because it will make me feel more like everyone "
                              "else."],
                "reaction2": ["Yeah, I guess there's still time..."],
                "reaction3": ["Maybe..."]
            },
        },        
        "4": {
            "text": ["Hi! I just wanted to let you know how the dance went. To be honest, ",
                     "There were awkward moments and moments I wished I was there with someone. ",
                     "But, it was still fun to get dressed up in the dress I picked out with my ",
                     "mom. My friends and I took pictures together and they played good songs. ",
                     "I'm glad I went. If I had listened to my insecurities, maybe I wouldn't ",
                     "have. So, thanks for encouraging me."],
            "trait_prompt": {},
            "trait_responses": {},
            "prompt": {},
            "responses": {},
            "reactions": ["I think this calls for a celebratory cupcake!"]
        }
    }
}