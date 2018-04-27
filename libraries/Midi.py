"""
描述： 该文件包含 MIDI 文件操作、MIDI 录制操作、MIDI 演奏操作等功能
作者： yowfung
日期： 2018-04-25
"""

import os
from midiutil.MidiFile3 import MIDIFile
from miditime.miditime import MIDITime


# MIDI 文件操作类
class MidiFile:
    # 文件是否存在
    @staticmethod
    def is_exists(filename):
        return os.access(filename, os.F_OK)

    # 文件是否可读
    @staticmethod
    def readable(filename):
        return os.access(filename, os.R_OK)

    # 文件是否可写
    @staticmethod
    def writable(filename):
        return os.access(filename, os.W_OK)

    # 是否为 MIDI 文件
    @staticmethod
    def is_midi_file(filename):
        if MidiFile.is_exists(filename):
            data = MidiFile.open_hex(filename)
            return True if data[:9] == '4d54 6864' else False
        else:
            return False

    # 打开文件并以十六进制形式返回
    @staticmethod
    def open_hex(filename):
        if MidiFile.is_exists(filename) is False:
            return None

        f = open(filename, 'rb')
        f.seek(0, 0)
        index = 0
        data = ""
        while True:
            temp = f.read(1)
            if len(temp) == 0:  # 读到文件尾
                break
            else:
                data += temp.hex()

            if index < 15:
                index += 1
                data += ' ' if index % 2 == 0 else ''
            else:
                index = 0
                data += '\n'
        f.close()

        return data

    # 删除文件
    @staticmethod
    def delete(filename):
        if MidiFile.is_exists(filename):
            os.remove(filename)
            return False if MidiFile.is_exists(filename) else True
        else:
            return False


# MIDI 录制类
class MidiMake(object):
    def __init__(self, filename='temp.midi', tempo=120, default_octave=5):
        self.filename = filename
        self.tempo = tempo
        self.default_octave = default_octave
        self.tracks = []
        self.channels = []
        self.track_selected = 0
        self.channel_selected = 0
        self.location = 0
        self.midi_file = MIDIFile(len(self.tracks))

    # 设置文件名
    def set_filename(self, filename):
        self.filename = filename

    # 设置文件信息
    def set_file_info(self, info):
        pass

    # 寻找起始点
    def find_origin(self):
        return self.midi_file.findOrigin()

    # 计算总时长
    def calc_total_time(self):
        pass

    # 切换通道
    def change_channel(self, channel_num):
        pass

    # 创建音轨
    def add_track(self, track_num, track_name):
        pass

    # 切换音轨
    def change_track(self, track_num):
        pass

    # 定位
    def locate(self, location):
        pass

    # 跳到末点
    def go_to_end(self):
        pass

    # 添加音符串(MIDI 音高形式)
    def add_notes(self, notes):
        """
        添加音符串
        notes = [[time, pitch, velocity, duration]]
        e.g: notes = [[0, 60, 127, 2]]
        """
        pass

    # 添加音符串(简谱/音名形式)
    def add_notes_use_name(self, notes):
        """
        添加音名/简谱形式的音符
        notes = [[time, name_pitch, octave, velocity, duration]]
        例：notes1 = [[0, 'Eb', 0, 127, 2]]; notes2 = [[0, '2#', 0, 127, 1]]
        """
        add_notes = []
        for note in notes:
            pitch = self.convert_pitch(note[1])
            pitch += 59 if pitch != 0 else 0
            add_notes.append([note[0], pitch, note[3], note[4]])

        # self.midi.add_track(add_notes)

    # 将简谱数字/音名转换成十二平均律数值
    @staticmethod
    def convert_pitch(pitch_char):
        """
        简谱/音名转十二平均律
        任何不在chart定义内的音符均转换成'0'
        """
        chart_plain = [["1"], ["1#", "2b"], ["2"], ["2#", "3b"], ["3"], ["4"], ["4#", "5b"], ["5"], ["5#", "6b"], ["6"],
                       ["6#", "7b"], ["7"]]
        chart_name = [["C"], ["C#", "Db"], ["D"], ["D#", "Eb"], ["E"], ["F"], ["F#", "Gb"], ["G"], ["G#", "Ab"], ["A"],
                      ["A#", "Bb"], ["B"]]

        i = 0
        for group in chart_plain:
            i += 1
            for char in group:
                if char == pitch_char:
                    return i
        i = 0
        for group in chart_name:
            i += 1
            for char in group:
                if char == pitch_char:
                    return i
        return 0

    # 删除当前音符
    def delete(self, note_id):
        pass

    # 播放当前音符
    def play(self, note_id):
        pass

    # 保存 MIDI 文件
    def save(self):
        self.midi.save_midi()

        # Create the MIDIFile Object with 1 track
        self.MIDIFile = MIDIFile(len(self.tracks))

        for i, note_list in enumerate(self.tracks):

            # Tracks are numbered from zero. Times are measured in beats.
            track = i
            time = 0

            # Add track name and tempo.
            self.MIDIFile.addTrackName(track, time, "Track %s" % i)
            self.MIDIFile.addTempo(track, time, self.tempo)

            for n in note_list:
                if len(n) == 2:
                    note = n[0]
                    channel = n[1]
                else:
                    note = n
                    channel = 0
                self.add_note(track, channel, note)

        # And write it to disk.
        binfile = open(self.outfile, 'wb')
        self.MIDIFile.writeFile(binfile)
        binfile.close()


# MIDI 演奏类
class MidiPlayer:
    def __init__(self):
        pass

    # 打开文件
    def open(self, filename):
        pass

    # 关闭文件
    def close(self):
        pass

    # 播放
    def play(self, locate=0):
        pass

    # 暂停
    def pause(self):
        pass

    # 获取总时长
    def get_time(self):
        pass

    # 获取播放位置
    def get_locate(self):
        pass

    # 定位
    def locate(self):
        pass

    # 设置播放速度
    def set_tempo(self, rate=0):
        pass


# MIDI 修饰类
class MidiModify:
    def __init__(self):
        pass

    # 修改文件基本信息
    def modify_info(self):
        pass

    # 删除音轨
    def del_track(self, track_num):
        pass

    # 删除通道数据
    def clear_channel(self, channel):
        pass

    # 删除音符
    def pitch_note(self, note):
        pass

    # 同音符去重
    def notes_renovate(self):
        pass

    # 寻找音符
    def notes_find(self, time):
        pass

    # 修改音符属性
    def note_modify(self, note, new_data):
        pass

    # 追加音符
    def add_notes(self, notes):
        pass
