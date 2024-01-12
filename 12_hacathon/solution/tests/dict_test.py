import unittest
import dict_functions as df

data1 = [('pesho', 4), ('gosho', 3), ('losho', 4),
         ('losho', 5), ('losho', 6), ('losho', 2), ('pesho', 2)]
data2 = [('pesho', 2), ('pesho', 3), ('pesho', 4)]
data3 = [('pesho', 2), ('pesho', 3), ('pesho', 4), ('gosho', 4)]


class DictTest(unittest.TestCase):

    # From String

    def test_from_string_1(self):
        test_str = 'a=b,b=c,c=d,d=e,e=f'
        expected_dict = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f'}
        self.assertDictEqual(df.from_string(test_str), expected_dict)

    def test_from_string_2(self):
        test_str = 'abc=b,b=cba,cd=de,df=efg,ef=fghi'
        expected_dict = {'abc': 'b', 'b': 'cba', 'cd': 'de', 'df': 'efg', 'ef': 'fghi'}
        self.assertDictEqual(df.from_string(test_str), expected_dict)

    def test_from_string_3(self):
        test_str = 'a=b|b=c|c=d|d=e|e=f'
        expected_dict = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f'}
        self.assertDictEqual(
            df.from_string(test_str, pair_sep='|'),
            expected_dict)

    def test_from_string_4(self):
        test_str = 'a->b,b->c,c->d,d->e,e->f'
        expected_dict = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f'}
        self.assertDictEqual(
            df.from_string(test_str, kv_sep='->'),
            expected_dict)

    def test_from_string_5(self):
        test_str = 'a->b|b->c|c->d|d->e|e->f'
        expected_dict = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f'}
        self.assertDictEqual(
            df.from_string(test_str, pair_sep='|', kv_sep='->'),
            expected_dict)
    
    def test_from_string_6(self):
        test_str = 'a=1.5,b=2.5,c=3.33,d=-0.21,e=0.0'
        expected_dict = {'a': 1.5, 'b': 2.5, 'c': 3.33, 'd': -0.21, 'e': 0.0}
        self.assertDictEqual(
            df.from_string(test_str, value_type='float'),
            expected_dict)

    def test_from_string_7(self):
        test_str = 'a=1,b=2,c=3,d=-2,e=0'
        expected_dict = {'a': 1, 'b': 2, 'c': 3, 'd': -2, 'e': 0}
        self.assertDictEqual(
            df.from_string(test_str, value_type='float'),
            expected_dict)

    # Aggregate

    def test_aggregate_1(self):
        self.assertDictEqual(
            df.aggregate(data1),
            {'pesho': [4, 2], 'gosho': [3], 'losho': [4, 5, 6, 2]})

    def test_aggregate_2(self):
        self.assertDictEqual(
            df.aggregate(data2),
            {'pesho': [2, 3, 4]})

    def test_aggregate_3(self):
        self.assertDictEqual(
            df.aggregate(data3),
            {'pesho': [2, 3, 4], 'gosho': [4]})

    # Aggregate Min

    def test_aggregate_min_1(self):
        self.assertDictEqual(
            df.aggregate_min(data1),
            {'pesho': 2, 'gosho': 3, 'losho': 2})

    def test_aggregate_min_2(self):
        self.assertDictEqual(
            df.aggregate_min(data2),
            {'pesho': 2})

    def test_aggregate_min_3(self):
        self.assertDictEqual(
            df.aggregate_min(data3),
            {'pesho': 2, 'gosho': 4})

    # Aggregate Max

    def test_aggregate_max_1(self):
        self.assertDictEqual(
            df.aggregate_max(data1),
            {'pesho': 4, 'gosho': 3, 'losho': 6})

    def test_aggregate_max_2(self):
        self.assertDictEqual(
            df.aggregate_max(data2),
            {'pesho': 4})

    def test_aggregate_max_3(self):
        self.assertDictEqual(
            df.aggregate_max(data3),
            {'pesho': 4, 'gosho': 4})

    # Aggregate Sorted

    def test_aggregate_sorted_1(self):
        self.assertDictEqual(
            df.aggregate_sorted(data1),
            {'pesho': [2, 4], 'gosho': [3], 'losho': [2, 4, 5, 6]})

    def test_aggregate_sorted_2(self):
        self.assertDictEqual(
            df.aggregate_sorted(data1, reverse=True),
            {'pesho': [4, 2], 'gosho': [3], 'losho': [6, 5, 4, 2]})

    def test_aggregate_sorted_3(self):
        self.assertDictEqual(
            df.aggregate_sorted(data2),
            {'pesho': [2, 3, 4]})

    def test_aggregate_sorted_4(self):
        self.assertDictEqual(
            df.aggregate_sorted(data2, reverse=True),
            {'pesho': [4, 3, 2]})

    def test_aggregate_sorted_5(self):
        self.assertDictEqual(
            df.aggregate_sorted(data3),
            {'pesho': [2, 3, 4], 'gosho': [4]})

    def test_aggregate_sorted_6(self):
        self.assertDictEqual(
            df.aggregate_sorted(data3, reverse=True),
            {'pesho': [4, 3, 2], 'gosho': [4]})

    # Aggregate Avg

    def test_aggregate_avg_1(self):
        self.assertDictEqual(
            df.aggregate_avg(data1),
            {'pesho': 3.0, 'gosho': 3.0, 'losho': 4.25})

    def test_aggregate_avg_2(self):
        self.assertDictEqual(
            df.aggregate_avg(data2),
            {'pesho': 3.0})

    def test_aggregate_avg_3(self):
        self.assertDictEqual(
            df.aggregate_avg(data3),
            {'pesho': 3.0, 'gosho': 4.0})

    # Aggregate Sum

    def test_aggregate_sum_1(self):
        self.assertDictEqual(
            df.aggregate_sum(data1),
            {'pesho': 6, 'gosho': 3, 'losho': 17})

    def test_aggregate_sum_2(self):
        self.assertDictEqual(
            df.aggregate_sum(data2),
            {'pesho': 9})

    def test_aggregate_sum_3(self):
        self.assertDictEqual(
            df.aggregate_sum(data3),
            {'pesho': 9, 'gosho': 4})

    # Aggregate Count

    def test_aggregate_count_1(self):
        self.assertDictEqual(
            df.aggregate_count(data1),
            {'pesho': 2, 'gosho': 1, 'losho': 4})

    def test_aggregate_count_2(self):
        self.assertDictEqual(
            df.aggregate_count(data2),
            {'pesho': 3})

    def test_aggregate_count_3(self):
        self.assertDictEqual(
            df.aggregate_count(data3),
            {'pesho': 3, 'gosho': 1})

    # With Keys

    def test_with_keys_inputDictNotModified(self):
        input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        copy = input_dict.copy()
        
        df.with_keys(input_dict, {'a', 'b', 'e'})

        self.assertDictEqual(copy, input_dict)

    def test_with_keys_1(self):
        self.assertDictEqual(
            df.with_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'a', 'b', 'e'}),
            {'a': 1, 'b': 2})

    def test_with_keys_2(self):
        self.assertDictEqual(
            df.with_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'c', 'd'}),
            {'c': 3, 'd': 4})

    def test_with_keys_3(self):
        self.assertDictEqual(
            df.with_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'e', 'f'}),
            {})

    # Exclude Keys

    def test_exclude_keys_inputDictNotModified(self):
        input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        copy = input_dict.copy()
        
        df.exclude_keys(input_dict, {'a', 'b', 'e'})

        self.assertDictEqual(copy, input_dict)

    def test_exclude_keys_1(self):
        self.assertDictEqual(
            df.exclude_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'a', 'b', 'e'}),
            {'c': 3, 'd': 4})

    def test_exclude_keys_2(self):
        self.assertDictEqual(
            df.exclude_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4},  {'c', 'd'}),
            {'a': 1, 'b': 2})

    def test_exclude_keys_3(self):
        self.assertDictEqual(
            df.exclude_keys({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'f', 'g', 'h'}),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    # Dicts Union Preserve

    def test_dicts_union_preserve_inputDictsNotModified(self):
        first_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        first_dict_copy = first_dict.copy()
        second_dict = {'a': 5, 'b': 6, 'c': 7, 'e': 8}
        second_dict_copy = second_dict.copy()

        df.dicts_union_preserve(first_dict, second_dict)

        self.assertDictEqual(first_dict_copy, first_dict)
        self.assertDictEqual(second_dict_copy, second_dict)

    def test_dicts_union_preserve_1(self):
        self.assertDictEqual(
            df.dicts_union_preserve(
                {'a': 1, 'b': 2, 'c': 3, 'd': 4},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'a': [1, 5], 'b': [2, 6], 'c': [3, 7], 'd': [4], 'e': [8]})

    def test_dicts_union_preserve_2(self):
        self.assertDictEqual(
            df.dicts_union_preserve(
                {},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'a': [5], 'b': [6], 'c': [7], 'e': [8]})

    def test_dicts_union_preserve_3(self):
        self.assertDictEqual(
            df.dicts_union_preserve(
                {'a': 1, 'b': 2, 'c': 3, 'd': 4},
                {}),
            {'a': [1], 'b': [2], 'c': [3], 'd': [4]})

    # Dicts Union Override

    def test_dicts_union_override_inputDictsNotModified(self):
        first_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        first_dict_copy = first_dict.copy()
        second_dict = {'a': 5, 'b': 6, 'c': 7, 'e': 8}
        second_dict_copy = second_dict.copy()

        df.dicts_union_override(first_dict, second_dict)

        self.assertDictEqual(first_dict_copy, first_dict)
        self.assertDictEqual(second_dict_copy, second_dict)

    def test_dicts_union_override_1(self):
        self.assertDictEqual(
            df.dicts_union_override(
                {'a': 1, 'b': 2, 'c': 3, 'd': 4},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'a': 5, 'b': 6, 'c': 7, 'd': 4, 'e': 8})

    def test_dicts_union_override_2(self):
        self.assertDictEqual(
            df.dicts_union_override(
                {},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'a': 5, 'b': 6, 'c': 7, 'e': 8})

    def test_dicts_union_override_3(self):
        self.assertDictEqual(
            df.dicts_union_override(
                {'a': 1, 'b': 2, 'c': 3, 'd': 4},
                {}),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    # Dicts Symmetric Difference

    def test_dicts_symmetric_difference_inputDictsNotModified(self):
        first_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        first_dict_copy = first_dict.copy()
        second_dict = {'a': 5, 'b': 6, 'c': 7, 'e': 8}
        second_dict_copy = second_dict.copy()

        df.dicts_symmetric_difference(first_dict, second_dict)

        self.assertDictEqual(first_dict_copy, first_dict)
        self.assertDictEqual(second_dict_copy, second_dict)

    def test_dicts_symmetric_difference_1(self):
        self.assertDictEqual(
            df.dicts_symmetric_difference(
                {'a': 1, 'b': 2, 'c': 3, 'd': 4},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'d': 4, 'e': 8})

    def test_dicts_symmetric_difference_2(self):
        self.assertDictEqual(
            df.dicts_symmetric_difference(
                {'a': 1, 'b': 2, 'c': 3},
                {'d': 6, 'e': 7, 'f': 8}),
            {'a': 1, 'b': 2, 'c': 3, 'd': 6, 'e': 7, 'f': 8})

    # Dicts Difference

    def test_dicts_difference_inputDictsNotModified(self):
        first_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        first_dict_copy = first_dict.copy()
        second_dict = {'a': 5, 'b': 6, 'c': 7, 'e': 8}
        second_dict_copy = second_dict.copy()

        df.dicts_difference(first_dict, second_dict)

        self.assertDictEqual(first_dict_copy, first_dict)
        self.assertDictEqual(second_dict_copy, second_dict)

    def test_dicts_difference_1(self):
        self.assertDictEqual(
            df.dicts_difference(
                {'a': 1, 'b': 2, 'c': 3, 'd': 4},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'d': 4})

    def test_dicts_difference_2(self):
        self.assertDictEqual(
            df.dicts_difference(
                {'a': 5, 'b': 6, 'c': 7, 'e': 8},
                {'a': 1, 'b': 2, 'c': 3, 'd': 4}),
            {'e': 8})

    # Dicts Intersection

    def test_dicts_intersection_inputDictsNotModified(self):
        first_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        first_dict_copy = first_dict.copy()
        second_dict = {'a': 5, 'b': 6, 'c': 7, 'e': 8}
        second_dict_copy = second_dict.copy()

        df.dicts_intersection(first_dict, second_dict)

        self.assertDictEqual(first_dict_copy, first_dict)
        self.assertDictEqual(second_dict_copy, second_dict)

    def test_dicts_intersection_1(self):
        self.assertDictEqual(
            df.dicts_intersection(
                {'a': 1, 'b': 2, 'c': 3, 'd': 4},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'a': [1, 5], 'b': [2, 6], 'c': [3, 7]})

    def test_dicts_intersection_2(self):
        self.assertDictEqual(
            df.dicts_intersection(
                {'a': 1, 'x': 2, 'c': 3, 'd': 4},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {'a': [1, 5], 'c': [3, 7]})

    def test_dicts_intersection_3(self):
        self.assertDictEqual(
            df.dicts_intersection(
                {'y': 1, 'x': 2, 'f': 3, 'd': 4},
                {'a': 5, 'b': 6, 'c': 7, 'e': 8}),
            {})

    # Dict Flatten

    def test_dict_flatten_inputDictNotModified(self):
        input_dict = {'a': [1, 2], 'b': [3, 4]}
        input_dict_copy = input_dict.copy()

        df.dict_flatten(input_dict)

        self.assertDictEqual(input_dict_copy, input_dict)

    def test_dict_flatten_1(self):
        self.assertEqual(
            df.dict_flatten({'a': [1, 2], 'b': [3, 4]}),
            [1, 2, 3, 4])

    def test_dict_flatten_2(self):
        self.assertEqual(
            df.dict_flatten({'a': [1, 2], 'b': []}),
            [1, 2])

    def test_dict_flatten_3(self):
        self.assertEqual(
            df.dict_flatten({'a': [], 'b': [3, 4]}),
            [3, 4])

    def test_dict_flatten_4(self):
        self.assertEqual(
            df.dict_flatten({'b': [3, 4]}),
            [3, 4])

    # Dict Keysort

    def test_dict_keysort_inputDictNotModified(self):
        input_dict = {'b': 5, 'a': 7, 'c': 1, 'e': 2, 'd': 4}
        input_dict_copy = input_dict.copy()

        df.dict_keysort(input_dict)

        self.assertDictEqual(input_dict_copy, input_dict)

    def test_dict_keysort_1(self):
        self.assertEqual(
            df.dict_keysort({'b': 5, 'a': 7, 'c': 1, 'e': 2, 'd': 4}),
            [('a', 7), ('b', 5), ('c', 1), ('d', 4), ('e', 2)])

    def test_dict_keysort_2(self):
        self.assertEqual(df.dict_keysort({}), [])

    # Dict Valuesort

    def test_dict_valuesort_inputDictNotModified(self):
        input_dict = {'b': 5, 'a': 7, 'c': 1, 'e': 2, 'd': 4}
        input_dict_copy = input_dict.copy()

        df.dict_valuesort(input_dict)

        self.assertDictEqual(input_dict_copy, input_dict)

    def test_dict_valuesort_1(self):
        self.assertEqual(
            df.dict_valuesort({'b': 5, 'a': 7, 'c': 1, 'e': 2, 'd': 4}),
            [('c', 1), ('e', 2), ('d', 4),  ('b', 5), ('a', 7)])

    def test_dict_valuesort_2(self):
        self.assertEqual(df.dict_valuesort({}), [])
