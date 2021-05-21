# AI50
My work on CS50's "Introduction to Artificial Intelligence with Python".

https://cs50.harvard.edu/ai/

This course explores the concepts and algorithms at the foundation of modern artificial intelligence, diving into the ideas that give rise to technologies like game-playing engines, handwriting recognition, and machine translation. Through hands-on projects, students gain exposure to the theory behind graph search algorithms, classification, optimization, reinforcement learning, and other topics in artificial intelligence and machine learning as they incorporate them into their own Python programs. By course’s end, students emerge with experience in libraries for machine learning as well as knowledge of artificial intelligence principles that enable them to design intelligent systems of their own.

## Notes
I've taken some notes on key concepts and algorithms throughout the lectures for future reference.


## Lecture 0: Search
Finding a solution to a problem, like a navigator app that finds the best route from your origin to the destination, or like playing a game and figuring out the next move.
### Projects
* [Degrees](https://github.com/nockifathi/AI50/tree/master/degrees)
* [Tictactoe](https://github.com/nockifathi/AI50/tree/master/tictactoe)
### Concepts
* **Agent**: entity that perceives its environment and acts upon that environment.
* **State**: a configuration of the agent and its environment.
* **Actions**: choices that can be made in a state.
* **Transition model**: a description of what state results from performing any applicable action in any state.
* **Path cost**: numerical cost associated with a given path.
* **Evaluation function**: function that estimates the expected utility of the game from a given state.
#### Algorithms
* **DFS (depth first search)**: search algorithm that always expands the deepest node in the frontier.
* **BFS (breath first search)**: search algorithm that always expands the shallowest node in the frontier.
* **Greedy best-first search**: search algorithm that expands the node that is closest to the goal, as estimated by an heuristic function h(n).
* __A* search__: search algorithm that expands node with lowest value of the "cost to reach node" plus the "estimated goal cost".
* **Minimax**: adversarial search algorithm.


## Lecture 1: Knowledge
Representing information and drawing inferences from it.
### Projects
* [Knights](https://github.com/nockifathi/AI50/tree/master/knights)
* [Minesweeper](https://github.com/nockifathi/AI50/tree/master/minesweeper)
### Concepts
* **Sentence**: an assertion about the world in a knowledge representation language.
* **Knowledge base**: a set of sentences known by a knowledge-based agent.
* **Entailment**: a entails b if in every model in which sentence a is true, sentence b is also true.
* **Inference**: the process of deriving new sentences from old ones.
* **unctive normal form**: logical sentence that is a conjunction of clauses.
* **First order logic**: Propositional logic.
* **Second order logic**: Proposition logic with universal and existential quantification.
### Algorithms
* **Model checking**: enumerate all possible models and see if a proposition is true in every one of them.
* **Conversion to CNF and Inference by resolution**


## Lecture 2: Uncertainty
Dealing with uncertain events using probability.
### Projects
* [Pagerank](https://github.com/nockifathi/AI50/tree/master/pagerank)
### Concepts
* **Unconditional probability**: degree of belief in a proposition in the absence of any other evidence.
* **Conditional probability**: degree of belief in a proposition given some evidence that has already been revealed.
* **Random variable**: a variable in probability theory with a domain of possible values it can take on.
* **Independence**: the knowledge that one event occurs does not affect the probability of the other event.
* **Bayes' Rule**: P(a) P(b|a) = P(b) P(a|b)
* **Bayesian network**: data structure that represents the dependencies among random variables.
* **Markov assumption**: the assumption that the current state depends on only a finite fixed number of previous states.
* **Markov chain**: a sequence of random variables where the distribution of each variable follows the Markov assumption.
* **Hidden Markov Model**: a Markov model for a system with hidden states that generate some observed event.
### Algorithms
* **Inference by enumeration**
* **Sampling**
* **Likelihood weighting**
