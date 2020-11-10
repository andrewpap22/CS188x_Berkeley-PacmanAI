# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        curPos = currentGameState.getPacmanPosition()
        curFoodList = currentGameState.getFood().asList()
        curGhostStates = currentGameState.getGhostStates()
        curScaredTimes = [ghostState.scaredTimer for ghostState in curGhostStates]

        distance = float("inf")
        for ghostState in newGhostStates:
          ghostPos = ghostState.getPosition()
          if ghostPos == newPos:
            return float("-inf")
        
        for food in curFoodList:
          distance = min(distance,manhattanDistance(food,newPos))
          if Directions.STOP in action:  
            return float("-inf")

        return 1.0/(1.0 + distance) 

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def minimax_value(self, gameState, agentIndex, nodeDepth):

        if agentIndex >= gameState.getNumAgents():
            agentIndex = 0
            nodeDepth += 1

        if nodeDepth == self.depth:
            return self.evaluationFunction(gameState)

        if agentIndex == self.index:
            return self.max_value(gameState, agentIndex, nodeDepth)
        else:
            return self.min_value(gameState, agentIndex, nodeDepth)

        return 'None'
     
    def max_value(self, gameState, agentIndex, nodeDepth):

      if gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      value = float("-inf")
      actionValue = "None"

      legalActions = gameState.getLegalActions(agentIndex)

      for actions in legalActions:

        if actions == Directions.STOP:
          continue;

        successor = gameState.generateSuccessor(agentIndex,actions)
        temp = self.minimax_value(successor,agentIndex+1,nodeDepth)

        if temp > value:
          value = max(temp,value)
          actionValue = actions

      if nodeDepth == 0:
        return actionValue
      else:
        return value

    def min_value(self, gameState, agentIndex, nodeDepth):

      if gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      value = float("inf")
      actionValue = "None"

      legalActions = gameState.getLegalActions(agentIndex)
      agentNumber = gameState.getNumAgents()

      for actions in legalActions:

        if actions == Directions.STOP:
          continue;

        successor = gameState.generateSuccessor(agentIndex,actions)
        temp = self.minimax_value(successor,agentIndex+1,nodeDepth)

        if temp < value:
          value = min(temp,value)
          actionValue = actions


      return value

    #       def max_value(self, gameState, agentIndex, nodeDepth):

    #   if gameState.isWin() or gameState.isLose():
    #     return self.evaluationFunction(gameState)

    #   value = float("-inf")
    #   actionValue = "None"

    #   legalActions = gameState.getLegalActions(agentIndex)

    #   for actions in legalActions:

    #     if actions == Directions.STOP:
    #       continue;

    #     successor = gameState.generateSuccessor(agentIndex,actions)

    #     if nodeDepth==self.depth:
    #       temp = self.evaluationFunction(gameState)

    #     temp = self.min_value(successor,agentIndex+1,nodeDepth+1)

    #     if temp > value:
    #       value = max(temp,value)
    #       actionValue = actions

    #   if nodeDepth == 0:
    #     return actionValue
    #   else:
    #     return value

    # def min_value(self, gameState, agentIndex, nodeDepth):

    #   if gameState.isWin() or gameState.isLose():
    #     return self.evaluationFunction(gameState)

    #   value = float("inf")
    #   actionValue = "None"

    #   legalActions = gameState.getLegalActions(agentIndex)
    #   agentNumber = gameState.getNumAgents()

    #   for actions in legalActions:

    #     if actions == Directions.STOP:
    #       continue;

    #     successor = gameState.generateSuccessor(agentIndex,actions)

    #     if agentIndex == agentNumber-1:

    #       if nodeDepth==self.depth:
    #         temp = self.evaluationFunction(successor)

    #       else:
    #         temp = self.max_value(successor,0,nodeDepth+1)
    #     else:
    #       temp = self.min_value(successor,agentIndex+1,nodeDepth)

    #     if temp < value:
    #       value = min(temp,value)
    #       actionValue = actions


    #   return value

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        return self.minimax_value(gameState,0,0)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def alpha_beta_value (self, gameState, agentIndex, nodeDepth, alpha, beta):

        if agentIndex >= gameState.getNumAgents():
            agentIndex = 0
            nodeDepth += 1

        if nodeDepth == self.depth:
            return self.evaluationFunction(gameState)

        if agentIndex == self.index:
            return self.max_value(gameState, agentIndex, nodeDepth, alpha, beta)
        else:
            return self.min_value(gameState, agentIndex, nodeDepth, alpha, beta)

        return 'None'

    def max_value(self, gameState, agentIndex, nodeDepth, alpha, beta):

      if gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      value = float("-inf")

      for legalActions in gameState.getLegalActions(agentIndex):

        if legalActions == Directions.STOP:
          continue

        successor = gameState.generateSuccessor(agentIndex, legalActions)
        temp = self.alpha_beta_value(successor, agentIndex+1, nodeDepth, alpha, beta)

        if temp > value:
          value = temp
          actionValue = legalActions

        if value > beta:
          return value

        alpha = max(alpha, value)

      if nodeDepth == 0:
        return actionValue
      else:
        return value

    def min_value(self, gameState, agentIndex, nodeDepth, alpha, beta):

      if gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      value = float("inf")

      for legalActions in gameState.getLegalActions(agentIndex):
        if legalActions == Directions.STOP:
          continue

        successor = gameState.generateSuccessor(agentIndex, legalActions)
        temp = self.alpha_beta_value(successor, agentIndex+1, nodeDepth, alpha, beta)

        if temp < value:
          value = temp
          actionValue = legalActions

        if value < alpha:
          return value

        beta = min (beta,value)

      return value

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        return self.alpha_beta_value(gameState, 0, 0, float("-inf"),float("inf"))

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def expectimax_value (self, gameState, agentIndex, nodeDepth):

        if agentIndex >= gameState.getNumAgents():
            agentIndex = 0
            nodeDepth += 1

        if nodeDepth == self.depth:
            return self.evaluationFunction(gameState)

        if agentIndex == self.index:
            return self.max_value(gameState, agentIndex, nodeDepth)
        else:
            return self.exp_value(gameState, agentIndex, nodeDepth)

        return 'None'

    def max_value(self, gameState, agentIndex, nodeDepth):

      if gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      value = float("-inf")
      actionValue = "Stop"

      for legalActions in gameState.getLegalActions(agentIndex):

        if legalActions == Directions.STOP:
          continue

        successor = gameState.generateSuccessor(agentIndex, legalActions)
        temp = self.expectimax_value(successor, agentIndex+1, nodeDepth)

        if temp > value:
          value = temp
          actionValue = legalActions

      if nodeDepth == 0:
        return actionValue
      else:
        return value

    def exp_value(self, gameState, agentIndex, nodeDepth):

      if gameState.isWin() or gameState.isLose():
        return self.evaluationFunction(gameState)

      value = 0

      probValue = 1.0/len(gameState.getLegalActions(agentIndex))

      for legalActions in gameState.getLegalActions(agentIndex):
        if legalActions == Directions.STOP:
          continue

        successor = gameState.generateSuccessor(agentIndex, legalActions)
        temp = self.expectimax_value(successor, agentIndex+1, nodeDepth)

        value = value + (temp * probValue)
        actionValue = legalActions

      return value

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        return self.expectimax_value(gameState,0,0)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: 

      1. State with less number of food would be worth more
      2. A state where the pacmac meets a ghost is unfavourable
      3. The min distance between the pacman and a ghost
      4. Number of capsules in a state
      5. 
    """
    "*** YOUR CODE HERE ***"
    curPos = currentGameState.getPacmanPosition()
    curFoodList = currentGameState.getFood().asList()
    curFoodCount = currentGameState.getNumFood()
    curGhostStates = currentGameState.getGhostStates()
    curScaredTimes = [ghostState.scaredTimer for ghostState in curGhostStates]
    curCapsules = currentGameState.getCapsules()
    curScore = currentGameState.getScore()

    foodLeft = 1.0/(curFoodCount + 1.0)
    ghostDist = float("inf")
    scaredGhosts = 0

    # print curScaredTimes

    for ghostState in curGhostStates:

      ghostPos = ghostState.getPosition()
      if curPos == ghostPos:
        return float("-inf")
      else:
        ghostDist = min(ghostDist,manhattanDistance(curPos,ghostPos))
      
      if ghostState.scaredTimer != 0:
        scaredGhosts += 1

    capDist = float("inf")
    for capsuleState in curCapsules:
      capDist = min(capDist,manhattanDistance(curPos,capsuleState))

    ghostDist = 1.0/(1.0 + (ghostDist/(len(curGhostStates))))
    # capDist = 1.0/(1.0 + capDist)
    capDist = 1.0/(1.0 + len(curCapsules))
    scaredGhosts = 1.0/(1.0 + scaredGhosts)


    return curScore + (foodLeft + ghostDist + capDist)

# Abbreviation
better = betterEvaluationFunction

