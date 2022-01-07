import sys, re
from datetime import datetime, timedelta
import jinja2

#render template HTML with data
def renderTemplate(data, weekNumber, week):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "Template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(data=data, weekNumber=weekNumber, week=week)
    fp = open("R&DReport.html", "w")
    fp.write(outputText)
    fp.close()


#extract data from file
def readData(dateList):
    data = dict()
    users = list()
    regexDate = ".\s\\[(.*?)\\:[0-9][0-9]\\:"
    regexUser = "[0-9]\s\\-\s(.*?)\s\\[[0-9]"
    endDate = datetime.strptime(dateList[-1],"%d/%b/%Y").date()
    Links = [
        "https://rddashboard.ptcnet.ptc.com/rd_dashboard/rest/team/rollup_counts",
        "https://rddashboard.pt.cnet.ptc.com/rd_dashboard/rest/team/immediate_reportees_rollups",
        "https://rddashboard.ptcnet.ptc.com/rd_dashboard/rest/user/user_customer_spr_missing_subs/overdue",
        "https://rddashboard.ptcnet.ptc.com/rd_dashboard/rest/user/user_customer_spr_missing_subs/ontrack",
        "https://rddashboard.pt.cnet.ptc.com/rd_dashboard/rest/user/user_customer_spr_missing_subs/urgent",
        "rd_dashboard/user_assignments?quserid"
    ]
    fp = open("access.log","r")
    for line in fp:
        lineDate = str(re.findall(regexDate, line))[2:-2]
        if datetime.strptime(lineDate,"%d/%b/%Y").date() > endDate:
            break
        if lineDate in dateList:
            for i in Links:
                if i in line:
                    user = str(re.findall(regexUser, line))[2:-2]
                    user = "Unknown" if user=="-" else user
                    if user not in users:
                        users.append(user)
                        data[user] = 0
                    data[user] += 1
    fp.close()
    return data


#date function
def valDate(inpDate):
    inpDate = datetime.strptime(inpDate,"%d/%b/%Y").date()
    dates = []
    if inpDate.weekday()==6:
        for i in range(0, 7):
            day = inpDate + timedelta(days=i)
            dates.append(day.strftime('%d/%b/%Y'))
    else:
        for i in range(inpDate.weekday()+1, -1, -1):
            day = inpDate - timedelta(days=i)
            dates.append(day.strftime('%d/%b/%Y'))
        for i in range(1, 6-inpDate.weekday()):
            day = inpDate + timedelta(days=i)
            dates.append(day.strftime('%d/%b/%Y'))
    return dates


#main function
def main():
    try:
        inpDate = sys.argv[1]
    except:
        print("Please provide the date. Here's an example:\n  >python script.py 25/Dec/2021")
        exit()
    dateList = valDate(inpDate)
    data = readData(dateList)
    #week starting from Sunday
    #print("WeekNumber: ", (datetime.strptime(inpDate,"%d/%b/%Y").date()).strftime("%U"))
    #week starting from Monday
    #print("WeekNumber: ", (datetime.strptime(inpDate,"%d/%b/%Y").date()).isocalendar()[1])
    #print(dateList[0][3:6]+"("+dateList[0][0:2]+"-"+dateList[-1][0:2]+")")
    weekNumber = (datetime.strptime(inpDate,"%d/%b/%Y").date()).strftime("%U")
    week = dateList[0][3:6]+"("+dateList[0][0:2]+"-"+dateList[-1][0:2]+")"
    if not data:
        print("Not found!")
    else:
        print(data)
        renderTemplate(data, weekNumber, week)


if __name__ == "__main__":
    main()