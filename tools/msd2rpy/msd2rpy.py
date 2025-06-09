import copy
import os
import re
import csv

from HANATools_MSD import MsdReader

HANA08p5_chars_dict = {
    0   :   "kaori" ,
    1   :   "amane" ,
    2   :   "koharu",
    3   :   "makoto",
    4   :   "kaori_makoto" ,
    5   :   "teacher" 
}

HANA08p5_chars_list = [
    "kaori" ,
    "amane" ,
    "koharu",
    "makoto",
]

HANA08p5_chars_images_dict = {
    "tam"   :   "amane" ,
    "tka"   :   "kaori" ,
    "tko"   :   "koharu",
    "tma"   :   "makoto" 
}

HANA08p5_chars_pos_dict = {
    (0xC8, 0xC9, 0xCA)  :   "c" ,
    (0xCB, 0xCC, 0xCD)  :   "l" ,
    (0xCE, 0xCF, 0xD0)  :   "r" ,
    (0xD1, 0xD2, 0xD3)  :   "sl",
    (0xD4, 0xD5, 0xD6)  :   "sr",
    (0xD7, 0xD8, 0xD9)  :   "c" 
}

def msd2rpy_main(path_input, path_output, encoding, chars_dict = {}, chars_images_dict = {}, chars_pos_dict = {}, chars_list = []):
    reader = MsdReader(path_input, encoding)
    codes = reader.MsdReadLight()

    bg_show = None
    bg_next = None
    chars_show = {}
    chars_next = {}
    chars_change = []
    chars_hide = []
    images_change = []
    image_changed = False
    window_show = False
    images = {}
    images_next = {}
    images_pos = {}

    rows_opt = []
    i = 0
    while i < len(codes):
        row = codes[i]
        if row['code'] == "title":
            title = row['args'][0].rstrip('　')
            rows_opt.append(f"$ save_name = \"{title}\"")
            rows_opt.append("")
            i += 1
        elif row['code'] == "bgm":
            bgm = row['args'][0]
            rows_opt.append(f"play music \"bgm/{bgm}.ogg\" fadein 1.0")
            rows_opt.append("")
            i += 1
        elif row['code'] == "se":
            se = row['args'][1]
            rows_opt.append(f"play sound \"se/{se}.ogg\"")
            rows_opt.append("")
            i += 1
        elif row['code'] == "char":
            if not window_show:
                rows_opt.append("window show")
                window_show = True
            rows_logs = rows_dialogue(codes[i], codes[i+1], codes[i+2], chars_dict)
            rows_opt += rows_logs
            rows_opt.append("")
            i += 3
        ##图像系列语句
        elif row['code'] == "image_clear":
            id = row['args'][0]
            if id in images:
                del images[id]
            if id in images_pos:
                del images_pos[id]
            images_change.append(id)
            i += 1
        elif row['code'] == "image":
            id = row['args'][0]
            image = row['args'][1]
            if image == "BLACK":
                image = "black"
            if id in images:
                images[id] = image
            else:
                images.setdefault(id, image)
            i += 1
        elif row['code'] == "image2":
            id = row['args'][0]
            if type(row['args'][1]).__name__ == 'str':
                image = row['args'][1]
                if id in images_next:
                    images_next[id] = image
                else:
                    images_next.setdefault(id, image)
            elif type(row['args'][1]).__name__ == 'int':
                id2 = row['args'][1]
                if id2 in images:
                    if id in images_next:
                        images_next[id] = images[id2]
                    else:
                        images_next.setdefault(id, images[id2])
            i += 1
        elif row['code'] == "image_show":
            id = row['args'][0]
            posID = (row['args'][1], row['args'][2], row['args'][3])
            pos = None
            if posID in chars_pos_dict:
                pos = chars_pos_dict[posID]
            
            if id in images_pos:
                images_pos[id] = pos
            else:
                images_pos.setdefault(id, pos)
            i += 1
        elif row['code'] == "transfrom":
            images |= images_next
            images_next.clear()
            transfrom = None
            if len(row['args']) == 5:
                transfrom = row['args'][3]
            ##去dammy
            if 0x0A in images:
                del images[0x0A]
            if 0x0A in images_pos:
                del images_pos[0x0A]
            if 0x0A in images_change:
                del images_change[0x0A]
            
            if 0 in images_change:
                bg_next = images[0]
                images_change.remove(0)
                ##not bg change
                if bg_next == bg_show:
                    for id in images_change:
                        if images[id][:3] in chars_images_dict:
                            char = chars_images_dict[images[id][:3]]
                        else:
                            char = images[id]
                        chars_next |= {char:{"image": images[id], "pos":images_pos[id]}}
                    for char in chars_show:
                        if not char in chars_next:
                            chars_hide.append(char)
                    for char in chars_next:
                        if not char in chars_show:
                            chars_change.append(char)
                        elif not chars_next[char] == chars_show[char]:
                            chars_change.append(char)

                    if len(chars_hide) > 0:
                        image_changed = True
                        for char in chars_hide:
                            rows_opt.append(f"hide {char}")

                    if len(chars_change) > 0:
                        for char in chars_change:
                            if not char in chars_list:
                                image_changed = True
                            elif not char in chars_show:
                                image_changed = True
                            elif not chars_show[char]['pos'] == chars_next[char]['pos']:
                                image_changed = True

                            if char in chars_list:
                                if chars_next[char]['pos'] == None:
                                    rows_opt.append(f"show {char} {chars_next[char]['image']}")
                                else:
                                    rows_opt.append(f"show {char} {chars_next[char]['image']} at {chars_next[char]['pos']}")
                            else:
                                rows_opt.append(f"show {char}")

                    if image_changed:
                        rows_opt.append("with dissolve")

                    chars_show = copy.deepcopy(chars_next)
                    chars_next.clear()
                    chars_hide.clear()
                    chars_change.clear()
                    images_change.clear()
                    image_changed = False

                ##bg change
                else:
                    if window_show:
                        rows_opt.append("window hide")
                        window_show = False
                    rows_opt.append(f"scene {bg_next}")
                    if transfrom == None:
                        if bg_next == 'black' or bg_show == 'black':
                            rows_opt.append("with fade")
                        else:
                            rows_opt.append("with dissolve")
                    else:
                        rows_opt.append(f"with {transfrom.lower()}")
                    bg_show = bg_next
                    bg_next = None
                    chars_show.clear()
                    chars_next.clear()
                    images_change.clear()
            ##not bg change
            else:
                for id in images_change:
                    if images[id][:3] in chars_images_dict:
                        char = chars_images_dict[images[id][:3]]
                    else:
                        char = images[id]
                    chars_next |= {char:{"image": images[id], "pos":images_pos[id]}}
                for char in chars_show:
                    if not char in chars_next:
                        chars_hide.append(char)
                for char in chars_next:
                    if not char in chars_show:
                        chars_change.append(char)
                    elif not chars_next[char] == chars_show[char]:
                        chars_change.append(char)

                if len(chars_hide) > 0:
                    image_changed = True
                    for char in chars_hide:
                        rows_opt.append(f"hide {char}")

                if len(chars_change) > 0:
                    for char in chars_change:
                        if not char in chars_list:
                            image_changed = True
                        elif not char in chars_show:
                            image_changed = True
                        elif not chars_show[char]['pos'] == chars_next[char]['pos']:
                            image_changed = True

                        if char in chars_list:
                            if chars_next[char]['pos'] == None:
                                rows_opt.append(f"show {char} {chars_next[char]['image']}")
                            else:
                                rows_opt.append(f"show {char} {chars_next[char]['image']} at {chars_next[char]['pos']}")
                        else:
                            rows_opt.append(f"show {char}")

                if image_changed:
                    rows_opt.append("with dissolve")

                chars_show = copy.deepcopy(chars_next)
                chars_next.clear()
                chars_hide.clear()
                chars_change.clear()
                images_change.clear()
                image_changed = False
            rows_opt.append("")
            i += 1
        elif row['code'] == "select":
            rows_opt.append("#menu")
            rows_opt.append("")
            i += 1
        elif row['code'] == "label":
            rows_opt.append("#label")
            rows_opt.append("")
            i += 1
        

    optdir = path_output[:- len(re.split(rf'[/\\]', path_output)[-1])]
    if not os.path.exists(optdir):
        os.makedirs(optdir)

    with open(path_output, 'w', encoding='utf8') as file:
        for row in rows_opt:
            file.write(row)
            file.write("\n")
        

        


