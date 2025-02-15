import numpy as np
import matplotlib.pyplot as plt

def plot_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'r')
    plt.fill(x, y, 'red', alpha=0.6)
    plt.axis("off")
    plt.title("❤️ Love in Code ❤️", fontsize=14)
    plt.show()

plot_heart()


print('I appreciate you every day! ❤️')

def make_coffee(partner_needs_coffee):
    if partner_needs_coffee:
        return "☕ Coffee is ready!"
    return "Would you like some coffee?"

print(make_coffee(True))

def surprise_gift():
    return "🎁 A thoughtful surprise just for you!"

print(surprise_gift())

together = True

while together:
    print("Enjoying every moment with you ❤️")
    break

hugs = []
hugs.append("🤗 Warm hug!")
print(hugs)