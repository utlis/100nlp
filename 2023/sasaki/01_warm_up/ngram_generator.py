def generate_n_gram(n: int, sequence: str | list) -> list:
    """
    文字列、または文字列のリストを受け取って、指定されたn-gramを返す
    word_n_gram が欲しい場合は、対象の文字列を空白区切りで分割したリストを渡す
    letter_n_gram が欲しい場合は、対象の文字列をそのまま渡す
    """
    is_str = type(sequence) is str
    joint_str = " "
    if (is_str):
        sequence = list(sequence)
        joint_str = ""

    result = []
    for i in range(0, len(sequence) - (n - 1)):
        result.append(joint_str.join(sequence[i:i + n]))
    return result
