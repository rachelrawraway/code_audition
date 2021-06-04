# Code Audition - Asteroids Tracker

## Local Setup

To setup this package, perform the following steps:

1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the package and test dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements_test.txt
```

3. Install the package for development:

```bash
python3 setup.py develop
```

4. Run the project:

```bash
asteroid_tracker <start_date> <end_date>
```

## Testing

To run the tests:

```bash
pytest
```

To run a specific test:

```bash
pytest tests/test_asteroids_tracker.py::test_2021_01_01_to_2021_01_02_success
```
