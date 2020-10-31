"""
Mode by grouping version 2.20.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
"""

import statistics
import time


size = []  # Class Interval/Size
freq = []  # Frequencies

groups = []  # An array/list to store the values of highest group in different groups.
opt = 0


def main():
    """
    The main function for execution of the program.
    """
    global size, opt
    global freq
    global groups

    while True:
        size = []
        freq = []
        groups = []
        try:
            while True:
                try:
                    opt = input("\n> Is your data grouped?[y/n] ")
                    if opt == 'y' or opt == 'n' or opt == "info":
                        break
                except ValueError:
                    continue
            if opt == "info":
                full_license_info()
            elif opt == "n":
                sizes()
                print("_______________________________________")
                print("             MODE (Z) =", size[size.index(modal_class())])  # Mode in sizes.
                print("---------------------------------------")
            elif opt == "y":
                class_intervals()
                print("_______________________________________")
                print("             MODE (Z) =", mode())  # Mode in class intervals.
                print("---------------------------------------")
        except KeyboardInterrupt:
            print("")
            print("Exiting...")
            time.sleep(2)
            break


def class_intervals():
    """
    A function to print the class intervals and to get the frequencies.
    """
    upper = ""
    lower = ""
    n = 0

    while True:
        try:
            n = int(input("\n> Enter the number of class intervals: "))
        except ValueError:
            continue
        else:
            break  
    while True:
        try:
            lower = float(input("> Enter the lower limit of first class: "))
        except ValueError:
            continue
        else:
            break
    while True:
        try:
            upper = float(input("> Enter the upper limit of first class: "))
        except ValueError:
            continue
        else:
            break
    
    diff = float(upper) - float(lower)
    class_interval_table()  # Calling the class interval table function to print a table.    
    for i in range(n):
        lower = str(lower)
        upper = str(upper)
        space = len(upper) - len(lower)
        if i == 0:
            space += 2
        print("  ", lower + '-' + upper, " " * (20 + space), end="")
        frequency()  # Calling the frequency function to get the input from the user.
        size.append(lower + '-' + upper)
        lower = float(lower) + diff
        upper = float(upper) + diff


def sizes():
    """
    A function to print the size and to get the frequency inputs.
    """
    n = int(input("\n> Enter the number of sizes: "))
    size1 = float(input("> Enter the value of 1st size: "))
    size2 = float(input("> Enter the value of 2nd size: "))
    diff = size2 - size1
    size_table()  # Calling the size table function to print a table. 
    for i in range(n):
        size1 = str(size1)
        size2 = str(size2)
        space = len(size2) - len(size1)
        
        if space > 0:
            space -= 3
        elif space == 0:
            space -= len(size2) - 1

        print("  ", size1, " " * (27 + space), end="") 
        frequency()  # Calling the frequency function to get the input from the user.
        size.append(size1)
        size1 = float(size1) + diff
        size2 = float(size2) + diff


def frequency():
    """
    A function to get the value of frequency of the relative class intervals or size.
    """
    while True:
        try:
            value = int(input())
        except ValueError:
            print(" " * 33, end="")
            continue
        else:
            freq.append(value)
            break


def modal_class():
    """
    A function to return the modal class or mode(in case of size).
    """
    analyzer()  # Calling the analyzer function to get the values ready for calculation of mode.
    modal = statistics.mode(groups)
    return modal


def analyzer():
    """
    A function to estimate and analyze the modal class or mode(in case of size).
    """
    group1()
    group2() 
    group3() 
    group4() 
    group5() 
    group6()


def mode():
    """
    A function to calculate mode in case of class intervals.
    !> It calls the other functions which return the values of required values.
    !> It returns the value of mode to nearest 2nd decimal place.
    """
    try:
        z = round(l1() + ((f1() - f0()) / ((2 * f1()) - f0() - f2()) * h()), 2)
    except ZeroDivisionError:
        print("        * Denominator is ZERO! *")
        print("_______________________________________")
        print("                FORMULA\n")
        print("l + (|f1-f0|) / (|f1-f0| + |f1-f2|) * h\n")
        print("---------------------------------------")
        z = round(l1() + (abs((f1() - f0())) / (abs(f1() - f0()) + abs(f1() - f2())) * h()), 2)
    return z


def l1():
    """
    A function to return the value of (lower limit of modal class).
    """
    lower_limit = ""
    for i in modal_class():
        if i == "-":
            break
        else:
            lower_limit += i
    lower_limit = float(lower_limit)
    return lower_limit