def rows_dialogue(row_char, row_voice, row_text, chars_dict):
    char = None
    voice = None
    text = ""
    output = []
    if row_char['args'][0] == -1:
        char = None
    elif row_char['args'][0] in chars_dict:
        char = chars_dict[row_char['args'][0]]
    else:
        char = f"char_{row_char['args'][0]}"

    if len(row_voice['args'][1]) > 0:
        voice = row_voice['args'][1]
    else:
        voice = None
    
    if len(row_text['args']) == 6:
        text = row_text['args'][3].rstrip('　')
    elif len(row_text['args']) > 6:
        for j in range(3, len(row_text['args'])-3):
            if type(row_text['args'][j]).__name__ == 'str' :
                text += row_text['args'][j]
            elif type(row_text['args'][j]).__name__ == 'int':
                text += "{heart}"
        if type(row_text['args'][len(row_text['args'])-3]).__name__ == 'str' :
            text += row_text['args'][len(row_text['args'])-3].rstrip('　')
        elif type(row_text['args'][len(row_text['args'])-3]).__name__ == 'int':
            text += "{heart}"

    if not voice == None:
        output.append(f"voice \"{voice}\"")

    if char == None:
        output.append(f"\"{text}\"")
    else:
        output.append(f"{char} \"{text}\"")

    return output

