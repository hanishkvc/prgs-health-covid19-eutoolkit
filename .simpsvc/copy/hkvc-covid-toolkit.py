#!/usr/bin/env python3
# Look at global COVID data from eu
# v20200329IST2329, HanishKVC
#

import time
import os
import matplotlib.pyplot as plt
import sys
import calendar


url="https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-20.xlsx"
xlssch="COVID-19-geographic-disbtribution-worldwide-{}-{:02}-{:02}.xlsx"
urlsch="https://www.ecdc.europa.eu/sites/default/files/documents/{}"
csvCovid="/tmp/covid.csv"


def _download_data_xlsts(d,m,y):
    """ timestamped xls file download.
        Given the Day, Month & Year, create the url for xlsx file
        and download the file using wget.
        If file already exists, it gives the option to user as to
        whether to redownload the file or not.
        Once downloaded, convert the xlsx file to csv using xlsx2csv.
        """
    xls = xlssch.format(y,m,d)
    url = urlsch.format(xls)
    bDownload = False
    if not os.path.exists(xls):
        bDownload = True
    else:
        got = input("INFO:download_data:%s\nDo you want to redownload?[Y/*]:" %(xls))
        if (got.strip() == "Y"):
            bDownload = True
    if bDownload:
        if os.system("wget -c {}".format(url)) != 0:
            return False
    os.system("./hkvc_pyuno_toolkit.py ss2csv {} {}".format(xls,csvCovid))
    print(url)
    return True


def download_data_ts(d=None, m=None, y=2020):
    """ Download timestamped data file
        If no day or month is given, then it is determined from
        the current date
        """
    if (d == None):
        d = time.gmtime().tm_mday
    if (m == None):
        m = time.gmtime().tm_mon
    if not _download_data_xlsts(d,m,y):
        _download_data_xlsts((d-1),m,y)



def _simpler_csvline(lIn, colDelim=",", strDelim='"', replaceChr="_"):
    """ Clean up the passed csv line, to make it safe for simple csv parsing
        Check if there are any string delimiter [default: "] in the line.
            Based on pairing of string delimiter logic, decide whether
            checking within a string or outside a string.
        Within a string, check if there is the column delimter [default: ,]
            If found, then replace with replaceChar [ default: _]
        """
    bInStr = False
    lOut = ""
    for i in range(len(lIn)):
        cCur = lIn[i]
        if lIn[i] == strDelim:
            bInStr = not bInStr
        if lIn[i] == colDelim:
            if bInStr:
                cCur = replaceChr
        lOut += cCur
    return lOut



def _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=True, iSkipLinesAtBegin=1, cDelim=','):
    """ Load a specified csv file (default delim [,] but user can change the same)
        sFile: The name (incl path) of file to load
        csvIndex: a dictionary which maps a column header name to its column index
        keyList: a list of column header names, whose corresponding record's values 
            will be used to generate the key for that record, in the returned dictionary.
        dataList: list of column header names. For each specified col, corresponding record
            value will be stored in the returned dictionary as a independent entry.
            Ex: If 2 col names are specified, then each record in the given csv file
                will have two records/entries in the returned dictionary
        bDataListInKey: if true, then specified col names in the dataList will be
            suffixed as part of the dictionary key for corresponding records.
            This helps ensure that one can distinguish the multiple records in the
            returned dictionary, corresponding to a given record in the csv file.
            NOTE: This needs to be True, if dataList has more than 1 col specified.
        iSkipLinesAtBegin: Specifies the number of lines to skip at the begining
            of the given csv file.
        cDelim: specify the delimiter char used in the given csv file.

        This func returns a dictionary containing one or more records corresponding
        to each record in the given csv file.
        """
    f = open(sFile)
    for i in range(iSkipLinesAtBegin):
        f.readline()
    dCur = {}
    dCnt = {}
    for l in f:
        l = l.strip()
        l = _simpler_csvline(l, colDelim=cDelim)
        la = l.split(cDelim)
        keyBase = ""
        for k in keyList:
            if (keyBase == ""):
                keyBase = "{}".format(la[csvIndex[k]])
            else:
                keyBase = "{}-{}".format(keyBase, la[csvIndex[k]])
        for d in dataList:
            if (bDataListInKey):
                tKey = keyBase + "-" + d
            else:
                tKey = keyBase
            dCur[tKey] = la[csvIndex[d]]
    return dCur



