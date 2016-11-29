# Perceptron implementation
# Josh Rees-Jones
# jmreesjo@ncsu.edu

# Problem statement (Exercise 1.4 - Learning From Data):
# Let us create our own target function f and data set D and see how the perceptron learning algorithm works. Take d = 2 so you
# can visualize the problem, and choose a random line in the plane as yor target function, where one side of the line maps to
# +1 and the other maps to -1. Choose the inputs x_n of the data set as random points in the plane, and evaluate the target
# function on each x_n to get the corresponding output y_n.

# Now, generate a data set of size 20. Try the perceptron learning algorithm on your data set and see how long it takes to
# converge and how well the final hypotheses g matches your target f. You can find other ways to play with this experiment in
# Problem 1.4.

import matplotlib.pyplot as plt

from random import random

X_MIN = 0
X_MAX = 10

def get_range(w):
    """Return a tuple containing information about the range of the data.

    Returns a tuple:
    (x1_min, x1_max, x2_min, x2_max)

    That specifies the minimum and maximum values of x1 and x2.

    Keyword arguments:
    w -- the weight vector used in this dataset
    """

    # w0 + x1*w1 + x2*w2 = 0

    # When x1 = x_min: w0 + x_min*w1 + x2*w2 = 0
    #                  x2*w2 = -w0 - x_min*w1
    #                     x2 = (-w0 - x_min*w1) / w2
    # -----------------------------------------------------
    # When x2 = x_max: w0 + x_max*w1 + x2*w2 = 0
    #                  x2*w2 = -w0 - x_max*w1
    #                     x2 = (-w0 - x_max*w1) / w2

    x1_min   = X_MIN
    x1_max   = X_MAX

    x2_min   = (-w[0] - x1_min*w[1]) / w[2]
    x2_max   = (-w[0] - x1_max*w[1]) / w[2]
    if x2_min > x2_max: x2_min, x2_max = x2_max, x2_min # Swap the minimum and maximum if necessary

    return (x1_min, x1_max, x2_min, x2_max)

def generate_points(n, w):
    """Return a list of n points randomly generated around the boundary line created
    by the specified weight vector. Points are generated with domain (0, 10) and range
    between the y-axis value of the boundary line at points 0 and 10.

    Keyword arguments:
    n -- the number of points to generate
    w -- the weight vector around whose boundary line points will be generated
    """

    x1_min, x1_max, x2_min, x2_max = get_range(w)
    x1_range = x1_max - x1_min
    x2_range = x2_max - x2_min

    points = []

    for i in range(n):
        # Choose a random value in the range (x1_min, x1_max)
        x1 = random() * x1_range + x1_min
        # Choose a random value in the range (x2_min, x2_max)
        x2 = random() * x2_range + x2_min
        
        x = (1, x1, x2)
        points.append(x)

    return points

def classify_points(points, w):
    """Take a list of points and add return a list of tuples of each point and its classification.

    Keyword arguments:
    points -- the list of points to classify
    w      -- the weight vector used to classify each point

    Returns:
    A list [(point, classification), (point, classification), ...] of tuples of points and their
    classification.
    """
    return [(x, evaluate(w, x)) for x in points]

def generate_weight_vector():
    """Return a randomly-generated, 3-dimensional weight vector (w0, w1, b) such that:
          0 < b  < 10,
          0 < w1 < 10, and
        -10 < w2 < 0.
    """
    b  = random() * 10      # in range (0, 10)
    w1 = random() * 10      # in range (0, 10)
    w2 = random() * 10 - 10 # in range (-10, 0)

    w = (b, w1, w2)

    return w

def evaluate(w, x):
    """Return the classification of the input point x based on the specified weights.

    Return +1 if the input is classified as 'yes' for 'true' and
    return -1 if the input is classified as 'no' or 'false'.

    Keyword arguments:
    w -- the weights to use in classifying the point
    x -- the point to classify
    """

    result = sum(a * b for a, b in zip(w, x))
    return 1 if result > 0 else -1

def get_update(w, x, y):
    """Update the specified weights with the given misclassified point.

    Use the rule w(t + 1) = w(t) + y(x)*x, where w(t) represents the weights at the
    current time and w(t + 1) represents the updated weights.

    Keyword arguments:
    w -- the current value of the weight vector
    x -- a misclassified point
    y -- the correct classification of this point (+1 or -1)
    """
    scaled = tuple(y * i for i in x)
    return tuple(m + n for m, n in zip(w, scaled))

