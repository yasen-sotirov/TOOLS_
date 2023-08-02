<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# Hackathon

## Description

Your task is to implement functions that work with <span style='color:#00bbff'>**tuples**</span> and <span style='color:#00bbff'>**dicts**</span>

## Getting Started

Create a private repository in GitHub and give access to all buddy group members.

One person from your buddy group has to _push_ a copy of the template folder to that repository. Other members should clone that repository on their computers. Get familiar with the functions, read the requirements, and gather with your buddy group to distribute your tasks and form a plan. 
Each member is responsible for committing and pushing their functions to the repository.

You have **48** hours.


## Requirements
- **Add a .gitignore file** to your buddy group repo. You can use the one from this repo.
- Please, **do not change** the function signatures (name and parameters).
- **Do not rename** any of the files in the provided template.
- You are allowed to create as many new functions as you like.
- **Each member _must_ implement at least 4 functions.**
- **Each member _must_ be able to explain how and why the entire project works the way it does.** 
- Each function **must** have a _docstring_. ([_Quick start on docstrings_](https://www.programiz.com/python-programming/docstrings))

### Docstring Example

```python
def sum_numbers(a, b = 0):
    '''Sum two numbers\n
    [a] - first number\n
    [b] - second number (optional, default = 0)
    '''
    return a + b
```

As a result, the IDE will generate the following documentation when mousing over the function

```python
Sum two numbers
[a] - first number
[b] - second number (optional, default = 0)
```

Good luck!

### Table of Contents
_Dictionary functions:_

- [`From String`](#from-string)
- [`Aggregate`](#aggregate)
- [`Aggregate Min`](#aggregate-min)
- [`Aggregate Max`](#aggregate-max)
- [`Aggregate Sorted`](#aggregate-sorted)
- [`Aggregate Avg`](#aggregate-avg)
- [`Aggregate Sum`](#aggregate-sum)
- [`Aggregate Count`](#aggregate-count)
- [`With Keys`](#with-keys)
- [`Exclude Keys`](#exclude-keys)
- [`Dicts Union Preserve`](#dicts-union-preserve)
- [`Dicts Union Override`](#dicts-union-override)
- [`Dicts Symmetric Difference`](#dicts-symmetric-difference)
- [`Dicts Difference`](#dicts-difference)
- [`Dicts Intersection`](#dicts-intersection)
- [`Dict Flatten`](#dict-flatten)
- [`Dict Keysort`](#dict-keysort)
- [`Dict Valuesort`](#dict-valuesort)

_Tuple functions:_

- [`Split Tuple`](#split-tuple)
- [`Merge Tuples`](#merge-tuples)
- [`Sum Tuples`](#sum-tuples)
- [`Sum Tuple With`](#sum-tuple-with)
- [`Contains Subtuple`](#contains-subtuple)
- [`Delete Subtuple`](#delete-subtuple)
- [`Subtuple Index`](#subtuple-index)
- [`Insert Subtuple`](#insert-subtuple)
- [`Concat Tuples`](#concat-tuples)
- [`Replace Subtuple`](#replace-subtuple)

---

## `From String`


_Parses a dictionary from a string._

#### Parameters

`the_string` <span style='color:#00bbff'>_(str)_</span> - _The source string_  
`pair_sep` <span style='color:#00bbff'>_(str)_</span> - _Pair separator_ (default = `','`)  
`kv_sep` <span style='color:#00bbff'>_(str)_</span> - _Key-Value separator_ (default = `'='`)  
`value_type` <span style='color:#00bbff'>_(str)_</span> - _Type of the value:('str', 'int', 'float')_ (default = `'str'`)  

#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The parsed dictionary_

#### Example

```python
the_dict = from_string('Bulgaria=Sofia,Greece=Athens')
# the_dict: {'Bulgaria': 'Sofia', 'Greece': 'Athens'}

the_dict = from_string('Bulgaria->Sofia,Greece->Athens', kv_sep='->')
# the_dict: {'Bulgaria': 'Sofia', 'Greece': 'Athens'}

the_dict = from_string('Sofia=1500000,Athens=2500000', value_type='int')
# the_dict: {'Sofia': 1500000, 'Athens': 2500000} # notice that values are now ints 
```

## `Aggregate`


_Aggregates a list of 2-tuples into a dictionary. Values with duplicate keys are grouped into a list._

#### Parameters

`data` <span style='color:#00bbff'>_(list)_</span> - _The list of 2-tuples_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The aggregated dictionary_

#### Example

```python
data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate(data)
# the_dict: {'Jack': [2,4], 'Steven': [3], 'Alice': [4]}
```

## `Aggregate Min`

_Aggregates a list of 2-tuples into a dictionary. The minimal of values with duplicate keys is assigned for each unique key_

#### Parameters

`data` <span style='color:#00bbff'>_(list)_</span> - _The list of 2-tuples_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The aggregated dictionary_

#### Example

```python
data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate_min(data)
# the_dict: {'Jack': 2, 'Steven': 3, 'Alice': 4}
```

## `Aggregate Max`


_Aggregates a list of 2-tuples into a dictionary. The maximum of values with duplicate keys is assigned for each unique key_

#### Parameters

`data` <span style='color:#00bbff'>_(list)_</span> - _The list of 2-tuples_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The aggregated dictionary_

#### Example

```python
data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate_max(data)
# the_dict: {'Jack': 4, 'Steven': 3, 'Alice': 4}
```

## `Aggregate Sorted`


_Aggregates a list of 2-tuples into a dictionary. The values for duplicate keys are sorted in increasing or decreasing order._

#### Parameters

`data` <span style='color:#00bbff'>_(list)_</span> - _The list of 2-tuples_  
`reverse` <span style='color:#00bbff'>_(bool)_</span> - Normal or Reverse sort (default = `False`)  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The aggregated dictionary_

#### Example

```python
data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate_sorted(data)
# the_dict: {'Jack': [2,4], 'Steven': [3], 'Alice': [4]}

data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate_sorted(data, reverse=True)
# the_dict: {'Jack': [4,2], 'Steven': [3], 'Alice': [4]}
```

## `Aggregate Avg`


_Aggregates a list of 2-tuples into a dictionary. The average of values for each unique key is aggregated._

#### Parameters

`data` <span style='color:#00bbff'>_(list)_</span> - _The list of 2-tuples_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The aggregated dictionary_

#### Example

```python
data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate_avg(data)
# the_dict: {'Jack': 3.0, 'Steven': 3.0, 'Alice': 4.0}
```

## `Aggregate Sum`

_Aggregates a list of 2-tuples into a dictionary. The sum of values for each unique key is aggregated._

#### Parameters

`data` <span style='color:#00bbff'>_(list)_</span> - _The list of 2-tuples_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The aggregated dictionary_

#### Example

```python
data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate_sum(data)
# the_dict: {'Jack': 6, 'Steven': 3, 'Alice': 4}
```

## `Aggregate Count`

_Aggregates a list of 2-tuples into a dictionary. The count of values for each unique key is aggregated._

#### Parameters

`data` <span style='color:#00bbff'>_(list)_</span> - _The list of 2-tuples_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The aggregated dictionary_

#### Example

```python
data = [('Jack', 2), ('Steven', 3), ('Alice', 4), ('Jack', 4)]
the_dict = aggregate_count(data)
# the_dict: {'Jack': 2, 'Steven': 1, 'Alice': 1}
```

## `With Keys`

_Returns a new dictionary consisting only of the keys specified in the keyset. Non-existing keys are ignored._

#### Parameters

`the_dict` <span style='color:#00bbff'>_(dict)_</span> - _The source dictionary_  
`keyset` <span style='color:#00bbff'>_(set)_</span> - _The set of keys_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The resulting dictionary_

#### Example

```python
the_dict = {'Steven': 25, 'Jack': 21, 'Alice': 31, 'John': 41}
key_set = {'Steven', 'Jack', 'Bob'}
new_dict = with_keys(the_dict, key_set))
# new_dict: {'Steven': 25, 'Jack': 21}
```

## `Exclude Keys`


_Returns a new dictionary consisting only of the keys NOT specified in the keyset._

#### Parameters

`the_dict` <span style='color:#00bbff'>_(dict)_</span> - _The source dictionary_  
`keyset` <span style='color:#00bbff'>_(set)_</span> - _The set of keys_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The resulting dictionary_

#### Example

```python
the_dict = {'Steven': 25, 'Jack': 21, 'Alice': 31, 'John': 41}
key_set = {'Steven', 'Jack', 'Bob'}
new_dict = exclude_keys(the_dict, key_set))
# new_dict: {'Alice': 31, 'John': 41}
```

## `Dicts Union Preserve`



_Returns a new dictionary where for duplicate keys, values are preserved in a list._

#### Parameters

`first_dict` <span style='color:#00bbff'>_(dict)_</span> - _The first dictionary_  
`second_dict` <span style='color:#00bbff'>_(dict)_</span> - _The second dictionary_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The resulting dictionary_

#### Example

```python
first_dict = {'Steven': 25, 'Jack': 21, 'Alice': 31, 'John': 41}
second_dict = {'Steven': 31, 'Jack': 17, 'Bob': 33}
new_dict = dicts_union_preserve(first_dict, second_dict)
# new_dict: {'Steven': [25, 31], 'Jack': [21, 17], 'Alice': [31], 'John': [41], 'Bob': [33]}
```

## `Dicts Union Override`


_Returns a new dictionary where for duplicate keys, the second value override the first value._

#### Parameters

`first_dict` <span style='color:#00bbff'>_(dict)_</span> - _The first dictionary_  
`second_dict` <span style='color:#00bbff'>_(dict)_</span> - _The second dictionary_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The resulting dictionary_

#### Example

```python
first_dict = {'Steven': 25, 'Jack': 21, 'Alice': 31, 'John': 41}
second_dict = {'Steven': 31, 'Jack': 17, 'Bob': 33}
new_dict = dicts_union_override(first_dict, second_dict)
# new_dict: {'Steven': 31, 'Jack': 17, 'Alice': 31, 'John': 41, 'Bob': 33}
```

## `Dicts Symmetric Difference`



_Returns a new dictionary where duplicate keys are excluded._

#### Parameters

`first_dict` <span style='color:#00bbff'>_(dict)_</span> - _The first dictionary_  
`second_dict` <span style='color:#00bbff'>_(dict)_</span> - _The second dictionary_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The resulting dictionary_

#### Example

```python
first_dict = {'Steven': 25, 'Jack': 21, 'Alice': 31, 'John': 41}
second_dict = {'Steven': 31, 'Jack': 17, 'Bob': 33}
new_dict = dicts_symmetric_difference(first_dict, second_dict)
# new_dict: {'Alice': 31, 'John': 41, 'Bob': 33}
```

## `Dicts Difference`


_Returns a new dictionary from keys in the first dictionary that are not present in the second dictionary._

#### Parameters

`first_dict` <span style='color:#00bbff'>_(dict)_</span> - _The first dictionary_  
`second_dict` <span style='color:#00bbff'>_(dict)_</span> - _The second dictionary_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The resulting dictionary_

#### Example

```python
first_dict = {'Steven': 25, 'Jack': 21, 'Alice': 31, 'John': 41}
second_dict = {'Steven': 31, 'Jack': 17, 'Bob': 33}

new_dict = dicts_difference(first_dict, second_dict)
# new_dict: {'Alice': 31, 'John': 41}

new_dict = dicts_difference(second_dict, first_dict)
# new_dict: {'Bob': 33}
```

## `Dicts Intersection`



_Returns a new dictionary from duplicate keys in both dictionaries where values are preserved in a list._

#### Parameters

`first_dict` <span style='color:#00bbff'>_(dict)_</span> - _The first dictionary_  
`second_dict` <span style='color:#00bbff'>_(dict)_</span> - _The second dictionary_  


#### Returns

<span style='color:#00bbff'>_(dict)_</span> - _The resulting dictionary_

#### Example

```python
first_dict = {'Steven': 25, 'Jack': 21, 'Alice': 31, 'John': 41}
second_dict = {'Steven': 31, 'Jack': 17, 'Bob': 33}
new_dict = dicts_intersection(first_dict, second_dict)
# new_dict: {'Steven': [25, 31], 'Jack': [21, 17]}
```

## `Dict Flatten`



_Returns a list containing all the values from a dictionary where the values are also list.

#### Parameters

`the_dict` <span style='color:#00bbff'>_(dict)_</span> - _The dictionary where values are lists_ 


#### Returns

<span style='color:#00bbff'>_(list)_</span> - _The resulting list

#### Example

```python
test_dict = {'Steven': [1, 2], 'Alice': [1, 3, 5]}
lst = dict_flatten(test_dict)
#lst: [1, 2, 1, 3, 5]
```

## `Dict Keysort`

_Returns a list of tuples containing the dictionary key:value pairs sorted by key

#### Parameters

`the_dict` <span style='color:#00bbff'>_(dict)_</span> - _The source dictionary_

#### Returns

<span style='color:#00bbff'>_(list)_</span> - _The resulting list of tuples_

#### Example

```python
a_dict = {'Steven': 20, 'Alice': 21, 'John':22}
lst = dict_keysort(a_dict)
# lst: [('Alice', 21), ('John', 22), ('Steven', 20)]
```

## `Dict Valuesort`

_Returns a list of tuples containing the dictionary key:value pairs sorted by value

#### Parameters

`the_dict` <span style='color:#00bbff'>_(dict)_</span> - _The source dictionary_

#### Returns

<span style='color:#00bbff'>_(list)_</span> - _The resulting list of tuples_

#### Example

```python
a_dict = {'Steven': 21, 'Alice': 23, 'John': 18}
lst = dict_valuesort(a_dict)
# lst: [('John', 18), ('Steven', 21), ('Alice', 23)]
```

## `Split Tuple`

_Returns a list of tuples created by splitting a larger tuple at provided splitter_

#### Parameters

`the_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The tuple to be split_  
`splitter` <span style='color:#00bbff'>_(any)_</span> - _Value that splits the tuple_

#### Returns

<span style='color:#00bbff'>_(list)_</span> - _List containing the tuple parts_

#### Example

```python
lst = split_tuple((1,2,3,4,5), 3)
# lst: [(1,2), (4,5)]
lst = split_tuple((1,2,3,4,5,3,6,7), 3)
# lst: [(1, 2), (4, 5), (6, 7)]
```

## `Merge Tuples`

_Returns a list of 2-tuples that is the product of the merging of two variable-length tuples. None is used to fill missing values in case of different lengths._

#### Parameters

`first_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The first tuple_    
`second_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The second tuple_

#### Returns

<span style='color:#00bbff'>_(list)_</span> - _List containing the merge 2-tuples_

#### Example

```python
lst = merge_tuples((1, 2, 3), (4, 5, 6))
# lst: [(1, 4), (2, 5), (3, 6)]

lst = merge_tuples((1, 2, 3), (4, 5))
# lst: [(1, 4), (2, 5), (3, None)]
```

## `Sum Tuples`

_Returns a new tuple that is the result of the summing of two other tuples._

#### Parameters

`first_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The first tuple_    
`second_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The second tuple_

#### Returns

<span style='color:#00bbff'>_(tuple)_</span> - _The resulting summed tuple_

#### Example

```python
result = sum_tuples((1, 2, 3), (4, 5, 6))
# result: (5, 7, 9)

result = sum_tuples((1, 2, 3), (4, 5))
# result: (5, 7, 3)
```

## `Sum Tuple With`

_Returns a new tuple that is the result of a number added to each of another tuples values._

#### Parameters

`the_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The source tuple_    
`number` <span style='color:#00bbff'>_(int)_</span> - _The number to add to each tuple value_

#### Returns

<span style='color:#00bbff'>_(tuple)_</span> - _The resulting summed tuple_

#### Example

```python
result = sum_tuple_with((1, 2, 3), 2)
# result: (3, 4, 5)

result = sum_tuple_with((1, 2, 3), -2)
# result: (-1, 0, 1)
```

## `Contains Subtuple`

_Returns a bool indicating whether a smaller tuple is a subrange of a larger tuple._

#### Parameters

`sub_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The tuple to check whether it's a part of the larger tuple_    
`the_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The larger tuple_

#### Returns

<span style='color:#00bbff'>_(bool)_</span> - _The result of the check_

#### Example

```python
is_subtuple = contains_subtuple((2,3), (1,2,3))
# is_subtuple: True

is_subtuple = contains_subtuple((1,3), (1,2,3))
# is_subtuple: False
```

## `Delete Subtuple`

_Returns a new tuple that is the result of a subtuple removed from a larger one. Returns the larger tuple if it does not contain the smaller one._

#### Parameters

`sub_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The tuple to be removed_    
`the_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The larger tuple_

#### Returns

<span style='color:#00bbff'>_(tuple)_</span> - _The resulting tuple_

#### Example

```python
new_tuple = delete_subtuple((2,3), (1,2,3,4))
# new_tuple: (1,4)

new_tuple = delete_subtuple((1,3), (1,2,3,4))
# new_tuple: (1,2,3,4)
```

## `Subtuple Index`

_Returns the index from where a subtuple starts in a large tuple, or -1 if it is not contained in it._

#### Parameters

`sub_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The smaller tuple_    
`the_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The larger tuple_

#### Returns

<span style='color:#00bbff'>_(int)_</span> - _The starting index_

#### Example

```python
idx = subtuple_index((2,3), (1,2,3,4))
# idx: 1

idx = subtuple_index((1,3), (1,2,3,4))
# idx: -1
```

## `Insert Subtuple`

_Returns a new tuple that is the result of a tuple inserted into another one at a specified index. Returns the second tuple, if the insertion index is invalid._

#### Parameters

`sub_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The tuple to be inserted_    
`the_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The tuple to insert at_   
`index` <span style='color:#00bbff'>_(int)_</span> - _The insertion index_   

#### Returns

<span style='color:#00bbff'>_(tuple)_</span> - _The result of the insertion._

#### Example

```python
new_tuple = insert_subtuple((2,3), (1,4), 1)
# new_tuple: (1, 2, 3, 4)
new_tuple = insert_subtuple((2,3), (1,4), 2)
# new_tuple: (1, 4, 2, 3)
new_tuple = insert_subtuple((2,3), (1,4), 3)
# new_tuple: (1, 4)
```

## `Concat Tuples`

_Returns a new tuple that is the result of the concatenation of zero or more other tuples._

#### Parameters

`*tuples` <span style='color:#00bbff'>_(variable-length argument list)_</span> - _The zero or more tuples to concat_    

#### Returns

<span style='color:#00bbff'>_(tuple)_</span> - _The result of the concatenation._

#### Example

```python
new_tuple = concat_tuples()
# new_tuple: ()
new_tuple = concat_tuples((2,3), (1,4))
# new_tuple: (2, 3, 1, 4)
new_tuple = concat_tuples((2,3), (1,4), (2,3))
# new_tuple: (2, 3, 1, 4, 2, 3)
```

## `Replace Subtuple`

_Replace a subtuple in a tuple with a new subtuple. Returns the original tuple if it does not contain the subtuple to be replaced._

#### Parameters

`sub_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The subtuple to be replace_    
`new_sub_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The new subtuple_  
`the_tuple` <span style='color:#00bbff'>_(tuple)_</span> - _The target tuple_  

#### Returns

<span style='color:#00bbff'>_(tuple)_</span> - _The resulting tuple_

#### Example

```python
new_tuple = replace_subtuple((1,2), (3,4), (1,2,3,4))
# new_tuple: (3, 4, 3, 4)
new_tuple = replace_subtuple((2,3), (3,4,5), (1,2,3,4))
# new_tuple: (1, 3, 4, 5, 4)
new_tuple = replace_subtuple((1,3), (3,4,5), (1,2,3,4))
# new_tuple: (1, 2, 3, 4)
```
