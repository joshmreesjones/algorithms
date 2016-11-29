import unittest
from perceptron import *

class PerceptronTestCase(unittest.TestCase):
    def test_generate_points(self):
        # The boundary line for this weight vector is the line going through
        # points (0, 10) and (10, 0). All points should have coordinates between
        # 0 and 10 in both dimensions (except the first, which is a placeholder 1).
        w = [-10, 1, 1]
        points = generate_points(20, w)

        #   b        x         y
        # w[0]           + w[2]*p[2] --> x is 0
        # w[0] + w[1]*10 + w[2]*p[2] --> x is 10

        for x in points:
            self.assertEqual(x[0], 1)
            self.assertTrue(0 < x[1] < 10)
            self.assertTrue(0 < x[2] < 10)

    def test_classify_points(self):
        # The boundary line for this weight vector is the line going through points (0, 10) and (10, 0).
        w = [-10, 1, 1]

        points = [
            (1, 0, 0),   # Below the line
            (1, 10, 10), # Above the line

            (1, 1, 1),   # Below the line
            (1, 9, 9),   # Above the line

            (1, 2, 7),   # Below the line
            (1, 7, 2),   # Below the line
            (1, 3, 8),   # Above the line
            (1, 8, 3)    # Above the line
        ]

        # Anything below the line should classify as -1 and anything above the line should classify as +1.

        classified_points = [
            ((1, 0, 0), -1),  # Below the line
            ((1, 10, 10), 1), # Above the line

            ((1, 1, 1), -1),  # Below the line
            ((1, 9, 9), 1),   # Above the line

            ((1, 2, 7), -1),  # Below the line
            ((1, 7, 2), -1),  # Below the line
            ((1, 3, 8), 1),   # Above the line
            ((1, 8, 3), 1)    # Above the line
        ]

        result = classify_points(points, w)

        # Test that the classifications are correct.
        for x_test, x_result in zip(classified_points, result):
            self.assertEqual(x_test, x_result, "classify_points returned a bad classification.")

        # Each of these points is on the boundary line.
        points = [
            (1, 0, 10),
            (1, 10, 0),
            (1, 5, 5)
        ]

        # Test that the function doesn't blow up when points are on the line
        result = classify_points(points, w)

        for x in result:
            self.assertTrue(x[1] == -1 or x[1] == 1)

    def test_generate_weight_vector(self):
        weights = [generate_weight_vector() for i in range(100)]
        for w in weights:
            self.assertIsNotNone(w, "Weight returned from generate_weight_vector() is None.")

            b  = w[0]
            w1 = w[1]
            w2 = w[2]

            self.assertTrue(  0 < b  < 10, "Invalid weight.")
            self.assertTrue(  0 < w1 < 10, "Invalid weight.")
            self.assertTrue(-10 < w2 <  0, "Invalid weight.")

    def test_evaluate(self):
        # 1*1 + 1*1 + 1*1 = 1 + 1 + 1 = 3
        self.assertEqual(evaluate([ 1,  1,  1], [ 1,  1,  1]),  1, "<1,1,1>*<1,1,1> should classify as 1, but it did not.")

        # -1*1 + -1*1 + -1*1 = -1 + -1 + -1 = -3
        self.assertEqual(evaluate([-1, -1, -1], [ 1,  1,  1]), -1, "<1,1,1>*<1,1,1> should classify as -1, but it did not.")

        # -1*-1 + -1*-1 + -1*-1 = 1 + 1 + 1 = 3
        self.assertEqual(evaluate([-1, -1, -1], [-1, -1, -1]),  1, "<1,1,1>*<1,1,1> should classify as 1, but it did not.")

        # 5*5 + -1*1 + -1*1 = 25 + -1 + -1 = 25 - 1 - 1 = 23
        self.assertEqual(evaluate([ 5, -1, -1], [ 5,  1,  1]),  1, "<1,1,1>*<1,1,1> should classify as 1, but it did not.")

    def test_get_update(self):
        # Test 1
        # The boundary line of w is above point x. w misclassifies x as -1, when it should be +1.

        x = (1, 2, 2)
        w = (-10, 1, 1.7)

        # Assume point x should classify as +1: y = sign(w*x) = +1
        # w misclassifies x as -1: w*x = (-10*1) + (1*2) + (1.7*2) = -10 + 2 + 3.4 = -10 + 5.4 = -4.4, sign(-4.4) = -1

        # Apply the update rule w(t + 1) = w(t) + y(x)*x:
        # (-10, 1, 1.7) + (1)*(1, 2, 2)
        # (-10, 1, 1.7) + (1, 2, 2)
        # (-10 + 1, 1 + 2, 1.7 + 2)
        # (-9, 3, 3.7)

        # We expect the updated weights to be (-9, 3, 3.4).
        result = get_update(w, x, 1)
        self.assertEqual(result, (-9, 3, 3.7))

        # Test 2
        # The boundary line of w is below point x. w misclassifies x as +1, when it should be -1.

        x = (1, 6, 6)
        w = (-10, 1, 1.5)
        y = -1

        # Assume point x should classify as -1: y = sign(w*x) = -1
        # w misclassifies as +1: w*x = (-10*1) + (1*6) + (1.5*6) = -10 + 6 + 9 = 5, sign(5) = +1

        # Apply the update rule w(t + 1) = w(t) + y(x)*x:
        # (-10, 1, 1.5) + (-1)*(1, 6, 6)
        # (-10, 1, 1.5) + (-1, -6, -6)
        # (-10 + -1, 1 + -6, 1.5 + -6)
        # (-11, -5, -4.5)

        # We expect the updated weights to be (-11, -5, -4.5).
        # This actually moves the boundary line away from the point, but the +1/-1 regions are
        # flipped so the point is correctly classified. Despite the fact that this now misclassifies +1 points
        # around (1, 6, 6), the algorithm is guaranteed to converge.
        result = get_update(w, x, y)
        self.assertEqual(result, (-11, -5, -4.5))

    def test_is_misclassified(self):
        """Return whether the specified input is correctly classified based on the
        specified weight vector.

        Keyword arguments:
        w -- the weight vector used to compute the classification in question
        x -- the input whose classification is in question
        y -- the correct classification of the point
        """
        w = (-10, 1, 1)
        x_above_line = (1, 6, 6)
        x_below_line = (1, 4, 4)

        # These are not misclassified.
        self.assertFalse(is_misclassified(w, x_above_line, 1))
        self.assertFalse(is_misclassified(w, x_below_line, -1))

        # These are misclassified.
        self.assertTrue(is_misclassified(w, x_above_line, -1))
        self.assertTrue(is_misclassified(w, x_below_line, +1))

    def test_get_misclassified_points(self):
        # The boundary line of this weight vector is the line passing through (0, 10) and (10, 0).
        w = (-10, 1, 1)

        points = [
            ((1, 6, 6), 1),  # Classified correctly
            ((1, 6, 6), -1), # Misclassified
            ((1, 4, 4), 1),  # Misclassified
            ((1, 4, 4), -1)  # Classified correctly
        ]

        # We expect get_misclassified_points to return a list containing the
        # middle two points: ((1, 6, 6), -1) and ((1, 4, 4), 1).
        result = get_misclassified_points(points, w)
        self.assertEqual(len(result), 2)
        self.assertTrue(((1, 6, 6), -1) in result)
        self.assertTrue(((1, 4, 4), 1) in result)

    def test_generate_setup(self):
        w_f, points, w = generate_setup()

        self.assertIsNotNone(w_f,       "w_f returned from generate_setup() is None.")
        self.assertIsNotNone(points, "points returned from generate_setup() is None.")
        self.assertIsNotNone(w,           "w returned from generate_setup() is None.")
        for x in points: self.assertIsNotNone(x, "a point in points returned from generate_setup() is None.")

if __name__ == '__main__':
    unittest.main()
