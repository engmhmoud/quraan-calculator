"""
Quran Data Module
Contains all 114 suras with their names and ayah counts
"""

# Complete list of Quran suras with their ayah counts
SURAS = {
    1: {"name": "Al-Fatiha", "ayahs": 7, "arabic": "الفاتحة", "page_start": 1, "page_end": 1},
    2: {"name": "Al-Baqarah", "ayahs": 286, "arabic": "البقرة", "page_start": 2, "page_end": 49},
    3: {"name": "Aal-e-Imran", "ayahs": 200, "arabic": "آل عمران", "page_start": 50, "page_end": 76},
    4: {"name": "An-Nisa", "ayahs": 176, "arabic": "النساء", "page_start": 77, "page_end": 106},
    5: {"name": "Al-Maidah", "ayahs": 120, "arabic": "المائدة", "page_start": 106, "page_end": 127},
    6: {"name": "Al-Anam", "ayahs": 165, "arabic": "الأنعام", "page_start": 128, "page_end": 150},
    7: {"name": "Al-Araf", "ayahs": 206, "arabic": "الأعراف", "page_start": 151, "page_end": 176},
    8: {"name": "Al-Anfal", "ayahs": 75, "arabic": "الأنفال", "page_start": 177, "page_end": 186},
    9: {"name": "At-Tawbah", "ayahs": 129, "arabic": "التوبة", "page_start": 187, "page_end": 207},
    10: {"name": "Yunus", "ayahs": 109, "arabic": "يونس", "page_start": 208, "page_end": 221},
    11: {"name": "Hud", "ayahs": 123, "arabic": "هود", "page_start": 221, "page_end": 235},
    12: {"name": "Yusuf", "ayahs": 111, "arabic": "يوسف", "page_start": 235, "page_end": 248},
    13: {"name": "Ar-Rad", "ayahs": 43, "arabic": "الرعد", "page_start": 249, "page_end": 255},
    14: {"name": "Ibrahim", "ayahs": 52, "arabic": "ابراهيم", "page_start": 255, "page_end": 261},
    15: {"name": "Al-Hijr", "ayahs": 99, "arabic": "الحجر", "page_start": 262, "page_end": 267},
    16: {"name": "An-Nahl", "ayahs": 128, "arabic": "النحل", "page_start": 267, "page_end": 281},
    17: {"name": "Al-Isra", "ayahs": 111, "arabic": "الإسراء", "page_start": 282, "page_end": 293},
    18: {"name": "Al-Kahf", "ayahs": 110, "arabic": "الكهف", "page_start": 293, "page_end": 304},
    19: {"name": "Maryam", "ayahs": 98, "arabic": "مريم", "page_start": 305, "page_end": 312},
    20: {"name": "Taha", "ayahs": 135, "arabic": "طه", "page_start": 312, "page_end": 321},
    21: {"name": "Al-Anbiya", "ayahs": 112, "arabic": "الأنبياء", "page_start": 322, "page_end": 331},
    22: {"name": "Al-Hajj", "ayahs": 78, "arabic": "الحج", "page_start": 332, "page_end": 341},
    23: {"name": "Al-Muminun", "ayahs": 118, "arabic": "المؤمنون", "page_start": 342, "page_end": 349},
    24: {"name": "An-Nur", "ayahs": 64, "arabic": "النور", "page_start": 350, "page_end": 359},
    25: {"name": "Al-Furqan", "ayahs": 77, "arabic": "الفرقان", "page_start": 359, "page_end": 366},
    26: {"name": "Ash-Shuara", "ayahs": 227, "arabic": "الشعراء", "page_start": 367, "page_end": 376},
    27: {"name": "An-Naml", "ayahs": 93, "arabic": "النمل", "page_start": 377, "page_end": 385},
    28: {"name": "Al-Qasas", "ayahs": 88, "arabic": "القصص", "page_start": 385, "page_end": 396},
    29: {"name": "Al-Ankabut", "ayahs": 69, "arabic": "العنكبوت", "page_start": 396, "page_end": 404},
    30: {"name": "Ar-Rum", "ayahs": 60, "arabic": "الروم", "page_start": 404, "page_end": 410},
    31: {"name": "Luqman", "ayahs": 34, "arabic": "لقمان", "page_start": 411, "page_end": 414},
    32: {"name": "As-Sajdah", "ayahs": 30, "arabic": "السجدة", "page_start": 415, "page_end": 417},
    33: {"name": "Al-Ahzab", "ayahs": 73, "arabic": "الأحزاب", "page_start": 418, "page_end": 427},
    34: {"name": "Saba", "ayahs": 54, "arabic": "سبأ", "page_start": 428, "page_end": 434},
    35: {"name": "Fatir", "ayahs": 45, "arabic": "فاطر", "page_start": 434, "page_end": 440},
    36: {"name": "Ya-Sin", "ayahs": 83, "arabic": "يس", "page_start": 440, "page_end": 445},
    37: {"name": "As-Saffat", "ayahs": 182, "arabic": "الصافات", "page_start": 446, "page_end": 452},
    38: {"name": "Sad", "ayahs": 88, "arabic": "ص", "page_start": 453, "page_end": 458},
    39: {"name": "Az-Zumar", "ayahs": 75, "arabic": "الزمر", "page_start": 458, "page_end": 467},
    40: {"name": "Ghafir", "ayahs": 85, "arabic": "غافر", "page_start": 467, "page_end": 476},
    41: {"name": "Fussilat", "ayahs": 54, "arabic": "فصلت", "page_start": 477, "page_end": 482},
    42: {"name": "Ash-Shuraa", "ayahs": 53, "arabic": "الشورى", "page_start": 483, "page_end": 489},
    43: {"name": "Az-Zukhruf", "ayahs": 89, "arabic": "الزخرف", "page_start": 489, "page_end": 495},
    44: {"name": "Ad-Dukhan", "ayahs": 59, "arabic": "الدخان", "page_start": 496, "page_end": 498},
    45: {"name": "Al-Jathiyah", "ayahs": 37, "arabic": "الجاثية", "page_start": 499, "page_end": 502},
    46: {"name": "Al-Ahqaf", "ayahs": 35, "arabic": "الأحقاف", "page_start": 502, "page_end": 506},
    47: {"name": "Muhammad", "ayahs": 38, "arabic": "محمد", "page_start": 507, "page_end": 510},
    48: {"name": "Al-Fath", "ayahs": 29, "arabic": "الفتح", "page_start": 511, "page_end": 515},
    49: {"name": "Al-Hujurat", "ayahs": 18, "arabic": "الحجرات", "page_start": 515, "page_end": 517},
    50: {"name": "Qaf", "ayahs": 45, "arabic": "ق", "page_start": 518, "page_end": 520},
    51: {"name": "Adh-Dhariyat", "ayahs": 60, "arabic": "الذاريات", "page_start": 520, "page_end": 523},
    52: {"name": "At-Tur", "ayahs": 49, "arabic": "الطور", "page_start": 523, "page_end": 525},
    53: {"name": "An-Najm", "ayahs": 62, "arabic": "النجم", "page_start": 526, "page_end": 528},
    54: {"name": "Al-Qamar", "ayahs": 55, "arabic": "القمر", "page_start": 528, "page_end": 531},
    55: {"name": "Ar-Rahman", "ayahs": 78, "arabic": "الرحمن", "page_start": 531, "page_end": 534},
    56: {"name": "Al-Waqiah", "ayahs": 96, "arabic": "الواقعة", "page_start": 534, "page_end": 537},
    57: {"name": "Al-Hadid", "ayahs": 29, "arabic": "الحديد", "page_start": 537, "page_end": 541},
    58: {"name": "Al-Mujadila", "ayahs": 22, "arabic": "المجادلة", "page_start": 542, "page_end": 545},
    59: {"name": "Al-Hashr", "ayahs": 24, "arabic": "الحشر", "page_start": 545, "page_end": 548},
    60: {"name": "Al-Mumtahanah", "ayahs": 13, "arabic": "الممتحنة", "page_start": 549, "page_end": 551},
    61: {"name": "As-Saff", "ayahs": 14, "arabic": "الصف", "page_start": 551, "page_end": 552},
    62: {"name": "Al-Jumuah", "ayahs": 11, "arabic": "الجمعة", "page_start": 553, "page_end": 554},
    63: {"name": "Al-Munafiqun", "ayahs": 11, "arabic": "المنافقون", "page_start": 554, "page_end": 555},
    64: {"name": "At-Taghabun", "ayahs": 18, "arabic": "التغابن", "page_start": 556, "page_end": 557},
    65: {"name": "At-Talaq", "ayahs": 12, "arabic": "الطلاق", "page_start": 558, "page_end": 559},
    66: {"name": "At-Tahrim", "ayahs": 12, "arabic": "التحريم", "page_start": 560, "page_end": 561},
    67: {"name": "Al-Mulk", "ayahs": 30, "arabic": "الملك", "page_start": 562, "page_end": 564},
    68: {"name": "Al-Qalam", "ayahs": 52, "arabic": "القلم", "page_start": 564, "page_end": 566},
    69: {"name": "Al-Haqqah", "ayahs": 52, "arabic": "الحاقة", "page_start": 566, "page_end": 568},
    70: {"name": "Al-Maarij", "ayahs": 44, "arabic": "المعارج", "page_start": 568, "page_end": 570},
    71: {"name": "Nuh", "ayahs": 28, "arabic": "نوح", "page_start": 570, "page_end": 571},
    72: {"name": "Al-Jinn", "ayahs": 28, "arabic": "الجن", "page_start": 572, "page_end": 573},
    73: {"name": "Al-Muzzammil", "ayahs": 20, "arabic": "المزمل", "page_start": 574, "page_end": 575},
    74: {"name": "Al-Muddaththir", "ayahs": 56, "arabic": "المدثر", "page_start": 575, "page_end": 577},
    75: {"name": "Al-Qiyamah", "ayahs": 40, "arabic": "القيامة", "page_start": 577, "page_end": 578},
    76: {"name": "Al-Insan", "ayahs": 31, "arabic": "الإنسان", "page_start": 578, "page_end": 580},
    77: {"name": "Al-Mursalat", "ayahs": 50, "arabic": "المرسلات", "page_start": 580, "page_end": 581},
    
    
    78: {"name": "An-Naba", "ayahs": 40, "arabic": "النبأ", "page_start": 582, "page_end": 583},
    79: {"name": "An-Naziat", "ayahs": 46, "arabic": "النازعات", "page_start": 583, "page_end": 584},
    80: {"name": "Abasa", "ayahs": 42, "arabic": "عبس", "page_start": 585, "page_end": 585},
    81: {"name": "At-Takwir", "ayahs": 29, "arabic": "التكوير", "page_start": 586, "page_end": 586},
    82: {"name": "Al-Infitar", "ayahs": 19, "arabic": "الإنفطار", "page_start": 587, "page_end": 586},
    83: {"name": "Al-Mutaffifin", "ayahs": 36, "arabic": "المطففين", "page_start": 587, "page_end": 588},
    84: {"name": "Al-Inshiqaq", "ayahs": 25, "arabic": "الإنشقاق", "page_start": 589, "page_end": 589},
    85: {"name": "Al-Buruj", "ayahs": 22, "arabic": "البروج", "page_start": 590, "page_end": 590},
    86: {"name": "At-Tariq", "ayahs": 17, "arabic": "الطارق", "page_start": 591, "page_end": 591},
    87: {"name": "Al-Ala", "ayahs": 19, "arabic": "الأعلى", "page_start": 591, "page_end": 592},
    88: {"name": "Al-Ghashiyah", "ayahs": 26, "arabic": "الغاشية", "page_start": 592, "page_end": 592},
    
    
    89: {"name": "Al-Fajr", "ayahs": 30, "arabic": "الفجر", "page_start": 593, "page_end": 594},
    90: {"name": "Al-Balad", "ayahs": 20, "arabic": "البلد", "page_start": 594, "page_end": 594},
    91: {"name": "Ash-Shams", "ayahs": 15, "arabic": "الشمس", "page_start": 595, "page_end": 595},
    
    
    92: {"name": "Al-Layl", "ayahs": 21, "arabic": "الليل", "page_start": 595, "page_end": 596},
    93: {"name": "Ad-Duhaa", "ayahs": 11, "arabic": "الضحى", "page_start": 596, "page_end": 596},
    94: {"name": "Ash-Sharh", "ayahs": 8, "arabic": "الشرح", "page_start": 596, "page_end": 596},
    95: {"name": "At-Tin", "ayahs": 8, "arabic": "التين", "page_start": 597, "page_end": 597},
    96: {"name": "Al-Alaq", "ayahs": 19, "arabic": "العلق", "page_start": 597, "page_end": 597},
    97: {"name": "Al-Qadr", "ayahs": 5, "arabic": "القدر", "page_start": 598, "page_end": 598},
    98: {"name": "Al-Bayyinah", "ayahs": 8, "arabic": "البينة", "page_start": 598, "page_end": 599},
    99: {"name": "Az-Zalzalah", "ayahs": 8, "arabic": "الزلزلة", "page_start": 599, "page_end": 599},
    100: {"name": "Al-Adiyat", "ayahs": 11, "arabic": "العاديات", "page_start": 599, "page_end": 600},
    101: {"name": "Al-Qariah", "ayahs": 11, "arabic": "القارعة", "page_start": 600, "page_end": 600},
    102: {"name": "At-Takathur", "ayahs": 8, "arabic": "التكاثر", "page_start": 600, "page_end": 600},
    
    103: {"name": "Al-Asr", "ayahs": 3, "arabic": "العصر", "page_start": 601, "page_end": 601},
    104: {"name": "Al-Humazah", "ayahs": 9, "arabic": "الهمزة", "page_start": 601, "page_end": 601},
    105: {"name": "Al-Fil", "ayahs": 5, "arabic": "الفيل", "page_start": 601, "page_end": 601},
    106: {"name": "Quraysh", "ayahs": 4, "arabic": "قريش", "page_start": 602, "page_end": 602},
    107: {"name": "Al-Maun", "ayahs": 7, "arabic": "الماعون", "page_start": 602, "page_end": 602},
    108: {"name": "Al-Kawthar", "ayahs": 3, "arabic": "الكوثر", "page_start": 602, "page_end": 602},
    109: {"name": "Al-Kafirun", "ayahs": 6, "arabic": "الكافرون", "page_start": 603, "page_end": 603},
    110: {"name": "An-Nasr", "ayahs": 3, "arabic": "النصر", "page_start": 603, "page_end": 603},
    111: {"name": "Al-Masad", "ayahs": 5, "arabic": "المسد", "page_start": 603, "page_end": 603},
    112: {"name": "Al-Ikhlas", "ayahs": 4, "arabic": "الإخلاص", "page_start": 604, "page_end": 604},
    113: {"name": "Al-Falaq", "ayahs": 5, "arabic": "الفلق", "page_start": 604, "page_end": 604},
    114: {"name": "An-Nas", "ayahs": 6, "arabic": "الناس", "page_start": 604, "page_end": 604}
}

def get_sura_names():
    """Return a list of all sura names for autocomplete"""
    return [sura["name"] for sura in SURAS.values()]

def get_sura_by_name(name):
    """Find sura by name (case-insensitive)"""
    for num, sura in SURAS.items():
        if sura["name"].lower() == name.lower():
            return num, sura
    return None, None

def get_sura_number_by_name(name):
    """Get sura number by name"""
    sura_num, _ = get_sura_by_name(name)
    return sura_num

def is_valid_sura_name(name):
    """Check if a sura name is valid"""
    return any(sura["name"].lower() == name.lower() for sura in SURAS.values())

def get_total_ayahs():
    """Get total number of ayahs in the Quran"""
    return sum(sura["ayahs"] for sura in SURAS.values()) 