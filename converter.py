import os
import sys
import json
from typing import Dict
import pandas as pd

playlist_keys = ['pid',
                 'name',
                 'collaborative']

track_keys = ['pos',
              'artist_name',
              'track_uri',
              'artist_uri',
              'track_name',
              'album_uri',
              'album_name']

class Converter:
    def _get_all_playlists(self, input_data_file: str) -> None:
        return json.load(open(input_data_file))['playlists']

    def _prepare_dataframe(self, input_data: Dict) -> None:
        row_list = []
        for playlist in input_data:
            p_row = {}
            for key in playlist_keys:
                p_row[key] = playlist[key]
            for track in playlist['tracks']:
                t_row = {}
                for key in track_keys:
                    if key == 'track_uri':
                        t_row[key] = track[key][14:]
                    elif key == 'artist_uri':
                        t_row[key] = track[key][15:]
                    elif key == 'album_uri':
                        t_row[key] = track[key][14:]
                    else:
                        t_row[key] = track[key]
                row_list.append(p_row | t_row)
        playlist_dataframe = pd.DataFrame(row_list)
        return(playlist_dataframe)
    
    def _prepare_csv_file(self, input_data: pd.DataFrame, output_file_name: str):
        input_data.to_csv(output_file_name, header=True, index=False)
    
    def execute(self, data_input_folder: str) -> None:
        for input_file in os.scandir(data_input_folder):
            input_data = self._get_all_playlists(input_file.path)
            playlist_dataframe = self._prepare_dataframe(input_data)
            self._prepare_csv_file(playlist_dataframe, f"output/{input_file.name[0:len(input_file.name)-5]}.csv")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_data_folder = sys.argv[1]
        Converter().execute('/Users/vinoddalavai/LocalDocuments/CSCI620_BigData/Project/data')
    else:
        print('Invalid input')