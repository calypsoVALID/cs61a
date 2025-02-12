"""Typing test implementation"""

from utils import (
    lower,
    split,
    remove_punctuation,
    lines_from_file,
    count,
    deep_convert_to_tuple,
)
from ucb import main, interact, trace
from datetime import datetime
import random


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which the SELECT returns True.
    If there are fewer than K such paragraphs, return an empty string.

    Arguments:
        paragraphs: a list of strings representing paragraphs
        select: a function that returns True for paragraphs that meet its criteria
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    picked_list = [p for p in paragraphs if select(p) is True]
    if k >= len(picked_list):
        return ''
    else:
        return picked_list[k]
    # END PROBLEM 1


def about(subject):
    """Return a function that takes in a paragraph and returns whether
    that paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), "subjects should be lowercase."

    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def is_equal(s):
        # 将段落处理为小写并移除标点后拆分成单词列表
        s_words = split(lower(remove_punctuation(s)))
        # 使用集合提高查找效率
        subject_set = set(subject)
        # 检查是否有任何单词在主题集合中
        return any(word in subject_set for word in s_words)
    return is_equal
    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    compared to the corresponding words in SOURCE.

    Arguments:
        typed: a string that may contain typos
        source: a model string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed_words) == 0 and len(source_words) == 0:
        return 100.0
    elif len(typed_words) == 0 or len(source_words) == 0:
        return 0.0
    else:
        correct_count = 0
        words_count = len(typed_words)
        max_index = min(len(source_words), len(typed_words))
        for i in range(max_index):
            if typed_words[i] == source_words[i]:
                correct_count += 1
        return correct_count / words_count * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, "Elapsed time must be positive"
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed) / 5) / (elapsed / 60)
    # END PROBLEM 4


################
# Phase 4 (EC) #
################


def memo(f):
    """A general memoization decorator."""
    cache = {}

    def memoized(*args):
        immutable_args = deep_convert_to_tuple(args)  # convert *args into a tuple representation
        if immutable_args not in cache:
            result = f(*immutable_args)
            cache[immutable_args] = result
            return result
        return cache[immutable_args]
    return memoized


def memo_diff(diff_function):
    """A memoization function."""
    cache = {}

    def memoized(typed, source, limit):
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        # END PROBLEM EC

    return memoized


###########
# Phase 2 #
###########


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD based on DIFF_FUNCTION. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, return TYPED_WORD instead.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if typed_word in word_list:
        return typed_word
    else:
        diff_list = [diff_function(typed_word, w, limit) for w in word_list]
        liked_word_diff = min(diff_list, key = abs)
        if liked_word_diff > limit:
            return typed_word
        else:
            for i in range(len(diff_list)):
                if diff_list[i] == liked_word_diff:
                    return word_list[i]
    # END PROBLEM 5


def furry_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> furry_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> furry_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> furry_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> furry_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> furry_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    # 定义一个辅助函数，该函数接受两个字符串和limit，返回两个字符串相同位置字符不同的个数
    def diff_count(str1, str2, lim):
        # 递归终止条件：如果其中一个字符串为空字符串则返回
        if not str1 or not str2:
            return 0
        # 递归终止条件： 如果更改字符个数大于limit则停止递归。
        elif lim < 0:
            return 0
        # 逐个字符比较两个字符串
        elif str1[0] == str2[0]:
            # 递归调用，比较剩余部分的字符
            return diff_count(str1[1:], str2[1:], lim)
        else:
            lim -= 1
            return 1 + diff_count(str1[1:], str2[1:], lim)

    # 返回长度之差加需要更改的字符个数
    return abs(len(typed) - len(source)) + diff_count(typed, source, limit)    

    # END PROBLEM 6


def minimum_mewtations(typed, source, limit):
    """计算从输入单词到目标单词的最小编辑距离（使用递归方法）。
    
    参数:
        typed (str): 用户输入的单词（可能包含拼写错误）
        source (str): 目标正确单词
        limit (int): 允许的最大编辑次数
    
    返回值:
        int: 将typed转换为source所需的最小操作次数。如果超过limit则返回当前计算值
        
    示例:
        >>> minimum_mewtations("cats", "scat", 10)
        2  # 操作步骤：添加's'（cats -> scats） -> 删除's'（scats -> scat）
        >>> minimum_mewtations("purng", "purring", 10)
        2  # 操作步骤：添加'r'（purng -> purrng） -> 添加'i'（purrng -> purring）
    """
    # 基本情况处理
    if limit < 0:
        # 超过允许的编辑次数限制，返回当前已计算的编辑次数
        return 0
    elif len(typed) == 0 or len(source) == 0:
        # 任一字符串为空时，需要编辑的次数为剩余字符的长度之和
        return len(typed) + len(source)
    
    # 递归情况处理
    if typed[0] == source[0]:
        # 首字符相同，处理剩余部分，不增加编辑次数
        return minimum_mewtations(typed[1:], source[1:], limit)
    else:
        # 计算三种可能的编辑操作：
        # 1. 添加操作：在typed开头添加source的首字符，继续比较typed和source[1:]
        add = minimum_mewtations(typed, source[1:], limit - 1)
        # 2. 删除操作：删除typed的首字符，继续比较typed[1:]和source
        remove = minimum_mewtations(typed[1:], source, limit - 1)
        # 3. 替换操作：将typed的首字符替换为source的首字符，继续比较剩余部分
        substitute = minimum_mewtations(typed[1:], source[1:], limit - 1)
        
        # 返回三种操作中的最小值加1（当前操作的代价）
        return 1 + min(add, remove, substitute)


# Ignore the line below
minimum_mewtations = count(minimum_mewtations)


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, "Remove this line to use your final_diff function."


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct_count = 0
    # 遍历typed遇到第一个错误str时结束循环
    for i in range(len(typed)):
        if typed[i] == source[i]:
            correct_count += 1
        else:
            break
    # 计算progress值
    progress = correct_count / len(source)
    # 将playerid和progress加入dict
    d = {'id': user_id, 'progress': progress}
    # 调用upload
    upload(d)
    # 返回progress值
    return progress
    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Return a dictionary {'words': words, 'times': times} where times
    is a list of lists that stores the durations it took each player to type
    each word in words.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time the
                          player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> result = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> result['words']
    ['collar', 'plush', 'blush', 'repute']
    >>> result['times']
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    tpp = timestamps_per_player  # A shorter name (for convenience)
    # BEGIN PROBLEM 9
    times = []
    for player in tpp:
        time = []
        for i in range(len(player) - 1):
            time.append(player[i + 1] - player[i])
        times.append(time)
    # END PROBLEM 9
    return {'words': words, 'times': times}


def fastest_words(words_and_times):
    """Return a list of lists indicating which words each player typed fastests.

    Arguments:
        words_and_times: a dictionary {'words': words, 'times': times} where
        words is a list of the words typed and times is a list of lists of times
        spent by each player typing each word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [p0, p1]})
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    check_words_and_times(words_and_times)  # verify that the input is properly formed
    words, times = words_and_times['words'], words_and_times['times']
    player_indices = range(len(times))  # contains an *index* for each player
    word_indices = range(len(words))    # contains an *index* for each word
    # 初始化结果列表，每个玩家一个空列表
    result = [[] for _ in player_indices]
    
    # 遍历每个单词
    for word_idx in word_indices:
        min_time = float('inf')
        fastest_player = 0
        
        # 查找输入该单词最快的玩家
        for player_idx in player_indices:
            current_time = times[player_idx][word_idx]
            if current_time < min_time:
                min_time = current_time
                fastest_player = player_idx
        
        # 将单词添加到对应玩家的结果列表
        result[fastest_player].append(words[word_idx])
    
    return result


