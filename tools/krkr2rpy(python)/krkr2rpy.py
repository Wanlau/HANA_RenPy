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

def krkr2rpy_main(text_input):
    text_lines = text_input.splitlines()
    result_lines = []
    scene_show = ''
    cu_show = ''
    chars_show = []
    last_change = []
    for line in text_lines:
        if re.match(rf'(\S+)', line) == None:
            result_lines.append('')
        elif line.startswith(';'):
            match = re.match(rf'(;)(.*)', line)
            result = match.group(2)
            result_lines.append('#' + result)
        elif line.startswith('#'):
            if line.startswith('#savetitle'):
                match = re.match(rf'(#savetitle)(.*?)(\S+)', line)
                result = match.group(3)
                result_lines.append('$ save_name = \"' + result + '\"')
            elif line.startswith('#voice'):
                match = re.match(rf'(#voice)(.*?)(\S+)', line)
                result = match.group(3)
                result_lines.append('voice \"' + result + '\"')
            elif line.startswith('#bgm'):
                match = re.match(rf'(#bgm)(\s+)(\S+)(\s+)(\S+)(\s*)(\S*)', line)
                if match.group(5) == 'stop':
                    result_lines.append('stop music fadeout 2.0')
                else:
                    result_lines.append('play music \"bgm/' + match.group(5) + '.ogg\" fadein 1.0')
            elif line.startswith('#mes'):
                match = re.match(rf'(#mes)(.*?)(\S+)', line)
                result = match.group(3)
                if result == 'on':
                    result_lines.append('window show')
                elif result == 'off':
                    result_lines.append('window hide')
            elif line.startswith('#system'):
                pass
            elif line.startswith('#bg'):
                match = re.match(rf'(#bg)(.*?)(\S+)', line)
                last_change = 
                result_lines.append('scene ' + match.group(3))
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
            result_lines.append('\"' + line + '\"')

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
krkr2rpy_file_write('D:\\ftest\\HANA15\\origin_files\\origin_script_CHN\\S120.src','D:\\test.rpy', encoding_old='utf_16_le') 