def dialogue_data_read(row_char, row_voice, row_text, chars_dict):
    char = None
    voice = None
    text = ""
    dialogue = []
    if row_char['args'][0] == -1:
        char = None
    elif row_char['args'][0] in chars_dict:
        char = chars_dict[row_char['args'][0]]
    else:
        char = f"char_{row_char['args'][0]}"

    if len(row_voice['args'][1]) > 0:
        voice = row_voice['args'][1]
    else:
        voice = None
    
    if len(row_text['args']) == 6:
        text = row_text['args'][3].rstrip('　')
    elif len(row_text['args']) > 6:
        for j in range(3, len(row_text['args'])-3):
            if type(row_text['args'][j]).__name__ == 'str' :
                text += row_text['args'][j]
            elif type(row_text['args'][j]).__name__ == 'int':
                text += "{heart}"
        if type(row_text['args'][len(row_text['args'])-3]).__name__ == 'str' :
            text += row_text['args'][len(row_text['args'])-3].rstrip('　')
        elif type(row_text['args'][len(row_text['args'])-3]).__name__ == 'int':
            text += "{heart}"

    dialogue = [char, voice, text]

    return dialogue

def dialogue_data_to_list(codes, chars_dict):
    dialogues_list = []
    i = 0
    while i < len(codes):
        row = codes[i]
        if row['code'] == "char":
            dialogue = dialogue_data_read(codes[i], codes[i+1], codes[i+2], chars_dict)
            dialogues_list.append(dialogue.copy())
            i += 3
        else:
            i += 1

    return dialogues_list
    

