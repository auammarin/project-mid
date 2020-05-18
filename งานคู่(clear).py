from os import system, name
def clear():#ล้าง
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def Menu():#การเข้าเมนู
    global choice
    print("Menu\n1.เพิ่มวิชา\n2.เช็คชื่อ\n3.ออกจากโปรเเกรม")
    print("Please select a menu by entering numbers 1 or 2 or 3")
    choice = input("Please Select Menu ::")
    clear()
    print('\n=====================================\n')
    clear()
def time_learning():#เช็คเวลา
        import time
        read_sub = open('subject.txt','r+')#อ่านข้อมูลลงใน txt ที่สร้างขึ้น
        while True:
                for line_sub in read_sub:#วนลูปใน subject.txt จนครบจำนวน split
                        id_sub,name_sub,in_time,end_time,late_time,day_sub,space = line_sub.split(',')
                        name_sub = name_sub.lower()
                        name_time = name_sub+'_time.txt'#เรียกใช้เวลาจากที่ txt ลงทะเบียบของเวลา
                        name_data = name_sub+'_data.txt'#เรียกใช้เวลาที่เข้าเรียนใน txt
                        hr = time.strftime('%H')#เรียกใช้ชั่วโมง
                        minute = time.strftime('%M')#เรียกใช้นาที
                        local_day = time.strftime('%A')#เรียกใช้วัน
                        local_day = local_day.lower()
                        hr_in,min_in = in_time.split(':')#เวลาเข้าเรียน split ด้วย :
                        hr_end,min_end = end_time.split(':')#เวลาเลิกเรียน split ด้วย :
                        if (int(hr) == int(hr_in)) and (int(minute) <= int(late_time)) and ((local_day)==(day_sub)):
                                late = ''#คำนวณว่ามาไม่สาย
                                runpro(name_time,name_data,late,name_sub)#เก็บข้อมูลไปที่ runpro
                        elif ((int(hr) == int(hr_end) and int(minute) <= int(min_end)) or (int(hr_in) <= int(hr) <= int(hr_end))) and ((local_day)==(day_sub)):
                                late = ',late'#คำนวณว่ามาสาย
                                runpro(name_time,name_data,late,name_sub)#เก็บข้อมูลไปที่ runpro
                else:
                        print('\n=====================================\n')
                        print('--------| !!ไม่มีวิชาที่เรียนเวลานี้!! |--------')
                        print('Please Enter to continue')
                        input('>>>')
                        print('\n=====================================\n')
                        clear()
                return Menu()