def is_misclassified(w, x, y):
    """Return whether the specified input is correctly classified based on the
    specified weight vector and correct classification.

    Keyword arguments:
    w -- the weight vector used to compute the classification in question
    x -- the input whose classification is in question
    y -- the correct classification of the point
    """
    return evaluate(w, x) != y

def get_misclassified_points(points, w):
    """Return a list of misclassified points from the given list of points based on the
    specified weight vector.

    Keyword arguments:
    points -- a list of tuples of points and their classifications: [(point, classification), ... ] used
              to find misclassified examples
    w      -- a weight vector used to test points for correct classification
    """
    return [x for x in points if is_misclassified(w, x[0], x[1])]

def generate_setup():
    """Generate and return a perceptron simulation setup.

    Returns a tuple with values (w_f, points, w) where w_f is a randomly-generated target weight vector,
    points is a list of test points with classifications, and w is an initial weight vector.
    """

    w_f    = generate_weight_vector()
    points = generate_points(20, w_f)
    points = classify_points(points, w_f)
    w      = [1, 1, 1]

    return (w_f, points, w)

def run_perceptron(w_f, points, w):
    """Run the perceptron learning algorithm (PLA) with the specified points, target weight vector, and
    initial weight vector. Return a tuple with the learned hypothesis weight vector and the number of
    updates the algorithm took.

    Keyword arguments:
    w_f    -- a target weight vector that we are approximating
    points -- a list of tuples of test points and classifications: (point, classification)
    w      -- an initial weight vector that will be improved to approximate w_f

    Returns:
    (w, count) -- a tuple with w (the learned hypothesis weight vector) and count (the number of updates computed)
    """

    # Initial hypothesis weights that are updated to correctly classify all test points.
    w = [1, 1, 1]

    count = 0

    # Update the weights until all points are correctly classified.
    while True:
        # Get a list of the misclassified points.
        misclassified = get_misclassified_points(points, w)

        # If there are misclassified points,
        if misclassified:
            # Loop through the misclassified points.
            #     If this one is misclassified,
            #         Update the weight vector with it.
            for x in misclassified:
                if is_misclassified(w, x[0], x[1]):
                    count += 1
                    w = get_update(w, x[0], x[1])
        else:
            # There are no more misclassified points, so our weights approximately
            # match the target function y.
            return w, count

def plot_points(points):
    """Plot the specified points on matplotlib.pyplot.
    
    Keyword arguments:
    points -- a list of tuples of points and classifications to plot: [(point, classification), (point, classification), ...]
    """

    yes_points_classified = [x for x in points if x[1] ==  1]
    no_points_classified  = [x for x in points if x[1] == -1]

    yes_points, ignore = zip(*yes_points_classified)
    no_points, ignore = zip(*no_points_classified)

    ignore, yes_x, yes_y = zip(*yes_points)
    ignore, no_x, no_y = zip(*no_points)

    plt.plot(yes_x, yes_y, 'go')
    plt.plot(no_x, no_y, 'ro')

def plot_boundary_line(w, label, color='k'):
    """Plot a dashed boundary line of the specified weight vector.

    Keyword arguments:
    w     -- the weight vector whose boundary line will be plotted
    label -- a string describing the line
    color -- a matplotlib color to use
    """
    x1_min, x1_max, x2_min, x2_max = get_range(w)

    plt.plot([x1_min, x1_max], [x2_min, x2_max], label=label, color=color, linestyle="--")

def plot(w_f, points, w_g):
    """Plot the specified points and classifications, the boundary line defined by the specified
    target weight vector, and the boundary line defined by the hypothesis (approximate) weight vector.

    Keyword arguments:
    w_f    -- the target weight vector
    points -- a list of tuples of points and classifications to plot: [(point, classification), (point, classification), ...]
    w_g    -- the hypothesis (approximate) weight vector
    """

    # Plot the data points
    plot_points(points)

    # Plot the boundary lines
    plot_boundary_line(w_f, "Target weights", color="b")
    plot_boundary_line(w_g, "Learned weights", color="#ffa500")

    legend = plt.legend(loc='upper center')

    plt.show()

if __name__ == '__main__':
    w_f, points, w = generate_setup()
    w_g, count = run_perceptron(w_f, points, w)
    print("Learned weight vector: " + str(w_g))
    print("Updates taken: " + str(count))
    plot(w_f, points, w_g)
