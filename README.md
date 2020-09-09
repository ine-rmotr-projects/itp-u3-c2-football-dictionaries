# Football Dictionaries

This project will deal with two of our greatest passions: dictionaries and football! 😉 This will require the use of nested collections (lists of lists, dicts nested under lists, etc) and nested control flow structures. It's the final challenge regarding collections for our course. If you can complete this project, you'll become a **Master of Data and Collections** and you might even get a gold star.

## Warm up

Before approaching the main tasks of the project, there's a warm up section to revisit topics about collections (especially when they're nested). Open the notebook `Warm Up Activities.ipynb` to practice with them. There's also a notebook containing the solutions in case you need some help.

## The Real Project

After finishing the warm up section, you'll be ready to take on the real project. This project is divided into 3 assignments, each one requires something different. However, all of the assignments will deal with the same initial data: **a list of players structured as a "list of lists"**.

Translation to human: There's a big list that has players inside. But each player is represented as a list, with each position in the list being a different piece of information about the player.



Example:

```python
SQUADS_DATA = [
  [
    "1",                                     # Number
    "GK",                                    # Position
    "Juan Botasso",                          # Name
    "(1908-10-23)23 October 1908 (aged 21)", # Date of Birth
    "",                                      # Caps
    "Quilmes",                               # Club
    "Argentina",                             # Country (Players Country)
    "Argentina",                             # Club Country
    "1930"                                   # Year
  ],
  [
    "9",
    "FW",
    "Roberto Cherro",
    "(1907-02-23)23 February 1907 (aged 23)",
    "",
    "Boca Juniors",
    "Argentina",
    "Argentina",
    "1930"
  ]
  # More Players...
]
```

Your job through this project will be to transform these lists to Dictionaries organized in various manners.

### Assignment 1 - Lists to Dicts

The first assignment just requires you to turn these players into dictionaries with the following structure:

```python
{
    'number': ...,
    'position': ...,
    'name': ...,
    'date_of_birth': ...,
    'caps': ...,
    'club': ...,
    'country': ...,
    'club_country': ...,
    'year': ...,
}
```

Given our previous example, now our new list containing **players as dictionaries** would look like:

```python
SQUADS_DATA = [
  {
    'number': "1",
    'position': "GK",
    'name': "Juan Botasso",
    'date_of_birth': "(1908-10-23)23 October 1908 (aged 21)",
    'caps': "",
    'club': "Quilmes",
    'country': "Argentina",
    'club_country': "Argentina",
    'year': "1930"
  },
  {
    'number': "9",
    'position': "FW",
    'name': "Roberto Cherro",
    'date_of_birth': "(1907-02-23)23 February 1907 (aged 23)",
    'caps': "",
    'club': "Boca Juniors",
    'country': "Argentina",
    'club_country': "Argentina",
    'year': "1930"
  }
  # More Players...
]
```

### Assignment 2

This assignment is similar to the previous one, but instead of having just one big list with all the players, we're going to group them by position. Your result will look something like:

```python
# Please note we're returning a dictionary instead of a list
{
  "GK": [{..player1..}, {..player2..}],
  "DF": [{..player1..}, {..player2..}],
  "MF": [{..player1..}, {..player2..}],
  "FW": [{..player1..}, {..player2..}],
}
```

### Assignment 3

And finally this is really similar to the previous assignment but we're adding one more level of nesting. This function will return the players grouped by country, and per each country, grouped by position. Example:

```python
{
  "Argentina": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  },
  "Brazil": {
    "GK": [{..player1..}, {..player2..}],
    "DF": [{..player1..}, {..player2..}],
    "MF": [{..player1..}, {..player2..}],
    "FW": [{..player1..}, {..player2..}],
  }
}
```
