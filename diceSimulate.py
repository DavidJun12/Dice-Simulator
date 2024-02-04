import random
from collections import Counter

# Simulate rolling a fair six-sided dice 1000 times with random numbers having 4 decimal places
dice_rolls = [round(random.uniform(0, 1), 4) for _ in range(1000)]

# Map random numbers to dice faces
dice_faces = [1 + int(6 * roll) for roll in dice_rolls]

# Create a table containing the roll number, random number generated, and corresponding dice face
print("Roll  | Random Number | Face")
print("-" * 38)
for roll_num, (roll, face) in enumerate(zip(dice_rolls, dice_faces), start=1):
    print(f"{roll_num:4}  | {roll:.4f}        | {face}")

# Calculate the frequency of each face
face_counts = Counter(dice_faces)

# Calculate the percentage occurrence for each face
total_rolls = len(dice_faces)
percentage_occurrence = {face: count / total_rolls * 100 for face, count in face_counts.items()}

# Display the table for frequency and percentage occurrence
print("\nFace  | Frequency | Percentage")
print("-" * 30)
for face in range(1, 7):
    print(f"{face:4}  | {face_counts[face]:9}  | {percentage_occurrence[face]:.2f}%")
