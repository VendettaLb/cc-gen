# coding=utf-8
import random
print('\n' *10000)

cc = """
╔════════════════════════╗
║    xxxxxxxxxxxxxxxx    ║
║                        ║
╠════════════════════════╣
║MM/YYYY                 ║
║                        ║
║                        ║      
║                    CVV ║
╚════════════════════════╝ """
print cc

#bin
v = raw_input("Bin:")

vdt1 = 0
vdt2 = 0

#nmbs
print('\n' *10000)
sqlsql = """CREATE TABLE IF NOT EXISTS `credit_cards` (
        `id` BIGINT(11) NOT NULL AUTO_INCREMENT,
        `card_number` VARCHAR(19) NOT NULL,
        `expiration_date` VARCHAR(7) NOT NULL,
        `cvv` VARCHAR(4) NOT NULL,
        PRIMARY KEY (`id`),
        KEY (`card_number`)
);
"""
nmbs0 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs1 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs2 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs3 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs4 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs5 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs6 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs7 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs8 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs9 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs10 = ["0","1","2","3","4","5","6","7","8","9"]
nmbs11 = ["0","1","2","3","4","5","6","7","8","9"]

#replace
vv = v.replace("x",random.choice(nmbs0), 1)#v
vvv = vv.replace("x",random.choice(nmbs1), 1)#e
vvvv = vvv.replace("x",random.choice(nmbs2), 1)#n
vvvvv = vvvv.replace("x",random.choice(nmbs3), 1)#x
vvvvvv = vvvvv.replace("x",random.choice(nmbs4), 1)
vvvvvvvv = vvvvvv.replace("x",random.choice(nmbs5), 1)
vvvvvvvvv = vvvvvvvv.replace("x",random.choice(nmbs6), 1)
vvvvvvvvvv = vvvvvvvvv.replace("x",random.choice(nmbs7), 1)
vvvvvvvvvvv = vvvvvvvvvv.replace("x",random.choice(nmbs8), 1)
vvvvvvvvvvvv = vvvvvvvvvvv.replace("x",random.choice(nmbs9), 1)
vvvvvvvvvvvvv = vvvvvvvvvvvv.replace("x",random.choice(nmbs10), 1)
vvvvvvvvvvvvvv = vvvvvvvvvvvvv.replace("x",random.choice(nmbs11), 1)

#count
count0 = v.count("0")
count1 = v.count("1")
count2 = v.count("2")
count3 = v.count("3")
count4 = v.count("4")
count5 = v.count("5")
count6 = v.count("6")
count7 = v.count("7")
count8 = v.count("8")
count9 = v.count("9")
countx = v.count("x")
cnt = count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count0 + countx
nmbs = count1 + count2 + count3 +  count4 + count5 + count6 + count7 + count8 + count9 + count0
cntx = 0

if cnt == 6:
    v = "%sxxxxxxxxxx"%v
    cntx = 6
elif cnt == 5:
    v = "%sxxxxxxxxxxx"%v
    cntx = 5
else:
    while cnt != 16:
        v = "%sx"% v
        cnt = cnt + 1
cc1 = """
╔════════════════════════╗
║    %s    ║
║                        ║
╠════════════════════════╣
║MM/YYYY                 ║
║                        ║
║                        ║      
║                    CVV ║
╚════════════════════════╝ """% v
print cc1

znc = 1
znc2 = 1
xxc = 1
#month
mm = raw_input("MM;1-12(Enter for random):")
gnm = 0
Month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
if mm == "":
    mm = "RN"
    gnm = 0
elif mm == "01":
    mm = "01"
    gnm = "01"
elif mm == "02":
    gnm = "02"
    mm = "02"
elif mm == "03":
    gnm = "03"
    mm = "03"
elif mm == "04":
    gnm = "04"
    mm = "04"
elif mm == "05":
    gnm = "05"
    mm = "05"
elif mm == "06":
    gnm = "06"
    mm = "06"
elif mm == "07":
    mm = "07"
    gnm = "07"
elif mm == "08":
    mm = "08"
    gnm = "08"
elif mm == "09":
    mm = "09"
    gnm = "09"
elif mm == "10":
    mm = "10"
    gnm = "10"
elif mm == "11":
    gnm = "11"
    mm = "11"
elif mm == "12":
    mm = "12"
    gnm = "12"
elif mm == "1":
    gnm = "01"
    mm = "01"
elif mm == "2":
    mm = "02"
    gnm = "02"
elif mm == "3":
    gnm = "03"
    mm = "03"
elif mm == "4":
    mm = "04"
    gnm = "04"
elif mm == "5":
    mm = "05"
    gnm = "05"
elif mm == "6":
    gnm = "06"
    mm = "06"
