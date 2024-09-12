q9 = [{"color": "red", "score": 0.13},
      {"color": "blue", "score": 1.00},
      {"color": "green", "score": 0.64},
      {"color": "red", "score": 0.98},
      {"color": "blue", "score": 0.52},
      {"color": "violet", "score": 0.25}]

color1 = q9[0]["score"]
# print(color1)


dct = {"color": "red", "score": 0.13}

# print(dct["color"])

answer = [x["color"] + " is the color" for x in q9 if x["color"] == "blue" or x["color"] == "violet"]

def check_color(row, x):
    return row["color"] == "blue" or row["color"] == "violet"

check_color(row={"color": "red", "score": 0.13}, x=4)

# The following two lines are equivalent.
# print(list(filter(check_color, q9)))
# print(list(filter(lambda x : x["color"] == "blue" or x["color"] == "violet", q9)))

# print(answer)

def check_even(x):
    # print("even")
    return "even" #This is the correct one

# print(check_even(2))

if check_even(4) == "even":
    print("the number is even!")

if None == "even":
    print("the number is even!")