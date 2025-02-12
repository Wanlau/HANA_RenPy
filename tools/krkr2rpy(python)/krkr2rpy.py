import os 
import re

chars_dict = {
            "璃　紗"	:	"risa",
			"璃　纱"	:	"risa",
			"美　夜"	:	"miya",
			"七　海"	:	"nanami",
			"優　菜"	:	"yuuna",
			"优　菜"	:	"yuuna",
			"玲　緒"	:	"reo",
			"玲　绪"	:	"reo",
			"麻　衣"	:	"mai",
			"沙　雪"	:	"sayuki",
			"六　夏"	:	"rikka",
			"楓"	:	"kaede",
			"　楓　"	:	"kaede",
			"　枫　"	:	"kaede",
			"紗　良"	:	"sara",
			"纱　良"	:	"sara",
			"エリス"	:	"erisu",
			"爱丽丝"	:	"erisu",
			"艾莉丝"	:	"erisu",
			"雫"	:	"sizuku",
			"　雫　"	:	"sizuku",
			"瑠　奈"	:	"runa",
			"貴　子"	:	"takako",
			"贵　子"	:	"takako",
			"麗　奈"	:	"rena",
			"丽　奈"	:	"rena",
			"？？？"	:	"unknown",
			"擔　任"	:	"teacher",
			"教　师"	:	"teacher",
			"教　師"	:	"teacher",
			"女子Ａ"	:	"girl_a",
			"女子Ｂ"	:	"girl_b",
			"女子Ｃ"	:	"girl_c",
			"女子Ｄ"	:	"girl_d",
			"女子Ｅ"	:	"girl_e",
			"会员Ａ"	:	"member_a",
			"会员Ｂ"	:	"member_b",
			"会员Ｃ"	:	"member_c",
			"沙雪祖母"	:	"sayuki_grandma",
			"沙雪母"	:	"sayuki_mother",
			"璃　恵"	:	"rie",
			"雪　乃"	:	"yukino",
			"七海母"	:	"nanami_mother",
			"七海父"	:	"nanami_father",
			"麻衣弟"	:	"mai_brother",
			"麻衣妹"	:	"mai_sister",
			"工作人员"	:	"staff",
			"摄影师"	:	"camera",
			"经纪人"	:	"manager",
			"监　督"	:	"monitor",
			"全　员"	:	"allchar",
			"全　員"	:	"allchar"
}

chars_images_dict = {
    'tyu' : 'yuuna',
    'tna' : 'nanami',
    'tsa' : 'sara',
    'tka' : 'kaede',
    'tma' : 'mai',
    'tre' : 'reo',
    'tta' : 'takako',
    'tru' : 'runa',
    'trn' : 'rena',
    'ter' : 'erisu',
    'tsi' : 'sizuku',
    'tmi' : 'miya',
    'tri' : 'risa',
    'trk' : 'rikka',
    'tsy' : 'sayuki',
}

chars_list = [
    'yuuna',
    'nanami',
    'sara',
    'kaede',
    'mai',
    'reo',
    'takako',
    'runa',
    'rena',
    'erisu',
    'sizuku',
    'miya',
    'risa',
    'rikka',
    'sayuki'
]