def check_words_and_times(words_and_times):
    """Check that words_and_times is a {'words': words, 'times': times} dictionary
    in which each element of times is a list of numbers the same length as words.
    """
    assert 'words' in words_and_times and 'times' in words_and_times and len(words_and_times) == 2
    words, times = words_and_times['words'], words_and_times['times']
    assert all([type(w) == str for w in words]), "words should be a list of strings"
    assert all([type(t) == list for t in times]), "times should be a list of lists"
    assert all([isinstance(i, (int, float)) for t in times for i in t]), "times lists should contain numbers"
    assert all([len(t) == len(words) for t in times]), "There should be one word per time."


def get_time(times, player_num, word_index):
    """Return the time it took player_num to type the word at word_index,
    given a list of lists of times returned by time_per_word."""
    num_players = len(times)
    num_words = len(times[0])
    assert word_index < len(times[0]), f"word_index {word_index} outside of 0 to {num_words-1}"
    assert player_num < len(times), f"player_num {player_num} outside of 0 to {num_players-1}"
    return times[player_num][word_index]


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file("data/sample_paragraphs.txt")
    random.shuffle(paragraphs)
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print("No more paragraphs about", topics, "are available.")
            return
        print("Type the following paragraph and then press enter/return.")
        print("If you only type part of it, you will be scored only on that part.\n")
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print("Goodbye.")
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print("Words per minute:", wpm(typed, elapsed))
        print("Accuracy:        ", accuracy(typed, source))

        print("\nPress enter/return for the next paragraph or type q to quit.")
        if input().strip() == "q":
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument("topic", help="Topic word", nargs="*")
    parser.add_argument("-t", help="Run typing test", action="store_true")

    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument("topic", help="Topic word", nargs="*")
    parser.add_argument("-t", help="Run typing test", action="store_true")

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
        run_typing_test(args.topic)
