from plyer import notification

num = 1
for i in range(100):
    notification.notify(
    title="Your computer has destory by Python",
    message="Your Notification will crash. Click here to see more details",
    app_name="NotificationBreak",
    timeout=0
    )
    
    old = num
    num *= 2
    print(str(old) + " * 2 = " + str(num)) 
