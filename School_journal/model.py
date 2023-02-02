_class_1 = ""
journal = {}
def open_journal(numb:str):
    global _class_1
    global journal
    _class_1 = f"classes/{numb}.txt"
    with open(_class_1, 'r', encoding="UTF-8") as file:
        input = file.readlines()
        for i in input:
            predm = i[:i.index(':')]
            chlds = {j.split(':')[0]: j.split(':')[1].strip().split(',')
                     for j in i[i.index(':')+1:].split(';')}
            journal[predm] = chlds
    return journal
def append_bal(key1, key_sbj ,key_std, el):
    student_list = []
    for k, v in key1.items():
        for key in v.keys():
            if key not in student_list:
                student_list.append(key)
    key3 = student_list[key_std-1]
    subject_list = list(k for k in key1.keys())
    key2 = subject_list[key_sbj-1]
    var = key1[key2][key3]
    var.append(el)
    return var
def save_journal(numb:str):
    global _class_1
    global journal
    _class_1 = f"classes\{numb}.txt"
    with open(_class_1, "w", encoding="UTF-8") as file:
        for k, v in journal.items():
            var = list(i+":"+",".join(j) for i, j in v.items())
            var = ";".join(var)
            file.write("".join(f"{k}:{var}\n"))

