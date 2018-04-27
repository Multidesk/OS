pygame_installed = True

try:
    import time, pygame
    from pygame.locals import *

except:
    pygame_installed = False

from static import *

def choose_time_to_play():
    pt("Prier d'entrer la durée en minutes ")

    duree = input()

    while not duree.isdigit() or int(duree) > 10:
        print()
        if not duree.isdigit():
            pt("Erreur, je veux  un entier petit con")
            pt("Prier d'entrer la durée en minutes ")
        else:
            pt("Une durée inférieure à 10 minutes stp")

        duree = input()
    print()

    return int(duree) * 60

def print_chrono(start_time, elapsed_time):
    chrono = start_time - elapsed_time
    M = chrono/60
    S = chrono%60
    pt_chrono(int(M),int(S))

def start_no_homo_bot():
    print()
    if pygame_installed:
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()

        duree = choose_time_to_play()

        son = pygame.mixer.Sound("nohomo.wav")

        start_time = time.time()
        print_chrono(duree, 0)
        elapsed_time = 0.0
        i = 0
        while elapsed_time < duree:
            son.play()
            time.sleep(1)
            son.stop()

            elapsed_time = time.time() - start_time
            i+=1
            print_chrono(duree, i)
    else:
        pt("Pygame doit être installer pour avoir recours au NoHomoBot")

    pt("NoHomoBot going to sleep...")


if __name__ == "__main__":
    start_no_homo_bot()
