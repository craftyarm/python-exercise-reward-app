# Fitness Reward Program

A simple Python application that tracks exercise activities for different users, rewards them with points based on duration and intensity, and then assigns badges depending on their total points. The program also saves activity logs to an external file for record-keeping.

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Example Interaction](#example-interaction)  
7. [Data Persistence](#data-persistence)  

---

## Overview

The **Fitness Reward Program** encourages healthy habits by allowing users to log their daily exercise sessions. Each exercise session earns a certain number of points based on **duration** and **intensity**. Over time, users accumulate points that increase their badge level (e.g., Bronze, Silver, Gold). This system is simple, easy to use, and motivates continued exercise.

---

## Features

- **User Profiles**  
  Create or access existing user profiles by entering a username.

- **Exercise Logging**  
  Enter the type of exercise, duration (in minutes), and intensity (1, 2, or 3).

- **Points Calculation**  
  Points are awarded by multiplying `duration × intensity`.

- **Badge Assignments**  
  - **No Badge**: 0–99 points  
  - **Bronze**: 100–199 points  
  - **Silver**: 200–499 points  
  - **Gold**: 500+ points

- **Data Storage**  
  Store total points in a JSON file (`users.json`) and log exercise history to `exercise_log.txt` with timestamps.

---

## Requirements

- **Python 3.7+** (or later)
- Standard libraries: `json`, `datetime`

---

## Installation

1. **Clone or Download**  
   - Clone the repo:
     ```bash
     git clone https://github.com/craftyarm/python-exercise-reward-app.git
     ```

## Usage

### Run the Program

```bash
python reward-program-exercise.py

### Menu Options

1. **Log exercise**  
2. **View summary**
3. **Exit**

### Logging Exercise

- If it is a new user, the system creates a profile with **0 initial points**
- Enter the activity name, duration (in minutes), and intensity (1, 2, or 3)
- **Points Awarded** = `duration × intensity`
- The system updates total points, displays the user's new total and current badge, and logs the details in a file

### Viewing Summary

- Enter your username to see your **total points** and current **badge** level

### Exiting

- When done, choose **3** to exit

## Example Interaction

```plaintext
Welcome to the Fitness Reward Program!

Choose an option:
1) Log exercise
2) View summary
3) Exit

Enter your choice (1/2/3): 1
Enter your username: Alice
Enter the activity (running, walking, etc.): Running
Enter the duration in minutes: 30
Enter intensity (1=low, 2=medium, 3=high): 3

Alice, you earned 90 points!
Your total points are now 90.
Your current badge is: Bronze

Choose an option:
1) Log exercise
2) View summary
3) Exit

Enter your choice (1/2/3): 2
Enter your username: Alice

--- Alice's Summary ---
Total Points: 90
Badge Level: Bronze

Choose an option:
1) Log exercise
2) View summary
3) Exit

Enter your choice (1/2/3): 3
Thank you for using the Fitness Reward Program!
```

## Data Persistence

1. **users.json**
   - Stores a mapping of `{ "username": totalPoints }` in JSON format
   - Automatically updated every time a user logs exercise

2. **exercise_log.txt**
   - Appends a line with the timestamp, user, activity, duration, intensity, and points earned for each exercise session
   - For example:

```yaml
2025-01-24 14:35:00 | User: Alice, Activity: Running, Duration: 30, Intensity: 3, Points: 90