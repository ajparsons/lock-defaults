import inspect

from lock_defaults import lockmutabledefaults


def test_demonstrate_problem_list_sig():
    def example(value=[]):
        value.append(1)
        return value

    example()
    assert inspect.signature(example).parameters["value"].default == [1]
    example()
    assert inspect.signature(example).parameters["value"].default == [1, 1]
    example()
    assert inspect.signature(example).parameters["value"].default == [1, 1, 1]
    example()
    assert inspect.signature(example).parameters["value"].default == [1, 1, 1, 1]


def test_problem_list_sig():
    @lockmutabledefaults
    def example(value=[]):
        value.append(1)
        return value

    example()
    assert inspect.signature(example).parameters["value"].default == []
    example()
    assert inspect.signature(example).parameters["value"].default == []
    example()
    assert inspect.signature(example).parameters["value"].default == []


def test_demonstrate_problem_list():
    def example(value=[]):
        value.append(1)
        return value

    assert example() == [1]
    assert example() == [1, 1]
    assert example() == [1, 1, 1]
    assert example() == [1, 1, 1, 1]


def test_lock_list():
    @lockmutabledefaults
    def example(value=[]):
        value.append(1)
        return value

    assert example() == [1]
    assert example() == [1]
    assert example() == [1]


def test_it_still_takes_value():
    @lockmutabledefaults
    def example(value=[]):
        value.append(1)
        return value

    assert example([10]) == [10, 1]
    assert example([5]) == [5, 1]
    assert example([2]) == [2, 1]


def test_lock_list_with_kw_only():
    @lockmutabledefaults
    def example(*, value=[]):
        value.append(1)
        return value

    assert example() == [1]
    assert example() == [1]
    assert example() == [1]


def demonstrate_problem_dict():
    def example(value={"foo": 0}):
        value["foo"] += 1
        return value["foo"]

    assert example() == 1
    assert example() == 2
    assert example() == 3


def test_lock_dict():
    @lockmutabledefaults
    def example(value={"foo": 0}):
        value["foo"] += 1
        return value["foo"]

    assert example() == 1
    assert example() == 1
    assert example() == 1


def test_demonstrate_problem_set():
    def example(value=set([1])):
        value.update([len(value) + 1])
        return value

    assert example() == set([1, 2])
    assert example() == set([1, 2, 3])
    assert example() == set([1, 2, 3, 4])


def test_lock_set():
    @lockmutabledefaults
    def example(value=set([1])):
        value.update([len(value) + 1])
        return value

    assert example() == set([1, 2])
    assert example() == set([1, 2])
    assert example() == set([1, 2])
