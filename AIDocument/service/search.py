from django.http import HttpResponse
from AIDocument.utils import kuaiyiAI
from django.shortcuts import render


def search(request):
    request.encoding = 'utf-8'
    document_type = request.GET['d_type']
    document_text = request.GET['q']
    chat_line = "请帮我生成一篇{}类型的，内容主要包括{}的文档，内容不少于500字".format(document_type, document_text)
    AI = kuaiyiAI.KuaiYi()
    response = AI.chat(chat_line)
    ctx = {}
    ctx['rlt'] = response
    return render(request, "search_form.html", ctx)