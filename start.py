import random

EnchantmentList = ["날카로움", "강타", "살충", "밀치기", "발화", "휘몰아치는 칼날", "약탈",
                   "급류", "집전", "충절", "찌르기", "보호", "화염 보호", "폭발 보호", "발사체 보호",
                   "호흡", "친수성", "가시", "가벼운 착지", "물갈퀴", "차가운 걸음", "영혼 가속", "효율", "섬세한 손길",
                   "행운", "바다의 행운", "미끼", "힘", "밀어내기", "화염", "무한", "수선", "관통", "다중 발사", "빠른 장전",
                   "내구성", "귀속 저주", "소실 저주"]

EnchantmentTier = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

random1 = random.randint(0, 37)
random2 = random.randint(0, 4)

Enchantmentresult = f"{EnchantmentList[random1]} {EnchantmentTier[random2]}"
print(Enchantmentresult)