def runpro(savetime,savedata,late,subj_name):#ใส่รหัส นศ.
        import time#เรียกใช้ข้อมูลเวลา
        add_time = open(savetime,'a+')#เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายและอ่านข้อมูลจากไฟล์ ถ้าหากไม่มีไฟล์อยู่จะสร้างไฟล์ใหม่
        add_data = open(savedata,'a+')#เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายและอ่านข้อมูลจากไฟล์ ถ้าหากไม่มีไฟล์อยู่จะสร้างไฟล์ใหม่
        time = time.strftime('%d'+'/'+'%b'+'/'+'%Y')
        add_time.close()#ปิดการทำงานของ File 
        add_data.close()#ปิดการทำงานของ File 
        while True:
            while True:
                try:
                    print('--------|'+subj_name+'|--------')#ขึ้นวิชาที่ต้องเรียนในตอนนั้น
                    in_stu = input('CheckID on day press C\nCheck late time prees I\nBack to Start menu press 0\nEnterStudentID\n: ')
                    clear()
                    in_stu = in_stu.lower()
                    if in_stu == 'c':#เลือก c เพื่อไปดูจำนวนผู้เข้าเรียนในวิชานั้น
                        print('\n=====================================\n')
                        clear()
                        check_id_on_day(savetime,time,subj_name)
                    elif in_stu == 'i':#เลือก v เพื่อไปดูว่าวิชานี้ตนเองนั้นสายเเละเข้าเรียนไปทั้งหมดกี่ครั้ง
                        print('\n=====================================\n')
                        clear()
                        check_late(savetime,savedata,subj_name)
                    elif in_stu == '0':#เลือก 0 เพื่อกลับไปยังหน้าเมนูหลัก
                        print('\n=====================================\n')
                        clear()
                        Menu()
                    check_num = in_stu.split('-')#รหัสนักศึกษาใช้ - ในการ split
                    check_num = check_num[0]+check_num[1]#เลขเเรกที่ก่อน "-" + เลขหลัง เช่น 613050450-6
                    clear()
                    break
                except:
                    print('\n=====================================\n')
                    clear()
                    continue#เมื่อไม่ถูกต้องจะไปที่ def savenew_data() เพื่อลงทะเบียนเข้าเรียน
            if in_stu == '':
                print('\n=====================================\n')
                clear()
                continue#พิมพ์อะไรเลยเเล้วกด Enter จะกลับไปยัง while True ตัวเเรกใน def runpro() เเละเริ่มลูบใหม่
            elif check_num.isnumeric():#เมื่อใส่รหัสนักศึกษาถูกต้อง
                in_stu = in_stu.lower()
                add_data = open(savedata,'r+')#เปิดไฟล์เพื่ออ่านและบันทึกข้อมูล
                for line_data in add_data :#ลูปเรียกข้อมูลของผู้เรียนในรายวิชา
                    if in_stu in line_data :
                        save_time(savetime,in_stu,late)#บันทึกเวลาเข้าเรียน,ข้อมูลนักศึกษา,จำนวนที่มาสาย
                        print('\n=====================================\n')
                        print('--------| !!บันทึกเวลาแล้ว!! |--------')
                        print('Please Enter to continue')
                        input('>>>')
                        print('\n=====================================\n')
                        clear()
                        add_data.close()#ปิดการทำงานของ File
                        time_learning()#กลับไปที่ def time_learning() เพื่อเช็คข้อมูล
                        break
                else:#เมื่อไม่ถูกต้องจะไปที่ def savenew_data() เพื่อลงทะเบียนเข้าเรียน 
                    print('\n=====================================\n')
                    print('--------| !!ไม่พบข้อมูล!! |--------')
                    print('Please Enter to continue')
                    input('>>>')
                    print('\n=====================================\n')
                    clear()
                    while True:
                        print('--------| ต้องการจะเพิ่มรหัสใหม่หรือไม่? |--------')#ให้ใส่รหัสใหม่อีกครั้ง
                        add_id = input('[Y/N]:')# y คือ ใช่ n คือ ไม่
                        add_id = add_id.lower()
                        if add_id == 'y':#ไปลงทะเบียนเรียนที่ def savenew_data()
                            clear()
                            savenew_data(savedata,in_stu,late,savetime)
                            break
                        elif add_id == 'n':#จะกลับไปที่เช็คเวลาเข้าเรียน def time_learning()
                            clear()
                            time_learning()
                        else :
                            print('--------| !!กรุณาใส่คำสั่งให้ถูกต้อง!! |--------')
                            continue#เมื่อใส่คำตอบไม่ถูกต้องจะกลับไปที่ "ต้องการจะเพิ่มรหัสใหม่หรือไม่"
            else:
                continue
            break#ออกจากลูป if in_stu
def save_time(savetime,in_stu,late):#เช็คชื่อเข้าเรียน
        import time
        time = time.strftime('%d'+'/'+'%b'+'/'+'%Y'+','+'%H'+':'+'%M'+':'+'%S')#บันทึกรหัสนักศึกษาเเละเวลาที่เข้าเรียน
        save_time = open(savetime,'a+')#เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายและอ่านข้อมูลจากไฟล์ ถ้าหากไม่มีไฟล์อยู่จะสร้างไฟล์ใหม่
        save_time.write(in_stu+','+time+late+'\n')#บันทึกรหัสนักศึกษา,เวลาเเละวันที่เข้าเรียน,late หรือไม่
        save_time.close()#ปิดการทำงานของ File