elif mm == "7":
    mm = "07"
    gnm = "07"
elif mm == "8":
    mm = "08"
    gnm = "08"
elif mm == "9":
    gnm = "09"
    mm = "09"
elif mm == "10":
    mm = "10"
    gnm = "10"
elif mm == "11":
    mm = "11"
    gnm = "11"
elif mm == "12":
    mm = "12"
    gnm = "12"

else:
    print "Month must be between 01-12"
    exit(0)
cc2 = cc1.replace("MM",mm)
print('\n' *10000)
print cc2

#year
print('\n' *10000)
Years = ["2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030"]
print cc2
YYYY = raw_input("YYYY;2020-2030(Enter for random):")
yyym = 0
cc3 = cc2.replace("YYYY",YYYY)
if YYYY == "":
    YYYY = "RNDM"
    yyym = 0
elif YYYY =="2021":
    YYYY = "2021"
    yyym = "21"
elif YYYY =="2022":
    YYYY = "2022"
    yyym = "22"
elif YYYY =="2023":
    YYYY = "2023"
    yyym = "23"
elif YYYY =="2024":
    YYYY = "2024"
    yyym = "24"
elif YYYY == "2025":
    YYYY = "2025"
    yyym = "25"
elif YYYY =="2026":
    YYYY = "2026"
    yyym = "26"
elif YYYY =="2027":
    YYYY = "2027"
    yyym = "27"
elif YYYY =="2028":
    YYYY = "2028"
    yyym = "28"
elif YYYY =="2029":
    YYYY = "2029"
    yyym = "29"
elif YYYY =="2030":
    YYYY = "2030"
    yyym = "30"
elif YYYY =="21":
    YYYY = "2021"
    yyym = "21"
elif YYYY =="22":
    YYYY = "2022"
    yyym = "22"
elif YYYY =="23":
    YYYY = "2023"
    yyym = "23"
elif YYYY =="24":
    YYYY = "2024"
    yyym = "24"
elif YYYY == "25":
    YYYY = "2025"
    yyym = "25"
elif YYYY =="26":
    YYYY = "2026"
    yyym = "26"
elif YYYY =="27":
    YYYY = "2027"
    yyym = "27"
elif YYYY =="28":
    YYYY = "2028"
    yyym = "28"
elif YYYY =="29":
    YYYY = "2029"
    yyym = "29"
elif YYYY =="30":
    YYYY = "2030"
    yyym = "30"
else:
    print "year must be between 2020-2030"
    exit(0)
vvx = 0
#cvv
print('\n' *10000)
cc3 = cc2.replace("YYYY",YYYY)
print cc3
cvv = raw_input("CVV:")
xo = " "
cvvx = ["100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156","157","158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176","177","178","179","180","181","182","183","184","185","186","187","188","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","231","232","233","234","235","236","237","238","239","240","241","242","243","244","245","246","247","248","249","250","251","252","253","254","255","256","257","258","259","260","261","262","263","264","265","266","267","268","269","270","271","272","273","274","275","276","277","278","279","280","281","282","283","284","285","286","287","288","289","290","291","292","293","294","295","296","297","298","299","300","301","302","303","304","305","306","307","308","309","310","311","312","313","314","315","316","317","318","319","320","321","322","323","324","325","326","327","328","329","330","331","332","333","334","335","336","337","338","339","340","341","342","343","344","345","346","347","348","349","350","351","352","353","354","355","356","357","358","359","360","361","362","363","364","365","366","367","368","369","370","371","372","373","374","375","376","377","378","379","380","381","382","383","384","385","386","387","388","389","390","391","392","393","394","395","396","397","398","399","400","401","402","403","404","405","406","407","408","409","410","411","412","413","414","415","416","417","418","419","420","421","422","423","424","425","426","427","428","429","430","431","432","433","434","435","436","437","438","439","440","441","442","443","444","445","446","447","448","449","450","451","452","453","454","455","456","457","458","459","460","461","462","463","464","465","466","467","468","469","470","471","472","473","474","475","476","477","478","479","480","481","482","483","484","485","486","487","488","489","490","491","492","493","494","495","496","497","498","499","500","501","502","503","504","505","506","507","508","509","510","511","512","513","514","515","516","517","518","519","520","521","522","523","524","525","526","527","528","529","530","531","532","533","534","535","536","537","538","539","540","541","542","543","544","545","546","547","548","549","550","551","552","553","554","555","556","557","558","559","560","561","562","563","564","565","566","567","568","569","570","571","572","573","574","575","576","577","578","579","580","581","582","583","584","585","586","587","588","589","590","591","592","593","594","595","596","597","598","599","600","601","602","603","604","605","606","607","608","609","610","611","612","613","614","615","616","617","618","619","620","621","622","623","624","625","626","627","628","629","630","631","632","633","634","635","636","637","638","639","640","641","642","643","644","645","646","647","648","649","650","651","652","653","654","655","656","657","658","659","660","661","662","663","664","665","666","667","668","669","670","671","672","673","674","675","676","677","678","679","680","681","682","683","684","685","686","687","688","689","690","691","692","693","694","695","696","697","698","699","700","701","702","703","704","705","706","707","708","709","710","711","712","713","714","715","716","717","718","719","720","721","722","723","724","725","726","727","728","729","730","731","732","733","734","735","736","737","738","739","740","741","742","743","744","745","746","747","748","749","750","751","752","753","754","755","756","757","758","759","760","761","762","763","764","765","766","767","768","769","770","771","772","773","774","775","776","777","778","779","780","781","782","783","784","785","786","787","788","789","790","791","792","793","794","795","796","797","798","799","800","801","802","803","804","805","806","807","808","809","810","811","812","813","814","815","816","817","818","819","820","821","822","823","824","825","826","827","828","829","830","831","832","833","834","835","836","837","838","839","840","841","842","843","844","845","846","847","848","849","850","851","852","853","854","855","856","857","858","859","860","861","862","863","864","865","866","867","868","869","870","871","872","873","874","875","876","877","878","879","880","881","882","883","884","885","886","887","888","889","890","891","892","893","894","895","896","897","898","899","900","901","902","903","904","905","906","907","908","909","910","911","912","913","914","915","916","917","918","919","920","921","922","923","924","925","926","927","928","929","930","931","932","933","934","935","936","937","938","939","940","941","942","943","944","945","946","947","948","949","950","951","952","953","954","955","956","957","958","959","960","961","962","963","964","965","966","967","968","969","970","971","972","973","974","975","976","977","978","979","980","981","982","983","984","985","986","987","988","989","990","991","992","993","994","995","996","997","998","999",]
if cvv == "":
    xo = "RNDX"
    cvv = "RND"
