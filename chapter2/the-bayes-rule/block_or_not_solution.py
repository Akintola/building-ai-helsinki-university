def bot8(pbot, p8_bot, p8_human):
    p8 = pbot * p8_bot + (1 - pbot) * p8_human

    if p8 == 0:
        return None  # avoid division by zero

    p_bot_given_8 = (p8_bot * pbot) / p8
    print(p_bot_given_8)

# you can change these values to test your program with different values
pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)