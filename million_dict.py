aliens = [] 
 
# Make a million green aliens, worth 5 points
#  each. Have them all start in one row.
for alien_num in range(1000000):
    new_alien = {'color': 'green', 'points': 5, 'x': 20 * alien_num, 'y': 0}
    aliens.append(new_alien)
 
# Prove the list contains a million aliens.
num_aliens = len(aliens) 
 
print("Number of aliens created:")
print(num_aliens)
print(new_alien['color'])
print(new_alien['x'])
