from django.http import HttpResponse

from testmodel.models import Test


# 数据库操作
# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list1 = Test.objects.all()

    test1 = Test.objects.get(id=1)
    test1.name = '0211-00001-0000'
    test1.save()

    # 输出所有数据
    for var in list1:
        response1 += var.name + "  " + var.desc + "<br>"
    response = response1
    return HttpResponse("<p>" + response + "</p>")
