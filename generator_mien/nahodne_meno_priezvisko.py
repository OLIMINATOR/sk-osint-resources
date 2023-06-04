import random


def zmen_priezvisko(priezvisko):
    if priezvisko.endswith(("a", "á")):
        return priezvisko[:-1] + "ová"
    elif priezvisko.endswith(("ý", "í")):
        return priezvisko[:-1] + "á"
    elif priezvisko.endswith("o"):
        return priezvisko[:-1] + "vá"
    else:
        return priezvisko + "ová"


def create_name(gender):
    with open("muzske_mena.txt", "r", encoding="utf-8") as mena_file, \
            open("zenske_mena.txt", "r", encoding="utf-8") as zeny_file, \
            open("priezviska.txt", "r", encoding="utf-8") as priezviska_file:
        mena = [meno.strip() for meno in mena_file]
        zeny = [zena.strip() for zena in zeny_file]
        priezviska = [priezvisko.strip() for priezvisko in priezviska_file]

        if gender == "man":
            meno = random.choice(mena)
            priezvisko = random.choice(priezviska)
        elif gender == "woman":
            meno = random.choice(zeny)
            priezvisko = random.choice(priezviska)
            priezvisko = zmen_priezvisko(priezvisko)
        else:
            raise ValueError("Invalid gender. Please specify 'man' or 'woman'.")

        return f"{meno.capitalize()} {priezvisko.capitalize()}"


print(create_name(input("Enter the gender (man/woman): ")))