def savenew_data(savedata,in_stu,late,savetime):#ลงทะเบียนผู้ใช้ใหม่
    print('--------| Register |--------')
    add_data = open(savedata,'a+')#เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายและอ่านข้อมูลจากไฟล์ ถ้าหากไม่มีไฟล์อยู่จะสร้างไฟล์ใหม่
    name = input('กรุณาใส่ชื่อ:')#ใส่ชื่อเก็บไว้ใน name
    surname = input('กรุณาใส่นามสกุล:')#ใส่นามสกุลเก็บไว้ใน surname
    fac = input('กรุณาใส่คณะที่กำลังศึกษา:')#ใส่คณะที่ศึกษาเก็บไว้ใน fac
    major = input('กรุณาใส่สาขาที่กำลังศึกษาอยู่:')#ใส่สาขาที่กำลังศึกษาไว้ใน major
    clear()
    while True:#เข้าลูปการถามเพื่อความเเน่ใจในการใส่ข้อมูล
        print('\n=====================================\n')
        print('--------| กรุณาตวจสอบข้อมูล |--------')
        print('รหัสนักศึกษา:'+in_stu+'\nชื่อ:'+name+'\nนามสกุล:'+surname+'\nคณะ:'+fac+'\nสาขา:'+major)#เเสดงข้อมูลที่กรอกไปใน def savenew_data()
        print('--------| ต้องการจะเเก้ไขหรือไม่? |--------')
        choose_fix = input('ต้องการจะเเก้ไข้หรือไม่?[Y/N]:')# y คือ ใช่ n คือ ไม่
        clear()
        choose_fix = choose_fix.lower()
        if choose_fix == 'y':
            while True:#ถ้าเลือก y จะเข้าสู่ลูบการเเก้ไข
                print('\n=====================================\n')
                print('--------| ข้อมูลปัจจุบัน |--------')
                print('รหัสนักศึกษา:'+in_stu+'\nชื่อ:'+name+'\nนามสกุล:'+surname+'\nคณะ:'+fac+'\nสาขา:'+major)
                print('--------| เลือกส่วนที่ต้องการเเก้ไข |--------')
                print('1.ชื่อ\n2.นามสกุล\n3.คณะที่กำลังศึกษา\n4.สาขาที่กำลังศึกษาอยู่')
                fix = input('เลือกส่วนที่ต้องการเเก้ไข[กด 0.เพื่อย้อนกลับ]:')
                print('---------------------------------')
                if fix == '1':#เลือกเลข 1 เพื่อเเก้ไขชื่อ
                    name = input('กรุณาใส่ชื่อ:')
                elif fix == '2':#เลือกเลข 2 เพื่อเเก้ไขนามสกุล
                    surname = input('กรุณาใส่นามสกุล:')
                elif fix == '3':#เลือกเลข 3 เพื่อเเก้ไขคณะ
                    fac = input('กรุณาใส่คณะที่กำลังศึกษา:')
                elif fix == '4':#เลือกเลข 4 เพื่อเเก้ไขชื่อสาขา
                    major = input('กรุณาใส่สาขาที่กำลังศึกษาอยู่:')
                elif fix == '0':#เลือกเลข 0 เพื่อย้อนกลับเเละจบลูป
                    break
                else :#เมื่อใส่คำสั่งไม่ถูกต้อง
                    print('\n=====================================\n')
                    print('--------| !!กรุณาใส่คำสั่งให้ถูกต้อง!! |--------')
                    print('Please Enter to continue')
                    input('>>>')
                    print('\n=====================================\n')
                    clear()
                    continue#กลับไปหน้าเเก้ไขข้อมูลใหม่
        elif choose_fix == 'n':#ถ้าเลือก n จะบันทึกไปที่ _data.txt
            add_data.write(in_stu+','+name+','+surname+','+fac+','+major+'\n')#บันทึกรหัสนักศึกษา,ชื่อ,นามสกุล,คณะ,สาขา
            save_time(savetime,in_stu,late)#เเละบันทึกเวลาเรียนหลังจากลงทะเบียนเเบบอัตโนมัติ
            print('\n=====================================\n')
            print('--------| !!บันทึกข้อมูลเสร็จสิ้น!! |--------')
            print('Please Enter to continue')
            input('>>>')
            print('\n=====================================\n')
            clear()
            add_data.close()#ปิดการทำงานของ File
            break
    print('\n=====================================\n')
    print('--------| !!บันทึกเวลาเข้าเรียนเสร็จสิ้น!! |--------')
    print('Please Enter to continue')
    input('>>>')
    print('\n=====================================\n')
    clear()
    time_learning()#กลับไปยังหน้าเช็คเลวาเข้าเรียน
def check_id_on_day(savetime,time,sub_n):#เช็คคนมาเรียนในวิชานั้น
    in_num = 0#กำหนดคนเข้าเรียนให้มีค่าเป็น 0 ก่อน
    print('--------|'+sub_n+'|--------')#ชื่อวิชา
    print('       '+time+'         ')#วันที่เรียน
    read_time = open(savetime,'r')#ข้อมูลที่บันทึกไว้ตอนเช็คชื่อใน _time.txt
    for line_time in read_time:#เข้าลูปนับจำนวนคนมาเรียนตามข้อมูลใน _time.txt
        if time in line_time:#นับจำนวนเเละ +1 จนกว่าข้อมูลจะหมด
            print (line_time)
            in_num += 1
    print('มาเรียนจำนวน: ',in_num,'คน')
    print('Please Enter to continue')
    input('>>>')
    print('\n=====================================\n')
    clear()
    read_time.close()#ปิดการทำงานของ File
