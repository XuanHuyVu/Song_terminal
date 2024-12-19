import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def play_song_lyrics():
    lyrics = """
Its the time...
The lights on the strings go blink blink blink ⭐
The bell on the church goes ring ring ring 🔔
Mariah Carey's has been on repeat,
Santa Claus 🎅 is coming but bring no gifts.

I'm your Christmas present 🎁 baby,
But don't put me by the tree instead🎄
Put me round your arms, feel your warmth,
I trynna calm, but my heart alarm.

You can mess up with me lately,
But tonight I want you to obey.
Cause I got reparations for our night,
So don't want to lose.
Sight out of your eyes ❤️
"""

    print(Style.BRIGHT+ Fore.BLUE + "🎁🎄\n")
    lines = lyrics.strip().split('\n')
    for i, line in enumerate(lines):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.2)

    print(Style.BRIGHT + Fore.MAGENTA + "\nXuanHuyVu 💻")

if __name__ == "__main__":
    play_song_lyrics()