def load_csv_eucovid(sFile=csvCovid):
    """ Load csv file generated from the daily eu geographics covid xlsx
        It also prints the total covid cases and deaths in the world
        as per the given csv file.
        """
    numCases = 0
    numDeath = 0
    # geoid-year-month-day-cases
    # geoid-year-month-day-death
    csvIndex = { 'day': 1, 'month': 2, 'year': 3, 'cases': 4, 'death': 5, 'geoid': 7 }
    keyList = [ 'geoid', 'year', 'month', 'day' ]
    dataList = [ 'cases', 'death' ]
    dD = _load_csv(sFile, csvIndex, keyList, dataList)
    for k in dD:
        if k.endswith('cases'):
            dD[k] = int(dD[k])
            numCases += dD[k]
        elif k.endswith('death'):
            dD[k] = int(dD[k])
            numDeath += dD[k]
    input("INFO:LOAD:Cases {}, Deaths {}: Press any key...".format(numCases, numDeath))
    return dD



def load_csv_cc(sFile):
    """ Load country code CC3 to CC2 mapping data.
        This logic is configured to work with github-lukes csv file
        """
    csvIndex= { 'cc2' : 1, 'cc3': 2 }
    keyList = [ 'cc3' ]
    dataList = [ 'cc2' ]
    dCC = _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=False)
    return dCC



def load_csv_pop(sFile):
    """ Load country population data.
        This logic is configured to work with github-dataset csv file
        It also takes care of converting the country code from CC3
        to CC2 format for use by other logics in the program.
        """
    csvIndex = { 'cc3': 1, 'year': 2, 'pop': 3 }
    keyList = [ 'cc3', 'year' ]
    dataList = [ 'pop' ]
    tdCP = _load_csv(sFile, csvIndex, keyList, dataList, bDataListInKey=False)
    dCP = {}
    dCP2010 = {}
    dCPLatest = {}
    lCCMissing = []
    dCPSeen = {}
    for k in tdCP:
        tS = k
        tCC3,tYear = tS.split('-')
        tYear = int(tYear)
        if tCC3 in dCPSeen:
            if dCPSeen[tCC3] < tYear:
                dCPSeen[tCC3] = tYear
        else:
            dCPSeen[tCC3] = tYear
        if tCC3 in dCC:
            tCC2 = dCC[tCC3]
            if (tCC2 == "UK"):
                print("DBUG:csv_pop: UK for GB, already taken")
                exit()
            if (tCC2 == "GB"):
                tCC2 = "UK"
            dCP["{}-{}".format(tCC2,tYear)] = float(tdCP[k])
            if tYear == 2010:
                dCP2010[tCC2] = float(tdCP[k])
        else:
            if not tCC3 in lCCMissing:
                lCCMissing.append(tCC3)
    print("WARN:Missing CC3 {}".format(lCCMissing))
    print("INFO:LatestPopInfoYear:{}".format(dCPSeen))
    return dCP, dCP2010



