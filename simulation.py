# Run simulations to see how likely players are to complete the game
import random
import pandas as pd
customers = ["Zoe", "Marcus", "Justin", "Crystal", "Michael", "Samantha", "Ted", "Joyce", "Arthur", "Diana"]
data = []
friendship_advancement_criteria = [2,10,20,28]
for game in range (1000): 
    weights = [.10] * len(customers)
    friendship = [0] *len(customers)
    visits = [0] *len(customers)
    rel_stages = [0] *len(customers)
    for round in range(50):
        #print("weights are", weights)
        selected_customer = random.choices(
            customers,
            weights,
            k= 1)[0]
       
        selected_cust_idx = customers.index(selected_customer)
        selected_cust_current_stage = rel_stages[selected_cust_idx]
        selected_visit = random.choices(
            ["regular", "progression"],
            weights=[.25, .75],
            k=1
        )[0]
        if selected_visit == "regular":
            order_correctness = random.choice([0,2])
            friendship[selected_cust_idx] += order_correctness
            visits[selected_cust_idx] += 1
        elif selected_visit == "progression":
            order_correctness = random.choice([0,2]) # if progression visits have both ordering and dialogue
            answer_correctness = random.choice([0,2,4])
            friendship[selected_cust_idx] += order_correctness + answer_correctness
            visits[selected_cust_idx] += 1
            if selected_cust_current_stage < len(friendship_advancement_criteria):
                if friendship[selected_cust_idx] >= friendship_advancement_criteria[selected_cust_current_stage]:
                    rel_stages[selected_cust_idx] += 1
                    if selected_cust_current_stage == 1:
                        weights[selected_cust_idx] *= 1.025
                    if selected_cust_current_stage == 2:
                        weights[selected_cust_idx] *= 1.05
                    if selected_cust_current_stage == 3:
                        weights[selected_cust_idx] *= 1.25
            if answer_correctness == 2:
                weights[selected_cust_idx] *= 1.10
            elif answer_correctness == 4:
                weights[selected_cust_idx] *= 1.20

   
    completed_characters = sum(stage == 4 for stage in rel_stages)

    for i, customer in enumerate(customers):
        data.append({
            "customer": customer,
            "visits": visits[i],
            "friendship": friendship[i],
            "stage": rel_stages[i]
            })


df = pd.DataFrame(data)
print(df.head(50))

print(df["visits"].describe())
print(df["stage"].describe())



# Re-run simulation if player actually maxes a character
# With increasing weights
customers = ["Zoe", "Marcus", "Justin", "Crystal", "Michael", "Samantha", "Ted", "Joyce", "Arthur", "Diana"]
data = []
friendship_advancement_criteria = [2,10,20,28]
for game in range (1000): 
    weights = [.10] * len(customers)
    friendship = [0] *len(customers)
    visits = [0] *len(customers)
    rel_stages = [0] *len(customers)
    for round in range(50):
        #print("weights are", weights)
        selected_customer = random.choices(
            customers,
            weights,
            k= 1)[0]
       
        selected_cust_idx = customers.index(selected_customer)
        selected_cust_current_stage = rel_stages[selected_cust_idx]
        selected_visit = random.choices(
            ["regular", "progression"],
            weights=[.25, .75],
            k=1
        )[0]
        if selected_visit == "regular":
            order_correctness = random.choice([0,2])
            friendship[selected_cust_idx] += order_correctness
            visits[selected_cust_idx] += 1
        elif selected_visit == "progression":
            order_correctness = random.choice([0,2]) # if progression visits have both ordering and dialogue

            if selected_customer == "Zoe":
                answer_correctness = 4
            else:
                answer_correctness = random.choice([0,2,4])
            friendship[selected_cust_idx] += order_correctness + answer_correctness
            visits[selected_cust_idx] += 1
            if selected_cust_current_stage < len(friendship_advancement_criteria):
                if friendship[selected_cust_idx] >= friendship_advancement_criteria[selected_cust_current_stage]:
                    rel_stages[selected_cust_idx] += 1
                    if selected_cust_current_stage == 1:
                        weights[selected_cust_idx] *= 1.025
                    if selected_cust_current_stage == 2:
                        weights[selected_cust_idx] *= 1.05
                    if selected_cust_current_stage == 3:
                        weights[selected_cust_idx] *= 1.25
            if answer_correctness == 2:
                weights[selected_cust_idx] *= 1.10
            elif answer_correctness == 4:
                weights[selected_cust_idx] *= 1.20

   
    completed_characters = sum(stage == 4 for stage in rel_stages)

    for i, customer in enumerate(customers):
        data.append({
            "customer": customer,
            "visits": visits[i],
            "friendship": friendship[i],
            "stage": rel_stages[i]
            })


df = pd.DataFrame(data)

print(df.loc[df["customer"] == "Zoe", "visits"].describe())
print(df.loc[df["customer"] == "Zoe", "visits"].value_counts())
print(df.loc[df["customer"] == "Zoe", "stage"].describe())
print(df.loc[df["customer"] == "Zoe", "stage"].value_counts())



        