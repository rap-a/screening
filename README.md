# Screening

## Implementation
The sorting algorithm receives the package's properties and determines if it is bulky, i.e. when the volume is greater than or equal to 1,000,000 cm3 or one of its dimensions are greater than or equal to 150 cm, and heavy, i.e. when its mass is greater than or equal to 20 kg.
Based on these criteria, the package is sorted to one of three stacks:
- Rejected: a bulk and heavy package
- Special: an either bulky or heavy package
- Standard: packages that are neither bulky or heavy

Additionally, when any of the properties is sent with an invalid value, that is, less than or equal to 0, the stack is returned as Invalid.

## Running the code
### Application
In order to execute the application, run:
```bash
python main.py <width> <height> <length> <mass>
```

To display the script's help:
```bash
python main.py -h
```

### Unit test
The unit tests can be analysed using:
```bash
python -m unittest
```

The coverage code is generated with:
```bash
python -m coverage run -m unittest
python -m coverage report -m
```