def get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY):
    """ Get covid data for the given period of dates from the
        specified covid data dictionary.

        dD: The covid data dictionary
        geoId: The CC2 code of the country
        iDS: the starting day
        iMS: the starting month
        iDE: the ending day
        iME: the ending month
        iY: the Year

        This returns both the list of cases and list of deaths.
        It also returns the range of date as a string.
        """
    lC = []
    lD = []
    sCStart = None
    sCEnd = None
    for m in range(iMS, iME+1):
        if (m == iMS):
            tDS = iDS
        else:
            tDS = 1
        if (m == iME):
            tDE = iDE+1
        else:
            tDE = 32
        for d in range(tDS,tDE):
            if d > calendar.mdays[m]:
                bSkip = True
                if (m == 2) and (d == 29):
                    if (calendar.isleap(iY)):
                        bSkip = False
                if bSkip:
                    print("INFO:get_covid_data: Skipping invalid date m-d [{}-{}]".format(m,d))
                    continue
            keyBase="{}-{}-{}-{}-".format(geoId, iY, m, d)
            keyCases = keyBase+"cases"
            keyDeath = keyBase+"death"
            if keyCases in dD:
                if sCStart == None:
                    sCStart = keyBase
                else:
                    sCEnd = keyBase
                lC.append(dD[keyCases])
                #print(keyCases, dD[keyCases])
            else:
                print("WARN: Missing data for %s" %(keyCases))
            if keyDeath in dD:
                lD.append(dD[keyDeath])
                #print(keyDeath, dD[keyDeath])
            else:
                print("WARN: Missing data for %s" %(keyDeath))
    sRange = "{} to {}".format(sCStart, sCEnd)
    return lC, lD, sRange


def calc_cumulatelist(lIn):
    """ Generate a new list where each entry is cumulated data
        over the given input list till (and including) that entry
        """
    tCur = 0
    lOut = []
    for c in lIn:
        tCur += c
        lOut.append(tCur)
    return lOut


def calc_deltalist(lIn):
    """ Generate a new list where each entry is delta between
        the current and previous entry in the input list.
        """
    lOut = []
    for i in range(1,len(lIn)):
        lOut.append(lIn[i] - lIn[i-1])
    return lOut


def calc_movingavglist(lIn, days=7):
    """ Generate a new list which contains a moving average
        over the last 7 days in the given input list.
        """
    lOut = []
    for i in range(1,len(lIn)):
        tSum = 0
        theEnd = i+days
        if (theEnd > len(lIn)):
            break
        for j in range(i, theEnd):
            tSum += lIn[j]
        lOut.append(tSum/days)
    return lOut


def plot_data(thePlt, datas, msgs, title=None, yscale="linear", xscale="linear"):
    i = 0
    for data in datas:
        thePlt.plot(data,"o-", label=msgs[i])
        i += 1
    thePlt.set_xscale(xscale)
    thePlt.set_yscale(yscale)
    if title != None:
        thePlt.set_title(title)
    thePlt.legend()
    thePlt.grid(True)


def calc_mortalityrate(lCC, lDC):
    """ Generate a new list which contains the mortality rate
        calculated from total cases and deaths for each entry
        in the given Cases and Deaths list
        """
    lMR = []
    for i in range(0,len(lCC)):
        if lCC[i] == 0:
            lMR.append(0)
        else:
            lMR.append(lDC[i]/lCC[i])
    return lMR


def calc_relativelist(lIn):
    """ Generate a new list where each entry is relative value 
        of corresponding entry in the given/input list to the 
        total value in the given list.
        """
    iMax = 0
    iSum = 0
    for i in range(len(lIn)):
        iSum += lIn[i]
        if (iMax < lIn[i]):
            iMax = lIn[i]
    iAvg = iSum/len(lIn)
    lOut = []
    for i in range(len(lIn)):
        lOut.append(lIn[i]/iAvg)
    return lOut


def calc_relative2pop(lIn, geoId, dCP):
    tPop = dCP[geoId]
    lOut = []
    for i in lIn:
        lOut.append(i/tPop)
    return lOut


def plt_getl1(axes, axesId):
    """ Helper logic to work with plots, irrespective of whether
        there is a single plot or multiple plots in the figure 
        being created

        This is used to handle the 1st level (the row) of plot matrix
        TOCHECK: Have to cross check the explanation once again later.
                    as I had created the logic few days back.
        """
    try:
        t = len(axes)
        if (axesId >= t):
            thePltL1 = axes[0]
        else:
            thePltL1 = axes[axesId]
    except TypeError:
        thePltL1 = [axes]
    return thePltL1, axesId+1


