import hashlib
import struct
import copy

class MsdCipher:
    def __init__(self, key):
        self.key = key
        self.block_num = 0
        self.block_size = 0x20
        
    def decrypt(self, data):
        output = bytearray()
        total_len = len(data)
        processed = 0

        # 处理完整块
        while processed + self.block_size <= total_len:
            chunk = data[processed : processed+self.block_size]
            self._process_chunk(chunk, output)
            processed += self.block_size

        # 处理最后不完整块
        if processed < total_len:
            remaining = data[processed:]
            self._process_chunk(remaining, output)

        return bytes(output)

    def _process_chunk(self, chunk: bytes, output: bytearray):
        chunk_key = f"{self.key}{self.block_num}".encode('shift_jis')
        md5_hash = hashlib.md5(chunk_key).hexdigest()  # 32字符
        for j in range(len(chunk)):  # 关键：按实际块长度循环
            output.append(chunk[j] ^ ord(md5_hash[j % 32])) 
        self.block_num += 1


##未完善
##尝试从MSD读取部分脚本信息(如语音、文本、背景、立绘等)
class MsdReader:
    def __init__(self, msd_path, encoding='utf8'):
        self.msd_path = msd_path
        self.encoding = encoding
        self.codes = []

    ##MSD读取轻量版（仅含对话、语音、背景、立绘、音效、背景音乐）
    def MsdReadLight(self):
        with open(self.msd_path, 'rb') as file:
            file_size = len(file.read())
            offset = 0

            ##文件头读取
            file.seek(offset)
            head = file.read(0x10).decode(encoding=self.encoding)
            if not head == "MSCENARIO FILE  ":
                raise ValueError("not MSD file")
            
            ##跳过头部数据区域
            file.seek(0x14)
            int01 = struct.unpack('<i', file.read(4))[0]
            int02 = struct.unpack('<i', file.read(4))[0]

            offset = 0x0458 + 4 * (int01 + int02)
            file.seek(offset)

            ##读取指令数据
            code = None
            size = None
            code_raw = None
            self.codes = []
            while offset + 3 < file_size:
                ##读取指令及参数区域大小
                code_raw = file.read(2)
                size = struct.unpack('<h', file.read(2))[0]
                offset += 4

                if not code_raw in self.codes_list_light:
                    offset += size
                    file.seek(offset)
                    continue
                else:
                    code = self.codes_list_light[code_raw]

                    ##读取部分已知及其参数
                    args_data = file.read(size)
                    offset  += size
                    args = self.ArgsRead(args_data)
                    self.codes.append({"code":code, "args":args})

        return  copy.deepcopy(self.codes)

    def ArgsRead(self, data):
        data_size = len(data)
        offset = 0
        args = []
        flag = None
        while offset < data_size:
            flag = data[offset]
            offset += 1
            ##`01 `为4字节整数标志
            if flag == 1:
                arg_data = data[offset:offset+4]
                offset += 4
                arg = struct.unpack('<i', arg_data)[0]
                args.append(arg)
            ##`02 `标志也是4字节数据，具体意义不明，暂当4字节整数处理
            elif flag == 2:
                arg_data = data[offset:offset+4]
                offset += 4
                arg = struct.unpack('<i', arg_data)[0]
                args.append(arg)
            ##`03 `为字符串标志，其后为字符串数据，直至字符串结束标志`00 `
            elif flag == 3:
                strbytes = bytearray()
                while  offset < data_size:
                    arg_data = data[offset]
                    offset += 1
                    if arg_data == 0:
                        break
                    else:
                        strbytes.append(arg_data)
                args.append(strbytes.decode(self.encoding))
            else:
                raise ValueError(f'unknown flag {flag}')
                #pass
            
        return args 
                        


    codes_list_light = {
        b"\xd7\x07" :   "char"  ,
        b"\xd8\x07" :   "voice" ,
        b"\xda\x07" :   "text"  ,
        b"\xed\x03" :   "title" ,
        b"\xc9\x00" :   "bgm"   ,
        b"\xd3\x00" :   "se"    ,
        b"\x64\x00" :   "image" ,
        b"\x65\x00" :   "image_clear"   ,
        b"\x66\x00" :   "image2" ,
        b"\x67\x00" :   "image_show"    ,
        b"\x6e\x00" :   "transfrom"     ,
        b"\xde\x07" :   "select"        ,   #???
        b"\x05\x00" :   "label"         ,   #???
    }