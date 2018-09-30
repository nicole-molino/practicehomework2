import string

tach_list = ["tachycardic"]
trans_table = str.maketrans(dict.fromkeys(string.punctuation))


def is_tachycardic(candidate):
    clean_candidate1 = candidate.strip()
    clean_candidate2 = clean_candidate1.lower()
    clean_candidate = clean_candidate2.translate(trans_table)
    print(candidate)
    print(clean_candidate)
    for item in tach_list:
        if item == clean_candidate:
            return True

    return False





