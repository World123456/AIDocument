import requests
import json


class KuaiYi:

    def get_token(self):
        url = 'https://is-gateway-test.corp.kuaishou.com/token/get?appKey=420b105f-6bea-4d7a-9799-0e06e8540691'
        response = requests.get(url)
        json_response = response.json()
        access_token = json_response['result']['accessToken']
        # print(access_token)
        return access_token


    def chat(self, question):
        token = self.get_token()  # 参照openapi文档自行申请# 根据调用环境选择openapi文档中对应的链接
        # print(token)
        url = 'https://is-gateway-test.corp.kuaishou.com/kwaiyii/chat'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(token)
        }
        params = {
        }
        json_data = {
            'req_id': '1',
            'query_history': [],
            'biz': 'hackthon_6a9e156729',
            'query': question,
            'session_id': '1',
            'config': {}
        }
        response = requests.post(
            url, params=params, headers=headers, json=json_data)
        json_response = json.loads(response.content)
        # print(json_response)
        # 提取 JSON 结构中的 answer 值
        answer = json_response['answer']

        print(answer)
        return answer


if __name__ == '__main__':
    AI = KuaiYi()
    AI.chat('请帮我生成一篇关于母爱的500字作文')