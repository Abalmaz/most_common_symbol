from triangle_max_path import max_path

tr = [[55], [94, 48], [95, 30, 96], [77, 71, 26, 67]] 

def test_max_path():
    assert max_path(tr, 0, 0) == 320