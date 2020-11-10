Artificial Intelligence, Pacman Game (Fall 2017)
================================================

## [CS188x](http://ai.berkeley.edu/home.html) Into to AI 
[The Pacman Projects](http://ai.berkeley.edu/project_overview.html) by the [University of California, Berkeley](http://berkeley.edu/).

![Animated gif pacman game](http://ai.berkeley.edu/images/pacman_game.gif)

> In this project, Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. Try to build general search algorithms and apply them to Pacman scenarios.

<hr> 

Start a game by the command:
```
$ python pacman.py
```
You can see the list of all options and their default values via:
```
$ python pacman.py -h
```

<hr>

## Project1: Search
- DFS, BFS, UCS, Astar, Astar heuristic 
- Files edited: search.py, searchAgents.py
- Inside the file: searchAgents.py you will find 2 implementations: 
  1. The *"braindead"* one
  2. The *"smart"* one
  <br>
  The "braindead" one is commented out and basically it explains in "pseudo code" (but python) how the working implementation works.

```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
$ python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
- Corner problem, Corner heuristic
```
$ python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
$ python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
- Eating all the dots
```
$ python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

- Grading: 25/25

> for more information, check [here](http://ai.berkeley.edu/search.html) !

<hr>

## Project2 Multi-Agent
- ReflexAgent: 
A capable reflex agent will have to consider both food locations and ghost locations to perform well.
```
$ python pacman.py --frameTime 0 -p ReflexAgent -k 2
$ python pacman.py -p ReflexAgent -l openClassic -n 10 -q
```
- MinimaxAgent: 
Write an adversarial search agent in the provided MinimaxAgent class stub in multiAgents.py
```
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
```
- Expectimax: 
ExpectimaxAgent is useful for modeling probabilistic behavior of agents who may make suboptimal choices.
```
$ python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better -q -n 30
```

- Grading: 25/25

> for more information, check [here](http://ai.berkeley.edu/multiagent.html) !

<hr>

> TODO: Implement the rest of the projects!

<hr>

## Credits
- This is the homework project for the course Artificial Intelligence I (2017 Fall), at NKUA [DiT](https://www.di.uoa.gr/en) .
- :copyright: Andrew Pappas, All Rights Reserved.
