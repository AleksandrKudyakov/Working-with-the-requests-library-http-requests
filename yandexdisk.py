import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path):
        try:
            href = self._get_upload(file_path).get("href", "")
            response = requests.put(href, data=open(path_to_file, 'rb'))
           # response.raise_for_status()
            if response.status_code == 201:
                print("Success")
        except Exception:
            print("Fail")    
if __name__ == '__main__':
    path_to_file = input( "имя файла для загузки: ")
    token = input("введите токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)