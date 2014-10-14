from cgi import parse_qs

def application(environ, start_response):
    outString = environ['REQUEST_METHOD'] + "\n"
    paramDic = parse_qs(environ['QUERY_STRING'])
    for i in paramDic.items():
        outString = outString + i[0] + " = " + str(i[1][0]) + "\n"
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [outString]