def plt_getl2(pltL1, pltId):
    """ Helper logic to work with plots, irrespective of whether
        there is a single plot or multiple plots in the figure 
        being created

        This is used to handle the 2nd level (i.e the col, with in
        a given row) of plot matrix
        TOCHECK: Have to cross check explanation once again later.
                    as I had created the logic few days back.
        """
    try:
        t = len(pltL1)
        if (pltId >= t):
            thePltL2 = pltL1[0]
        else:
            thePltL2 = pltL1[pltId]
    except TypeError:
        thePltL2 = pltL1
    return thePltL2, pltId+1


def fill_needed_data(dD, dD2, geoIds, iDS=1, iMS=1, iDE=31, iME=12, iY=2020):
    if dD2 == None:
        dD2 = { 'C': {}, 'D': {}, 'CP': {}, 'DP': {},
                'CC': {}, 'DC': {}, 'CD': {}, 'DD': {},
                'CM': {}, 'DM': {}, 'CMR': {}, 'DMR': {},
                'CR': {}, 'MR': {}, 'sRange': {} }

    for geoId in geoIds:
        if geoId in dD2['C']:
            #print("INFO:fill_needed_data:CC2[{}]:filled, skipping...".format(geoId))
            continue
        print("INFO:fill_needed_data:CC2[{}]:filling...".format(geoId))
        dD2['C'][geoId], dD2['D'][geoId], dD2['sRange'][geoId] = get_covid_data(dD, geoId, iDS, iMS, iDE, iME, iY)
        dD2['CP'][geoId] = calc_relative2pop(dD2['C'][geoId], geoId, dCP2010)
        dD2['DP'][geoId] = calc_relative2pop(dD2['D'][geoId], geoId, dCP2010)
        dD2['CC'][geoId] = calc_cumulatelist(dD2['C'][geoId])
        dD2['CD'][geoId] = calc_deltalist(dD2['C'][geoId])
        dD2['CR'][geoId] = calc_relativelist(dD2['C'][geoId])
        dD2['CM'][geoId] = calc_movingavglist(dD2['C'][geoId])
        dD2['CMR'][geoId] = calc_relativelist(dD2['CM'][geoId])
        dD2['DC'][geoId] = calc_cumulatelist(dD2['D'][geoId])
        dD2['DM'][geoId] = calc_movingavglist(dD2['D'][geoId])
        dD2['MR'][geoId] = calc_mortalityrate(dD2['CC'][geoId], dD2['DC'][geoId])
        print("\nINFO:needed_data: ####### Data for {} #######".format(geoId))
        print("theCasesData:{}:{}".format(len(dD2['C'][geoId]), dD2['C'][geoId]))
        print("theCasesCumuData:{}:{}".format(len(dD2['CC'][geoId]), dD2['CC'][geoId]))
        print("theCasesDeltaData:{}:{}".format(len(dD2['CD'][geoId]), dD2['CD'][geoId]))
        print("theCasesMovAvg:{}:{}".format(len(dD2['CM'][geoId]), dD2['CM'][geoId]))
        print("theCasesMovAvrRel:{}:{}".format(len(dD2['CMR'][geoId]), dD2['CMR'][geoId]))
        print("theDeathData:{}:{}".format(len(dD2['D'][geoId]), dD2['D'][geoId]))
        print("theDeathCumuData:{}:{}".format(len(dD2['DC'][geoId]), dD2['DC'][geoId]))
        print("CasesCumu/Pop:{}\nDeathCumu/Pop:{}".format(dD2['CC'][geoId][-1]/dCP2010[geoId], dD2['DC'][geoId][-1]/dCP2010[geoId]))
        print("1.0% of Pop:{}".format(dCP2010[geoId]*0.01))

    return dD2


