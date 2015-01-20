import mystery_word as myst

def test_type():
    assert type(myst.new_word()) != list
    assert type(myst.new_word()) == str

def test_game_win_counter():
    start_guess = 1
    assert myst.game_check() == False

def test_game_win_string():
    start_word = ["a", "b", "c"]
    blank_word = ["a", "b", "c"]
    assert myst.game_check() == True

def test_letter_get():
    letter = "a"
    assert myst.get_letter() == "a"


# Obviously, I really struggled to grasp the proper way to write test parameters
# I want to understand this and get this right. If you have some one-on-one time
# at some point, I would appreciate a review.
