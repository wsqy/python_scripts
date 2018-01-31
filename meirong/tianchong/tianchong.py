import xlrd


# 打开xls文件
def open_excel(filename):
    try:
        data = xlrd.open_workbook(filename)
        return data
    except Exception as e:
        print(e)


# 按 索引递归 xls
def excel_table_byindex(file, colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    # 行数
    ncols = table.ncols
    # 列数
    colnames = table.row_values(colnameindex)
    # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
        list.append(app)
    return list


# 按名称递归xls
def excel_table_byname(file='file.xls', colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    # 行数
    colnames = table.row_values(colnameindex)
    # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def main():
    aaa = excel_table_byindex('1.xls')
    bbb = excel_table_byindex('2.xls')

    results = []
    for a in aaa:
        res = []
        result = {}
        for b in bbb:
            if (a["承包方编码"][-4:] == b["承包方编码"]) and a['合同面积'] == b['合同面积']:
                res.append(b)

        result["承包方编码"] = a["承包方编码"]
        result["合同面积"] = a["合同面积"]
        if len(res) == 1:
            result["地块名称"] = res[0]["地块名称"]
        else:
            result["地块名称"] = ""
        results.append(result)

    print(results)
    #
    for a in range(len(results)):
        for b in range(a+1, len(results)):
            if(results[a]["承包方编码"] == results[b]["承包方编码"]) and (results[a]['合同面积'] == results[b]['合同面积']):
                results[a]["地块名称"] = ''
                results[b]["地块名称"] = ''
            else:
                results[a]["地块名称"] = results[a]["地块名称"]
                results[b]["地块名称"] = results[b]["地块名称"]
    with open("aaa.csv", "w") as f:
        for i in results:
            f.write("%s,%s,%s\n" % ("'"+i['承包方编码'], i['地块名称'], i['合同面积']))


if __name__ == "__main__":
    main()
