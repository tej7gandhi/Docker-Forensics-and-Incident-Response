# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DockerForensics.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

#Modules for Zipping the evidences together
import hashlib
import checksumdir
from checksumdir import dirhash
from zipfile import ZipFile
#Modules for utilizing operating system coommands
import subprocess

#import modules for running subprocesses
import sys
import os
import re

#import module for zipping files 
import zipfile
import shutil


#import modules for debugging the code
import pdb
#import modules for dropbox module for uploading code to dropbox
import dropbox
from subprocess import Popen, PIPE, STDOUT

from PyQt5 import QtCore, QtGui, QtWidgets
from RunningImages4 import Ui_Dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(400, 420, 89, 25))
        self.Run.setObjectName("Run")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 1051, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 80, 80))
        self.label_2.setObjectName("label_2")
        self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setGeometry(QtCore.QRect(400, 180, 251, 23))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 360, 271, 23))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 210, 361, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 300, 301, 23))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 420, 351, 23))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 450, 331, 23))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setGeometry(QtCore.QRect(400, 150, 251, 23))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 180, 361, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 240, 351, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(10, 330, 321, 23))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 150, 211, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 270, 301, 23))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(400, 240, 201, 23))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 521, 20))
        self.label.setObjectName("label")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 390, 351, 23))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(400, 210, 331, 23))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(400, 270, 301, 23))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setGeometry(QtCore.QRect(400, 300, 301, 23))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_20.setGeometry(QtCore.QRect(400, 330, 301, 23))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_21.setGeometry(QtCore.QRect(400, 360, 301, 23))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_22.setGeometry(QtCore.QRect(400, 390, 301, 23))
        self.checkBox_22.setObjectName("checkBox_22")
        self.plainTextEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit2.setGeometry(QtCore.QRect(650, 130, 401, 21))
        self.plainTextEdit2.setObjectName("plainTextEdit2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 160, 111, 25))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit =QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(650, 100, 401, 21))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 22))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.showimages)
        self.Run.clicked.connect(self.CollectArtifacts) #Function call on clicking the run button
        cmd1= "docker ps"


        stdouterr =os.popen(cmd1).read()
        self.textEdit.setText(stdouterr)
        #Location where to collect the artifacts
     
         
        #global i
        #global imageno
     #   imageno =[]
       # usercount =images.split()
       # for k in range(0,len(usercount)):
       ###   print imageno

       # for i in range(0,len(count)):
       ##     for j in range(0,len(usercount)):
         #     if(i==int(imageno[j])):
          #       allimages=output1.split()[i]
				#file1= open(location +"/dockerlogs " +allimages+".txt","w")
				#file3= open(location +"/dockercommanddetails " +allimages+".txt","w")
      		                #file5= open(location +"/dockerinspectiondetails "+si+".txt","w")
               			#file6= open(location +"/seetheprocesslist "+allimages+".txt","w")
                		#file9= open(location +"/dockerevents "+allimages+".txt","w")
        
        #print allimages
    def CollectArtifacts(self):# Here is the function
        global images
        images =self.plainTextEdit.toPlainText()
        
        global location
        location=self.plainTextEdit2.toPlainText()
        global i
        global imageno
        imageno =[]
        cmd="docker ps -q"
        global output1
        output1 = os.popen(cmd).read()
        count=output1.split()
        
        usercount =images.split()
        for k in range(0,len(usercount)):
            imageno.append(images.split()[k])
        
        for i in range(0,len(count)):
            for j in range(0,len(usercount)):
                if(i==int(imageno[j])):
                    allimages=output1.split()[i]
                #Docker inspection details    
                    if(self.checkBox.isChecked()):
                      file1= open(location +"/dockerfilechanges "+allimages+".txt","w")
                      subprocess.call(["docker","container","diff",allimages],stdout=file1)
                    
                    if(self.checkBox_2.isChecked()):
                      file2= open(location +"/dockerinspectiondetails "+allimages+".txt","w")
                      subprocess.call(["docker","container","inspect",allimages],stdout=file2)

                    if(self.checkBox_3.isChecked()):
                      file3= open(location +"/dockerrunningprocess" +allimages+".txt","w")
       	              subprocess.call(["docker","top",allimages],stdout=file3)

                    if(self.checkBox_4.isChecked()):
                      output =location +"/" +allimages+".tar"
                      subprocess.call(["docker","export",allimages,"-o",output])
	                  #subprocess.call(['docker','export',allimages,'-o',output])

                    if(self.checkBox_5.isChecked()):
                      file5= open(location +"/dockerprocessesdesc "+allimages+".txt","w")
                      subprocess.call(["pstree"],stdout=file5)

                    if(self.checkBox_6.isChecked()):
                      file1= open(location +"/dockerfilechanges "+allimages+".txt","w")
                      subprocess.call(["docker","container","diff",allimages],stdout=file1)

                    if(self.checkBox_7.isChecked()):
                      file8= open(location +"/dockerinformation "+allimages+".txt","w")
                      subprocess.call(["docker","info"],stdout=file8)

                #    if(self.checkBox_8.isChecked()):
                 #     file9=open(location+"/dockerstats " +allimages +".txt","w")
                  #    subprocess.call(["docker","stats"],stdout=file9)

                    if(self.checkBox_9.isChecked()):
                      print ("Copying logs and configuration of container")
                      log=allimages+":/var/log"
                      os.chdir(location)
                      os.mkdir(allimages)
                      pathlog=location +"/"+allimages
                      locationlogs=pathlog+"/log"
                      subprocess.call(['docker','cp',log,locationlogs])
                      etc=allimages+":/etc"
                      locationetc=pathlog+"/etc"
                      subprocess.call(['docker','cp',etc,locationetc])
                    
                    if(self.checkBox_10.isChecked()):
                      print ("Copying logs of the host")
                      subprocess.call(["cp","-r","/var/log",location])
                    
                    if(self.checkBox_11.isChecked()):
                      print ("Copying configurations of the host")
                      subprocess.call(["cp","-r","/etc",location])  
                    
                    if(self.checkBox_15.isChecked()):
                      print("Copying Command history")
                      file10= open(location +"/history "+allimages+".txt","w")
                      e = Popen("bash -i -c  'history -r;history' ", shell=True, stdin=PIPE, stdout=file10, stderr=STDOUT)
                      
                    if(self.checkBox_17.isChecked()):
                      print("Docker images")
                      file11=open(location +"/imagedetails"+".txt","w")
                      subprocess.call(["docker","images"])
                      subprocess.call(["docker","images"],stdout=file11)
                    
                    if(self.checkBox.isChecked()):
                      print("Docker File changes")
                      file1= open(location +"/dockerfilechanges "+allimages+".txt","w")                 
                      subprocess.call(["docker","container","diff",allimages],stdout=file1)
                    
                    if(self.checkBox_19.isChecked()):
                      print("Copying memory to analyze with volatility")
                      subprocess.call(["chmod","+x","/home/tej/Downloads/linpmem-2.1.post4"])
                      subprocess.call(["./linpmem-2.1.post4","-o",location+"mem1.aff4r"])

                    if(self.checkBox_12.isChecked()):
                      print ("Extracting firewall logs")
                      file13= open(location +"/Firewalllogsnat.txt","w")
                      subprocess.call(["iptables","-t","nat","-nL"],stdout=file13)
                      file14= open(location +"/Firewalllogsmangle"+allimages+".txt","w")
                      subprocess.call(["iptables","-t","mangle","-nL"],stdout=file14)
                      file15= open(location +"/Firewalllogsfilter"+allimages+".txt","w")
                      subprocess.call(["iptables","-t","filter","-nL"],stdout=file15)
                      file16= open(location +"/Firewalllogsraw"+allimages+".txt","w")
                      subprocess.call(["iptables","-t","raw","-nL"],stdout=file16)
                    
                    if(self.checkBox_16.isChecked()):
                      file12= open(location +"/NetworkConnectionsHostAll "+allimages+".txt","w")
                      subprocess.call(["netstat","-ant"],stdout=file12)
                    
                    if(self.checkBox_20.isChecked()):
                      file13= open(location +"/ipconfigurations"+allimages+".txt","w")
                      subprocess.call(["ifconfig"],stdout=file13)

                    if(self.checkBox_21.isChecked()):
                      file14= open(location +"/Allservices"+allimages+".txt","w")
                      subprocess.call(["service","--status-all"],stdout=file14)

                    if(self.checkBox_22.isChecked()):
                      file15= open(location +"/Cronjobrunning"+allimages+".txt","w")
                      subprocess.call(["crontab","-l"],stdout=file15)
          
                    
                    
                    self.ZipAllEvidences() # Want to call this function

    
        

    def ZipAllEvidences(self): # Here is the function definition
        hash =checksumdir.dirhash(location)
        print(hash)
        file16=open(location +"hash.txt","w")
        file16.write(hash)
	    # path to folder which needs to be zipped
        print ("Zip all artifacts")
        directory = location
        print(directory)
        #Hash the directory before zipping
        
        # calling function to get all file paths in the directory
        file_paths = self.get_all_file_paths(directory)

        # printing the list of all files to be zipped
        print('Following files will be zipped:')
        for file_name in file_paths:
                print(file_name)

        # writing files to a zipfile
        with ZipFile('artifacts.zip','w',allowZip64=True) as zip:
        # writing each file one by one
             for file in file_paths:
                 zip.write(file)
        print ("All artifacts zipped successfully")
      # self.UploadToDropbox()
  
    def get_all_file_paths(self, directory):
   
        # initializing empty file paths list
        file_paths = []

        # crawling through directory and subdirectories
        for root, directories, files in os.walk(directory):
                for filename in files:
                        # join the two strings in order to form the full filepath
                        filepath = os.path.join(root, filename)
                        if not os.path.islink(filepath):
                           file_paths.append(filepath)


        # returning all file paths
        return file_paths


    def UploadToDropbox(self):
        dbx =dropbox.Dropbox('wAanjYfFMIAAAAAAAAAAFXHHv_gFBZQX89VC4ODwAm4S3MFWUx4Ht2dZAAtmX1')
        file_path='/home/tej/Downloads/artifacts.zip'
        dest_path='/artifacts.zip'
        f = open(file_path)
        file_size = os.path.getsize(file_path)

        CHUNK_SIZE = 10 * 1024 * 1024

        if file_size <= CHUNK_SIZE:

           print (dbx.files_upload(f, dest_path))

        else:

            upload_session_start_result = dbx.files_upload_session_start(f.read(CHUNK_SIZE))
            cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id,
                                               offset=f.tell())
            commit = dropbox.files.CommitInfo(path=dest_path)

            while f.tell() < file_size:
                if ((file_size - f.tell()) <= CHUNK_SIZE):
                     print (dbx.files_upload_session_finish(f.read(CHUNK_SIZE),cursor,commit))
                else:
                   dbx.files_upload_session_append(f.read(CHUNK_SIZE),cursor.session_id,cursor.offset)
                   cursor.offset = f.tell()
        f.close()



    def showimages(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Docker Forensics"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.label_2.setText(_translate("MainWindow", "Enter the location where artifact will be stored"))
        self.checkBox_18.setText(_translate("MainWindow", "Capture cron job details"))
        self.checkBox_8.setText(_translate("MainWindow", "Docker statistics"))
        self.checkBox_4.setText(_translate("MainWindow", "Docker snapshot"))
        self.checkBox_7.setText(_translate("MainWindow", "Information regarding dockers"))
        self.checkBox_10.setText(_translate("MainWindow", "Copy logs  of the host system"))
        self.checkBox_11.setText(_translate("MainWindow", "Copy configuration of the host system"))
        self.checkBox_17.setText(_translate("MainWindow", "Capture all docker images present"))
        self.checkBox_3.setText(_translate("MainWindow", "Docker top command details Process id and logs"))
        self.checkBox_5.setText(_translate("MainWindow", "Docker Process description tree"))
        self.checkBox_15.setText(_translate("MainWindow", "Copy command history"))
        self.checkBox_2.setText(_translate("MainWindow", "Docker Inspection Details"))
        self.checkBox_6.setText(_translate("MainWindow", "File differences"))
        self.checkBox.setText(_translate("MainWindow", "Docker File Changes"))
        self.label.setText(_translate("MainWindow", "Enter image number"))
        self.checkBox_9.setText(_translate("MainWindow", "Copy logs and configurations for the container"))
        self.checkBox_16.setText(_translate("MainWindow", "Network connections"))
        self.checkBox_12.setText(_translate("MainWindow", "Copy firewall logs"))
        self.pushButton.setText(_translate("MainWindow", "Show images"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.checkBox_19.setText(_translate("MainWindow","Capture Memory of the host"))
        self.checkBox_20.setText(_translate("MainWindow","Host network details"))
        self.checkBox_21.setText(_translate("MainWindow","List all services running"))
        self.checkBox_22.setText(_translate("MainWindow","List all the Scheduled task"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
