""" MIDI演播类 """

from Midi import MidiMake, MidiFile, MidiPlayer, MidiModify


# MIDI 录制测试类
class MidiMakeTest:
    def __init__(self):
        test = MidiMake('test.midi', 200)
        test.add_notes_use_name([
            [0, '5', 0, 127, 1],
            [1, '3', 0, 127, 1],
            [2, '5', 0, 127, 1],
            [3, '7', 0, 127, 1],
            [4, '6', 0, 127, 2],
            [7, '5', 0, 127, 2],
            [9, '4', 0, 127, 2]
        ])

        test.save()


# MIDI 文件操作测试类
class MidiFileTest:
    def __init__(self):
        filename = 'Canon.mid'
        print("Exists: " + str(MidiFile.is_exists(filename)))
        print("Readable: " + str(MidiFile.readable(filename)))
        print("Writable: " + str(MidiFile.writable(filename)))
        print("MIDI: " + str(MidiFile.is_midi_file(filename)))
        print("Data: ")
        print(MidiFile.open_hex(filename))
        print("Deleted: " + str(MidiFile.delete(filename)))


# MIDI 演奏测试类
class MidiPlayTest:
    def __init__(self):
        test = MidiPlayer()


# MIDI 文件修饰测试类
class MidiModifyTest:
    def __init__(self):
        pass


# 程序入口
if __name__ == '__main__':
    # 录制测试
    # unit = MidiMakeTest()

    # 文件操作测试
    unit = MidiFileTest()
