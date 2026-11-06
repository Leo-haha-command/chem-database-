def extract(data):
    i = 0
    while i < len(data):
        if data.startswith("CE", i):
            return 1  # 1 = CE file
        if data.startswith("AL", i):
            return 2  # 2 = A level file
        if data.startswith("DSE", i):
            return 3  # 3 = DSE
        i += 1
    return 0  # or None, if no match
    
Here's a complete, runnable program that stores all your answers in a dictionary and lets you query them.

```python
ANSWERS = {
    # HKCEE
    "CE90_02": "D", "CE90_03": "C", "CE90_04": "A", "CE90_25": "D", "CE90_26": "C",
    "CE91_01": "B", "CE91_02": "A", "CE91_04": "A",
    "CE92_02": "D", "CE92_03": "C", "CE92_04": "A", "CE92_30": "A", "CE92_45": "C",
    "CE93_01": "D", "CE93_02": "B", "CE93_23": "D",
    "CE94_01": "C", "CE94_02": "B", "CE94_03": "A", "CE94_36": "A", "CE94_46": "B",
    "CE95_01": "A", "CE95_02": "D", "CE95_03": "A", "CE95_04": "C", "CE95_06": "A",
    "CE95_26": "B", "CE95_34": "A", "CE95_39": "A",
    "CE96_01": "C", "CE96_02": "B", "CE96_03": "A", "CE96_39": "A", "CE96_44": "C",
    "CE96_45": "B", "CE96_50": "C",
    "CE97_01": "D", "CE97_02": "B", "CE97_03": "D", "CE97_05": "B", "CE97_30": "C",
    "CE98_01": "D", "CE98_18": "B", "CE98_33": "B", "CE98_45": "A",
    "CE99_01": "B", "CE99_05": "D", "CE99_11": "A", "CE99_19": "B", "CE99_34": "D",
    "CE99_39": "C", "CE99_46": "A",
    "CE00_01": "B", "CE00_07": "C", "CE00_09": "D", "CE00_17": "B", "CE00_34": "D",
    "CE00_39": "D", "CE00_42": "D", "CE00_46": "C",
    "CE01_01": "D", "CE01_07": "A", "CE01_18": "B", "CE01_20": "B", "CE01_37": "D",
    "CE01_42": "A", "CE01_49": "D",
    "CE02_01": "C", "CE02_28": "A", "CE02_36": "D", "CE02_46": "A", "CE02_49": "A",
    "CE03_01": "C", "CE03_12": "B", "CE03_25": "D", "CE03_46": "B",
    "CE04_01": "C", "CE04_02": "D", "CE04_10": "B", "CE04_23": "C", "CE04_30": "A",
    "CE04_31": "B",
    "CE05SP_03": "B", "CE05SP_16": "D", "CE05SP_31": "A",
    "CE05_03": "B", "CE05_06": "D", "CE05_07": "C", "CE05_09": "B", "CE05_13": "D",
    "CE05_27": "B",
    "CE06_01": "D", "CE06_02": "D", "CE06_04": "B", "CE06_05": "B", "CE06_06": "C",
    "CE06_14": "B", "CE06_24": "D",
    "CE07_03": "D", "CE07_12": "D", "CE07_13": "A", "CE07_18": "B", "CE07_28": "C",
    "CE07_29": "C", "CE07_43": "A",
    "CE08_02": "D", "CE08_18": "D", "CE08_19": "B", "CE08_46": "B",
    "CE09_01": "C", "CE09_07": "D", "CE09_18": "A", "CE09_19": "C", "CE09_22": "D",
    "CE09_28": "B",
    "CE10_01": "A", "CE10_13": "D", "CE10_17": "B",
    "CE11_01": "D", "CE11_02": "B", "CE11_03": "C", "CE11_31": "D",

    # HKAL
    "AL10(I)_03": "D",

    # HKDSE
    "DSE11SP_07": "A", "DSE11SP_11": "C", "DSE11SP_22": "D", "DSE11SP_24": "C",
    "DSE11SP_36": "C",
    "DSE12PP_01": "B", "DSE12PP_03": "A", "DSE12PP_04": "D", "DSE12PP_15": "D",
    "DSE12PP_18": "A",
    "DSE12_01": "D", "DSE12_08": "C", "DSE12_15": "D",
    "DSE13_01": "C", "DSE13_02": "C", "DSE13_04": "B", "DSE13_12": "D",
    "DSE14_01": "C", "DSE14_02": "D",
    "DSE15_03": "B", "DSE15_15": "A", "DSE15_35": "B",
    "DSE16_02": "C",
    "DSE17_01": "C", "DSE17_16": "A",
    "DSE18_02": "C", "DSE18_05": "C",
    "DSE19_01": "C", "DSE19_02": "A", "DSE19_24": "A",
    "DSE2020_02": "D", "DSE2020_03": "C", "DSE2020_05": "B", "DSE2020_14": "C",
    "DSE2021_01": "D", "DSE2021_19": "C", "DSE2021_21": "C",
    "DSE2022_06": "B", "DSE2022_07": "D", "DSE2022_10": "A", "DSE2022_18": "D",
}