bFigSizeSetup=True
def plot_what(dD, dD2, geoIds = ['IN', 'UK', 'CN'], dataTypes = [ "Cases", "CasesCumu", "Death" ], iDS=1, iMS=1, iDE=31, iME=12, iY=2020, bSingle=True, sTitle=None, iPltRows=None, iPltCols=None):
    axesId = 0
    if (iPltRows == None) or (iPltCols == None):
        if bSingle:
            fig,axes = plt.subplots(1)
            iPltRows = 1
            iPltCols = 1
            figWidth = 12
            figHeight = 8
        else:
            iPltRows = len(geoIds)
            iPltCols = len(dataTypes)
            fig,axes = plt.subplots(iPltRows, iPltCols)
            figWidth = 12*iPltCols
            figHeight = 8*iPltRows
    else:
        fig,axes = plt.subplots(iPltRows, iPltCols)
        figWidth = 12*iPltCols
        figHeight = 8*iPltRows
    if bFigSizeSetup:
        print("Pre:figWidth: {}, figHeight: {}".format(figWidth, figHeight))
        widthThres = int(figHeight*2)
        heightThres = int(figWidth*2)
        if figWidth > widthThres:
            figWidth = widthThres
        if figHeight > heightThres:
            figHeight = heightThres
        print("Post:figWidth: {}, figHeight: {}".format(figWidth, figHeight))
        fig.set_figwidth(figWidth)
        fig.set_figheight(figHeight)
    lAllC = []
    lAllCP = []
    lAllD = []
    lAllDP = []
    for geoId in geoIds:
        dD2 = fill_needed_data(dD, dD2, [geoId], iDS, iMS, iDE, iME, iY)
        lC = dD2['C'][geoId]
        lD = dD2['D'][geoId]
        lCP = dD2['CP'][geoId]
        lDP = dD2['DP'][geoId]
        lAllCP.append(lCP)
        lAllDP.append(lDP)
        lAllC.append(lC)
        lAllD.append(lD)
        lCC = dD2['CC'][geoId]
        lCD = dD2['CD'][geoId]
        lCR = dD2['CR'][geoId]
        lCM = dD2['CM'][geoId]
        lCMR = dD2['CMR'][geoId]
        lDC = dD2['DC'][geoId]
        lDM = dD2['DM'][geoId]
        lMR = dD2['MR'][geoId]
        sRange = dD2['sRange'][geoId]
        thePltL1, axesId = plt_getl1(axes, axesId)
        pltId = 0
        if "Cases" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lC], ["Cases "+sRange])
        if "CasesMovAvg" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lCM], ["CasesMovAvg "+sRange])
        if "CasesMovAvgRel" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lCMR], ["CasesMovAvgRel "+sRange])
        if "CasesRelative" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lCR], ["CasesRelative "+sRange])
        if "CasesMovAvgPlus" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lC,lCM], ["Cases "+sRange, "CasesMovAvg"])
        if "CasesLog" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lC], ["CasesLog "+sRange], yscale="log")
        if "CasesCumu" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lCC], ["CasesCumu "+sRange])
        if "CasesDelta" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lCD], ["CasesDelta "+sRange])
        if "Death" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lD], ["Death "+sRange])
        if "DeathMovAvg" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lDM], ["DeathMovAvg "+sRange])
        if "DeathCumu" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lDC], ["DeathCumu "+sRange])
        if "DeathPlus" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lD, lDC], ["Death "+sRange, "DeathCumu"])
        if "MortalityRate" in dataTypes:
            thePlt, pltId = plt_getl2(thePltL1, pltId)
            plot_data(thePlt, [lMR], ["MortalityRate "+sRange])
    if "CasesBox" in dataTypes:
        axesId = 0
        print("axesId",axesId)
        thePltL1, axesId = plt_getl1(axes, axesId)
        print("axesId",axesId)
        pltId = 0
        thePlt, pltId = plt_getl2(thePltL1, pltId)
        thePlt.boxplot(lAllC)
        thePlt.set_yscale("log")
        thePlt.set_xticklabels(geoIds)
        thePlt.set_title("Cases/Day")
        thePlt.grid(True)
        thePltL1, axesId = plt_getl1(axes, axesId)
        print("axesId",axesId)
        pltId = 0
        thePlt, pltId = plt_getl2(thePltL1, pltId)
        thePlt.boxplot(lAllCP)
        thePlt.set_yscale("log")
        thePlt.set_xticklabels(geoIds)
        thePlt.set_title("CasesRel2Pop/Day")
        thePlt.grid(True)
        # thePlt.boxplot(lAllC, 0, '') # No outliers
    if "DeathBox" in dataTypes:
        thePltL1, axesId = plt_getl1(axes, axesId)
        pltId = 0
        thePlt, pltId = plt_getl2(thePltL1, pltId)
        thePlt.boxplot(lAllD)
        thePlt.set_yscale("log")
        thePlt.set_xticklabels(geoIds)
        thePlt.grid(True)
        # thePlt.boxplot(lAllC, 0, '') # No outliers
    if sTitle != None:
        plt.title(sTitle)
    ts = time.strftime("%Y%m%d%H%M%S")
    fig.text(0.01, 0.98, "Data: Europa.EU Covid Consolidated, hkvc")
    fig.set_tight_layout(True)
    sImgFile = "/tmp/{}-covid.png".format(ts)
    fig.savefig(sImgFile, bbox_inches="tight")
    sImgFile = "/tmp/{}-covid.svg".format(ts)
    fig.savefig(sImgFile, bbox_inches="tight")
    plt.margins(0,0)
    plt.show()
    return dD2


