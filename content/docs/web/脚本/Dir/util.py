# 格式化备份文件搜索结果
def __formatBackupResults(resultList, f):
    def __log(s):
        print(s)
        f.write(s)
        f.write('\n')
    statusCodeMap = {}
    lenMap = {}
    for result in resultList:
        statusCode = result['status_code']
        length = len(result['text'])
        statusCodeMap[statusCode] = statusCodeMap.get(statusCode, 0) + 1
        lenMap[length] = lenMap.get(length, 0) + 1
    # 打印状态异常的
    maxStatusCode = -1
    maxStatusCodeCount = -1
    for statusCode, count in statusCodeMap.items():
        if maxStatusCodeCount < count:
            maxStatusCodeCount = count
            maxStatusCode = statusCode
    __log('-----------unnormal status code:')
    for result in resultList:
        if result['status_code'] != maxStatusCode:
            __log(f'{result["status_code"]:<8}{len(result["text"]):<5}{result["url"]}')
    # 打印长度异常的
    maxLength = -1
    maxLengthCount = -1
    for length, count in lenMap.items():
        if maxLengthCount < count:
            maxLengthCount = count
            maxLength = length
    __log('-----------unnormal length:')
    for result in resultList:
        if len(result['text']) != maxLength:
            __log(f'{result["status_code"]:<8}{len(result["text"]):<5}{result["url"]}')

# 搜索备份文件、压缩包、泄露的源代码等
# rootUrl: 要搜索的网址
# interval: 两次请求之间的间隔，单位s
# verbose: 是否打印详细信息
# logFile: 把详细信息写入文件中，这个参数为文件路径
def searchBackupFiles(rootUrl, interval = 0.1, verbose = True, logFile = 'searchBackupFiles.log'):
    import time
    import requests
    urlList = []

    # 备份文件
    FILE_LIST = ['index.php', 'flag.php', 'robots.txt', 'login.php', 'profile.php', 'source.php', 'phpinfo.php', 'test.php', 'register.php', '%3f']
    for file in FILE_LIST:
        urlList.append(f'{rootUrl}/{file}')
        urlList.append(f'{rootUrl}/{file}.bak')
        urlList.append(f'{rootUrl}/{file}~')
        urlList.append(f'{rootUrl}/{file}.swp')
        urlList.append(f'{rootUrl}/.{file}.swp')
        urlList.append(f'{rootUrl}/.{file}.un~')

    # 源代码
    SOURCE_LIST = [
        '.svn', '.svn/wc.db', '.svn/entries', # svn
        '.git/', '.git/HEAD', '.git/index', '.git/config', '.git/description', '.gitignore' # git
        '.hg/', # hg
        'CVS/', 'CVS/Root', 'CVS/Entries', # cvs
        '.bzr', # bzr
        'WEB-INF/web.xml', 'WEB-INF/src/', 'WEB-INF/classes', 'WEB-INF/lib', 'WEB-INF/database.propertie', # java
        '.DS_Store', # macos
        'README', 'README.md', 'README.MD', # readme
        '_viminfo', '.viminfo', # vim
        '.bash_history',
        '.htaccess'
    ]
    for source in SOURCE_LIST:
        urlList.append(f'{rootUrl}/{source}')

    # 压缩包
    suffixList = ['.rar','.zip','.tar','.tar.gz', '.7z']
    keyList = ['www','wwwroot','site','web','website','backup','data','mdb','WWW','新建文件夹','ceshi','databak',
    'db','database','sql','bf','备份','1','2','11','111','a','123','test','admin','app','bbs','htdocs','wangzhan']
    num1 = rootUrl.find('.')
    num2 = rootUrl.find('.', num1 + 1)
    keyList.append(rootUrl[num1 + 1:num2])
    keyList.append(rootUrl) 
    keyList.append(rootUrl.replace('.', '_'))  
    keyList.append(rootUrl.replace('.', '')) 
    keyList.append(rootUrl[num1 + 1:]) 
    keyList.append(rootUrl[num1 + 1:].replace('.', '_'))  
    for key in keyList:
        for suff in suffixList:
            urlList.append(f'{rootUrl}/{key}{suff}')

    # 发送请求
    ret = []
    if verbose:
        f = open(logFile, 'w')
    for url in urlList:
        count = 0
        while count < 5:
            try:
                r = requests.get(url)
            except:
                count += 1
                continue
            break
        if count >= 5:
            print(f'request failed:{url}')
            continue

        # 打印
        if verbose:
            log = f'{r.status_code:<8}{len(r.text):<5}{url}'
            print(log)
            f.write(log)
            f.write('\n')

        # 添加到ret
        ret.append({
            'status_code': r.status_code,
            'text': r.text,
            'url': url
        })

        time.sleep(interval)
    if verbose:
        __formatBackupResults(ret, f)
        f.close()
    return ret
