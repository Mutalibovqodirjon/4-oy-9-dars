# 1 misol
import time
from threading import Thread

# def calculate_sum(digits: str):
#     total = 0
#     for digit in digits:
#         print("Raqamlar hisoblanmoqda")
#         time.sleep(0.5)
#         total += int(digit)
#         print("Hisoblandi!")
#
# if __name__ == "__main__":
#     num = input("Son kiriting: ")
#     start_time = time.time()
#
#     threads = []
#
#     for _ in range(100):
#         thread = Thread(target=calculate_sum, args=(num,))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
#     end_time = time.time()
#
#     print(f"sariflanganvaqt : {round(end_time - start_time, 2)} seconds")

#
# #3 misol
#
# from threading import Thread
#
# def capitalize(words : str):
#     global new_names
#     if words.isalpha():
#         new_names.append(words.capitalize())
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# new_names = []
# tredings = []
#
# for i in names:
#     th = Thread(target=capitalize , args=(i,))
#     tredings.append(th)
#     th.start()
#
# for j in tredings:
#     j.join()
#
# print(new_names)
#
#

# #  4 misol
# from threading import Thread
#
# def capitalize(nums):
#     global new_nums
#     if nums > 75:
#         new_nums.append(nums)
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# new_nums = []
# tredings = []
#
# for i in scores:
#     th = Thread(target=capitalize , args=(i,))
#     tredings.append(th)
#     th.start()
#
# for j in tredings:
#     j.join()
#
# print(new_nums)


#  5 misol
# from threading import Thread
# def capitalize(words : str):
#     global new_names
#     if words.lower() == words[::-1].lower():
#             new_names.append(words)
#
# names = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# new_names = []
# tredings = []
#
# for i in names:
#     th = Thread(target=capitalize , args=(i,))
#     tredings.append(th)
#     th.start()
#
# for j in tredings:
#     j.join()
#
# print(new_names)



# 6 misol
import threading
# text = input("Matn kiriting: ")
# str = ""
# i = 0
# while i < len(text):
#     if text[i] == 'e':
#         str += '3'
#     else:
#         str += text[i]
#     i += 1
# print(str)
#

# 7 misol
# import threading
# import time
#
# def boshliq(matn):
#     res = ""
#     i = 0
#     while i < len(matn):
#         if matn[i] != " ":
#             res += matn[i]
#         i += 1
#     return res
# def a(matn):
#     res = boshliq(matn)
#     time.sleep(0.5)
#     print(f"Yangilangan matn: {res}")
# def b():
#     try:
#         matn = input("Matn kiriting: ")
#         print("bajarilmoqda..")
#         start = time.time()
#         hisoblash_oqimi = threading.Thread(target=a, args=(matn,))
#         hisoblash_oqimi.start()
#         hisoblash_oqimi.join()
#         end = time.time()
#         print(f"Ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# b()



# 8 misol
#
# import threading
# import time
#
# def thred(index, list):
#     list[index] *= 2
#     print(f"Element {index+1} ko'paytirildi: {list[index]}")
# def ab():
#     try:
#         list = [i+1 for i in range(10, 20, 1)]
#         print(f"Ro'yxat: {list}")
#         print("Bajarilmoqda...")
#         start = time.time()
#         threads = []
#         for i in range(len(list)):
#             hisoplash = threading.Thread(target=thred, args=(i, list))
#             threads.append(hisoplash)
#             hisoplash.start()
#         for oqim in threads:
#             oqim.join()
#         end = time.time()
#         print(f" ro'yxat: {list}")
#         print(f" ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# ab()



# 9 misol

# import threading
# import time
# import random
#
# def generator(index):
#     num = random.randint(1, 100)
#     print(f"Son {index+1}: Tasodifiy son {num}")
# def a():
#     try:
#         print("Bajariloqda...")
#         start = time.time()
#         threads = []
#         for i in range(10):
#             hisoblash_oqimi = threading.Thread(target=generator, args=(i,))
#             threads.append(hisoblash_oqimi)
#             hisoblash_oqimi.start()
#         for oqim in threads:
#             oqim.join()
#         end = time.time()
#         print(f" ketgan vaqt: {round(end - start, 2)} soniya.")
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# a()
#
#



