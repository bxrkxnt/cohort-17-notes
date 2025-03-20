# Inheritance

- There are different types of thing (Cat, Dog, Fridge)
- Some types of things overlap
- Some types of things are more specific versions of other types
  - Animal
    - Mammal
      - Cat & Dog
- Inheritance allows classes to be more specific version of other classes

## Liskov Substitution Principle

- Every instance of a subclass is a valid instance of the parent class

## Resources

- [Theory of Forms](https://en.wikipedia.org/wiki/Theory_of_forms)

## Task

- `BankAccount` class
  - withdraw()
  - deposit()
  - balance
- `InterestAccount` class
  - interest_rate
  - collect_interest()
- `TaxFreeInterestAccount` class
  - On every deposit, increases the amount by 20%