t = int(input())

for test_case in range(1,t+1):
    sm, sd, em, ed = map(int, input().split())
    dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    ans = 0
    if em - sm == 0:
        ans = ed-sd+1
    else:
        ans = dict[sm] - sd + 1
        for i in range(sm+1, em):
            ans += dict[i]
        ans += ed
    print("#{} {}".format(test_case, ans))

            
	    

