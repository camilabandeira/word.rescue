## Introduction

### Word Rescue

Introducing a fun and educational word game that challenges you to identify famous people from history based on intriguing clues about their lives and achievements. Perfect for history lovers, students, and trivia fans, this game lets you learn while you play. Developed as a project for Code Institute, it's designed to make learning history enjoyable and engaging. Test your knowledge and see how many historical figures you can recognize!

## User Experience (UX)

### User Stories

1. **As a history enthusiast**, I want to challenge my knowledge about historical figures, so I can learn and have fun at the same time.
2. **As a student**, I want to use this game to study historical figures in an interactive way, making learning more engaging.
3. **As a trivia fan**, I want to improve my recall of historical facts through a structured game format, enhancing my trivia skills.

### User Goals

1. **Engagement**: Provide an engaging and interactive way to learn about historical figures.
2. **Education**: Help users improve their knowledge of history through gameplay.
3. **Challenge**: Offer varying levels of difficulty to cater to different skill levels.
4. **Accessibility**: Ensure the game is easy to understand and play for users of all ages.


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!