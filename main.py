from pathlib import Path
from tqdm import tqdm
import requests


def to_cookie(c):
    a = c.strip(';').split(';')
    cookies = {pair.split('=')[0].strip(): pair.split('=')[1].strip() for pair in a}
    return cookies


def check_series_id(sid):
    try:
        sid_int = int(sid)
        return
    except ValueError:
        print("seriesId 输入有误")
        exit(0)


def get_content_id_list(cookies, series_id):
    pre = "https://www.cctalk.com/webapi/content/v1.1/series/"
    suf = "/get_content_unit_struts"
    url = f"{pre}{series_id}{suf}"
    r = requests.get(url=url, cookies=cookies)
    res = r.json()
    content = res["data"]["unitList"][0]["contentIdList"]
    return content


def get_series_name(video_id, series_id, cookies):
    pre = "https://www.cctalk.com/webapi/content/v1.1/video/detail?videoId="
    suf = f"&seriesId={series_id}"
    url = f"{pre}{video_id}{suf}"
    r = requests.get(url=url, cookies=cookies)
    res = r.json()
    s_name = res["data"]["seriesInfo"]["seriesName"]
    return s_name


def get_video_information(video_id, series_id, cookies):
    pre = "https://www.cctalk.com/webapi/content/v1.1/video/detail?videoId="
    suf = f"&seriesId={series_id}"
    url = f"{pre}{video_id}{suf}"
    r = requests.get(url=url, cookies=cookies)
    res = r.json()
    v_name = res["data"]["videoName"]
    v_url = res["data"]["videoUrl"]
    return v_name, v_url


def download_videos(video_id, series_id, cookies, i, dir_name):
    video_name, video_url = get_video_information(video_id, series_id, cookies)
    filename = f"{i}-{video_name}"
    filepath = f"{dir_name}/{filename}.mp4"
    file = Path(filepath)
    if file.exists():
        print(f"文件已存在，跳过下载: {filename}")
        return
    response = requests.get(url=video_url, cookies=cookies, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with file.open('wb') as file:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    bar.update(len(chunk))
    print(f"{filename} 下载完成")


def main():
    print("--CCtalk视频课程下载--")
    c = input("输入cookie: ")
    cookies = to_cookie(c)
    series_id = input("输入seriesId: ")
    check_series_id(series_id)
    content_id_list = get_content_id_list(cookies, series_id)
    series_name = get_series_name(content_id_list[-1], series_id, cookies)
    dir_name = f"D:/{series_name}"
    dir_path = Path(dir_name)
    dir_path.mkdir(parents=True, exist_ok=True)
    print(f"即将要下载的是:    {series_id}")
    print(f"下载目录:   {dir_name}")
    print(f"共计{len(content_id_list)}项")
    print("---开始下载---")
    for index, v_id in enumerate(content_id_list, 1):
        print(f"正在下载第{index}项")
        download_videos(v_id, series_id, cookies, index, dir_name)
    print("--任务完成--")
    out = input("回车退出")


if __name__ == "__main__":
    main()
