# Video Game Organizer
Hey, I'm Brett. Thanks for checking out my Video Game Organizer app here.

As a lifelong gamer and new-ish software developer, I saw the opportunity to create my own
program to keep track of my video game collection. The original build of this program took shape
from late November 2021 - January 5, 2022. I built it in a virtual environment on my Raspberry Pi 400, 
using Django 4.0 and Python 3.9.7.

## Installation
Clone the repo down to your local machine with this command:
   <b> *git clone https://github.com/brettandrews3/Switch-Organizer.git*</b>

From your terminal, navigate to the file with the manage.py file:
    cd Switch-Organizer/Switch_Organizer (this directory holds the manage.py file)

Make the migrations, then create an admin login for the site:
    python manage.py migrate
    python manage.py createsuperuser
        //Enter your new username, email, and password

Launch the server. If everything is in order, your terminal will display some new text that ends with,
'Quit the server with CONTROL-C.':
    python manage.py runserver

Open a tab in your web browser and navigate to:
    http://127.0.0.1:8000/admin

Enter your new username and password to access the admin page. Here, you should see the 'Video Game Organizer'
header across the top of the page, as well as a sidebar button to add a video game. The app takes your input
for game name, release year, genre, developer, publisher, and console. There should be the option at the bottom
of the entry page to add your review and rate the game from 1-10. You can view reviews on the details page for
each individual game.

The app lists the games in alphabetical order, though you can order them by the other values, if you choose.
There's no graphics for game art or a non-admin site yet; I hope to add these items in the future. If you can
write these features into the code, be my guest. The license should allow for other GitHub users to make edits.

## Planned additions
- Create drop-down menus for game_console, release_date, rating (1-10 scale)
- Confirm that app can run on Windows and Mac (developed and tested on Linux)
- Change review_text window to be more user-friendly (text in box that's 5-10 lines deep)
- Option to add image of game art OR find an API that can match game art to game name (a la GameFAQs)
- Create a book organizer that can live independently or in the same organizer program

## Signing Off
Thanks so much for checking out my coding project here. I'm tremendously proud of this project and hope to continue
adding features to it as I gain more coding experience. Email me at brettandrews3@gmail.com if you've got any 
questions or comments. Take care.

Brett - January 21, 2022
