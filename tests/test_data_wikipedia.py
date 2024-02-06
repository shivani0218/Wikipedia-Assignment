valid_input = {"topic": "Python (programming language)", "n": 5}

missing_topic = {"topic": "", "n": 5}

negative_n = {"topic": "Python (programming language)", "n": -5}

missing_n = {"topic": "Python (programming language)", "n": None}

invalid_namespace_filter = {"topic": "Python (programming language)", "n": 5}

test_data_list = [
    valid_input,
    missing_topic,
    negative_n,
    missing_n,
    invalid_namespace_filter,
    # Add more test cases as needed
    {"topic": "Java", "n": 3},
    {"topic": "JavaScript", "n": 7, "namespace_filter": ["Web"]},
    {"topic": "C++", "n": 5},
    {"topic": "Go (programming language)", "n": 4},
    {"topic": "Dynamic", "n": lambda: 2 + 3},
]
