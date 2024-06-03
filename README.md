# Introduction

### Word Rescue

Introducing a fun and educational word game that challenges you to identify famous people from history based on intriguing clues about their lives and achievements. Perfect for history lovers, students, and trivia fans, this game lets you learn while you play. Developed as a project for Code Institute, it's designed to make learning history enjoyable and engaging. Test your knowledge and see how many historical figures you can recognize!

<h3 align="center"><a href="https://wordrescuepp3-b8f67715878a.herokuapp.com/">Live Demo</a></h3>

# User Experience (UX)

### User Stories

1. **As a history enthusiast**, I want to challenge my knowledge about historical figures, so I can learn and have fun at the same time.
2. **As a student**, I want to use this game to study historical figures in an interactive way, making learning more engaging.
3. **As a trivia fan**, I want to improve my recall of historical facts through a structured game format, enhancing my trivia skills.

### User Goals

1. **Engagement**: Provide an engaging and interactive way to learn about historical figures.
2. **Education**: Help users improve their knowledge of history through gameplay.
3. **Challenge**: Offer varying levels of difficulty to cater to different skill levels.
4. **Accessibility**: Ensure the game is easy to understand and play for users of all ages.


### Color Scheme

The game's color scheme is designed to provide a visually appealing and coherent experience. Key colors used include:

- **Background**: A gradient background ranging from deep purple to dark purple, creating a deep, immersive atmosphere.
- **Primary Text**: Various colors such as bold yellow for rules and guesses to make important information stand out.
- **Panels and Highlights**: Magenta borders for panels to create a distinct separation of content.
- **Feedback Colors**: Green for correct guesses and red for incorrect guesses to provide clear and immediate feedback.

##### The terminal interface:

- **Background Color**: Dark purple for the terminal background, ensuring the text is readable.
- **Button Color**: Buttons are styled with a bright yellow background, purple text, and a border to make them stand out and be easily identifiable.

### Logo

<img width="642" alt="Logo" src="https://github.com/camilabandeira/word.rescue/assets/118302468/9d82536b-9ae4-4ac3-8074-1f7a0993e5df">

I chose to use the pyfiglet library to create this logo. The pyfiglet library allows for the generation of text-based art using various fonts and styles, making it an ideal choice for creating an engaging and visually appealing logo in a command-line environment. Its ease of use and flexibility in rendering ASCII art made it the perfect tool for achieving the desired look and feel for the Word Rescue logo.

### Flowchart
<img width="642" alt="Flowchart" src="https://github.com/camilabandeira/word.rescue/assets/118302468/48f76bb0-98f4-48dd-a2a1-01e31388258e">

I chose to use Lucidchart for creating the flowchart because it made it easy to visually map out the logical flow of the game. Its intuitive interface allowed me to quickly organize and present the game's structure in a clear manner, helping to ensure that all steps and decision points are easily understandable.


# Features

### Existing Features

1. **Interactive Gameplay**: Players guess letters to identify historical figures based on given clues.
2. **Multiple Difficulty Levels**: Choose from easy, medium, and hard levels to match your skill level.
3. **Rich Text Formatting**: Engaging game interface using rich text formatting with the `rich` library.
4. **Dynamic Hints**: Up to three additional hints available per person to help you guess the correct name.
5. **Scoring System**: Track your score over 4 rounds of gameplay.
6. **Replayability**: Option to play multiple rounds and improve your knowledge.

### Terminal

The game interface is built using the `rich` library, which enhances the visual appeal of the terminal. The terminal provides:

<img width="642" alt="Terminal" src="https://github.com/camilabandeira/word.rescue/assets/118302468/9e291121-dc04-4201-a1de-2376997992d1">


### Run Program Button

The "Run Program" button allows users to easily restart the game. The button:

- **Functionality**: Clicking the button reloads the program, resetting the game state and allowing users to start a new session.
- **Design**: The button is styled with a bright yellow background and purple text to make it stand out and be easily identifiable. The border and rounded corners add to the button's visibility and user experience.

<img width="260" alt="Button" src="https://github.com/camilabandeira/word.rescue/assets/118302468/f5c88098-0a71-4542-b588-2dc517ae7596">

# Technologies

In building Word Rescue, we harnessed a variety of technologies to ensure a fun, educational, and seamless experience. Here’s a closer look at what we used:

### Languages

- **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)**: For the basic structure of the web pages.
- **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)**: To add style and make the pages look great.
- **[Python](https://www.python.org/)**: The backbone of the game logic, handling everything behind the scenes.
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)**: To manage the terminal interface and make everything interactive.

### Applications and Libraries

- **[Git](https://git-scm.com/)**: version control system, helping me track changes and collaborate smoothly.
- **[VSCode](https://code.visualstudio.com/)**: The code editor I used to write and manage all the code.
- **[GitHub](https://github.com/)**: Where the project's repository lives, making it easy to share and collaborate.
- **[Heroku](https://www.heroku.com/)**: The platform I used to deploy the game online, so everyone can play it.
- **[Lucidchart](https://www.lucidchart.com/)**: I used this for creating the flowchart, mapping out the game's logic clearly and simply.
- **[Pyfiglet](https://github.com/pwaller/pyfiglet)**: This Python library helped me create awesome ASCII art for the game logo.
- **[Rich](https://rich.readthedocs.io/en/stable/)**: Another Python library that made the terminal output look fantastic with styled text and panels.

# Credits

- **[MDN Web Docs](https://developer.mozilla.org/)**: For comprehensive documentation on HTML, CSS, and JavaScript.
- **[Python.org](https://www.python.org/)**: For extensive resources and documentation on Python.
- **[GitHub Repositories](https://github.com/)**: For various code snippets and open-source projects that inspired and guided the development process.
- **[YouTube](https://www.youtube.com/)**: For tutorials that helped me learn and implement new features.