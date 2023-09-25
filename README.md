# Bop It! Game - Circuitry Project
The task was to design an activity project with micro:bits that employs at least 4 different inputs components, 2 different outputs, and some kind of physical activity. To satisfy these task requirements, we decided to build an adapted version of the game "Bop It!". 

We have multiple inputs that all use different micro:bit or circuitry components. These inputs correlate with the commands “bop it”, “spin it”, “pull it”, and “shake it”. One of these tasks is chosen at random, and the user performs the task. 

A push-button, potentiometer, accelerometer and joystick are used as the inputs (for “bop it”, “spin it”, “shake it”, and “pull it”, respectively). Each of these components are connected to separate micro:bits and  placed around the room. The user runs to each component and performs the task – which ensures physical activity occurring. We also have one central micro:bit for task assignment and keeping track of the score.

There is a timer for each task. When the task is given, if you respond in time, your score increases, and you receive the next task. When you don’t respond in time, the score is reset and the game restarts. 

We signify a task being sent by using different outputs on the micro:bits. The micro:bit speaker is used to play music, images on the micro:bit LED matrix on different micro:bits are displayed, and the REPL is utilised to see the score. Other sound effects are used for when a task is completed, on both that micro:bit and the central micro:bit. Different images on each of the micro:bits to make the game more visually appealing. The score is displayed in the REPL each time the user performs a task properly.

<h3>Image of "Bop It!" components put together:</h3>

<img width="500" alt="image" src="https://github.com/shree-3143/Bop-It-Game-Circuitry-Project/assets/130221650/ee9152f4-e472-47b8-a18b-eb36100999b5">







