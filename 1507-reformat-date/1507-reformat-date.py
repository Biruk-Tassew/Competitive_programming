class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        day_idx = 0
        while date[0][day_idx].isdigit():
            day_idx += 1
            
        day = ""
        if day_idx == 1:
            day = "0"+ date[0][0]
        else:
            day = date[0][:day_idx]
       
        return date[-1]+"-"+months[date[1]]+"-"+day