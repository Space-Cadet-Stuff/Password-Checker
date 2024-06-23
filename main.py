import gooeypie as gp


def checkpassword(event):
    global password_strength

    password_strength = 0
    
    password = pwd_input.text
    
    possible_additions.clear()
    
    symbols = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    
    special_characters = 0

    digit_characters = 0

    upper_characters = 0

    lower_characters = 0
    
    for char in password:
        if char in symbols:
            special_characters += 1
    
    for char in password:
        if char.isdigit():
            digit_characters += 1
    
    for char in password:
        if char.isupper():
            upper_characters += 1
    
    for char in password:
        if char.islower():
            lower_characters += 1

    if len(password) < 8:
        len_score = 0
    elif len(password) == 8:
        len_score = 10
    elif len(password) == 9:
        len_score = 15
    elif len(password) == 10:
        len_score = 20
    elif len(password) == 11:
        len_score = 25
    elif len(password) == 12:
        len_score = 30
    elif len(password) == 13:
        len_score = 35
    elif len(password) == 14:
        len_score = 40
    elif len(password) == 15:
        len_score = 45
    elif len(password) >= 16:
        len_score = 50
    password_strength += len_score
    
    if special_characters < 1:
        symbol_score = 0
    elif special_characters == 1:
        symbol_score = 5
    elif special_characters >= 2:
        symbol_score = 15
    password_strength += symbol_score

    if digit_characters < 1:
        digit_score = 0
    elif digit_characters == 1:
        digit_score = 5
    elif digit_characters >= 2:
        digit_score = 15
    password_strength += digit_score

    if upper_characters < 1:
        upper_score = 0
    elif upper_characters == 1:
        upper_score = 5
    elif upper_characters >= 2:
        upper_score = 10
    password_strength += upper_score

    if lower_characters < 1:
        lower_score = 0
    elif lower_characters == 1:
        lower_score = 5
    elif lower_characters >= 2:
        lower_score = 10
    password_strength += lower_score


    pwd_strength.value = password_strength

def showpassword(event):
    pwd_input.toggle()

app = gp.GooeyPieApp('Password Checker')
app.width = 400
app.height = 400
app.set_grid(5, 3)
app.set_icon("appicon.ico")

headline = gp.StyleLabel(app, 'Fishlock')
headline.font_size = 40
headline.font_name = "Segoe UI Black"

pwd_strength = gp.Progressbar(app)
pwd_strength.width = 550

prompt = gp.Label(app, "Input Password:")
pwd_input = gp.Secret(app)
pwd_input.add_event_listener('change', checkpassword)
show_pwd = gp.Checkbox(app, "Show Password")
show_pwd.add_event_listener('change', showpassword)

possible_additions_label = gp.StyleLabel(app, 'For A Higher Score:')
possible_additions_label.font_size = 15
possible_additions_label.font_name = "Segoe UI Semibold"

possible_additions = gp.Textbox(app)
possible_additions.width = 90
possible_additions.disabled = True

app.add(headline, 1, 1, column_span=3)
app.add(prompt, 2, 1)
app.add(pwd_input, 2, 2, fill=True)
app.add(show_pwd, 2, 3)
app.add(pwd_strength, 3, 1, column_span=3)
app.add(possible_additions_label, 4, 1, column_span=3)
app.add(possible_additions,5, 1, column_span=3)

app.run()

# Test for commit