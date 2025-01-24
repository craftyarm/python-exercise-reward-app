########################################
# Fitness Reward Program
# Author: Justin Calmus
# Date: 01/24/2025
# Purpose: Track user exercise, reward points, and display badges to encourage fitness. 
# Class: Python Journal Project Touchstone 4
########################################

import json
from datetime import datetime

def determineBadge(totalPoints):
    """
    Determine user's badge level based on
    totalPoints earned.
    """
    if totalPoints >= 500:
        return "Gold"
    elif totalPoints >= 200:
        return "Silver"
    elif totalPoints >= 100:
        return "Bronze"
    else:
        return "No badge yet"

def loadUserData():
    """
    Load user data from a JSON file if it exists.
    Returns a dictionary of userName -> totalPoints.
    """
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # If file doesn't exist, return empty data
        return {}

def saveUserData(userData):
    """
    Save user data dictionary to a JSON file.
    """
    with open("users.json", "w") as f:
        json.dump(userData, f)

def logExerciseEntry(userName, activity, duration, intensity, pointsAwarded):
    """
    Log a single exercise entry to an external text file
    with date/time and details. 
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("exercise_log.txt", "a") as logFile:
        logFile.write(f"{now} | User: {userName}, Activity: {activity}, "
                      f"Duration: {duration}, Intensity: {intensity}, "
                      f"Points: {pointsAwarded}\n")

def main():
    """
    Main function:
    1. Load current user data.
    2. Provide a menu to log exercise or view summary.
    3. Save updates and log each exercise entry.
    """
    userData = loadUserData()
    
    print("Welcome to the Fitness Reward Program!")
    
    while True:
        print("\nChoose an option:")
        print("1) Log exercise")
        print("2) View summary")
        print("3) Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Log a new exercise
            userName = input("Enter your username: ").strip()
            
            # If user does not exist yet, create them
            if userName not in userData:
                userData[userName] = 0
            
            activity = input("Enter the activity (running, walking, etc.): ").strip()
            
            # Validate duration input
            while True:
                try:
                    duration = int(input("Enter the duration in minutes: "))
                    break
                except ValueError:
                    print("Invalid numeric value. Please try again.")
            
            # Validate intensity input
            while True:
                try:
                    intensity = int(input("Enter intensity (1=low, 2=medium, 3=high): "))
                    if intensity < 1 or intensity > 3:
                        print("Intensity must be 1, 2, or 3.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid integer (1/2/3).")
            
            # Calculate points
            pointsAwarded = duration * intensity
            
            # Update user total
            userData[userName] += pointsAwarded
            
            # Determine badge
            currentBadge = determineBadge(userData[userName])
            
            print(f"{userName}, you earned {pointsAwarded} points!")
            print(f"Your total points are now {userData[userName]}.")
            print(f"Your current badge is: {currentBadge}")
            
            # Log this entry to a file
            logExerciseEntry(userName, activity, duration, intensity, pointsAwarded)
            
            # Save data
            saveUserData(userData)
            
        elif choice == '2':
            # View summary
            userName = input("Enter your username: ").strip()
            if userName in userData:
                totalPoints = userData[userName]
                currentBadge = determineBadge(totalPoints)
                print(f"--- {userName}'s Summary ---")
                print(f"Total Points: {totalPoints}")
                print(f"Badge Level: {currentBadge}")
            else:
                print("User not found. Try logging exercise first!")
        
        elif choice == '3':
            # Exit program
            print("Thank you for using the Fitness Reward Program!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()