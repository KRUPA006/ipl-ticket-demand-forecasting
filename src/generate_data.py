
import pandas as pd
import random

# Updated team list (includes all current teams)
teams = ["RCB", "CSK", "MI", "KKR", "SRH", "RR", "DC", "PBKS", "LSG", "GT"]

# Stadiums with capacity
stadiums = [
    ("Chinnaswamy", 40000),
    ("Wankhede", 33000),
    ("Chepauk", 38000),
    ("Eden Gardens", 66000),
    ("Narendra Modi Stadium", 132000)
]

def generate_data(n=100):
    data = []

    for _ in range(n):
        # Select two different teams
        team1, team2 = random.sample(teams, 2)

        # Assign popularity scores
        pop1 = random.randint(5, 10)
        pop2 = random.randint(5, 10)

        # Select stadium
        stadium, capacity = random.choice(stadiums)

        # Match conditions
        match_day = random.choice([0, 1])  # 0 = weekday, 1 = weekend
        weather = random.choice([0, 1])    # 0 = bad, 1 = good

        # Add randomness (noise)
        noise = random.randint(-2000, 2000)

        # Calculate tickets sold (core logic)
        tickets = (
            0.4 * capacity
            + 2000 * pop1
            + 2000 * pop2
            + 8000 * match_day
            + 10000 * weather
            + noise
        )

        # Ensure tickets do not exceed capacity
        tickets = int(min(max(tickets, 0), capacity))

        # Store data
        data.append([
            team1, team2, pop1, pop2,
            stadium, capacity,
            match_day, weather,
            tickets
        ])

    # Create DataFrame
    df = pd.DataFrame(data, columns=[
        "team1", "team2",
        "popularity_team1", "popularity_team2",
        "stadium", "capacity",
        "is_weekend", "good_weather",
        "tickets_sold"
    ])

    return df


if __name__ == "__main__":
    df = generate_data(200)

    # Save to CSV (make sure 'data' folder exists)
    df.to_csv("data/ipl_data.csv", index=False)

    print("Dataset generated successfully!")