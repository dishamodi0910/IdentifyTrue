def processUserAgentString(userAgentStr):
    userAgentStrSplitted = userAgentStr.split(" ")
    legacyToken = userAgentStrSplitted[0]
    parsedLegacyToken = legacyToken.split("/")[0]
    compatibleBrowswer = userAgentStrSplitted[-1]
    actualBrowser = userAgentStrSplitted[-2]
    validStr = ""
    startIndex = 0
    stringsParanthesis = []
    for i in range(len(userAgentStr)):
        if userAgentStr[i] == "(":  
            validStr = validStr + userAgentStr[i]
            startIndex = i
        if i > startIndex and startIndex!=0 and userAgentStr[i]!=")":
            validStr = validStr + userAgentStr[i]
        if userAgentStr[i] == ")" :
            startIndex = 0
            stringsParanthesis.append(validStr)
            validStr = ""

    validStr = ""
    startIndex = 0
    stringsParanthesisOpposite = []
    for i in range(len(userAgentStr)):
        if userAgentStr[i] == ")":  
            validStr = validStr + userAgentStr[i]
            startIndex = i
        if i > startIndex and startIndex!=0 and userAgentStr[i]!="(":
            validStr = validStr + userAgentStr[i]
        if userAgentStr[i] == "(" :
            startIndex = 0
            stringsParanthesisOpposite.append(validStr)
            validStr = ""

    stringsParanthesis[0] = stringsParanthesis[0].removeprefix("(")
    stringsParanthesis[1] = stringsParanthesis[1].removeprefix("(")
    stringsParanthesisOpposite[1] = stringsParanthesisOpposite[1].removeprefix(") ")
    stringsParanthesisOpposite[1] = stringsParanthesisOpposite[1].removesuffix(" ")

    operatingSystem = stringsParanthesis[0]
    compatibleRenderingEngine = stringsParanthesis[1]
    browserRenderingEngine = stringsParanthesisOpposite[1]
    # print(userAgentStr)
    # print(stringsParanthesis)
    # print(stringsParanthesisOpposite)
    # print(legacyToken)
    # print(actualBrowser)
    # print(compatibleBrowswer)
    # print(operatingSystem)
    # print(compatibleRenderingEngine)
    # print(browserRenderingEngine)
    return {
        "legacyToken" : legacyToken,
        "parsedLegacyToken" : parsedLegacyToken,
        "operatingSystem" : operatingSystem,
        "browserRenderingEngine" : browserRenderingEngine,
        "compatibleRenderingEngine" : compatibleRenderingEngine,
        "actualBrowser" : actualBrowser,
        "compatibleBrowser" : compatibleBrowswer
    }


# dict = processUserAgentString("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
# print(dict)