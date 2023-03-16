# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     date = list(map(int, input())) #0123 / 45 / 67
#     year = date[:4]
#     month = date[4:6]
#     day = date[6:]
#     month_ans = 0
#     day_ans = 0
#     year_ans = year[0] * 1000 + year[1] * 100 + year[2] * 10 + year[3]
#     if 1 <= month[0] * 10 + month[1] <= 12:
#         month_ans = month[0] * 10 + month[1]
#         if month_ans == 1 or month_ans == 3 or month_ans == 5 or month_ans == 7 or month_ans == 8 or month_ans == 10 or month_ans == 12 :
#             if 1 <= day[0] * 10 + day[1] <= 31:
#                 day_ans = day[0] * 10 + day[1]
#             else:
#                 print("#{} {}".format(test_case, -1))
#                 continue
#         elif month_ans == 4 or month_ans == 6 or month_ans == 9 or month_ans == 11:
#             if 1<= day[0] * 10 + day[1] <= 30:
#                 day_ans = day[0] * 10 + day[1]
#             else:
#                 print("#{} {}".format(test_case, -1))
#                 continue
#         else:
#             if 1<= day[0] * 10 + day[1] <= 28:
#                 day_ans = day[0] * 10 + day[1]
#             else:
#                 print("#{} {}".format(test_case, -1))
#                 continue
#         if month_ans < 10:
#             if day_ans < 10:
#                 print("#{0} {1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format(test_case, year[0],year[1], year[2], year[3], "/", 0, month_ans, "/", 0, day_ans))
#             else:
#                 print("#{0} {1}{2}{3}{4}{5}{6}{7}{8}{9}".format(test_case, year[0],year[1], year[2], year[3], "/", 0, month_ans, "/", day_ans))
#         else:
#             if day_ans < 10:
#                 print("#{0} {1}{2}{3}{4}{5}{6}{7}{8}{9}".format(test_case, year[0],year[1], year[2], year[3], "/", month_ans, "/", 0, day_ans))
#             else:
#                 print("#{0} {1}{2}{3}{4}{5}{6}{7}{8}".format(test_case, year[0],year[1], year[2], year[3], "/", month_ans, "/", day_ans))
            
#     else:
#         print("#{} {}".format(test_case, -1))
#         continue


# t = int(input())
# for test_case in range(1, t+1):
#     date = list(input())
#     #빈 문자열 초기화
#     year = "" 
#     month = ""
#     day = ""
#     #for문을 돌면서 date 값을 더해준다. 
#     #이렇게 하면 1+1+1+1 = 1111 이 된다. (문자열의 더하기)
#     for i in range(4):
#         year += date[i]
#     for j in range(4,6):
#         month += date[j]
#     for k in range(6,8):
#         day += date[k]

#     #리스트를 만들어주고 <in> 을 통해 리스트 중 일치하는 값이 있는지 체크한다.
#     if (int(month) in [1,3,5,7,8,10,12]) and (0 < int(day) < 32):
#         ans = str(year) + "/" + str(month) + "/" + str(day)
#     elif (int(month) in [4,6,9,11]) and (0 < int(day) < 31):
#         ans = str(year) + "/" + str(month) + "/" + str(day)
#     elif int(month) == 2 and (0 < int(day) < 29):
#         ans = str(year) + "/" + str(month) + "/" + str(day)
#     else:
#         ans = "-1"
#     print("#{} {}".format(test_case, ans))

t = int(input())

for test_case in range(1, t+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, \
            8:31, 9:30, 10:31, 11:30, 12:31}
    
    if 0 < int(month) < 13 and int(day) <= days[int(month)]:
        print("#{} {}/{}/{}".format(test_case, year, month, day))
    else:
        print("#{} {}".format(test_case, -1))