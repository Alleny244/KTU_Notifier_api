# KTU Notifier Api

A simple python script that notifies you when there is a new announcement from KTU. Data is obtained by web scraping 
The python script is hosted with Flask in Heroku


The api call returns the 
* Newest first seven notifications  in json format </br>
 * Each Notification consists of the following json data </br>
     * 'dte' : The time at which notification is released  </br>
     * 'link' : Url to download the new notifiction in pdf format  </br>
     * 'notification_head' : Subject of the new notification  </br>
     * 'updated' : Returns True if there is a new notification else returns False  </br>

### Request

`GET /`

    https://ktu-notifier-api.herokuapp.com/

### Response

    HTTP/1.1 200 OK
    Date: Sun, 02 May 2021 19:58:46 GMT
    Status: 200 OK
    Connection: keep-alive
    Content-Type: application/json
    Content-Length: 2940

    [    
    {
        "dte": "Time : Sun May 02 00:00:00 IST 2021",
        "link": "https://ktu.edu.in//eu/att/attachments.htm?download=file&id=68u14S%2FmAsmio89WzMrg%2Bd3l8r4k%2FNqalbCkVuNJClo%3D&announcementId=Bc9rrUcUfdXWeyeh1HWiYqQaU9wMasuo34irS%2B47Dv4%3D&fileName=certificaterequestwithholding.pdf&downloadType=QJ90vzjHQWlKFOWVY5myyzCMCIUNRmRxMKOPdaUfZJQ%3D",
        "notification_head": "APJAKTU-EXAM-III-issuance of Degree Certificates-Withhold the Express/fast Track/Normal mode in the portal Temporarily -regarding",
        "updated": false
    },
    {
        "dte": "Time : Thu Apr 29 00:00:00 IST 2021",
        "link": "https://ktu.edu.in//eu/att/attachments.htm?download=file&id=8Sh5Cs3XRjiYjbsLn4drkcR0UtA%2FGtEm%2BMKuaso2%2BpA%3D&announcementId=vwWwjaNzjeMY0XP8X7YPDlq8BRkRfyHhzkFyJ%2FXqpN8%3D&fileName=KTU-AC1-217-2021(3).pdf&downloadType=TKZ8l2VQhwb1uQeZubB9WMX%2BdOvAVCIlboyL3MlHRY4%3D",
        "notification_head": "B.Tech 2019-20 Semester 1-FE Practical Courses - Re-registraion - Reg:",
        "updated": false
    },
    {
        "dte": "Time : Thu Apr 29 00:00:00 IST 2021",
        "link": "https://ktu.edu.in//eu/att/attachments.htm?download=file&id=PO1q0P2brB97y6YYYGEGwAYuN4F97Uq0989uZ1A6GFY%3D&announcementId=fJskYOtC9kxa0ZDpmZ2QwrgF61ZWJYISMP19Gy4h4rw%3D&fileName=Corrigendum-1(EOI).pdf&downloadType=xohwkTu8jeIzmfnXYXUV3isSPQFbPBqNJCDzq489V2c%3D",
        "notification_head": "'Corrigendum I' for the EoI for KIIDC project'",
        "updated": false
    },
    {
        "dte": "Time : Thu Apr 29 00:00:00 IST 2021",
        "link": "https://ktu.edu.in/https://tinyurl.com/technologydaycelebrations",
        "notification_head": "KSCSTE- National Technology Day Celebration in association with KTU - WEBINAR SERIES",
        "updated": false
    },
    {
        "dte": "Time : Mon Apr 26 00:00:00 IST 2021",
        "link": "https://ktu.edu.in//eu/att/attachments.htm?download=file&id=osRQ3TPle8CR%2F%2FScDmG3kkUvVfFMvSlquGceQzXVK%2Bc%3D&announcementId=WNynN6LKbGhPJTnYvcKYr4umSlEnc9Ir93E6Gy0C%2FfU%3D&fileName=Notif-RVB.TechS6SS3SS1,S2SS20.pdf&downloadType=0gaKbdlycYlJXfNeCbeQGnWuRGQjWESjvPdh9XmBEPU%3D",
        "notification_head": "Revaluation result published - B.Tech S1,S2 (S), S3 (S) and S6 (S) Sept 2020 examinations",
        "updated": false
    },
    {
        "dte": "Time : Mon Apr 26 00:00:00 IST 2021",
        "link": "https://ktu.edu.in//eu/att/attachments.htm?download=file&id=S0U5bj%2BCGdUnZ5rHzyuDYETQX%2BwXW3qUlghEnQzDDiM%3D&announcementId=6hVMHeB3hHlAfiQnSle%2FJQrW%2BRiYjQ7IOYUlcY888oo%3D&fileName=EoI_Colleges_KSITM.pdf&downloadType=Ovf9C44G7EaTJjo7XO5lG%2B217uPOWD0IdRw4Z57qFDM%3D",
        "notification_head": "\"Colleges which have submitted EoI for KSITM Mapathon project being facilitated by KTU\"",
        "updated": false
    },
    {
        "dte": "Time : Mon Apr 26 00:00:00 IST 2021",
        "link": "https://ktu.edu.in//eu/att/attachments.htm?download=file&id=6dE6gdl7u9oYeQeeGGpoyBdrRalYVMOyc%2BrCwU%2F%2BF%2FU%3D&announcementId=Q6jFD%2F9bXY71RnYpmB9qzprtOqFA%2FjkVBSdHZD4knZQ%3D&fileName=CourseExtension-2015Admission-U.O.pdf&downloadType=SgjUpvi%2BU9TMp3gxGGAio6gMOohsaSlq2zKzC1yJ6zk%3D",
        "notification_head": "Course extension granted to 2015 UG admission students",
        "updated": false
    }]
