from cool_package import cool_function, not_covered, this_is_not_covered

def test_cool_function():
    assert cool_function() == "Hello from cool_function!"


def test_not_covered():
    not_covered()  # not covered by tests
    this_is_not_covered()
