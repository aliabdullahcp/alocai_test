Year 2271.  
German territory is occupied by Aliens.  
Playing video games is strictly banned because of the Entertainment Limitation For Humans Law.  
Video games black market prices gone crazy.

You're a hacker who has physical access to the old-fashioned Alien PC containing all games that have ever been
developed.  
You're about to download games with your old-fashioned pen-drive and sell them to the rich game collectors.  
There is one issue though: you'll know what's the available space of your pen-drive just 5 minutes before the action.  
So you need to find a way to know which games to pick basing on the pen-drive space to make this risky operation as much
profitable as possible.  
You wanna create a service which will return a combination of games with the highest possible
total value for the given pen-drive space and steal returned games from the computer.

There are 3 endpoints created for this task:

/docs
- Documentation for the endpoints using OPEN API (redoc)

/docs/swagger-ui
- Documentation for the endpoints using OPEN API (swagger)

/api/v1/games
- Endpoint to add new games

/api/v1/best_value_games
- Endpoint to get the best games within a max space

## Pre req
- docker should be installed

## Setting up the project:
- Clone the repository at local
- rename example.env file at root to .env
- update the values in the environment as per your use
- run command "docker-compose up"

## Requirements
1. Create a Python (>= 3.8) web application using web framework you find appropriate (we use Flask)
   and implement endpoints presented below
2. The application is covered by unit and integration tests using pytest
3. Local deployment, tests and others are run using Docker/docker-compose
4. Repository contains README with local deployment and tests instruction
5. Application uses PostgreSQL as database
6. Codebase is typed and commented
7. Repository is pushed to Github and link is provided to the recruiter
8. Error handling and edge cases

