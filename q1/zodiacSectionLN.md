# Chinese Zodiac Activity

## Requirements

The program asks the user to enter their year of birth. The year should not be earlier than 1900. The program determines the user's Chinese Zodiac sign based on their birth year.

## Python Code

```python
birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
    print("Invalid year, it should not be earlier than 1900")
    exit()

zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tú)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

index = (birth_year - 1900) % 12
zodiac = zodiac_signs[index]

print("Your Chinese Zodiac Sign is:", zodiac)

![Chinese Zodiac Output](zodiac-output.png)
