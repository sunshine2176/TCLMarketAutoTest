#coding:utf-8

import os

class updateReport:
    
    #----------------------------------------------------------------------
    def readFiles(self,readPath):
        """获取文件列表"""
        iconList = ''
        for root,dirs,files in os.walk(readPath):
            for f in files:
                iconList = iconList + f + ','
        iconList = iconList[:-1]
        return iconList
    
    #----------------------------------------------------------------------
    def insertInfo(self,writePath,info,target):
        """插入信息"""
        with open(writePath,'r') as report:
            content = report.read()
            pos = content.find(target)
            if pos != -1:
                content = content[:pos + len(target)] + info + content[pos + len(target):]
                report = open(writePath,'w')
                report.write(content)
                report.close()
        
    
    #----------------------------------------------------------------------
    def writeInfo(self,writePath):
        """将图片文件位置信息写入文件"""
        iconDir = r'D:/tools/workspacePy/TCLMarketAutoTest/image'
        iconStr = self.readFiles(iconDir)
        
        iconFun = '''var dir = document.getElementById("dir").textContent.trim();
    var icons = document.getElementById("iconList").textContent.trim();
    var iconList = icons.split(",");
    var times = document.getElementsByClassName("details-col-times");
  	var count = times.length - 1;
  	for (j = 0; j < count; j++) {
  		 // code to be executed
  		 var time = times[j+1].textContent;
  		 var reg = /-| |:/g;
  		 time = time.replace(reg,'');
  		 var startTime = parseFloat(time.substring(0,time.length/2-4));
  		 var endTime = parseFloat(time.substring(time.length/2,time.length-4));
  		 var textContent = '';
  		 for(i=0; i<iconList.length; i++){
  		 	var iconTime = parseFloat(iconList[i].match(/[0-9]*/g).join(''));
  		 	
  		 	if (iconTime >= startTime && iconTime <= endTime) {
  		 		textContent = textContent + "<a href='file:///" + dir + "/" + iconList[i] + "' target='_blank'>" + iconList[i] + "<br>";
  		 	}
    	}
    	document.getElementById("test-details").getElementsByClassName("details-col-icons")[j+1].innerHTML=textContent;
  	}'''
        
        funTarget = "rows.appendTo(target);"
        
        self.insertInfo(writePath, iconFun, funTarget)
        
        
        
        iconList = '''<th class="details-col-icons" title="Icon">
        	<div class='details-col-header'>Icon</div>
        </th>

        <th hidden="yes" class="details-col-iconlist" id="iconList" >
        	<div class='details-col-header'>%s</div>
        </th>
        <th hidden="yes" class="details-col-dir" id="dir" >
        	<div class='details-col-header'>%s</div>
        </th>''' % (iconStr,iconDir)
        
        listTarget = '''<div class='details-col-header'>Start / End</div>
        </th>'''
        
        self.insertInfo(writePath, iconList, listTarget)
        
        displayIcon = '<td class="details-col-icons"><div><a href=""></div></td>'
        
        displayTarget = '<td class="details-col-times"><div>${times.startTime}<br>${times.endTime}</div></td>'
        
        self.insertInfo(writePath, displayIcon, displayTarget)
        
        with open(writePath,'r') as report:
            content = report.read()  
        content = content.replace('''<tr onclick="location = '${$item.logURL}#${id}'" title="{{html fullName}}">''','<tr title="{{html fullName}}">')
        report = open(writePath,'w')
        report.write(content)
        report.close()        


if __name__ == "__main__":
    r = updateReport()
    r.writeInfo(r'D:/tools/workspacePy/TCLMarketAutoTest/report/report.html')
    #r.readFiles(r"D:\tools\workspacePy\TCLMarketAutoTest\image")