def check_late(savetime,savedata,subname):#เช็คมาสาย
    in_num = late_num = 0#กำหนดจำนวนนักศึกษาที่เข้าเรียนเเละจำนวนนักศึกษาที่มาสายเท่ากับ 0
    read_time = open(savetime,'r+')#เปิดอ่านข้อมูลเวลาใน _time.txt
    read_data = open(savedata,'r+')#เปิดอ่านข้อมูลผู้เรียนใน _data.txt
    print('--------| เช็คข้อมูลการมาเรียน |--------')
    id_stu = input('ใส่รหัสนักศึกษา:')#ใส่รหัสนักศึกษาเพื่อดู
    print('\n=====================================\n')
    clear()
    for line_time in read_time:#ลูปนับจำนวนข้อมูลใน _time.txt
        in_num += 1#ถ้าไม่คำว่า late ให้นับเป็น in
        if id_stu and 'late' in line_time:
            late_num += 1#ถ้ามีคำว่า late ให้นับเป็น late
    for line_data in read_data:#ลูปนับจำวนวข้อมูลใน _data.txt
        if id_stu in line_data:#ลูปนับข้อมูลใน _data.txt โดยใช้ id ผู้เรียน
            id_stu,name,surname,fac,major = line_data.split(',')#ข้อมูทั้ง 4 อย่าง split ด้วย ','
            print('--------|'+subname+'|--------')
            print('รหัสนักศึกษา:'+id_stu+'\n\t    ชื่อ:'+name+'\n\t นามสกุล:'+surname+'\n\t   คณะ:'+fac+'\n\t   สาขา:'+major+'\n\t   เข้าเรียนทั้งหมด: '+str(in_num)+'ครั้ง\n\t   มาเรียนสายจำนวน: '+str(late_num)+'ครั้ง')            
            print('Please Enter to continue')
            input('>>>')
            print('\n=====================================\n')
            clear()
    read_time.close()#ปิดการทำงานของ File
    read_data.close()#ปิดการทำงานของ File
def check_subj():#เช็ควิชา
    import time
    add_sub = open('subject.txt','a+')#เปิดไฟล์เพื่อเขียนข้อมูลต่อท้ายและอ่านข้อมูลจากไฟล์ ถ้าหากไม่มีไฟล์อยู่จะสร้างไฟล์ใหม่
    read_sub = open('subject.txt','r+')#เปิดอ่านข้อมูล
    while True:
        for line_sub in read_sub:#ลูปอ่านข้อมูลใน subject.txt
            id_sub,name_sub,in_time,end_time,late_min,day,space = line_sub.split(',')
            print('Subject:'+name_sub,'เรียนวัน:'+day,'\nช่วงเวลาที่เรียน:'+in_time,'-',end_time)
        print('---------------------------------')
        add = input('ต้องการจะเพิ่มรหัสวิชาใหม่หรือไม่[Y/N]:')#มีการถามว่าจะเพิ่มวิชาอีกไหมใน subject.txt
        print('---------------------------------')
        clear()
        add = add.upper()#เป็นตัวใหญ่เสมอ
        if add == 'Y':#ตอบ Y คือ ใช่
            print('\n=====================================\n')
            print('--------| ลงทะเบียนวิชาเรียน |--------')
            newsubject_data()#เมื่้อตอบใช่จะไปที่ daf newsubject_data() เพื่อเพิ่มรายวิชา
            read_sub.close()#เเละปิดการอ่าน subject.txt
            break
        elif add == 'N':#ตอบ N คือ ไม่
            print('\n=====================================\n')
            return time_learning()#เมื่อตอบไม่ ก็จะกลับไปให้เช็คชื่อเข้าเรียน
            add_sub.close()#ปิดการใช้งาน subject.txt
            break
        else :
            print('กรุณาใส่คำสั่งให้ถูกต้อง!!')
            continue#ถ้าใส่ไม่ถูกต้องกลับไปทำลูปเดิม