def f0():
    """
    A function to return the value of (frequency of pre-modal class).
    """
    modal_class_freq = freq[size.index(modal_class()) - 1]
    return modal_class_freq


def f1():
    """
    A function to return the value of (frequency of modal class).
    """
    pre_modal_class_freq = freq[size.index(modal_class())]
    return pre_modal_class_freq


def f2():
    """
    A function to return the value of (frequency of next higher class or post-modal class).
    """
    post_modal_class_freq = freq[size.index(modal_class()) + 1]
    return post_modal_class_freq


def h():
    """
    A function to return the value of (size of the modal class).
    """
    h1 = l1()
    h2 = ""
    for i in modal_class()[::-1]:
        if i == "-":
            break
        else:
            h2 = i + h2
    h2 = float(h2)
    width = h2 - h1
    return width


def class_interval_table():
    """
    A function to print the class interval table.
    """
    print("_______________________________________")
    print("                TABLE")
    print("---------------------------------------")
    print("CLASS INTERVALS               FREQUENCY")


def size_table():
    """
    A function to print the size table.
    """
    print("_______________________________________")
    print("                TABLE")
    print("---------------------------------------")
    print("   SIZE                       FREQUENCY")


def group1():
    """
    A function to note the frequencies given by the user.
    !> It also returns the biggest value in this group.
    """
    m1 = []
    for i in range(len(size)):
        group = freq[i]
        m1.append(group)

    mode1 = max(m1)
    groups.append(size[freq.index(mode1)])


def group2():
    """
    A function to group the frequencies in form of (twos) beginning with the (1st) item.
    !> It also returns the biggest value in this group.
    """
    m2 = []
    for i in range(0, len(size) - 1, 2):
        group = freq[i] + freq[i + 1]
        m2.append(group)

    mode2 = max(m2)
    groups.append(size[m2.index(mode2) * 2])
    groups.append(size[m2.index(mode2) * 2 + 1])


def group3():
    """
    A function to group the frequencies in form of (twos) beginning with the (2nd) item.
    !> It also returns the biggest value in this group.
    """
    m3 = []
    for i in range(1, len(size) - 1, 2):
        group = freq[i] + freq[i + 1]
        m3.append(group)

    mode3 = max(m3)
    groups.append(size[m3.index(mode3) * 2 + 1])
    groups.append(size[m3.index(mode3) * 2 + 2])


def group4():
    """
    A function to group the frequencies in form of (threes) beginning with the (1st) item.
    !> It also returns the biggest value in this group.
    """
    m4 = []
    for i in range(0, len(size) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m4.append(group)

    mode4 = max(m4)
    groups.append(size[m4.index(mode4) * 3])
    groups.append(size[m4.index(mode4) * 3 + 1])
    groups.append(size[m4.index(mode4) * 3 + 2])


def group5():
    """
    A function to group the frequencies in form of (threes) beginning with the (2nd) item.
    !> It also returns the biggest value in this group.
    """
    m5 = []
    for i in range(1, len(size) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m5.append(group)

    mode5 = max(m5)
    groups.append(size[m5.index(mode5) * 3 + 1])
    groups.append(size[m5.index(mode5) * 3 + 2])
    groups.append(size[m5.index(mode5) * 3 + 3])


def group6():
    """
    A function to group the frequencies in form of (threes) beginning with the (3rd) item.
    !> It also returns the biggest value in this group.
    """
    m6 = []
    for i in range(2, len(size) - 2, 3):
        group = freq[i] + freq[i + 1] + freq[i + 2]
        m6.append(group)

    mode6 = max(m6)
    groups.append(size[m6.index(mode6) * 3 + 2])
    groups.append(size[m6.index(mode6) * 3 + 3])
    groups.append(size[m6.index(mode6) * 3 + 4])


def software_info():
    """
    A function to print the information related to the software.
    """
    print("""
Mode by grouping version 2.20.10.20

Copyright (c) 2020 Shahibur Rahaman
Licensed under MIT
""")


def full_license_info():
    """
    A funtion to print the full license info related to this software.
    """
    print("""
MIT License

Copyright (c) 2020 Shahibur Rahaman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")


if __name__ == "__main__":
    software_info()    
    print("Type (\"info\") for license information.")
    print("Press (Ctrl + C) to exit the program.\n")

    main()
