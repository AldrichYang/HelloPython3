def write_ticket():
    print("write a ticket done!")


speed = 85
mood = 'bad'
if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
        print('You have the right to remain slient')
    elif mood == 'bad' or speed >= 90:
        print("I'm going to have to write you a ticket")
        write_ticket()
    else:
        print("Let's try to keep it under 80, OK? ")