def krkr2rpy_main(text_input):
    text_lines = text_input.splitlines()
    result_lines = []
    scene_show = 'black'
    ids_show = {}
    chars_pos_show = {}
    chars_image_show = {}
    ids_change = {}
    chars_pos_change = {}
    chars_image_change = {}
    clear_chars = []
    select_labels = []
    window_show = False
    scene_change = False
    char_change = False
    
    for line in text_lines:
        if re.match(rf'(\S+)', line) == None:
            result_lines.append('')
        elif line.startswith(';'):
            match = re.match(rf'(;)(.*)', line)
            result = match.group(2)
            result_lines.append('#' + result)
        elif line.startswith('#'):
            if line.startswith('#savetitle '):
                match = re.match(rf'(#savetitle)(\s+)(\S+)', line)
                result = match.group(3)
                result_lines.append('$ save_name = \"' + result + '\"')
            elif line.startswith('#voice '):
                match = re.match(rf'(#voice)(\s+)(\S+)', line)
                result = match.group(3)
                result_lines.append('voice \"' + result + '\"')
            elif line.startswith('#bgm '):
                match = re.match(rf'(#bgm)(\s+)(\S+)(\s+)(\S+)(\s*)(\S*)', line)
                if match.group(5) == 'stop':
                    result_lines.append('stop music fadeout 2.0')
                else:
                    result_lines.append('play music \"bgm/' + match.group(5) + '.ogg\" fadein 1.0')
            elif line.startswith('#se '):
                match = re.match(rf'(#se)(\s+)(\S+)(\s+)(\S+)', line)
                nom = match.group(5)
                if nom.startswith('SE'):
                    nom = 'se' + nom[2:]
                result_lines.append('play sound \"se/' + nom + '.ogg\"')
            elif line.startswith('#mes '):
                match = re.match(rf'(#mes)(\s+)(\S+)', line)
                result = match.group(3)
                if result == 'on':
                    window_show = True
                    result_lines.append('window show')
                elif result == 'off':
                    window_show = False
                    result_lines.append('window hide')
            elif line.startswith('#system '):
                pass
            elif line.startswith('#bg '):
                match = re.match(rf'(#bg)(\s+)(\S+)', line)
                scene_next = match.group(3)
                if scene_next.startswith('ev'):
                    scene_next = 'EV' + scene_next[2:]
                scene_change = True
                result_lines.append('scene ' + scene_next)
                chars_pos_show.clear()
                chars_image_show.clear()
                ids_show.clear()
            elif line.startswith('#cg '):
                if line.startswith('#cg all clear'):                    
                    for char in chars_pos_show:
                        clear_chars.append(char)                    
                elif not re.search(rf'(#cg)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)', line) == None:
                    match = re.match(rf'(#cg)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)', line)
                    id = match.group(3)
                    name = match.group(5)
                    pos = [match.group(7), match.group(9)]
                    posd = None
                    char = None
                    if pos == ['400', '0']:
                        posd = 'c'
                    elif pos == ['200', '0']:
                        posd = 'l'
                    elif pos == ['600', '0']:
                        posd = 'r'                    
                    elif pos == ['150', '0']:
                        posd = 'sl'                    
                    elif pos == ['650', '0']:
                        posd = 'sr'
                    if name[:3] in chars_images_dict:
                        char = chars_images_dict[name[:3]]
                    else:
                        char = name
                    if id in ids_show:
                        if not ids_show[id] == char:
                            clear_chars.append(ids_show[id])
                    ids_change.setdefault(id, char)
                    chars_pos_change.setdefault(char, posd)
                    chars_image_change.setdefault(char, name)
                elif not re.search(rf'(#cg)(\s+)(\S+)(\s+)(\S+)', line) == None:
                    match = re.match(rf'(#cg)(\s+)(\S+)(\s+)(\S+)', line)
                    if match.group(5) == 'clear':
                        clear_chars.append(ids_show[match.group(3)])
                    else:
                        if id in ids_show:
                            if not ids_show[id] == char:
                                clear_chars.append(ids_show[id])
                        ids_change.setdefault(match.group(3), match.group(5))
                        chars_pos_change.setdefault(match.group(5), None)
                        chars_image_change.setdefault(match.group(5), match.group(5))
                else:
                    result_lines.append(line)
            elif line.startswith('#wipe '):
                match = re.match(rf'(#wipe)(\s+)(\S+)', line)
                if match == None:
                    result_lines.append(line)
                elif match.group(3) == 'rrotate':
                    result_lines.append('with gs_r')
                elif match.group(3) == 'lrotate':
                    result_lines.append('with gs_l')
                elif match.group(3) == 'fade':                    
                    if scene_change == True:
                        if scene_show == 'black' or scene_next == 'black':
                            if window_show == False:
                                result_lines.append('with fade')
                            else:
                                result_lines.append('with dissolve')
                        else:
                            result_lines.append('with dissolve')
                        scene_show = scene_next
                        scene_next = ''
                        scene_change = False
                    elif len(clear_chars) > 0:
                        hide_chars = []
                        ids_show_list = list(ids_show)
                        for id in ids_show_list:
                            if ids_show[id] in clear_chars:
                                hide_chars.append(ids_show[id])                                
                                del chars_pos_show[ids_show[id]]
                                del chars_image_show[ids_show[id]]
                                del ids_show[id] 
                        ids_new = ids_show
                        chars_pos_new = chars_pos_show
                        chars_image_new = chars_image_show
                        for id in ids_change:
                            if id in ids_new:
                                ids_new[id] = ids_change[id]
                            else:
                                ids_new.setdefault(id, ids_change[id])
                        for char in chars_image_change:
                            if char in chars_pos_new:
                                if not chars_pos_new[char] == chars_pos_change[char]:
                                    char_change = True
                                    chars_pos_new[char] = chars_pos_change[char]
                                chars_image_new[char] = chars_image_change[char]
                            elif char in hide_chars:
                                char_change = True
                                hide_chars.remove(char)
                                chars_pos_new.setdefault(char, chars_pos_change[char])
                                chars_image_new.setdefault(char, chars_image_change[char])
                            else:
                                char_change = True
                                chars_pos_new.setdefault(char, chars_pos_change[char])
                                chars_image_new.setdefault(char, chars_image_change[char])
                        if len(hide_chars) > 0:
                            char_change = True
                            for char in hide_chars:
                                result_lines.append('hide ' + char)
                        for char in chars_pos_change:
                            if char in chars_list:
                                if chars_pos_change[char] == None:
                                    result_lines.append('show ' + char + ' ' + chars_image_change[char])
                                else:
                                    result_lines.append('show ' + char + ' ' + chars_image_change[char] + ' at ' + chars_pos_change[char])
                            else:
                                result_lines.append('show ' + char)
                        if char_change == True:
                            result_lines.append('with dissolve')
                            char_change = False
                        ids_show = ids_new
                        chars_pos_show = chars_pos_new
                        chars_image_show = chars_image_new
                        ids_change.clear()
                        chars_pos_change.clear()
                        chars_image_change.clear()
                        clear_chars.clear()
                    else:
                        ids_new = ids_show
                        chars_pos_new = chars_pos_show
                        chars_image_new = chars_image_show
                        for id in ids_change:
                            if id in ids_new:
                                ids_new[id] = ids_change[id]
                            else:
                                ids_new.setdefault(id, ids_change[id])
                        for char in chars_image_change:
                            if char in chars_pos_new:
                                if not chars_pos_new[char] == chars_pos_change[char]:
                                    char_change = True
                                    chars_pos_new[char] = chars_pos_change[char]
                                chars_image_new[char] = chars_image_change[char]
                            else:
                                char_change = True
                                chars_pos_new.setdefault(char, chars_pos_change[char])
                                chars_image_new.setdefault(char, chars_image_change[char])
                        for char in chars_pos_change:
                            if char in chars_list:
                                if chars_pos_change[char] == None:
                                    result_lines.append('show ' + char + ' ' + chars_image_change[char])
                                else:
                                    result_lines.append('show ' + char + ' ' + chars_image_change[char] + ' at ' + chars_pos_change[char])
                            else:
                                result_lines.append('show ' + char)
                        if char_change == True:
                            result_lines.append('with dissolve')
                            char_change = False
                        ids_show = ids_new
                        chars_pos_show = chars_pos_new
                        chars_image_show = chars_image_new
                        ids_change.clear()
                        chars_pos_change.clear()
                        chars_image_change.clear()
            elif line.startswith('#label '):
                match = re.match(rf'(#label)(\s+)(\S+)', line)
                result_lines.append('label ' + match.group(3) + ':')
            elif line.startswith('#goto '):
                match = re.match(rf'(#goto)(\s+)(\S+)', line)
                result_lines.append('jump ' + match.group(3))
            elif line.startswith('#select '):
                match00 = re.match(rf'(#select)(.*)', line)
                matches = re.findall(rf'(\s+)(\S+)', match00.group(2))
                #last_line = result_lines[-1]
                #first_line = None
                #if last_line.endswith('\"'):
                #    first_line = last_line[:-1] + '{fast}\"'
                result_lines.append('menu:')
                #if not first_line == None:
                #    result_lines.append('    ' + first_line)
                select_labels = []
                for match in matches:
                    select_labels.append(match[1])         
            else:
                result_lines.append(line)
        elif line.startswith('【'):
            match = re.match(rf'(【)(.*?)(】)(.*)', line)
            result_nom = match.group(2)
            result_text = match.group(4)
            if result_nom in chars_dict:
                result_char = chars_dict[result_nom]
            else:
                result_char = 'undefine_char'
            result_lines.append(result_char + ' \"' + result_text + '\"')
        else:
            if len(select_labels) > 0:
                result_lines.append('    \"' + line + '\":')
                result_lines.append('        jump ' + select_labels[0])
                select_labels.remove(select_labels[0])
            else:
                result_lines.append('\"' + line + '\"')

    ##特殊字符转换
    for i in range(0, len(result_lines)):        
        if not re.search(r'\\001', result_lines[i]) == None:
            result_lines[i] = result_lines[i].replace('\\001', '{font=Tuffy-Regular-EN.ttf}♡{/font}')
        if not re.search('♪', result_lines[i]) == None:
            result_lines[i] = result_lines[i].replace('♪', '{font=Tuffy-Regular-EN.ttf}♪{/font}')
    return result_lines

def krkr2rpy_file_write(file_old, file_new, encoding_old='utf8', encoding_new='utf8'):
    with open(file_old, 'r', encoding=encoding_old) as file:
        text = file.read()
        char = b'\xef\xbb\xbf'.decode()
        text = text.replace(char, '')
    result = krkr2rpy_main(text)
    with open(file_new, 'w', encoding=encoding_new) as file:
        for line in result:
            file.write(line)
            file.write('\n')


##test
krkr2rpy_file_write('D:\\ftest\\HANA15\\origin_files\\origin_script_CHN\\S090.src','D:\\test.rpy', encoding_old='utf_16_le') 
