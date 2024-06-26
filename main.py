import gooeypie as gp
import pyhibp
from pyhibp import pwnedpasswords as pw
import webbrowser
import pyperclip as pc

pyhibp.set_user_agent(ua="Fishlock (A password checking application)")

def checkpassword(event):
    password_strength = 0
    
    password = pwd_input.text
    
    symbols = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    
    special_characters = 0

    digit_characters = 0
    
    upper_characters = 0

    lower_characters = 0
    
    possible_additions.disabled = False
    possible_additions.clear()
    possible_additions.append_line('Follow these suggestions for maximum scoring:')

    
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

    if len_score < 50:
        possible_additions.append_line("Try making your password longer")
    
    if special_characters < 1:
        symbol_score = 0
    elif special_characters == 1:
        symbol_score = 5
    elif special_characters >= 2:
        symbol_score = 15
    password_strength += symbol_score

    if symbol_score < 15:
        possible_additions.append_line("Try adding more symbols")

    if digit_characters < 1:
        digit_score = 0
    elif digit_characters == 1:
        digit_score = 5
    elif digit_characters >= 2:
        digit_score = 15
    password_strength += digit_score

    if digit_score < 15:
        possible_additions.append_line("Try adding some more numbers")

    if upper_characters < 1:
        upper_score = 0
    elif upper_characters == 1:
        upper_score = 5
    elif upper_characters >= 2:
        upper_score = 10
    password_strength += upper_score

    if upper_score < 10:
        possible_additions.append_line("Try adding some more uppercase letters")

    if lower_characters < 1:
        lower_score = 0
    elif lower_characters == 1:
        lower_score = 5
    elif lower_characters >= 2:
        lower_score = 10
    password_strength += lower_score

    if lower_score < 10:
        possible_additions.append_line("Try addins some lowercase letters")

    pwd_strength.value = password_strength

    possible_additions.disabled = True

def checkpwn(event):
    password = pwd_input.text
    if password != "":
        resp = pw.is_password_breached(password)
        app.alert('Breach', 'Warning! This password has been breached {0} time(s) before'.format(resp), 'warning')

def showpassword(event):
    pwd_input.toggle()

def opengithub(event):
    webbrowser.open('https://github.com/Space-Cadet-Stuff/Password-Checker')

def showmoreinfo(event):
    app.alert("More Infomation", "This application was developed by SpaceCadet for my SEN task 2 in Year 11", 'info')

def copypassword(event):
    password = pwd_input.text
    pc.copy(password)

app = gp.GooeyPieApp('Password Checker')
app.width = 400
app.height = 400
app.set_grid(7, 3)
app.set_icon("appicon.ico")

linkbox = gp.Container(app)
linkbox.set_grid(7,3)
githublink = gp.ImageButton(app, 'github.png', opengithub)
moreinfo = gp.Button(app, '?', showmoreinfo)
moreinfo.width = 7
copytoclipboard = gp.Button(app, 'Copy Password', copypassword)
copytoclipboard.width = 50

headline = gp.StyleLabel(app, 'Fishlock')
headline.font_size = 40
headline.font_name = "Segoe UI Black"
logo = gp.Image(app, 'appicon.png')

pwd_strength = gp.Progressbar(app)
pwd_strength.width = 550

prompt = gp.Label(app, "Input Password:")
pwd_input = gp.Secret(app)
pwd_input.add_event_listener('change', checkpassword)
show_pwd = gp.Checkbox(app, "Show Password")
show_pwd.add_event_listener('change', showpassword)
checkpwnbtn = gp.Button(app, 'Check for Breach', checkpwn)
checkpwnbtn.width = 90

possible_additions_label = gp.StyleLabel(app, 'For A Higher Score:')
possible_additions_label.font_size = 15
possible_additions_label.font_name = "Segoe UI Semibold"

possible_additions = gp.Textbox(app)
possible_additions.width = 90
possible_additions.disabled = True

app.add(headline, 1, 2, column_span=2)
app.add(logo, 1, 1, align='right')
app.add(prompt, 2, 1)
app.add(pwd_input, 2, 2, fill=True)
app.add(show_pwd, 2, 3)
app.add(pwd_strength, 3, 1, column_span=3)
app.add(checkpwnbtn, 4, 1, column_span=3)
app.add(possible_additions_label, 5, 1, column_span=3)
app.add(possible_additions,6, 1, column_span=3)
app.add(linkbox, 7, 1, column_span=3, valign='bottom')

linkbox.add(githublink, 7, 1, valign='bottom')
linkbox.add(moreinfo, 7, 3, valign='bottom', align='right', stretch='True')
linkbox.add(copytoclipboard, 7, 2, align='center',valign='bottom', stretch='True')

app.run()