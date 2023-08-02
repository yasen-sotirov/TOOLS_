import unittest
import tuple_functions as tf


class TupleTest(unittest.TestCase):

    # Split Tuple

    def test_split_tuple_1(self):
        self.assertEqual(
            tf.split_tuple((1, 2, 3), 2),
            [(1,), (3,)])

    def test_split_tuple_2(self):
        self.assertEqual(
            tf.split_tuple((1, 2, 3, 2, 3, 3, 5), 2),
            [(1,), (3,), (3, 3, 5)])

    def test_split_tuple_3(self):
        self.assertEqual(
            tf.split_tuple((1, 2, 2, 2, 3, 3, 5), 2),
            [(1,), (), (), (3, 3, 5)])

    def test_split_tuple_4(self):
        self.assertEqual(
            tf.split_tuple((1, 2, 2, 2, 3, 3, 5, 2), 2),
            [(1,), (), (), (3, 3, 5), ()])

    # Merge Tuples

    def test_merge_tuples_1(self):
        self.assertEqual(
            tf.merge_tuples((1, 2, 3), (4, 5, 6)),
            [(1, 4), (2, 5), (3, 6)])

    def test_merge_tuples_2(self):
        self.assertEqual(
            tf.merge_tuples((1, 2, 3), (4, 5)),
            [(1, 4), (2, 5), (3, None)])

    def test_merge_tuples_3(self):
        self.assertEqual(
            tf.merge_tuples((1,), (4, 5, 6)),
            [(1, 4), (None, 5), (None, 6)])

    def test_merge_tuples_4(self):
        self.assertEqual(
            tf.merge_tuples((), (4, 5, 6)),
            [(None, 4), (None, 5), (None, 6)])

    # Sum Tuples

    def test_sum_tuples_1(self):
        self.assertEqual(tf.sum_tuples((1, 2, 3), (4, 5, 6)), (5, 7, 9))

    def test_sum_tuples_2(self):
        self.assertEqual(tf.sum_tuples((1, 2, 3), (4, 5)), (5, 7, 3))

    def test_sum_tuples_3(self):
        self.assertEqual(tf.sum_tuples((1,), (4, 5, 6)), (5, 5, 6))

    def test_sum_tuples_4(self):
        self.assertEqual(tf.sum_tuples((), (4, 5, 6)), (4, 5, 6))

    # Sum Tuple With

    def test_sum_tuple_with_1(self):
        self.assertEqual(tf.sum_tuple_with((1, 2, 3), 4), (5, 6, 7))

    def test_sum_tuple_with_2(self):
        self.assertEqual(tf.sum_tuple_with((1, 2, 3), -2), (-1, 0, 1))

    def test_sum_tuple_with_3(self):
        self.assertEqual(tf.sum_tuple_with((1,), 5), (6,))

    def test_sum_tuple_with_4(self):
        self.assertEqual(tf.sum_tuple_with((), 2), ())

    # Contains Subtuple

    def test_contains_subtuple_1(self):
        self.assertEqual(tf.contains_subtuple((2, 3), (2, 3, 4)), True)

    def test_contains_subtuple_2(self):
        self.assertEqual(tf.contains_subtuple((3, 4), (2, 3, 4)), True)

    def test_contains_subtuple_3(self):
        self.assertEqual(tf.contains_subtuple(
            (2, 3, 4, 5), (2, 3, 4, 5)), True)

    def test_contains_subtuple_4(self):
        self.assertEqual(tf.contains_subtuple((2, 3, 4, 5), (2, 3, 4)), False)

    def test_contains_subtuple_5(self):
        self.assertEqual(tf.contains_subtuple((2, 3, 5), (2, 3, 4, 5)), False)

    def test_contains_subtuple_6(self):
        self.assertEqual(tf.contains_subtuple((4, 5), (4, 3, 5)), False)

    # Delete Subtuple

    def test_delete_subtuple_1(self):
        self.assertEqual(tf.delete_subtuple((2, 3), (1, 2, 3, 4)), (1, 4))

    def test_delete_subtuple_2(self):
        self.assertEqual(tf.delete_subtuple((3, 4), (2, 3, 4)), (2,))

    def test_delete_subtuple_3(self):
        self.assertEqual(tf.delete_subtuple((2,), (2, 3, 4)), (3, 4))

    def test_delete_subtuple_4(self):
        self.assertEqual(tf.delete_subtuple((4,), (2, 3, 4)), (2, 3))

    def test_delete_subtuple_5(self):
        self.assertEqual(tf.delete_subtuple((1, 2, 3, 4), (1, 2, 3, 4)), ())

    def test_delete_subtuple_6(self):
        self.assertEqual(tf.delete_subtuple(
            (1, 3, 4), (1, 2, 3, 4)), (1, 2, 3, 4))

    # Subtuple Index

    def test_subtuple_index_1(self):
        self.assertEqual(tf.subtuple_index((2, 3), (1, 2, 3, 4)), 1)

    def test_subtuple_index_2(self):
        self.assertEqual(tf.subtuple_index((3, 4), (2, 3, 4)), 1)

    def test_subtuple_index_3(self):
        self.assertEqual(tf.subtuple_index((2,), (2, 3, 4)), 0)

    def test_subtuple_index_4(self):
        self.assertEqual(tf.subtuple_index((4,), (2, 3, 4)), 2)

    def test_subtuple_index_5(self):
        self.assertEqual(tf.subtuple_index((1, 2, 3, 4), (1, 2, 3, 4)), 0)

    def test_subtuple_index_6(self):
        self.assertEqual(tf.subtuple_index((1, 3, 4), (1, 2, 3, 4)), -1)

    # Insert Subtuple

    def test_insert_subtuple_1(self):
        self.assertEqual(
            tf.insert_subtuple((2, 3), (1, 2, 5, 6), 2),
            (1, 2, 2, 3, 5, 6))

    def test_insert_subtuple_2(self):
        self.assertEqual(
            tf.insert_subtuple((1,), (2, 3, 4), 0),
            (1, 2, 3, 4))

    def test_insert_subtuple_3(self):
        self.assertEqual(
            tf.insert_subtuple((4,), (1, 2, 3), 3),
            (1, 2, 3, 4))

    def test_insert_subtuple_4(self):
        self.assertEqual(
            tf.insert_subtuple((4,), (1, 2, 3), 2),
            (1, 2, 4, 3))

    def test_insert_subtuple_5(self):
        self.assertEqual(tf.insert_subtuple(
            (2, 3, 4, 5), (1, 6), 1),
            (1, 2, 3, 4, 5, 6))

    def test_insert_subtuple_6(self):
        self.assertEqual(
            tf.insert_subtuple((2, 3, 4, 5), (1, 6), -1),
            (1, 6))

    # Concat Subtuple

    def test_concant_tuples_1(self):
        self.assertEqual(
            tf.concat_tuples((2, 3), (1, 2, 5, 6), (2,)),
            (2, 3, 1, 2, 5, 6, 2))

    def test_concant_tuples_2(self):
        self.assertEqual(
            tf.concat_tuples((1,), (2, 3, 4), (0,)),
            (1, 2, 3, 4, 0))

    def test_concant_tuples_3(self):
        self.assertEqual(tf.concat_tuples((4,)), (4,))

    def test_concant_tuples_4(self):
        self.assertEqual(
            tf.concat_tuples((2, 3, 4, 5), (1, 6), (1, 1, 1, 1)),
            (2, 3, 4, 5, 1, 6, 1, 1, 1, 1))

    def test_concant_tuples_5(self):
        self.assertEqual(
            tf.concat_tuples((2, 3, 4, 5), (1, 6), (-1, 2), (3,)),
            (2, 3, 4, 5, 1, 6, -1, 2, 3))

    def test_concant_tuples_6(self):
        self.assertEqual(tf.concat_tuples(), ())

    # Replace Subtuple

    def test_replace_subtuple_1(self):
        self.assertEqual(
            tf.replace_subtuple((2, 3), (7, 8), (1, 2, 3, 4)),
            (1, 7, 8, 4))

    def test_replace_subtuple_2(self):
        self.assertEqual(
            tf.replace_subtuple((3, 4), (4, 3), (2, 3, 4)),
            (2, 4, 3))

    def test_replace_subtuple_3(self):
        self.assertEqual(
            tf.replace_subtuple((2,), (1,), (2, 3, 4)),
            (1, 3, 4))

    def test_replace_subtuple_4(self):
        self.assertEqual(
            tf.replace_subtuple((4,), (2,), (2, 3, 4)),
            (2, 3, 2))

    def test_replace_subtuple_5(self):
        self.assertEqual(
            tf.replace_subtuple((1, 2, 3, 4), (5, 6, 7, 8), (1, 2, 3, 4)),
            (5, 6, 7, 8))

    def test_replace_subtuple_6(self):
        self.assertEqual(
            tf.replace_subtuple((1, 2), (5, 6, 7, 8), (1, 2, 3, 4)),
            (5, 6, 7, 8, 3, 4))