download_data_ts()
dD = load_csv_eucovid()
#print(dD)
dCC = load_csv_cc(sys.argv[1])
input("CountryCodes: {}\nPress any key...".format(dCC))
dCP,dCP2010 = load_csv_pop(sys.argv[2])
input("CountryPopulation:2010: {}\nPress any key...".format(dCP2010))
dD2 = None

def do_plots(dD, dD2):
    geoIds = [ 'IN', 'US', 'CA', 'IT', 'CN' ]
    geoIds = [ 'IN', 'US', 'CA', 'IT' ]
    geoIds = [ 'IN', 'CA', 'UK', 'CN' ]
    geoIds = [ 'IN', 'CA', 'UK', 'US', 'CN' ]
    dataTypes = [ "Death" ]
    dataTypes = [ "Cases", "Death" ]
    dataTypes = [ "Cases", "CasesMovAvg", "Death", "DeathCumu" ]
    dataTypes = [ "CasesMovAvgPlus", "Death", "DeathCumu" ]
    dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "Death", "DeathCumu" ]
    dataTypes = [ "CasesMovAvgPlus", "CasesCumu", "DeathCumu", "MortalityRate" ]
    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
    dataTypes = [ "CasesMovAvgRel" ]
    geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
    dataTypes = [ "MortalityRate" ]
    geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
    dataTypes = [ "CasesRelative" ]
    geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True)
    dataTypes = [ "CasesRelative", "MortalityRate" ]
    geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=False)
    return dD2

def do_boxplot(dD, dD2):
    geoIds = [ 'IN', 'CA', 'UK' ]
    geoIds = [ 'IN', 'CA', 'UK', 'ES', 'FR', 'US', 'IT', 'CN' ]
    dataTypes = [ "CasesBox" ]
    #plot_what(dD, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Cases/Day")
    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, iPltRows=2, iPltCols=1)
    dataTypes = [ "DeathBox" ]
    dD2 = plot_what(dD, dD2, geoIds, dataTypes, iDS, iMS, iDE, iME, bSingle=True, sTitle="Death/Day")
    return dD2

iDS = 20
iMS = 1
iDE = time.gmtime().tm_mday
iME = time.gmtime().tm_mon
input("From: 2020-{}-{} to 2020-{}-{}, press any key to continue...".format(iMS,iDS, iME,iDE))
dD2 = do_plots(dD, dD2)
dD2 = do_boxplot(dD, dD2)

