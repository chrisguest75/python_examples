import directory_trie


def test_one_path_contained():
    trie = directory_trie.Trie(["/Code/scratch/hackerrank/algorithms"])
    assert trie.contains("/Code/scratch/hackerrank/algorithms") is True
    # assert False == True


def test_does_not_exist():
    trie = directory_trie.Trie(["/Code/scratch/hackerrank/algorithms"])
    assert trie.contains("/Code/scratch") is False
    assert trie.contains("/Test/path") is False


def test_one_path_find_all():
    trie = directory_trie.Trie(["/Code/scratch/hackerrank/algorithms"])
    files = trie.find_all()
    print(files)
    assert files == ["/Code/scratch/hackerrank/algorithms"]


def test_multiple_path_find_all():
    trie = directory_trie.Trie(
        [
            "/Code/scratch/hackerrank/algorithms",
            "/Test/scratch/hackerrank/algorithms",
            "/Test/scratch/leetcode/algorithms",
        ]
    )
    files = trie.find_all()
    print(files)
    assert files == [
        "/Code/scratch/hackerrank/algorithms",
        "/Test/scratch/hackerrank/algorithms",
        "/Test/scratch/leetcode/algorithms",
    ]


def test_multiple_path():
    trie = directory_trie.Trie(
        ["/Code/scratch/hackerrank/algortihms", "/Test/scratch/hackerrank/algortihms"]
    )
    assert trie.contains("/Code/scratch/hackerrank/algortihms") is True
    assert trie.contains("/Test/scratch/hackerrank/algortihms") is True
