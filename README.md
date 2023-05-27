# wvalidate

## Introduction

WValidate is a validation library.

## Installation

### Requirements

- Python 3.8+

```sh
pip install wvalidate  
```

## Basic usage

Creating a simple string validator

```py
from wvalidate import Validate as v

# creating a validator for string
my_validator = v.string()

my_validator.is_valid("Maria") # => (True, None)
my_validator.is_valid(42) # => (False, ValidatorError)
```

Creating a dict validator

```py
from wvalidate import Validate as v

user_validator = v.dict({
  "name": v.string()
})

user_validator.is_valid({ "name": "Fernanda" }) # => (True, None)
user_validator.is_valid({ "name": 31 }) # => (False, ValidatorError)
```


## Primitives

```py
from wvalidate import Validate as v

# primitive values
v.string()
v.integer()
v.float()
v.numeric()
```

## Strings

```py
from wvalidate import Validate as v

v.string(equal="EQUAL")
v.string(min=1)
v.string(max=5)
v.string(min=2, max=7)
v.email()
```

## Numbers

```py
from wvalidate import Validate as v

v.integer(min=1)
v.integer(max=5)
v.integer(min=2, max=7)

v.float(min=1)
v.float(max=5)
v.float(min=2, max=7)

# valid integers and floats
v.numeric(min=1)
v.numeric(max=5)
v.numeric(min=2, max=7)
```

## Enums

```py
from wvalidate import Validate as v

# A list of any type must be passed
v.enum(["rock", "paper", "scissors"])
v.enum([True, False])
v.enum([5, "FIVE"])

my_validator_enum = v.enum([5, "FIVE"])

my_validator_enum.is_valid(5) # => (True, None)
my_validator_enum.is_valid("SIX") # => (Flase, ValidatorError)
```

## Nullables

```py
from wvalidate import Validate as v

# Any Validator must be passed
v.nullable(v.string())
v.nullable(v.enum([True, False]))
v.nullable(v.dict({
  "name": v.string(),
  "age": v.integer()
}))

my_validator_nullable = v.nullable(v.string())

my_validator_nullable.is_valid("Maria") # => (True, None)
my_validator_nullable.is_valid(None) # => (True, None)
my_validator_nullable.is_valid(3) # => (Flase, ValidatorError)
```

## Lists

```py
from wvalidate import Validate as v

# Any Validator must be passed
v.list(v.string())
v.list(v.enum([True, False]))
v.list(v.dict({
  "name": v.string(),
  "age": v.integer()
}))

my_validator_list = v.list(v.string())

my_validator_list.is_valid(["ONE", "TWO", "THREE"]) # => (True, None)
my_validator_list.is_valid(["ONE", "TWO", 3]) # => (Flase, ValidatorError)
```

## Dictionaries

```py
from wvalidate import Validate as v

v.dict({
  "name": v.string(),
  "price": v.numeric(min=0),
  "category": v.enum(["food", "drink"])
})

v.dict({
  "name": v.string(),
  "price": v.integer(min=0),
  "address": {
    "city": v.string()
  }
})

v.dict({
  "users": v.list(
    v.dict({
      "name": v.string(),
      "price": v.integer(min=0),
    })
  )
})

user_validator = v.dict({
  "name": v.string()
})

user_validator.is_valid({ "name": "Fernanda" }) # => (True, None)
user_validator.is_valid({ "name": 31 }) # => (False, ValidatorError)
```
