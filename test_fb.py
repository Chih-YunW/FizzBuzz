import fizzBuzz

def test_print_FizzBuzz():
	value = (15)
	assert fizzBuzz.fizzBuzz(value) == "FizzBuzz"
def test_print_Fizz():
	value = (3)
	assert fizzBuzz.fizzBuzz(value) == "Fizz"
def test_print_Buzz():
        value = (5)
        assert fizzBuzz.fizzBuzz(value) == "Buzz"

