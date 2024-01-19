from calculate_similarity import calculate_similarity

# testing
candidate_list = [
    "int value = value / 10;",
    "double value = value % 10;",
    "int value = value2 / 10;"
]
# TestCase 1: 完全相同的补丁代码
test_case_1 = {
    'candidate_list': [
        "int value = value % 10;",
        "double ratio = ratio / 10;",
        "float index = index * 2.5;"
    ],
    'patch_str': "int value = value % 10;"
}

# TestCase 2: 细微差异的补丁代码
test_case_2 = {
    'candidate_list': [
        "int value = value % 10;",
        "int val = val % 10;",
        "int value = value / 10;"
    ],
    'patch_str': "int value = value % 10;"
}

# TestCase 3: 结构类似但有显著差异的补丁代码
test_case_3 = {
    'candidate_list': [
        "int value = value * 10;",
        "double value = value % 10;",
        "int result = value % 10;"
    ],
    'patch_str': "int value = value % 10;"
}

# TestCase 4: 完全不相关的补丁代码
test_case_4 = {
    'candidate_list': [
        "void processData() {}",
        "double computeRatio(double val) { return val / 10; }",
        "bool checkValue(int val) { return val > 10; }"
    ],
    'patch_str': "int value = value % 10;"
}

test_case = test_case_4
patch_str = "int value = value % 10;"
top_k_list = calculate_similarity(test_case['candidate_list'], test_case['patch_str'], top_k=1)
print(top_k_list)