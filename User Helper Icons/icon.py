# Import necessary libraries for more modern styling

import matplotlib.patches as patches
from matplotlib import pyplot as plt


# Redraw the icon with a modern style and new emblem

fig, ax = plt.subplots(figsize=(5, 5), dpi=100)



# Set the background color to white

fig.patch.set_facecolor('red')

ax.set_facecolor('white')



# Hide the axes

ax.axis('off')



# Drawing the modern style user manual icon

# Base of the manual (closed book appearance)

book_base = patches.FancyBboxPatch((0.2, 0.2), 0.6, 0.6, boxstyle="round,pad=0.1", fc='green', ec='blue', lw=2)

ax.add_patch(book_base)



# New emblem: A simplified, abstract user icon with a modern style

# Head (circular with a gradient effect)

head = plt.Circle((0.7, 0.7), 0.2, fc='darkblue')

ax.add_patch(head)



# Body: abstract representation with simple lines

body = patches.FancyBboxPatch((0.15, 0.1), 0.3, 0.5, boxstyle="round,pad=0.05", fc='lightblue')

ax.add_patch(body)



# Arms: simplified, attached to the body

arm_left = patches.FancyBboxPatch((0.4, 0.45), 0.05, 0.1, boxstyle="round,pad=0.05", fc='blue')

arm_right = patches.FancyBboxPatch((0.55, 0.45), 0.05, 0.1, boxstyle="round,pad=0.05", fc='blue')

ax.add_patch(arm_left)

ax.add_patch(arm_right)



# Adding text "User Helper" with a modern font style

plt.text(0.5, 0.2, 'User Helper', fontsize=20, color='black', ha='center', weight='bold', family='sans-serif')



# Save the icon

modern_icon_path = "/home/cristian/Documents/Projects/python/UserHelper/VM UserHelper/icon2.png"

plt.savefig(modern_icon_path, bbox_inches='tight', pad_inches=0.1)

plt.close()



modern_icon_path