else:
    cvv = cvv
    xo = "na"
    while cnt != 16:
        cnt = "%sx"% cnt

#format
cc4 = cc3.replace("CVV",cvv)
print('\n' *10000)
print cc4
print """         Format
1-Pipe             2-CSV
3-XML              4-JSON
5-SQL              6-Recommended
"""
frmtt = int(raw_input("Format(6 for Default):"))

#qntt
print('\n' *10000)
print cc4
qntt = int(raw_input("quantity:"))
cbn = 0
gnmx = ""
brh = ""

pipp = "xxxxxxxxxxxxxxxx|mm|yyyy|cvv"
csvvvv = "xxxxxxxxxxxxxxxx, mm/yyyy, cvv"
xmlx = """        <CreditCard> 
                <CardNumber>
                        xxxxxxxxxxxxxxxx
                </CardNumber>
                <ExpirationDate>
                        mm/yyyy
                </ExpirationDate>
                <Cvv>
                        cvv
                </Cvv>
        </CreditCard> """
jsns = """  {
    \"card_number\": \"xxxxxxxxxxxxxxxx\",
    \"expiration_date\": \"mm/yyyy\",
    \"cvv\": \"cvx\"
  },"""
sqls = """INSERT INTO credit_cards (card_number,expiration_date,cvv) $,cvv) VALUES ('xxxxxxxxxxxxxxxx','mm/yyyy','cvv');"""
while qntt != cbn:

    if cntx == 6:
        v = "%s" % v
    elif cntx == 5:
        v = "%s" % v
    vv = v.replace("x", random.choice(nmbs0), 1)  # v
    vvv = vv.replace("x", random.choice(nmbs1), 1)  # e
    vvvv = vvv.replace("x", random.choice(nmbs2), 1)  # n
    vvvvv = vvvv.replace("x", random.choice(nmbs3), 1)  # x
    vvvvvv = vvvvv.replace("x", random.choice(nmbs4), 1)
    vvvvvvvv = vvvvvv.replace("x", random.choice(nmbs5), 1)
    vvvvvvvvv = vvvvvvvv.replace("x", random.choice(nmbs6), 1)
    vvvvvvvvvv = vvvvvvvvv.replace("x", random.choice(nmbs7), 1)
    vvvvvvvvvvv = vvvvvvvvvv.replace("x", random.choice(nmbs8), 1)
    vvvvvvvvvvvv = vvvvvvvvvvv.replace("x", random.choice(nmbs9), 1)
    vvvvvvvvvvvvv = vvvvvvvvvvvv.replace("x", random.choice(nmbs10), 1)
    vvvvvvvvvvvvvv = vvvvvvvvvvvvv.replace("x", random.choice(nmbs11), 1)
    vvvvvvvvvvvvvvvv = vvvvvvvvvvvvvv.replace("x", random.choice(nmbs11), 1)
    vvvvvvvvvvvvvvvvvv = vvvvvvvvvvvvvvvv.replace("x", random.choice(nmbs11), 1)
    vvvvvvvvvvvvvvvvvvvv = vvvvvvvvvvvvvvvvvv.replace("x", random.choice(nmbs11), 1)
    vvvvvvvvvvvvvvvvvvvvvv = vvvvvvvvvvvvvvvvvvvv.replace("x", random.choice(nmbs11), 1)



    if xo == "RNDX":
        brh = random.choice(cvvx)
    else:
        brh = cvv

    if gnm == 0:
        gnmx = random.choice(Month)
    elif gnm == "01":
        gnmx = "01"
    elif gnm == "02":
        gnmx = "02"
    elif gnm == "03":
        gnmx = "03"
    elif gnm == "04":
        gnmx = "04"
    elif gnm == "05":
        gnmx = "05"
    elif gnm == "06":
        gnmx = "06"
    elif gnm == "07":
        gnmx = "07"
    elif gnm == "08":
        gnmx = "08"
    elif gnm == "09":
        gnmx = "09"
    elif gnm == "10":
        gnmx = "10"
    elif gnm == "11":
        gnmx = "11"
    elif gnm == "12":
        gnmx = "12"

    yyyx = ""
    if yyym == 0:
        yyyx = random.choice(Years)
    elif yyym ==  "21":
        yyyx = "2021"
    elif yyym ==  "22":
        yyyx = "2022"
    elif yyym == "23":
        yyyx = "2023"
    elif yyym == "24":
        yyyx = "2024"
    elif yyym == "25":
        yyyx = "2025"
    elif yyym == "26":
        yyyx = "2026"
    elif yyym == "27":
        yyyx = "2027"
    elif yyym == "28":
        yyyx = "2028"
    elif yyym == "29":
        yyyx = "2029"
    elif yyym == "30":
        yyyx = "2030"

       #pipe
    if frmtt == 1:
        cxv = pipp.replace("xxxxxxxxxxxxxxxx", vvvvvvvvvvvvvvvvvvvvvv)
        cxv1 = cxv.replace("mm",gnmx)
        cxv2 = cxv1.replace("yyyy", yyyx)
        cxv3 = cxv2.replace("cvv",brh)
        print cxv3

        #csv
    elif frmtt == 2:
        cjtx = csvvvv.replace("xxxxxxxxxxxxxxxx", vvvvvvvvvvvvvvvvvvvvvv)
        cjtx1 = cjtx.replace("mm",gnmx)
        cjtx2 = cjtx1.replace("yyyy", yyyx)
        cjtx3 = cjtx2.replace("cvv",brh)
        print cjtx3

        #xml
    elif frmtt == 3:
        xmlx1 = xmlx.replace("xxxxxxxxxxxxxxxx", vvvvvvvvvvvvvvvvvvvvvv)
        xmlx2 = xmlx1.replace("mm",gnmx)
        xmlx3 = xmlx2.replace("yyyy", yyyx)
        xmlx4 = xmlx3.replace("cvv",brh)
        if znc == 1:
            print "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
            print "<CreditCards>"
            znc = 1 + znc
        print xmlx4
        znc2 = znc2 + 1
        if znc2 == qntt + 1:
            print "</CreditCards>"
            znc2 = 1 + znc2

      #json
    elif frmtt == 4:
        jsns1 = jsns.replace("xxxxxxxxxxxxxxxx",vvvvvvvvvvvvvvvvvvvvvv)
        jsns2 = jsns1.replace("mm",gnmx)
        jsns3 = jsns2.replace("yyyy", yyyx)
        jsns4 = jsns3.replace("cvx", brh)
        if znc == 1:
            print "["
            znc = 1 + znc
        if xxc != qntt:
            print jsns4
            xxc = xxc + 1
        znc2 = znc2 + 1
        if znc2 == qntt + 1:
            print jsns4.replace("},", "}")
            print "]"
            znc2 = 1 + znc2
    elif frmtt == 5:
        sqls1 = sqls.replace("xxxxxxxxxxxxxxxx",vvvvvvvvvvvvvvvvvvvvvv)
        sqls2 = sqls1.replace("yyyy", yyyx)
        sqls3 = sqls2.replace("mm",gnmx)
        sqls4 = sqls3.replace("cvv", brh)
        if xxc == 1:
            print sqlsql
            xxc = xxc +1
        print sqls4




    cbn = cbn + 1

#year = yyyx
#gnmx = month
#brh = cvv
#ccnb = vvvvvvvvvvvvvvvvvvvvvv
#formt = frmtt
#pipe = dn
#csv = ndmn
#end rndm all dn sql csv xml json 