def newsubject_data():#เพิ่มวิชา
    import time
    add_sub = open('subject.txt','a+')#เขียนข้อมูต่อท้ายใน subject.txt
    id_sub = input('กรุณาใส่รหัสวิชา:')#ใส่รหัสวิชาเเละเก็บไว้ใน id_sub
    name_sub = input('กรุณาใส่ชื่อวิชา:')#ใส่ชื่อวิชาเเละเก็บไว้ใน name_sub
    in_hr = input('กรุณาใส่เวลาเข้าเรียน[Hr]:')#ใส่เวลาเข้าเรียนเป็นชั่วโมงเเละเก็บไว่ใน in_hr
    in_min = input('\t         [M]:')#ใส่เวลาเข้าเรียนเป็นนาทีเเละเก็บไว่ใน in_min
    end_hr = input('กรุณาใส่เวลาหมดคาบ[Hr]:')#ใส่เวลาเข้าเรียนเป็นชั่วโมงเเละเก็บไว่ใน end_hr
    end_min = input('\t         [M]:')#ใส่เวลาเข้าเรียนเป็นนาทีเเละเก็บไว่ใน end_min
    late_time = input('กรุณาใส่เวลาสาย:')#ใส่เวลาเข้าเรียนเกินเวลาเป็นนาทีเเละเก็บไว่ใน late_time
    clear()
    while True:#เข้าสู่ลูปเลือกวันที่เรียน
        day = input('วันที่เรียน 1.วันจันทร์\n\t2.วันอังคาร\n\t3.วันพุธ\n\t4.วันพฤหัสบดี\n\t5.วันศุกร์\n\t6.วันเสาร์\n\t7.วันอาทิตย์\n:')
        clear()
        print('Please choose number')#เลือกเเละเก็บไว้ใน day (จ-ศ)
        if day == '1':
                day = 'monday'
                clear()
        elif day == '2':
                day = 'Tuesday'
                clear()
        elif day == '3':
                day = 'Wednesday'
                clear()
        elif day == '4':
                day = 'Thursday'
                clear()
        elif day == '5':
                day = 'Friday'
                clear()
        elif day == '6':
                day = 'Saturday'
                clear()
        elif day == '7':
                day = 'Sunday'
                clear()
        else:
                clear()
                continue#เมื่อใส่ไม่ถูกต้องจะกลับไปทำลูปเดิม
        clear()
        break
    while True:#เมื่อเพิ่มวิชาเสร็จจะโชว์ข้อมูลวิชาเเละถามว่าจะเเก้ไขไหม
        print('\n=====================================\n')
        print('--------| ตรวจสอบข้อมูล |--------')
        print('รหัสวิชา:'+id_sub+'\nชื่อวิชา:'+name_sub+'\nเวลาเข้าเรียน:'+in_hr+':'+in_min+'\nเวลาสาย:'+late_time+'\nเวลาหมดคาบ:'+end_hr+':'+end_min+'\nวัน:'+day)
        fix = input('ต้องการจะเเก้ไขหรือไม่?[Y/N]:')
        clear()
        fix = fix.lower()
        if fix == 'y':#ถ้าตอบ y คือ ใช่
            while True:#เข้าสู่ลูปการเเก้ไข
                print('\n=====================================\n')
                print('--------| เลือกส่วนที่ต้องการเเก้ไข |--------')
                print('1.ชื่อวิชา\n2.เวลาเข้าเรียน\n3.เวลาหมดคาบ\n4.เวลาสาย\n5.วันที่เรียน')
                choose = input('[กด 0.เพื่อย้อนกลับ]:')
                if choose == '1':#เลือก 1 จะไปเเก้ไข ชื่อวิชา
                    name = input('กรุณาใส่ชื่อวิชา:')
                    print('\n=====================================\n')
                    print('--------| กรุณาตวจสอบข้อมูล |--------')
                    print('รหัสวิชา:'+id_sub+'\nชื่อวิชา:'+name_sub+'\nเวลาเข้าเรียน:'+in_hr+':'+in_min+'\nเวลาสาย:'+late_time+'\nเวลาหมดคาบ:'+end_hr+':'+end_min+'\nวัน:'+day)
                elif choose == '2':#เลือก 2 จะไปเเก้ไข เวลาเข้าเรียน
                    in_hr = input('กรุณาใสเวลาเข้าเรียน[Hr]:')
                    in_min = input('\t        [M]:')
                    print('\n=====================================\n')
                    print('--------| กรุณาตวจสอบข้อมูล |--------')
                    print('รหัสวิชา:'+id_sub+'\nชื่อวิชา:'+name_sub+'\nเวลาเข้าเรียน:'+in_hr+':'+in_min+'\nเวลาสาย:'+late_time+'\nเวลาหมดคาบ:'+end_hr+':'+end_min+'\nวัน:'+day)
                elif choose == '3':#เลือก 3 จะไปเเก้ไข เวลาเลิอกเรียน 
                    end_hr = input('กรุณาใส่เวลาหมดคาบ[Hr]:')
                    end_min = input('\t        [M]:')
                    print('\n=====================================\n')
                    print('--------| กรุณาตวจสอบข้อมูล |--------')
                    print('รหัสวิชา:'+id_sub+'\nชื่อวิชา:'+name_sub+'\nเวลาเข้าเรียน:'+in_hr+':'+in_min+'\nเวลาสาย:'+late_time+'\nเวลาหมดคาบ:'+end_hr+':'+end_min+'\nวัน:'+day)
                elif choose == '4':#เลือก 4 จะไปเเก้ไข เวลาสาย(นาที)
                    late_time = input('กรุณาใส่เวลาสาย:')
                    print('\n=====================================\n')
                    print('--------| กรุณาตวจสอบข้อมูล |--------')
                    print('รหัสวิชา:'+id_sub+'\nชื่อวิชา:'+name_sub+'\nเวลาเข้าเรียน:'+in_hr+':'+in_min+'\nเวลาสาย:'+late_time+'\nเวลาหมดคาบ:'+end_hr+':'+end_min+'\nวัน:'+day)
                elif choose == '5':#เลือก 5 จะไปเเก้ไข วันที่เรียน(จ-ศ)
                    while True:
                        day = input('วันที่เรียน 1.วันจันทร์\n\t2.วันอังคาร\n\t3.วันพุธ\n\t4.วันพฤหัสบดี\n\t5.วันศุกร์\n\t6.วันเสาร์\n\t7.วันอาทิตย์\n:')
                        clear()
                        if day == '1':#เลือกเเละเก็บไว้ใน day (จ-ศ)
                                day = 'monday'
                                clear()
                        elif day == '2':
                                day = 'Tuesday'
                                clear()
                        elif day == '3':
                                day = 'Wednesday'
                                clear()
                        elif day == '4':
                                day = 'Thursday'
                                clear()
                        elif day == '5':
                                day = 'Friday'
                                clear()
                        elif day == '6':
                                day = 'Saturday'
                                clear()
                        elif day == '7':
                                day = 'Sunday'
                                clear()
                        else:
                                clear()
                                continue#เมื่อใส่ไม่ถูกต้องจะกลับไปทำลูปเดิม
                    clear()
                    break
                    print('\n=====================================\n')
                    print('--------| กรุณาตวจสอบข้อมูล |--------')
                    print('รหัสวิชา:'+id_sub+'\nชื่อวิชา:'+name_sub+'\nเวลาเข้าเรียน:'+in_hr+':'+in_min+'\nเวลาสาย:'+late_time+'\nเวลาหมดคาบ:'+end_hr+':'+end_min+'\nวัน:'+day)
                    clear()
                elif choose == '0':#เลือก 0 ออกจากลูปการเเก้ไขวิชา
                    break
                else :
                    print('\n=====================================\n')
                    print('กรุณาใส่คำสั่งให้ถูกต้อง!!')
                    print('Please Enter to continue')
                    input('>>>')
                    print('\n=====================================\n')
                    clear()
                    continue#เมื่อใส่ไม่ถูกต้องจะกลับไปทำลูปเดิม (0-5)
        elif fix == 'n' :#ถ้าตอบ n คือ ไม่
            day = day.lower()#วันภาษาอังกฤษจะเป็นตัวเล็กหมด
            min_late = int(in_min)+int(late_time)#เวลาที่เกินมาคือ นาทีที่เข้าเรียน+เวลาที่กำหมดมาสาย (ถ้าเกินที่คำนวณเป็นนาทีมาจะขึ้นเช็คชือว่า late) เเละเก็บไว้ใน min_late
            add_sub.write(id_sub+','+name_sub+','+in_hr+':'+in_min+','+end_hr+':'+end_min+','+str(min_late)+','+day+','+'\n')#เขียนข้อมูลลงใน subject.txt
            print('บันทึกข้อมูลเสร็จสิ้น')
            print('\n=====================================\n')
            clear()
            add_sub.close()#ปิดการเขียนข้อมูลใน subject.txt
            return check_subj()
            break
while True:
    Menu()
    if choice =='1':
        newsubject_data()
    elif choice =='2':
        time_learning()
    elif choice =='3':
        break
    else :
        print("")
print("Thank you for using the program")