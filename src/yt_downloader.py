from pytube import YouTube
from typing import List


def download_mp3(urls: List[str]):
    """Download music files from provided url"""
    for url in urls:
        video = YouTube(url)
        video.streams.get_audio_only().download(
            output_path="../Muzyka")


def download_video(urls: List[str]):
    """Download video files from provided url"""
    for url in urls:
        video = YouTube(url)
        try:
            video.streams.get_by_itag(22).download(
                output_path="../Filmy")
        except AttributeError:
            video.streams.get_by_itag(18).download(
                output_path="../Filmy")
