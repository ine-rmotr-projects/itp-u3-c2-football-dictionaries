# Football Dictionaries

Today's project will deal with two of our greatest passions: dictionaries and football 😉.

This project is divided into 3 assignments, each one requires something different. But all these assignments will deal with the same initial data: **a list of players structured as a "list of lists"**.

To put it in human: There's a big list that has players inside. But each player is represented as a list, with each position in the list being a different piece of information for the player.

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

Your job through this entire group project will be to transform these lists to Dictionaries.

## Assignment 1 - Lists to Dicts

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

## Assignment 2

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

## Assignment 3

And finally this is really similar to the second assignment but we'll add one more level of nesting. This function will return the players grouped by country, and per each country, grouped by position. Example:

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

## Walkthrough solution

We've got together with a few students to present a possible solution. Watch it on YouTube:

<p align="center">
  <a href="https://youtu.be/p-tWuQc95YQ" target="_blank">
    <img src="https://img.youtube.com/vi/p-tWuQc95YQ/0.jpg">
  </a>
</p>


