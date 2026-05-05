def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


factorial(4)

import math   # Used to access infinity values

# Initialize values
max_value = -math.inf   # Start with the smallest possible value for max
min_value = math.inf    # Start with the largest possible value for min

# List of numbers
numbers = [2, 7, 3, 10, 2, 11]

# -------------------- Finding Maximum --------------------
for num in numbers:
    max_value = max(max_value, num)
    print('Current Value : ', num, 'max_value : ', max_value)

print('=============================================================')

# -------------------- Finding Minimum --------------------
for num in numbers:
    min_value = min(min_value, num)
    print('Current Value : ', num, 'min_value : ', min_value)

print("Max:", max_value)
print("Min:", min_value)

import math  

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None


def minmax(node, depth, maximizing_player=True):

    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        value = -math.inf
        for child in node.children:
            value = max(value, minmax(child, depth-1, False))
        node.minmax_value = value
        return value

    else:
        value = math.inf
        for child in node.children:
            value = min(value, minmax(child, depth-1, True))
        node.minmax_value = value
        return value


root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(2)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

minmax(root, 3)

print("Minimax values:")
print("A:", root.minmax_value)
print("B:", n1.minmax_value)
print("C:", n2.minmax_value)









import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None

def alpha_beta(node, depth, alpha, beta, maximizing_player=True):

    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        node.minmax_value = value
        return value

    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        node.minmax_value = value
        return value


root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(2)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

alpha_beta(root, 3, -math.inf, math.inf)

print("Alpha-Beta values:")
print("A:", root.minmax_value)
print("B:", n1.minmax_value)
print("C:", n2.minmax_value)






import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return node.minmax_value
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)


class Environment:
    def __init__(self, tree):
        self.tree = tree

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):

        if depth == 0 or not node.children:
            return node.value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.alpha_beta_search(child, depth-1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            node.minmax_value = value
            return value

        else:
            value = math.inf
            for child in node.children:
                value = min(value, self.alpha_beta_search(child, depth-1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            node.minmax_value = value
            return value


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    return agent.act(percept, environment)


root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(1)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

agent = MinimaxAgent(3)
environment = Environment(root)

result = run_agent(agent, environment, root)

print("Result:", result)













#------Bayesian Network-----


from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian Network structure
model = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'David_calls'),
    ('Alarm', 'Sophia_calls')
])

# CPD for Burglary
cpd_burglary = TabularCPD(
    variable='Burglary',
    variable_card=2,
    values=[[0.999], [0.001]],  # [False, True]
    state_names={'Burglary': ['False', 'True']}
)

# CPD for Earthquake
cpd_earthquake = TabularCPD(
    variable='Earthquake',
    variable_card=2,
    values=[[0.998], [0.002]],  # [False, True]
    state_names={'Earthquake': ['False', 'True']}
)

# CPD for Alarm (depends on Burglary and Earthquake)
cpd_alarm = TabularCPD(
    variable='Alarm',
    variable_card=2,
    values=[
        # B=F E=F  B=F E=T  B=T E=F  B=T E=T
        [0.999,   0.71,   0.06,   0.05],  # Alarm=False
        [0.001,   0.29,   0.94,   0.95]   # Alarm=True
    ],
    evidence=['Burglary', 'Earthquake'],
    evidence_card=[2, 2],
    state_names={
        'Alarm': ['False', 'True'],
        'Burglary': ['False', 'True'],
        'Earthquake': ['False', 'True']
    }
)

# CPD for David_calls (depends on Alarm)
cpd_david = TabularCPD(
    variable='David_calls',
    variable_card=2,
    values=[
        # A=F    A=T
        [0.95,  0.1],  # David_calls=False
        [0.05,  0.9]   # David_calls=True
    ],
    evidence=['Alarm'],
    evidence_card=[2],
    state_names={
        'David_calls': ['False', 'True'],
        'Alarm': ['False', 'True']
    }
)

# CPD for Sophia_calls (depends on Alarm)
cpd_sophia = TabularCPD(
    variable='Sophia_calls',
    variable_card=2,
    values=[
        # A=F    A=T
        [0.99,  0.3],  # Sophia_calls=False
        [0.01,  0.7]   # Sophia_calls=True
    ],
    evidence=['Alarm'],
    evidence_card=[2],
    state_names={
        'Sophia_calls': ['False', 'True'],
        'Alarm': ['False', 'True']
    }
)

# Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_david, cpd_sophia)

# Check if the model is valid
assert model.check_model()

# Perform inference
infer = VariableElimination(model)

# Calculate P(Alarm=True | Burglary=True)
prob_alarm_given_b_true = infer.query(
    variables=['Alarm'],
    evidence={'Burglary': 'True'}
)
print("P(Alarm=True | Burglary=True):", prob_alarm_given_b_true.values[1])  # Index 1 is 'True'

# Calculate P(Alarm=True | Burglary=False)
prob_alarm_given_b_false = infer.query(
    variables=['Alarm'],
    evidence={'Burglary': 'False'}
)
print("P(Alarm=True | Burglary=False):", prob_alarm_given_b_false.values[1])  # Index 1 is 'True'

# Optional: Calculate P(Burglary=True | Alarm=True)
prob_burglary_given_a_true = infer.query(
    variables=['Burglary'],
    evidence={'Alarm': 'True'}
)
print("P(Burglary=True | Alarm=True):", prob_burglary_given_a_true.values[1])  # Index 1 is 'True'










#------------Markov Model--------


import numpy as np

# Define the states and transition matrix
states = ["Red", "Blue"]
transition_matrix = np.array([[0.5, 0.5],  # From Red -> Red or Blue
                              [0.5, 0.5]]) # From Blue -> Red or Blue

# Function to simulate the Markov process
def simulate_markov_process(initial_state, num_steps):
    current_state = initial_state
    state_sequence = [current_state]

    for _ in range(num_steps):
        if current_state == "Red":
            next_state = np.random.choice(states, p=transition_matrix[0])
        else:
            next_state = np.random.choice(states, p=transition_matrix[1])

        state_sequence.append(next_state)
        current_state = next_state

    return state_sequence

# Simulate the process starting from "Red" and for 10 steps
initial_state = "Red"
num_steps = 10
state_sequence = simulate_markov_process(initial_state, num_steps)

# Output the sequence of states
print(f"State sequence for {num_steps} steps starting from {initial_state}:")
print(" -> ".join(state_sequence))