## 仅输出语音及对话
def dialogue_data_opt_csv(path_input, path_output, encoding="utf8", chars_dict = {}):
    reader = MsdReader(path_input, encoding)
    codes = reader.MsdReadLight()
    data_list = dialogue_data_to_list(codes, chars_dict)

    with open(path_output, "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerows(data_list)

    return

## renpy翻译填充
def rpy_translation_fill(msd_path, rpy_tl_path, chars_dict, language, msd_encoding="utf8", rpy_encoding="utf8"):
    reader = MsdReader(msd_path, msd_encoding)
    codes = reader.MsdReadLight()
    dialogue_list = dialogue_data_to_list(codes, chars_dict)
    dialogue_list = tl_text_preprocess(dialogue_list, language)

    with open(rpy_tl_path, "r", encoding=rpy_encoding) as file:
        text_tl_raw = file.read()
    tl_labels = rpy_translation_parse(text_tl_raw, language)

    check = tl_voice_check(dialogue_list, tl_labels)

    if not check:
        raise ValueError("unexpected voice id")
    
    with open(rpy_tl_path, "w", encoding=rpy_encoding) as file:
        lines = []
        i = 0
        for label in tl_labels:
            label_type = label["type"]
            label_id = label["id"]
            if label_type == "dialogue":
                voice = label["translation"]["voice"]
                char = label["translation"]["char"]
                text = dialogue_list[i][2]

                file.write(f"translate {language} {label_id}:\n")
                if voice is not None:
                    file.write(f"    voice \"{voice}\"\n")
                if char is None:
                    file.write(f"    \"{text}\"\n")
                else:
                    file.write(f"    {char} \"{text}\"\n")

                file.write("\n\n")
                i += 1

            elif label_type == "strings":
                file.write(f"translate {language} strings:\n")
                for string in label["translation"]:
                    old = string["old"]
                    new = string["new"]
                    file.write(f"    old \"{old}\"\n")
                    file.write(f"    new \"{new}\"\n")
                    file.write("\n")
            
            elif label_type == "nointeract":
                char = label["translation"]["char"]
                text = label["translation"]["text"]
                file.write(f"translate {language} {label_id}:\n")
                if char is None:
                    file.write(f"    \"{text}\" nointeract\n")
                else:
                    file.write(f"    {char} \"{text}\" nointeract\n")

                file.write("\n\n")
                

    return





def rpy_translation_parse(text_raw, language):
    rows = text_raw.splitlines()
    tl_labels = []
    tl_label = {}
    label_raw = []
    for row in rows:
        if re.match(rf"(\s*)(#)", row) is not None:
            pass
        elif re.search(rf"(\S+)", row) is None:
            pass
        elif re.fullmatch(rf"(translate)(\s+)({language})(\s+)(\S+)(:)(\s*)", row) is not None:
            if len(label_raw) > 0:
                tl_label = tl_label_parse(label_raw)
                tl_labels.append(tl_label.copy())
                label_raw.clear()
            match00 = re.fullmatch(rf"(translate)(\s+)({language})(\s+)(\S+)(:)(\s*)", row)
            label_raw.append({"tl_label_ID":match00.group(5)})
        elif re.fullmatch(rf"(\s+)([\"])(.*)([\"])(\s*)", row) is not None:
            match00 = re.fullmatch(rf"(\s+)([\"])(.*)([\"])(\s*)", row)
            label_raw.append({"code":None, "text":match00.group(3)})
        elif re.fullmatch(rf"(\s+)(\S+)(\s+)([\"])(.*)([\"])(\s*)", row) is not None:
            match00 = re.fullmatch(rf"(\s+)(\S+)(\s+)([\"])(.*)([\"])(\s*)", row)
            label_raw.append({"code":match00.group(2), "text":match00.group(5)})
        elif re.fullmatch(rf"(\s+)([\"])(.*)([\"])(\s+)(nointeract)(\s*)", row) is not None:
            match00 = re.fullmatch(rf"(\s+)([\"])(.*)([\"])(\s+)(nointeract)(\s*)", row)
            label_raw.append({"code":None, "text":match00.group(3), "sp":match00.group(6)})
        elif re.fullmatch(rf"(\s+)(\S+)(\s+)([\"])(.*)([\"])(\s+)(nointeract)(\s*)", row) is not None:
            match00 = re.fullmatch(rf"(\s+)(\S+)(\s+)([\"])(.*)([\"])(\s+)(nointeract)(\s*)", row)
            label_raw.append({"code":match00.group(2), "text":match00.group(5), "sp":match00.group(8)})


    if len(label_raw) > 0:
        tl_label = tl_label_parse(label_raw)
        tl_labels.append(tl_label.copy())
        label_raw.clear()

    return tl_labels


def tl_label_parse(label_raw):
    label = {}
    id = label_raw[0]["tl_label_ID"]
    if len(label_raw) == 1:
        raise ValueError(f"label {id} is empty")
    label["id"] = id
    if label["id"] == "strings":
        if (len(label_raw) - 1) % 2 > 0:
            raise ValueError("translation for strings should be even")
        i = 1
        strings = []
        while i < len(label_raw) - 1:
            if label_raw[i]["code"] == "old" and label_raw[i+1]["code"] == "new":
                strings.append({"old":label_raw[i]["text"], "new":label_raw[i+1]["text"]})
                i += 2
            else:
                raise ValueError("unexpected flags in strings label")
        label["type"] = "strings"
        label["translation"] = strings
    else:
        sp = False
        voice = None
        char = None
        text = None
        for row in label_raw[1:]:
            if "sp" in row:
                sp = True
                sp_type = row["sp"]

            if row["code"] is None:
                if text is None:
                    text = row["text"]
                else:
                    raise ValueError(f"multiple string in label {id}")
            elif row["code"] == "voice":
                if voice is None:
                    voice = row["text"]
                else:
                    raise ValueError(f"multiple voice in label {id}")
            else:
                if text is None:
                    char = row["code"]
                    text = row["text"]
                else:
                    raise ValueError(f"multiple string in label {id}")
        if sp:
            label["type"] = sp_type
        else:
            label["type"] = "dialogue"
        label["translation"] = {"voice":voice, "char":char, "text":text}

    return label

def tl_count_check(dialogue_list, tl_labels):
    check = False
    i = 0
    for label in tl_labels:
        if label["type"] == "dialogue":
            i += 1
    
    if i == len(dialogue_list):
        check = True

    return check

## ???
def tl_voice_check(dialogue_list, tl_labels):
    dialogue_labels = []
    strings_labels = []
    for label in tl_labels:
        if label["type"] == "dialogue":
            dialogue_labels.append(label)
        else:
            strings_labels.append(label)
    
    if len(dialogue_list) != len(dialogue_labels):
        raise ValueError("unexpected dialogues count")
    
    for i in range(0, len(dialogue_list)):
        if (dialogue_list[i][1] is None) and (dialogue_labels[i]["translation"]["voice"] is None):
            pass
        elif dialogue_list[i][1].lower() == dialogue_labels[i]["translation"]["voice"].lower():
            pass
        else:
            id = dialogue_labels[i]["id"]
            raise ValueError(f"different voice id in label {id}")
        
    return True

def tl_text_preprocess(dialogue_list, language):
    dialogues = copy.deepcopy(dialogue_list)
    if language == "English":
        for dialogue in dialogues:
            text = dialogue[2]
            if re.search(rf"(\s*)(　)", text) is not None:
                dialogue[2] = re.sub(rf"(\s*)(　)", " ", text)
            if re.search(rf"(～)", text) is not None:
                dialogue[2] = re.sub(rf"(～)", "~", text)
            if re.search(rf"(♪)", text) is not None:
                dialogue[2] = re.sub(rf"(♪)", "{note}", text)

    elif language == "Japanese":
        for dialogue in dialogues:
            text = dialogue[2]
            if re.search(rf"(♪)", text) is not None:
                dialogue[2] = re.sub(rf"(♪)", "{note}", text)

    return dialogues
            
