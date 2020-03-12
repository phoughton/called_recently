# called_recently is an example implementation of an interview question.
## Specification

The goal is to create a function that will return `True` if the method has been called in the last 3 seconds.
The function should return `False` if it has not been called in the previous 3 seconds.

## Tests

I have included a small set of PyTest tests to check the behaviour of the function.
The function allows you to inject the python time class, 
this allows our tests to mock the current time and therefore not have slow running tests full of hard sleeps. 

The tests can be run with:
```bash
pytest basic_tests.py
```
